import customtkinter as ctk

class ProgressBar():
    def __init__(self, root):
        self.root        = root
        self.progressBar = None
    
    # start progress bar
    def startBar(self):
        self.progressbar = ctk.CTkProgressBar(self.root, orientation="horizontal")
        self.progressbar.pack()
        self.progressbar.start()