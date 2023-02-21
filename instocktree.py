from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class adddbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("INSTOCK DATAS")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("1400x200+60+200")
        self.root.focus_force()
        
        
        #----------SEARCH BAR-----------------
        code= Entry(self.root,width=50,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',15))
        code.place(x=450,y=15)
        code.insert(0,'Search order inventory')
        #fillings ---------------------------
        instock_frame=Frame(self.root,bd=3,relief=RIDGE)
        instock_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(instock_frame,orient=VERTICAL)
        scrollx=Scrollbar(instock_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        
        
        self.instocktable=ttk.Treeview(instock_frame,columns=("ic", "in", "it", "ip", "av", "cp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.instocktable.heading("ic",text="ITEM CODE")
        self.instocktable.heading("in",text="ITEM NAME")
        self.instocktable.heading("it",text="ITEM TYPE")
        self.instocktable.heading("ip",text="ITEM PRICE")
        self.instocktable.heading("av",text="ITEM AVAILABILITY")
        self.instocktable.heading("cp",text="COST PRICE")
        self.instocktable["show"]="headings"
        
        self.instocktable.column("ic",width=100)
        self.instocktable.column("in",width=100)
        self.instocktable.column("it",width=150)
        self.instocktable.column("ip",width=100)
        self.instocktable.column("av",width=200)
        self.instocktable.column("cp",width=100)
        
        
        self.instocktable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.instocktable.xview)
        scrolly.config(command=self.instocktable.yview)
        
        self.show()
        
    def show(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            cur.execute("select * from instock")
            rows1=cur.fetchall()
            self.instocktable.delete(*self.instocktable.get_children())
            for row in rows1:
                self.instocktable.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=adddbclass(root)
    root.mainloop()