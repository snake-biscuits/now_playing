# https://doc.qt.io/qtforpython-6/examples/example_widgets_desktop_systray.html

from PySide6 import QtWidgets  # QSystemTrayIcon
from PySide6 import QtGui  # QIcon


# QtWidgets.QSystemTrayIcon.isSystemTrayAvailable()


class TrayDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.icon = QtGui.QIcon("svg/tray.svg")

        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.icon)

        # action_binds = {
        #     "Minimize": self.hide,
        #     "Maximize": self.showMaximized,
        #     "Restore": self.showNormal}
        # # TODO: "Quit": qApp.quit
        # self.actions = dict()
        # for action, method in action_binds.items():
        #     self.actions[action] = QtGui.QAction(action, self)
        #     self.actions[action].triggered.connect(method)

        self.setWindowTitle("now_playing test")
        self.resize(384, 192)
