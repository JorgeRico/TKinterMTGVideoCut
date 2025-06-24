from moviepy import VideoFileClip, concatenate_videoclips
from tkinter import *
from datetime import datetime
import customtkinter as ctk
from video.files import File
from video.videoOptions import VideoOptions

class VideoConcat():
    def __init__(self, root):
        self.root       = root
        self.firstFile  = None
        self.secondFile = None
        self.savetitle  = 'file_merged_'+ f'{datetime.now():%Y_%m_%d_%H_%M_%S}' + '.mkv'
        self.options    = VideoOptions(self.root)

    # get contat file name
    def getFileName(self):
        return self.savetitle

    # merge videos
    def concatVideos(self):
        clip1  = VideoFileClip(self.firstFile.getFile())
        clip2  = VideoFileClip(self.secondFile.getFile())
        result = concatenate_videoclips([clip1, clip2])
        result.write_videofile(self.savetitle)

    # concat button upload first file
    def concatFiles(self):
        button = ctk.CTkButton(self.root, text="Select starting video", command=self.getStartingFile)
        button.pack(padx=10, pady=10)
       
    # get from computer first file
    def getStartingFile(self):
        self.clearFrame()
        self.firstFile = File(self.root)
        if self.firstFile.checkComputerFile() == True:
            self.firstFile.printFileName(self.firstFile.getFile())
            self.options.breakLine()
            button = ctk.CTkButton(self.root, text="Select second video", command=self.getsecondFile)
            button.pack(padx=10, pady=10)
            self.options.breakLine()

    # second file upload and submit button
    def getsecondFile(self):
        def submitConcatClick():
            submit_button.pack_forget()
            submit_button.after(10, self.getProgressBar)
            submit_button.after(100, self.concatVideo)

        self.clearFrame()
        self.secondFile = File(self.root)
        if self.secondFile.checkComputerFile() == True:
            self.secondFile.printFileName(self.firstFile.getFile())
            self.secondFile.printFileName(self.secondFile.getFile())
            submit_button = ctk.CTkButton(self.root, text="Concat videos", command=submitConcatClick)
            submit_button.pack(padx=10, pady=10)

    def concatVideo(self):
        self.concatVideos()
        self.clearFrame()
        self.firstFile.printFileName(self.getFileName())
        title = Label(self.root, text="Done!", justify="center")
        title.pack(pady=5)

    # show progress bar
    def getProgressBar(self):
        title = Label(self.root, text="merging videos . . . . ", justify="center")
        title.pack(pady=5)

    # clear frame info
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()