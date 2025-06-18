from tkinter import *
import customtkinter as ctk
from video.videoOptions import VideoOptions
from video.videoEdit import VideoEdit
# from video.progressBar import ProgressBar
from video.files import File
from errors.errors import Errors

class VideoFile():
    def __init__(self, root):
        self.root  = root
        self.start = None
        self.end   = None
        self.file  = None

    # select file on computer
    def selectFile(self):
        self.file = File(self.root)

        if self.file.getFileExtension() != '':
            if self.file.getFileExtension() not in self.file.getAllowedFileExtensions():
                error = Errors()
                error.notAllowedError()
            else:
                self.file.printFileName(self.file.getFile())
                self.start = VideoOptions(self.root)
                self.start.setTimeOptions("Start to cut on :")
                self.end   = VideoOptions(self.root)
                self.end.setTimeOptions("End to cut on :")
                self.setSubmitButton()

    # set spinbox results
    def setTimeResults(self):
        self.start.setTimeResult()
        self.end.setTimeResult()
       
    # call edit video
    def editVideo(self):
        editVideo = VideoEdit(self.start.getTimeResult(), self.end.getTimeResult(), self.file.getFile())
        editVideo.edit()
        self.clearFrame()
        self.file.printFileName(editVideo.getCutFileName())
        title = Label(self.root, text="Done!", justify="center")
        title.pack(pady=5)

    # show progress bar
    def getProgressBar(self):
        title = Label(self.root, text="cutting video . . . . ", justify="center")
        title.pack(pady=5)
        # extrange progressbar stop on edit video launch
        # progressBar = ProgressBar(self.root)
        # progressBar.startBar()

    # add a break line space
    def breakLine(self):
        some_label = Label(self.root, justify="left")
        some_label.pack(pady=0, padx=10, anchor="w")
        
    # submit button - starts cut process
    def setSubmitButton(self):
        def submitClicked():
            submit_button.pack_forget()
            submit_button.after(10, self.printResults)
            submit_button.after(100, self.processVideo)
        
        self.breakLine()
        submit_button = ctk.CTkButton(self.root, text="Crop video", command=submitClicked)
        submit_button.pack(padx=10, pady=10)

    # process video
    def processVideo(self):
        self.editVideo()
        
    # print data
    def printResults(self):
        self.clearFrame()
        self.file.printFileName(self.file.getFile())
        self.breakLine()
        self.setTimeResults()
        self.getProgressBar()

    # clear frame info
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()