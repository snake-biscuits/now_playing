from typing import List

from . import browse
from . import queue


# from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QTabWidget,
    QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        tabs = QTabWidget()

        audio = browse.audio.AudioPool()

        tabs.addTab(audio, "&Audio")
        tabs.addTab(QLabel("Video"), "&Video")
        tabs.addTab(QLabel("Books"), "&Books")
        tabs.addTab(QLabel("Files"), "&Downloads")

        # TODO: QGridLayout (vertical)
        # -- mini player (playback controls)
        # -- queue / media description / metadata
        viewer = queue.MediaQueue()

        layout = QGridLayout()
        layout.addWidget(tabs, 0, 0)
        layout.setColumnStretch(0, 3)
        layout.addWidget(viewer, 0, 1)
        layout.setColumnStretch(1, 1)

        main = QWidget()
        main.setLayout(layout)
        self.setCentralWidget(main)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    main_window = MainWindow()
    main_window.show()

    return app.exec()
