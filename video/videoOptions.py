from tkinter import *

class VideoOptions():
    def __init__(self, root):
        self.root        = Frame(root)
        self.hours       = StringVar(value=00)
        self.minutes     = StringVar(value=00)
        self.seconds     = StringVar(value=00)
        self.miliseconds = StringVar(value=00)
        self.result      = StringVar(value=None)

    def setTimeOptions(self, text):
        self.root.pack(pady=5, padx=10)
        self.setTitleOptions(text)
        self.printSpinbox(self.hours, 0, 12)
        self.printSeparator()
        self.printSpinbox(self.minutes, 0 , 59)
        self.printSeparator()
        self.printSpinbox(self.seconds, 0, 59)
        self.printSeparator()
        self.printSpinbox(self.miliseconds, 0, 999)

    def setTitleOptions(self, text):
        title = Label(self.root, text=text, justify="left")
        title.pack(pady=5, anchor="w")

    def printSeparator(self):
        separator = Label(self.root, text=":")
        separator.pack(side=LEFT)

    def printSpinbox(self, item, fromTime, toTime):
        spinbox = Spinbox(self.root, from_=fromTime, to=toTime, textvariable=item, wrap=True, width=8)
        spinbox.pack(side=LEFT, anchor="w")

    def setTimeResult(self):
        self.result.set( self.hours.get() + ':' + self.minutes.get() + ':' + self.seconds.get() + ':' + self.miliseconds.get() )

    def getTimeResult(self):
        return self.result.get()
