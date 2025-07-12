from typing import List

from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QScrollArea,
    QWidget)


# TODO: grid layout calendar
# -- populate each day w/ info from db
# -- episode release dates etc.

# TODO: make it a button
class MediaEntry(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        icon = QSvgWidget("./svg/vinyl.33.svg")
        # icon = QSvgWidget("./svg/vinyl.45.svg")
        # icon = QSvgWidget("./svg/vinyl.78.svg")
        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            padding: 1.5rem;
            background-color: #333;
            color: #CCC;
            font-family: sans-serif;
            font-size: 24px;""")

        layout = QGridLayout()
        layout.addWidget(icon, 0, 0)
        layout.addWidget(label, 1, 0)
        self.setLayout(layout)


# TODO: resize to fit widget
# -- might involve adjusting layout row & column counts
class MediaList(QWidget):
    # TODO: manage layout rows & columns
    # -- handles to push & pop entries
    # -- scrollable (QScrollArea?)
    # -- maintain proportions of entries

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout()
        for i in range(8):
            label = MediaEntry(f"Episode {i:03d}")
            x = i % 3
            y = i // 3
            layout.addWidget(label, y, x)

        self.setLayout(layout)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    # TODO: contain scrollarea in a parent widget
    # -- add a filter section

    # scrollable list of media
    media_list = MediaList()
    main_widget = QScrollArea()
    main_widget.setWidget(media_list)
    main_widget.show()

    # TODO: visual queue organiser

    return app.exec()
