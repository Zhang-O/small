from tkinter import *
import tkinter.messagebox as messagebox
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)
        # os.system('ffmpeg ./QT-742440ans.mp3')

app = Application()
app.master.title('Hello World')

import pygame
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load("./QT-742440ans.mp3")
pygame.mixer.music.play()

app.mainloop()