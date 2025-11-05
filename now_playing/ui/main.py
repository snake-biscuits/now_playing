from typing import List

# from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QTabWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        tabs = QTabWidget()
        tabs.addTab(QLabel("Audio"), "Podcasts & Music")
        tabs.addTab(QLabel("Video"), "Youtube & Videos")
        tabs.addTab(QLabel("Books"), "Books")
        tabs.addTab(QLabel("Files"), "Downloads")

        viewer = QLabel("Viewer")

        main = QHBoxLayout()
        main.addWidget(tabs)
        main.addWidget(viewer)

        self.setCentralWidget(main)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    main_window = MainWindow()
    main_window.show()

    return app.exec()
