from moviepy import VideoFileClip
from tkinter import *
from datetime import datetime
from tkinter import *
import customtkinter as ctk
from video.videoOptions import VideoOptions
# from video.progressBar import ProgressBar
from video.files import File

class VideoEdit():
    def __init__(self, root):
        self.root         = root
        self.start        = VideoOptions(self.root)
        self.end          = VideoOptions(self.root)
        self.file         = None
        self.options      = VideoOptions(self.root)
        self.vcodec       = "libx264"
        self.videoquality = "24"
        # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
        self.compression  = "ultrafast"
        self.savetitle    = 'file_cutted_'+ f'{datetime.now():%Y_%m_%d_%H_%M_%S}' + '.mkv'

    def getFileName(self):
        return self.savetitle

    # edit video function
    def edit(self, start, end, file):
        video       = VideoFileClip(file)
        videoCutted = video.subclipped(start, end)

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

    # select file on computer
    def cutFile(self):
        self.file = File(self.root)
        if self.file.checkComputerFile() == True:
            self.file.printFileName(self.file.getFile())
            self.start.setTimeOptions("Start to cut on :")
            self.end.setTimeOptions("End to cut on :")
            self.setSubmitButton()

    # set spinbox results
    def setTimeResults(self):
        self.start.setTimeResult()
        self.end.setTimeResult()
       
    # call edit video
    def editVideo(self):
        self.edit(self.start.getTimeResult(), self.end.getTimeResult(), self.file.getFile())
        self.clearFrame()
        self.file.printFileName(self.getFileName())
        title = Label(self.root, text="Done!", justify="center")
        title.pack(pady=5)

    # show progress bar
    def getProgressBar(self):
        title = Label(self.root, text="cutting video . . . . ", justify="center")
        title.pack(pady=5)
        # extrange progressbar stop on edit video launch
        # progressBar = ProgressBar(self.root)
        # progressBar.startBar()
        
    # submit button - starts cut process
    def setSubmitButton(self):
        def submitClicked():
            submit_button.pack_forget()
            submit_button.after(10, self.printResults)
            submit_button.after(100, self.processVideo)
        
        self.options.breakLine()
        submit_button = ctk.CTkButton(self.root, text="Crop video", command=submitClicked)
        submit_button.pack(padx=10, pady=10)

    # process video
    def processVideo(self):
        self.editVideo()
        
    # print data
    def printResults(self):
        self.clearFrame()
        self.file.printFileName(self.file.getFile())
        self.options.breakLine()
        self.setTimeResults()
        self.getProgressBar()

    # clear frame info
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

