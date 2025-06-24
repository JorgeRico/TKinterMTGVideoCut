from moviepy import VideoFileClip
from tkinter import *
from datetime import datetime

class VideoEdit():
    def __init__(self, start, end, file):
        self.start        = start
        self.end          = end
        self.vcodec       = "libx264"
        self.videoquality = "24"
        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
        self.compression = "ultrafast"
        self.savetitle   = 'file_cutted_'+ f'{datetime.now():%Y_%m_%d_%H_%M_%S}' + '.mkv'
        self.file        = file

    def getCutFileName(self):
        return self.savetitle

    # edit video function
    def edit(self):
        video       = VideoFileClip(self.file)
        videoCutted = video.subclipped(self.start, self.end)

        # save file
        videoCutted.write_videofile(
            self.savetitle, 
            threads       = 4, 
            fps           = 24,
            codec         = self.vcodec,
            preset        = self.compression,
            ffmpeg_params = ["-crf", self.videoquality]
        )

        video.close()
