from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class orderinvdbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("ORDER INVENTORY DATAS")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x200")
        self.root.focus_force()
        
        
        #fillings ---------------------------
        orderinv_frame=Frame(self.root,bd=3,relief=RIDGE)
        orderinv_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(orderinv_frame,orient=VERTICAL)
        scrollx=Scrollbar(orderinv_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.orderinv=ttk.Treeview(orderinv_frame,columns=("ic1", "itn1", "cc", "cn", "fb", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.orderinv.heading("ic1",text="ITEM CODE")
        self.orderinv.heading("itn1",text="ITEM NAME")
        self.orderinv.heading("cc",text="CUSTOMER CONTACT")
        self.orderinv.heading("cn",text="CUSTOMER NAME")
        self.orderinv.heading("fb",text="FOLLOWED BY")
        self.orderinv.heading("status",text="STATUS")
        self.orderinv["show"]="headings"
        
        self.orderinv.column("ic1",width=100)
        self.orderinv.column("itn1",width=100)
        self.orderinv.column("cc",width=150)
        self.orderinv.column("cn",width=100)
        self.orderinv.column("fb",width=200)
        self.orderinv.column("status",width=100)
        
        
        self.orderinv.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.orderinv.xview)
        scrolly.config(command=self.orderinv.yview)
        
        self.show()
        
    def show(self):
        con = sqlite3.connect(database="ims3.db")
        cur = con.cursor()
        try:
            cur.execute("select * from ")
            rows=cur.fetchall()
            self.orderinv.delete(*self.orderinv.get_children())
            for row in rows:
                self.orderinv.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=orderinvdbclass(root)
    root.mainloop()