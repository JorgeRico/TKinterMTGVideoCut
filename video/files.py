from tkinter import *
from tkinter import filedialog

class File():
    def __init__(self, root):
        self.root     = root
        # get file from computer
        self.filename = filedialog.askopenfilename()

    # get file name
    def getFileName(self):
        return self.filename

    # get file extension
    def getFileExtension(self):
        fileExtension = self.filename[-4:]

        return fileExtension
    
    # allowed file extensions
    # TODO: delete .jpg 
    def getAllowedFileExtensions(self):
        return [ '.mov', '.flv', '.avi', '.jpg' ]
    
    # print filename
    def printFileName(self):
        label = Label(self.root, text="File: ", justify="left")
        label.pack(pady=5, padx=10, anchor="w")

        frame      = Frame(self.root, width="100", bg='#0c446e')
        some_label = Label(frame, text=self.filename, justify="left", fg='#fdde0e', bg='#0c446e')
        some_label.pack(pady=5, padx=10, anchor="w")

        frame['borderwidth'] = 1
        frame['relief']      = 'solid'
        frame.pack(side="top", fill="x", pady=5, padx=10)

            