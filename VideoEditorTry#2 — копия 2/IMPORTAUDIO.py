from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, \
    QComboBox, QFileDialog, QRadioButton

import sys

from random import randint

from moviepy.video.io.VideoFileClip import VideoFileClip

from VideoItself import VideoWindow


class AudioWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, vindow, w, h):
        super().__init__()
        self.file_name = ""
        self.vindow = vindow
        self.resize(w, h)
        self.setBaseSize(w, h)

        self.layout = QVBoxLayout()
        self.concat = QPushButton('Import Audio')
        self.done = QPushButton("Concatenate")

        self.layout.addWidget(self.concat)
        self.layout.addWidget(self.done)
        self.concat.clicked.connect(self.import_vid)
        self.done.clicked.connect(lambda: self.vindow.concatenate_audio(self, self.file_name))

        self.setLayout(self.layout)

    def import_vid(self):
        file_name, _ = QFileDialog.getOpenFileName()
        if file_name != '':
            self.file_name = file_name