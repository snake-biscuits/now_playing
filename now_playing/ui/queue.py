"""basic vertical media queue"""
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QScrollArea,
    QWidget)


# TODO: always stretch to fit parent width
class QueuedMedia(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        # TODO: custom icon per entry
        icon = QSvgWidget("./svg/vinyl.45.svg")  # TEMP
        # TODO: QSvgRenderer setAspectRatioMode
        # -- Qt.KeepAspectRatio

        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            padding: 1.5rem;
            background-color: #A45;
            color: #CCC;
            font-family: sans-serif;
            font-size: 24px;""")

        layout = QGridLayout()
        layout.addWidget(icon, 0, 0)
        layout.addWidget(label, 0, 1)
        # TODO: menu / handle

        # TODO: stretch rules
        # -- 1:1 aspect icon
        # -- strech left-aligned label w/ marquee on hover
        # -- 1:1 aspect menu / handle icon
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, -1)  # stretch to fill

        self.setLayout(layout)
        self.setStyleSheet("""
            border-radius: 24px;
            background-color: #CBA;
            padding: 0.25rem;
            border: 2px solid #333;""")


class MediaQueue(QScrollArea):
    # TODO: drag & drop to shuffle
    # TODO: get entries with a Model-View system
    # -- also need to deal with caching outside the visible area

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout()
        # lorem ipsum widgets
        for i in range(8):
            label = QueuedMedia(f"Episode {i:03d}")
            layout.addWidget(label, i, 0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setWidget(widget)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    queue = MediaQueue()
    queue.show()

    return app.exec()
