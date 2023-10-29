# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
from moviepy.editor import *   # pip install moviepy

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

# VIDEO_FILE_PATH = "C:/Course/If you're willing to imagine it, it's possible to make it happen!.mp4"
# AUDIO_FILE_PATH = "C:/Course/If you're willing to imagine it, it's possible to make it happen!.mp3"


MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
# MoviePy - Done.                    


# get now path
print(os.getcwd())