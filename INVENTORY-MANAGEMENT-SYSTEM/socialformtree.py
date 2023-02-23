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
        socialmedia_frame=Frame(self.root,bd=3,relief=RIDGE)
        socialmedia_frame.place(x=0,y=50,relwidth=1,height=150)
        
        scrolly=Scrollbar(socialmedia_frame,orient=VERTICAL)
        scrollx=Scrollbar(socialmedia_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        
        
        self.socialmediatable=ttk.Treeview(socialmedia_frame,columns=("ic1", "it1", "cc", "cn", "fb", "status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.socialmediatable.heading("ic1",text="ITEM CODE")
        self.socialmediatable.heading("it1",text="ITEM NAME")
        self.socialmediatable.heading("cc",text="CUSTOMER CONTACT")
        self.socialmediatable.heading("cn",text="CUSTOMER NAME")
        self.socialmediatable.heading("fb",text="FOLLOWED BY")
        self.socialmediatable.heading("status",text="STATUS")
        self.socialmediatable["show"]="headings"
        
        self.socialmediatable.column("ic1",width=100)
        self.socialmediatable.column("it1",width=100)
        self.socialmediatable.column("cc",width=150)
        self.socialmediatable.column("cn",width=100)
        self.socialmediatable.column("fb",width=200)
        self.socialmediatable.column("status",width=100)
        
        
        self.socialmediatable.pack(fill=BOTH,expand=1)
        
        scrollx.config(command=self.socialmediatable.xview)
        scrolly.config(command=self.socialmediatable.yview)
        
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
        con = sqlite3.connect(database="ims1.db")
        cur = con.cursor()
        try:
            cur.execute("select * from socialform")
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