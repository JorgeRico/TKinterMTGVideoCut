from tkinter import *

class About():
    def __init__(self, root):
        self.root  = root
        self.title = "About"

    # about section
    def setAbout(self):
        self.getDescriptionBlockText("How to use", 10, 10)

        texts = [ "1. Select a video file", "2. Select start video time to cut", "3. Select end video time to cut", "4. Press process button", "5. Wait for success message", "6. Use your new croped video" ]
        for item in texts:
            self.getDescriptionBlockText(item, 5, 20)

    # block text
    def getDescriptionBlockText(self, text, py, px):
        label = Label(self.root, text=text, justify="left")
        label.pack(pady=py, padx=px, anchor="w")
