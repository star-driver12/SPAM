import time
import keyboard
import threading
class spam(threading.Thread):
    def __init__(self,string:str,repeat=0):
        super().__init__()
        self.repeat=repeat
        self.spammingtoggle=False
        self.destroy=False
        self.string=string
        self.temprepeat=repeat
    def run(self):
        while True:
            while self.repeat>=0:
                for char in self.string:
                    if self.spammingtoggle==True:
                        try:
                            keyboard.press_and_release(char[0])
                        except Exception as e:
                            print(e)
                        time.sleep(0.01)
                if self.destroy==True:
                    break
                self.repeat-=1
    def spammingstart(self):
        self.repeat=self.temprepeat
        self.spammingtoggle=True
    def spammingstop(self):
        self.spammingtoggle=False