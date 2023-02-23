from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class classorderdbclass:
    def __init__(self,root):
        self.root=root
        self.root.title("ORDER INVENTORY DATA")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("1400x200+60+200")
        self.root.iconbitmap(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\My_project.ico")
        self.root.focus_force()
        
        
        #----------SEARCH BAR-----------------
        self.delete_label=Entry(self.root,width=20,fg='black',border=0,bg="white",font=('Arial',19))
        self.delete_label.place(x=500,y=15)
        
        #Delete button
        self.delete_btn = Button(self.root, text="DELETE", width=10, font=('Arial Bold)', 13), bg="#6e0211", 
                              fg="white",command=self.delete)
        self.delete_btn.place(x=750,y=15)
        
        #fillings ---------------------------
        classorder_frame=Frame(self.root,bd=3,relief=RIDGE)
        classorder_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(classorder_frame,orient=VERTICAL)
        scrollx=Scrollbar(classorder_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        
        
        self.classordertable=ttk.Treeview(classorder_frame,columns=("ic1", "it1", "cc", "cn", "fb", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.classordertable.heading("ic1",text="ITEM CODE")
        self.classordertable.heading("it1",text="ITEM NAME")
        self.classordertable.heading("cc",text="ITEM TYPE")
        self.classordertable.heading("cn",text="CUSTOMER NAME")
        self.classordertable.heading("fb",text="FOLLOWED BY")
        self.classordertable.heading("status",text="CUSTOMER CONTACT")
        self.classordertable["show"]="headings"
        
        self.classordertable.column("ic1",width=100)
        self.classordertable.column("it1",width=100)
        self.classordertable.column("cc",width=150)
        self.classordertable.column("cn",width=100)
        self.classordertable.column("fb",width=200)
        self.classordertable.column("status",width=100)
        
        
        self.classordertable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.classordertable.xview)
        scrolly.config(command=self.classordertable.yview)
        
        self.show()

    def delete(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        
        con.execute("DELETE from class order WHERE item_code = "+ self.delete_label.get())

        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
         
        if option:
            self.delete_label.delete(0, END)
        
        
        con.commit()
        con.close()
        
        self.show()

    def show(self):
        con = sqlite3.connect(database="ims3.db")
        cur = con.cursor()
        try:
            cur.execute("select * from classorder")
            rows1=cur.fetchall()
            self.classordertable.delete(*self.classordertable.get_children())
            for row in rows1:
                self.classordertable.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        
if __name__=="__main__":
    root=Tk()
    obj=classorderdbclass(root)
    root.mainloop()