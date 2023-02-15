from tkinter import*
from subprocess import call
from PIL import Image, ImageTk

class signin:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="#000")
        self.root.state("zoomed")
        self.root.title("SIGN IN")
        
        btn1=Button(self.root)
     
     
        
if __name__=="__main__":
    root=Tk()
    obj=signin(root)
    root.mainloop()