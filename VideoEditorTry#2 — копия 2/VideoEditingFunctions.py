import os
import sys
import threading

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout


class QMovie:
    started = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self, name):
        self.clip = VideoFileClip(name)



    def _cut(self, clip, startCut, endCut):
        self.clip = clip
        self.clip.cutout(startCut, endCut)

    #def _fadeInOut(self, input, duration):
    #    clip = VideoFileClip(input)
    #    clip1 = clip.subclip(0, 5)
    #    clip2 = clip.subclip(5, 7)
    #    clip2 = clip2.crossfadein(2.0)
    #    clip3 = clip.subclip(7)
    #    clip3 = clip3.crossfade
    #   final = CompositeVideoClip([clip1, clip2])

    def crossfadein(self, clip, duration):
        self.clip = clip
        clip.mask.duration = clip.duration
        new_clip = clip.copy()
        new_clip.mask = clip.mask.fx(fadein, duration)
        return new_clip

    def crossfadeout(self, clip, duration):
        self.clip = clip
        clip.mask.duration = self.clip.duration
        new_clip = self.clip.copy()
        new_clip.mask = self.clip.mask.fx(fadeout, duration)
        return new_clip

    def rotate(self, clip, angle, start, end):
        self.clip = clip
        clip1 = self.clip.subclip(0, start)
        clip2 = self.clip.subclip(start, end)
        clip3 = self.clip.subclip(end)
        clip2.rotate(angle)
        final_clip = concatenate_videoclips([clip1, clip2, clip3])
        self.clip = final_clip



