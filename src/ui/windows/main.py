# internal
from src.ui.resources import icons
from src.ui.component import BaseWidget, BaseButton
# pyqt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QTextDocument, QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QSystemTrayIcon, QVBoxLayout, QHBoxLayout,
                             QMainWindow, QLabel, QMenu)


class MainWindow(QMainWindow):
    """Main Window UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # bootstrap
        self._bootstrap()
        # menu
        self.menuHandler(0)
        # stylesheet
        self._styleSheet()

    def _bootstrap(self):
        self.setFixedSize(800, 600)
        # central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        # general layout
        self.generalLayout = QHBoxLayout()
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        # self.generalLayout.setAlignment(Qt.AlignLeft)
        self._centralWidget.setLayout(self.generalLayout)
        # attach
        # - menu
        self.menu = Menu()
        self.generalLayout.addWidget(self.menu)
        # - red window
        self.redWindow = RedWindow()
        self.generalLayout.addWidget(self.redWindow)
        # - green window
        self.greenWindow = GreenWindow()
        self.generalLayout.addWidget(self.greenWindow)
        # - blue window
        self.blueWindow = BlueWindow()
        self.generalLayout.addWidget(self.blueWindow)
        # - yellow window
        self.yellowWindow = YellowWindow()
        self.generalLayout.addWidget(self.yellowWindow)
        # connect signals
        # self.connectSignal()
        # window widget list
        self.windowList = [self.redWindow, self.greenWindow, self.blueWindow, self.yellowWindow]
        self.SystemTray()

    def menuHandler(self, index):
        for i, win in enumerate(self.windowList):
            win.hide()
        self.ani = QPropertyAnimation(self.windowList[index], b'geometry')
        self.ani.setDuration(1100)
        self.ani.setStartValue(QRect(830, 0, 0, 0))
        self.ani.setEndValue(QRect(220, 0, 0, 0))
        self.windowList[index].show()
        self.windowList[index].raise_()
        self.ani.start()

    def connectSignal(self):
        self.menu.btnRed.clicked.connect(self.print_document)

    def SystemTray(self):
        icon = QIcon(':/icons/tray-icon')
        menu = QMenu()
        action_show = menu.addAction("Show/Hide")
        action_show.triggered.connect(lambda: self.hide() if self.isVisible() else self.show())
        action_quit = menu.addAction("Quit")
        action_quit.triggered.connect(self.close)
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.setToolTip('Un go!')
        self.tray.showMessage('WTF?', 'FAQ')
        self.tray.activated.connect(self.onTrayIconActivated)
        self.tray.show()

    def onTrayIconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def _styleSheet(self):
        self.setStyleSheet("""
            background: white;
        """)


class Menu(BaseWidget):
    """Menu"""
    def craftWidget(self):
        self.setFixedSize(200, 600)
        # red button
        self.btnRed = BaseButton('RED')
        self.btnRed.alt = 'WTF'
        self.btnRed.craftButton(100, 100)
        # green button
        self.btnGreen = BaseButton('GREEN')
        self.btnGreen.craftButton(100, 100)
        # blue button
        self.btnBlue = BaseButton('BLUE')
        self.btnBlue.craftButton(100, 100)
        # yellow button
        self.btnYellow = BaseButton('YELLOW')
        self.btnYellow.craftButton(100, 100)
        # attach
        self.generalLayout.addWidget(self.btnRed)
        self.generalLayout.addWidget(self.btnGreen)
        self.generalLayout.addWidget(self.btnBlue)
        self.generalLayout.addWidget(self.btnYellow)

    def craftStyle(self):
        self.setStyleSheet("""
            QPushButton {
                background: QLinearGradient(x1: 1 y1: 1,
                                            x2: 0 y2: 0,
                                            stop: 1 #c2e59c,
                                            stop: 0 #64b3f4);
                border: 1px solid #ccc;
                color: #555;
                border-radius: 50px;
            }
            QPushButton:hover {
                background: QLinearGradient(x1: 1 y1: 1,
                                            x2: 0 y2: 0,
                                            stop: 1 #64b3f4,
                                            stop: 0 #c2e59c);
                border-color: #888;
                color: #222;
            }
            QPushButton:pressed {
                border-style: double;
                color: #000
            }
        """)


class RedWindow(BaseWidget):
    """Red Window"""
    def craftWidget(self):
        self.setFixedSize(580, 600)
        self.lbl = QLabel('RED ONE')
        self.generalLayout.addWidget(self.lbl)

    def craftStyle(self):
        self.setStyleSheet("""
            QWidget {
                background: #FF3B3B;
            }
        """)


class GreenWindow(BaseWidget):
    def craftWidget(self):
        self.setFixedSize(580, 600)
        self.lbl = QLabel('GREEN ONE')
        self.generalLayout.addWidget(self.lbl)

    def craftStyle(self):
        self.setStyleSheet("""
            QWidget {
                background: #A3FF3B;
            }
        """)


class BlueWindow(BaseWidget):
    """Blue Window"""
    def craftWidget(self):
        self.setFixedSize(580, 600)
        self.lbl = QLabel('BLUE ONE')
        self.generalLayout.addWidget(self.lbl)

    def craftStyle(self):
        self.setStyleSheet("""
            QWidget {
                background: #3B90FF;
            }
        """)


class YellowWindow(BaseWidget):
    """Yellow Window"""
    def craftWidget(self):
        self.setFixedSize(580, 600)
        self.lbl = QLabel('YELLOW ONE')
        self.generalLayout.addWidget(self.lbl)

    def craftStyle(self):
        self.setStyleSheet("""
            QWidget {
                background: #FFFC3B;
            }
        """)
