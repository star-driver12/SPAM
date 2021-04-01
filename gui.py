from tkinter import *
from tkinter import filedialog
import threading
import os
from pynput.keyboard import Listener,Key
import spammer
mystrvar=None
text_1=""
spam_thread=spammer.spam(text_1)
class GUI(threading.Thread):
    def __init__(self):
        super().__init__()
        self.Instance_root=Tk()
        self.Instance_root.geometry("0x0")
        self.Instance_root.overrideredirect(1)
        self.root = Toplevel(self.Instance_root)
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")
        global mystrvar
        self.colourselectionvar=StringVar()
        self.path=StringVar()
        self.path.trace("w", lambda name, index, mode, sv=self.path: self.settext(sv))
        mystrvar=self.colourselectionvar
        self.colourselectionvar.trace("w", lambda name, index, mode, sv=self.colourselectionvar: self.changecol(sv))
        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), borderwidth=0, highlightthickness=0, bg="white")
    def settext(self,path):
        t=open(path.get(),'r')
        global text_1
        text_1=t.read()
    def menuwindow(self):
        self.menu=Toplevel(self.Instance_root)
        Entry(self.menu,textvariable=self.path)
        Button(self.menu, text ='Select a .txt/.csv file', command = lambda:self.file_opener()).pack()
    def file_opener(self):
        inputfile = filedialog.askopenfile(initialdir="/")
        print(inputfile.name)
        self.path.set(inputfile.name)
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    Canvas.create_circle = _create_circle
    def create(self):
        self.canvas.grid()
        self.canvas.create_circle((self.root.winfo_screenwidth()-50), 100, 30, fill=self.colourselectionvar.get(), outline="#DDD", width=4)
        self.colourselectionvar.set('red')
        self.menuwindow()
        self.root.mainloop()
    def exit(self):
        self.Instance_root.quit()
        os._exit(0)
    def changecol(self,color):
        self.canvas.create_circle((self.root.winfo_screenwidth()-50), 100, 30, fill=color.get(), outline="#DDD", width=4)
class mylistner(threading.Thread):
    def __init__(self,):
        super().__init__()
    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
    def on_press(self,key):
        global spam_thread
        if type(key)==Key:
            if key==key.f2:
                try:
                    if spam_thread.spammingtoggle==False:
                        mystrvar.set('green')
                        spam_thread=spammer.spam(text_1)
                        spam_thread.start()
                        spam_thread.spammingstart()
                    else:
                        spam_thread.spammingstop()
                        mystrvar.set('red')
                except:
                    pass
            elif key==key.f3:
                os._exit(0)
if __name__=='__main__':
    main=mylistner()
    main.start()
    guithread=GUI()
    guithread.create()