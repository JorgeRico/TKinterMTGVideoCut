from tkinter import *
from about.about import About
from video.videofile import VideoFile

class AppMenu():
    def __init__(self):
        self.root = Tk()
        self.setDimensionAndTitle()
        self.setMenu()

    # set main frame
    def setDimensionAndTitle(self):
        self.root.title("Video Cut App")
        self.root.geometry("500x500")

    # menu
    def setMenu(self):
        self.menubar = Menu(self.root)
        self.setOptions()
        self.root.config(menu=self.menubar)
        self.root.mainloop()

    # menu options
    def setOptions(self):
        self.getFileMenu()
        self.getHelpMenu()

    # get file menu option
    def getFileMenu(self):
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.getFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)

        self.menubar.add_cascade(label="File", menu=filemenu)
    
    # get help menu option
    def getHelpMenu(self):
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.getAbout)

        self.menubar.add_cascade(label="Help", menu=helpmenu)

    # app exit
    def exit(self):
        self.root.quit()

    # get file
    def getFile(self):
        self.clearFrame()
        video = VideoFile(self.root)
        video.selectFile()

    # get abount
    def getAbout(self):
        self.clearFrame()
        about = About(self.root)
        about.setAbout()

    # clear frame
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()