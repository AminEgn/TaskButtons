# standard
from functools import partial
# pyqt
from PyQt5.QtCore import QPropertyAnimation, QRect


class Views(object):
    """View"""
    def __init__(self, ui):
        self.ui = ui
        self.menu = self.ui.menu
        self.red = self.ui.redWindow
        self.green = self.ui.greenWindow
        self.blue = self.ui.blueWindow
        self.yellow = self.ui.yellowWindow
        self.btnList = [self.menu.btnRed, self.menu.btnGreen, self.menu.btnBlue, self.menu.btnYellow]
        self.connectSignals()

    def connectSignals(self):
        for i, btn in enumerate(self.btnList):
            btn.clicked.connect(partial(self.ui.menuHandler, i))
