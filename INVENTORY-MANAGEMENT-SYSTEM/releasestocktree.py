from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class releaseformdbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("RELEASE STOCKS")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("1400x200+60+200")
        self.root.focus_force()
        self.root.iconbitmap(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\My_project.ico")
        
        
        #----------SEARCH BAR-----------------
        self.delete_label=Entry(self.root,width=20,fg='black',border=0,bg="white",font=('Arial',19))
        self.delete_label.place(x=500,y=15)
        
        #Delete button
        self.delete_btn = Button(self.root, text="DELETE", width=10, font=('Arial Bold)', 13), bg="#6e0211", 
                              fg="white",command=self.delete)
        self.delete_btn.place(x=750,y=15)

        #fillings ---------------------------
        releaseform_frame=Frame(self.root,bd=3,relief=RIDGE)
        releaseform_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(releaseform_frame,orient=VERTICAL)
        scrollx=Scrollbar(releaseform_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        
        
        self.releaseformtable=ttk.Treeview(releaseform_frame,columns=("ic", "in", "it", "ip", "av", "cp"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.releaseformtable.heading("ic",text="CUSTOMER NAME")
        self.releaseformtable.heading("in",text="CUSTOMER CONTACT")
        self.releaseformtable.heading("it",text="ITEM CODE")
        self.releaseformtable.heading("ip",text="QUANTITY")
        self.releaseformtable.heading("av",text="ADDRESS")
        self.releaseformtable.heading("cp",text="REMARKS")
        self.releaseformtable["show"]="headings"
        
        self.releaseformtable.column("ic",width=100)
        self.releaseformtable.column("in",width=100)
        self.releaseformtable.column("it",width=150)
        self.releaseformtable.column("ip",width=100)
        self.releaseformtable.column("av",width=200)
        self.releaseformtable.column("cp",width=100)
        
        
        self.releaseformtable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.releaseformtable.xview)
        scrolly.config(command=self.releaseformtable.yview)
        
        self.show()

    def delete(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        
        con.execute("DELETE from release stock WHERE item_code = "+ self.delete_label.get())

        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
         
        if option:
            self.delete_label.delete(0, END)
        
        
        con.commit()
        con.close()
        
        self.show()

    def show(self):
        con = sqlite3.connect(database="ims2.db")
        cur = con.cursor()
        try:
            cur.execute("select * from releaseform")
            rows1=cur.fetchall()
            self.releaseformtable.delete(*self.releaseformtable.get_children())
            for row in rows1:
                self.releaseformtable.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=releaseformdbclass(root)
    root.mainloop()