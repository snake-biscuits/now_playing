from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QWidget,
    )


# TODO: grid layout calendar
# -- populate each day w/ info from db
# -- episode release dates etc.


class MediaList(QWidget):
    def __init__(self, parent=None):
        super(MediaList, self).__init__(parent)

        layout = QGridLayout()
        for i in range(8):
            # TODO: use a icon box / podcast icon widget
            # -- pull up some menu when clicked
            label = QLabel(f"Episode {i:03d}")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                padding: 1.5rem;
                background-color: #333;
                color: #CCC;
                font-family: sans-serif;
                font-size: 24px;""")
            x = i % 3
            y = i // 3
            layout.addWidget(label, y, x)

        self.setLayout(layout)


def main(argv: List[str]):
    """sys.exit(main(sys.argv))"""
    app = QApplication(argv)

    test_widget = MediaList()
    test_widget.show()

    return app.exec()
