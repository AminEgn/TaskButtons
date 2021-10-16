# internal
from src import Controller
from src.ui import MainWindow
# standard
import os
import sys
# pyqt
from PyQt5.QtWidgets import QApplication


def single_instance(app_name):
    apps = os.popen(f'TASKLIST /FI "IMAGENAME eq {app_name.lower()}*"').read()
    if app_name in apps:
        return False
    else:
        return True


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    controller = Controller(window)
    sys.exit(app.exec())


if __name__ == '__main__':
    if single_instance('TaskButton'):
        main()
    else:
        sys.exit(-1)

