from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class socialdbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("SOCIAL MEDIA DATA")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("1400x200+60+80")
        self.root.focus_force()
        
        
        #----------SEARCH BAR-----------------
        code= Entry(self.root,width=50,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',15))
        code.place(x=450,y=15)
        code.insert(0,'Search order inventory')
        #fillings ---------------------------
        socialmedia_frame=Frame(self.root,bd=3,relief=RIDGE)
        socialmedia_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(socialmedia_frame,orient=VERTICAL)
        scrollx=Scrollbar(socialmedia_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        
        
        self.socialmediatable=ttk.Treeview(socialmedia_frame,columns=("ic", "in", "it", "ip", "av", "cp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.socialmediatable.heading("ic",text="ITEM CODE")
        self.socialmediatable.heading("in",text="ITEM NAME")
        self.socialmediatable.heading("it",text="ITEM TYPE")
        self.socialmediatable.heading("ip",text="ITEM PRICE")
        self.socialmediatable.heading("av",text="ITEM AVAILABILITY")
        self.socialmediatable.heading("cp",text="COST PRODUCTION")
        self.socialmediatable["show"]="headings"
        
        self.socialmediatable.column("ic",width=100)
        self.socialmediatable.column("in",width=100)
        self.socialmediatable.column("it",width=150)
        self.socialmediatable.column("ip",width=100)
        self.socialmediatable.column("av",width=200)
        self.socialmediatable.column("cp",width=100)
        
        
        self.socialmediatable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.socialmediatable.xview)
        scrolly.config(command=self.socialmediatable.yview)
        
        self.show()
        
    def show(self):
        con = sqlite3.connect(database="ims1.db")
        cur = con.cursor()
        try:
            cur.execute("select * from socialmedia")
            rows1=cur.fetchall()
            self.socialmediatable.delete(*self.socialmediatable.get_children())
            for row in rows1:
                self.socialmediatable.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=socialdbclass(root)
    root.mainloop()