# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from moviepy.editor import *   # pip install moviepy



# 將mp4轉mp3
def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()



# 取出當前資料夾下的.mp4
mp4_files = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".mp4")]



# 當前路徑
path = os.path.dirname(__file__)



# 創建mp3資料夾
folder_path = path + "\\mp3_file"

if os.path.exists(folder_path):
    print("folder " + '\mp3_file' + " exist")
else:
    os.makedirs(folder_path)
    print("create a " + '\mp3_file' + " folder")



if __name__ == '__main__':

    for mp4_file in mp4_files:
        
        VIDEO_FILE_PATH = path + "\\" + mp4_file
        AUDIO_FILE_PATH = path + "\mp3_file\\" + os.path.splitext(mp4_file)[0] + ".mp3"
                
        MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
        # MoviePy - Done.                    



