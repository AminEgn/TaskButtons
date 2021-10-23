# internal
from src import Controller
from src.ui import MainWindow
# standard
import os
import sys
# pyqt
from PyQt5.QtWidgets import QApplication


def single_instance(app_name):
    """check only one instance of application"""
    try:
        # get process list
        apps = os.popen(f'TASKLIST /FI "IMAGENAME eq {app_name.lower()}*"').read()\
            .replace('               ', '\n').split('\n')

        # empty list
        expected_list = list()
        for p in apps:
            if p.lower() == f'{app_name.lower()}.exe':
                expected_list.append(p)
        # check number of instances
        if len(expected_list) > 1:
            return False
        else:
            return True
    except Exception:
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # weak reference
    controller = Controller(window)
    sys.exit(app.exec())


if __name__ == '__main__':
    if single_instance('TaskButton'):
        main()
    else:
        sys.exit(-1)
