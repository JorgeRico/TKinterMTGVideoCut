from tkinter import *
from tkinter import filedialog
import os
from errors.errors import Errors

class File():
    def __init__(self, root):
        self.root     = root
        # get file from computer
        self.file     = filedialog.askopenfilename()
        self.filename = os.path.basename(self.file)

    # select file on computer
    def checkComputerFile(self):
        if self.getFileExtension() != '':
            if self.getFileExtension() not in self.getAllowedFileExtensions():
                error = Errors()
                error.notAllowedError()
                return False

        return True

    # get file with absolute route
    def getFile(self):
        return self.file

    # get file name
    def getFileName(self):
        return self.filename
    
    # get file extension
    def getFileExtension(self):
        fileExtension = self.filename[-4:]

        return fileExtension
    
    # allowed file extensions
    def getAllowedFileExtensions(self):
        return [ '.mov', '.flv', '.avi', '.mp4', '.mkv' ]
    
    # print filename
    def printFileName(self, filename):
        label = Label(self.root, text="File: ", justify="left")
        label.pack(pady=5, padx=10, anchor="w")

        frame      = Frame(self.root, width="100", bg='#0c446e')
        some_label = Label(frame, text=filename, justify="left", fg='#fdde0e', bg='#0c446e')
        some_label.pack(pady=5, padx=10, anchor="w")

        frame['borderwidth'] = 1
        frame['relief']      = 'solid'
        frame.pack(side="top", fill="x", pady=5, padx=10)

            