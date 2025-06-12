from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
from video.videoOptions import VideoOptions
from video.videoEdit import VideoEdit
from video.progressBar import ProgressBar
from errors.errors import Errors

class VideoFile():
    def __init__(self, root):
        self.root      = root
        self.start     = None
        self.end       = None
        self.filename  = None

    def getFileExtension(self):
        self.filename = filedialog.askopenfilename()
        fileExtension = self.filename[-4:]

        return fileExtension
    
    def printFileName(self):
        label = Label(self.root, text="File: ", justify="left")
        label.pack(pady=5, padx=10, anchor="w")

        frame      = Frame(self.root, width="100", bg='#0c446e')
        some_label = Label(frame, text=self.filename, justify="left", fg='#fdde0e', bg='#0c446e')
        some_label.pack(pady=5, padx=10, anchor="w")

        frame['borderwidth'] = 1
        frame['relief']      = 'solid'
        frame.pack(side="top", fill="x", pady=5, padx=10)

    def selectFile(self):
        fileExtension = self.getFileExtension()

        if fileExtension != '':
            if fileExtension not in [ '.mov', '.flv', '.avi', '.jpg' ]:
                error = Errors()
                error.notAllowedError()
            else:
                self.printFileName()
                self.start = VideoOptions(self.root)
                self.start.setTimeOptions("Start to cut on :")
                self.end   = VideoOptions(self.root)
                self.end.setTimeOptions("End to cut on :")

                self.setSubmitButton()

    def setTimeResults(self):
        self.start.setTimeResult()
        self.end.setTimeResult()

    def editVideo(self):
        editVideo = VideoEdit(self.start.getTimeResult(), self.end.getTimeResult())
        editVideo.edit()

    def getProgressBar(self):
        progressBar = ProgressBar(self.root)
        progressBar.startBar()

    def breakLine(self):
        some_label = Label(self.root, justify="left")
        some_label.pack(pady=0, padx=10, anchor="w")
        
    def setSubmitButton(self):
        def submitClicked():
            self.processVideo()   
        
        self.breakLine()
        submit_button = ctk.CTkButton(self.root, text="Crop video", command=submitClicked)
        submit_button.pack(padx=10, pady=10)

    def processVideo(self):
        self.setTimeResults()
        self.editVideo()
        self.clearFrame()
        self.printFileName()
        self.breakLine()
        self.printResults()
        self.breakLine()
        self.getProgressBar()

    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def printResults(self):
        title = Label(self.root, text="start: " + self.start.getTimeResult(), justify="center")
        title.pack(pady=5)
        title = Label(self.root, text="end: " + self.end.getTimeResult(), justify="center")
        title.pack(pady=5)