# internal
from src.views import Views


class Controller(object):
    """Controller"""
    def __init__(self, ui):
        self.ui = ui
        self.view = Views(self.ui)
