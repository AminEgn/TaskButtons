# pyqt
from PyQt5.QtWidgets import QWidget, QVBoxLayout


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
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.generalLayout)

    def craftWidget(self):
        pass

    def craftStyle(self):
        pass

    def connectSignals(self):
        pass
