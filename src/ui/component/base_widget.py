# pyqt
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class BaseWidget(QWidget):
    """Basic Widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bootstrap()

    def bootstrap(self):
        self.craftLayout()
        self.craftWidget()
        self.craftStyle()
        self.connectSignals()

    def craftLayout(self):
        self.generalLayout = QHBoxLayout()
        self.setLayout(self.generalLayout)

    def craftWidget(self):
        pass

    def craftStyle(self):
        pass

    def connectSignals(self):
        pass
