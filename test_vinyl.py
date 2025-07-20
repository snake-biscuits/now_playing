"""planning to convert .wav to a vinyl bumpmap"""
import dearpygui.dearpygui as imgui
import numpy as np
from PIL import Image


# TODO: visualise the waveform w/ a dpg plot
def visualise(filename: str, start: int, length: float):
    sps = 176400  # samples per second
    # NOTE: we can get bps from the wav header, but I don't care
    # -- CDDA is always 16-bit signed pcm (stereo) @ 44.1KHz
    byte_length = int(sps * length) * 2
    with open(filename, "rb") as wave_file:
        wave_file.seek(start)
        data = wave_file.read(byte_length)
    # TODO: convert data to plot
    y_axis = np.frombuffer(data, dtype=np.int16)
    x_axis, y_axis = zip(*enumerate(y_axis))
    x_axis = np.array(x_axis) / sps

    # render w/ imgui
    imgui.create_context()

    width = int(128 * length)
    with imgui.window(label="Visualiser"):
        with imgui.plot(label="Waveform", height=256, width=width):
            imgui.add_plot_axis(imgui.mvXAxis, label="seconds")
            imgui.add_plot_axis(imgui.mvYAxis, label="amplitude", tag="y_axis")
            imgui.add_line_series(x_axis, y_axis, parent="y_axis")

    imgui.create_viewport(title="Waveform Visualiser", height=544, width=960)
    imgui.setup_dearpygui()
    imgui.show_viewport()
    imgui.start_dearpygui()
    imgui.destroy_context()


def sample(filename: str, start: int, width: int = 512, height: int = 512):
    with open(filename, "rb") as wave_file:
        wave_file.seek(start)
        image = Image.frombytes(
            "L",  # 8-bit grayscale
            (width, height),
            wave_file.read(width * height),
            "raw")
    return image


if __name__ == "__main__":
    # NOTE: track_0.wav was extracted from Quake III for Dreamcast
    # -- except for the header (44 bytes) data is all 0x00 until 0x6E6C
    sample("track_0.wav", 0x6E6C).save("test_vinyl.png")

    # NOTE: 16-bit PCM @ 44.1KHz is crazy dense, loading even 10s takes a while
    # -- would be best to stream this data in or something
    # -- having to provide imgui w/ x-axis values certainly doesn't help
    # -- might be better to do this sort of thing in a shader instead
    visualise("track_0.wav", 0x6E6C, 10)

    # TODO: load .wav as a 16-bit grayscale ?x1 texture
    # -- barymetric vertex position (fragment shader) -> texture uv
    # -- calculating the spiral texture in the shader
    # -- could also do the circle in a shader
