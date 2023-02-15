from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class socialdbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("SOCIAL FORM DATAS")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x200")
        self.root.focus_force()
        
        
        #fillings ---------------------------
        socialform_frame=Frame(self.root,bd=3,relief=RIDGE)
        socialform_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(socialform_frame,orient=VERTICAL)
        scrollx=Scrollbar(socialform_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.instocktable=ttk.Treeview(socialform_frame,columns=("ic1", "itn1", "cc", "cn", "fb", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.instocktable.heading("ic1",text="ITEM CODE")
        self.instocktable.heading("itn1",text="ITEM NAME")
        self.instocktable.heading("cc",text="CUSTOMER CONTACT")
        self.instocktable.heading("cn",text="CUSTOMER NAME")
        self.instocktable.heading("fb",text="FOLLOWED BY")
        self.instocktable.heading("status",text="STATUS")
        self.instocktable["show"]="headings"
        
        self.instocktable.column("ic1",width=100)
        self.instocktable.column("itn1",width=100)
        self.instocktable.column("cc",width=150)
        self.instocktable.column("cn",width=100)
        self.instocktable.column("fb",width=200)
        self.instocktable.column("status",width=100)
        
        
        self.instocktable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.instocktable.xview)
        scrolly.config(command=self.instocktable.yview)
        
        self.show()
        
    def show(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from ")
            rows=cur.fetchall()
            self.instocktable.delete(*self.instocktable.get_children())
            for row in rows:
                self.instocktable.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=socialdbclass(root)
    root.mainloop()