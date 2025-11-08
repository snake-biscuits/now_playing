from typing import List

from . import browse


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

        viewer = QLabel("Viewer")

        main = QGridLayout()
        main.addWidget(tabs, 0, 0)
        main.addWidget(viewer, 0, 1)

        main.setColumnStretch(0, 3)
        main.setColumnStretch(1, 1)

        core = QWidget()
        core.setLayout(main)

        self.setCentralWidget(core)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    main_window = MainWindow()
    main_window.show()

    return app.exec()
