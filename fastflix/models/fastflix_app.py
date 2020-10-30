# -*- coding: utf-8 -*-

from qtpy import QtWidgets

from fastflix.models.fastflix import FastFlix


class FastFlixApp(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fastflix: FastFlix = FastFlix()
