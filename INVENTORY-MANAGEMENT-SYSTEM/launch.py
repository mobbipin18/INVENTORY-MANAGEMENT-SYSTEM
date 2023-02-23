from tkinter import*
from tkinter import font
from PIL import ImageTk, Image 
import time
from dashboard import IMS
import sys
import os


class launchscreen:
    def __init__(self,root):
        self.root=root
        #Using piece of code from old splash screen
        width_of_window = 427
        height_of_window = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        #self.root.configure(bg='#ED1B76')
        self.root.overrideredirect(1) #for hiding titlebar

        #new window to open
        def form(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=IMS(self.new_win)

        Frame(self.root, width=427, height=250, bg='#272727').place(x=0,y=0)
        label1=Label(self.root, text='INVENTORY MANAGEMENT SYSTEM ', fg='white', bg='#272727') 
        label1.configure(font=("Game Of Squids", 24, "bold"))   
        label1.place(x=120,y=50)

        label2=Label(self.root, text='Loading...', fg='white', bg='#272727') 
        label2.configure(font=("Calibri", 11))
        label2.place(x=10,y=215)

        #making animation

        image_a=ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\c2.png'))
        image_b=ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\c1.png'))




        for i in range(5): #5loops
            l1=Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
            l2=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
            l3=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
            l4=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
            l2=Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
            l3=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
            l4=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
            l2=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
            l3=Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
            l4=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
            l2=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
            l3=Label(self.root, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
            l4=Label(self.root, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)
            
            



try:
    root = Tk()
    launchscreen(root)
    root.mainloop()
except Exception as e:
    print("Error while launching window:", e)
    root.destroy()


