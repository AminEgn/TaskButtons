# internal
from src.ui.component import BaseWidget, BaseButton
# pyqt
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QSystemTrayIcon, QVBoxLayout, QHBoxLayout


class MainWindow(BaseWidget):
    """Main Window UI"""
    def craftWidget(self):
        self.setFixedSize(500, 500)
        # widget
        self.btnWidget = QWidget(self)
        self.btnLayout = QVBoxLayout()
        self.btnWidget.setFixedSize(200, 500)
        self.btnWidget.setLayout(self.btnLayout)
        # red button
        self.btnRed = BaseButton('RED')
        self.btnRed.craftButton(100, 100)
        self.redLayout = QHBoxLayout()
        self.redLayout.addWidget(self.btnRed)
        # green button
        self.btnGreen = BaseButton('GREEN')
        self.btnGreen.craftButton(100, 100)
        self.greenLayout = QHBoxLayout()
        self.greenLayout.addWidget(self.btnGreen)
        # blue button
        self.btnBlue = BaseButton('BLUE')
        self.btnBlue.craftButton(100, 100)
        self.blueLayout = QHBoxLayout()
        self.blueLayout.addWidget(self.btnBlue)
        # attach
        self.btnLayout.addLayout(self.redLayout)
        self.btnLayout.addLayout(self.greenLayout)
        self.btnLayout.addLayout(self.blueLayout)
        self.generalLayout.addWidget(self.btnWidget)
        self.generalLayout.addStretch(1)

    def craftStyle(self):
        self.setStyleSheet("""
            QPushButton {
                background: #555;
                border-radius: 50px;
            }
            QPushButton:hover {
                background: #999;
            }
        """)
