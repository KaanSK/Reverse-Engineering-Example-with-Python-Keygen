#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#Kaan Sadik KARADAG 156328IVCM
#kaakar@ttu.ee

import Tkinter
import re
import pygame

def KeyGen(self):
    serial = "Validation Error in Name."
    match = re.search('^[a-z]*$', self.entryVariable.get().lower())
    if match is None or len(self.entryVariable.get().lower()) < 3:
        return serial
    small_letters = map(chr, range(ord('a'), ord('z') + 1))
    serial = "".join([small_letters[(small_letters.index(char) + 10) % len(small_letters)] for char in
                self.entryVariable.get().lower()])
    return serial

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        #self.entryVariable.set(u"Enter text here.")

        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Entry(self,textvariable=self.labelVariable)
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        label.configure(background='black')
        label.configure(fg='white')
        #self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        #self.geometry(self.geometry())
        self.geometry("375x50+100+100")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)



    def OnButtonClick(self):
        self.labelVariable.set( KeyGen(self) )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( KeyGen(self) )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Jaanus Kääp Malware Homework KeyGen.')
    pygame.init()
    pygame.mixer.music.load("music.xm")
    pygame.mixer.music.play(loops=-1)
    app.mainloop()