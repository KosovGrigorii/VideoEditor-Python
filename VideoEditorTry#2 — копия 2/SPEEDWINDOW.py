from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, \
    QComboBox, QFileDialog, QLineEdit, QSlider

import sys

from random import randint

from moviepy.video.io.VideoFileClip import VideoFileClip

from VideoItself import VideoWindow
from PyQt5.QtCore import Qt


class SpeedWindow(QWidget):
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


        self.slider = QSlider(
            orientation=Qt.Horizontal,
            minimum=0,
            maximum=10,
            singleStep=1,
            pageStep=1
        )
        label_value = QLabel(alignment=Qt.AlignCenter)
        self.slider.valueChanged.connect(label_value.setNum)
        label_value.setNum(self.slider.value())


        self.layout = QVBoxLayout()
        self.note = QLabel("5 is normal")
        self.ok = QPushButton("Set New Speed")

        self.layout.addWidget(self.note)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(label_value)
        self.layout.addWidget(self.ok)
        self.ok.clicked.connect(lambda: self.vindow.change_speed_video(self, (self.slider.value()/5)))

        self.setLayout(self.layout)