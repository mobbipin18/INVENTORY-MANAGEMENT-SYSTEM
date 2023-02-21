from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class classorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Order form")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.focus_force()

        # giving variable for db
        self.var_ic3 = StringVar() 
        self.var_itn5 = StringVar()
        self.var_it4 = StringVar()
        self.var_cn = StringVar()
        self.var_fb = StringVar()
        self.var_it43 = StringVar()

        # title label
        self.tittlelabel = Label(self.root, text="ORDER INVENTORY", font=("Arial", 33, "bold"), bg="#1c1c1c", fg="white")
        self.tittlelabel.pack(pady=30)

        # item code
        self.ic3 = Label(self.root, text="Item code", font=('Arial', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.ic3.place(x=260, y=120)
        self.ic3_entry = Entry(self.root, textvariable=self.var_ic3, width=30, font=('Arial', 13), bg="#1c1c1c", fg="white")
        self.ic3_entry.place(x=160, y=150)

        # item name
        self.itn5 = Label(self.root, text="Item name", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.itn5.place(x=260, y=200)
        self.itn5_entry = Entry(self.root, textvariable=self.var_itn5, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.itn5_entry.place(x=160, y=230)

        # item type
        self.it4 = Label(self.root, text="Item type", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.it4.place(x=260, y=280)
        self.it4_entry = Entry(self.root, textvariable=self.var_it4, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.it4_entry.place(x=160, y=313)

        # customer name
        self.cn = Label(self.root, text="Customer Name", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cn.place(x=240, y=360)
        self.cn_entry = Entry(self.root, textvariable=self.var_cn, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.cn_entry.place(x=160, y=390)
        

        # followed by
        self.fb = Label(self.root, text="Followed By", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.fb.place(x=252, y=440)
        self.fb_entry = Entry(self.root, textvariable=self.var_fb, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.fb_entry.place(x=160, y=470)
    

        # Customer contact
        self.it43 = Label(self.root, text="Customer contact", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.it43.place(x=230, y=520)
        self.cp_entry = Entry(self.root, textvariable=self.var_it43, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.cp_entry.place(x=160, y=550)

        # buttons
        self.btn_frame = Frame(self.root, bg="#1c1c1c")
        self.btn_frame.place(x=150, y=620, width=595, height=50)

        self.add_btn = Button(self.btn_frame, text="Add", width=10, font=('Arial Bold)', 13), bg="#6e0211", 
                              fg="white", command=self.add_stock)
        self.add_btn.grid(row=0, column=0)

        self.clear_btn = Button(self.btn_frame, text="Clear", width=10, font=('Arial Bold)', 13), bg="#ECECEC", 
                                fg="black", command=self.clear)
        self.clear_btn.grid(row=0, column=1)

        self.exit_btn = Button(self.btn_frame, text="Exit", width=10, font=('Arial Bold)', 13), bg="#6e0211", 
                               fg="white", command=self.exit)
        self.exit_btn.grid(row=0, column=2)

    def add_stock(self):
        # getting form data
        ic3 = self.var_ic3.get()
        itn5 = self.var_itn5.get()
        it4 = self.var_it4.get()
        cn = self.var_cn.get()
        fb = self.var_fb.get()
        it43 = self.var_it43.get()

        if ic3 == '' or itn5 == '' or it4 == '' or cn == '' or fb == '' or it43 == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # establishing connection with db
                con = sqlite3.connect(database="ims3.db")
                cur = con.cursor()

                # inserting values
                cur.execute("insert into classorder(item_code, item_name, item_type , customer_name, followed_by, customer_contact) values (?,?,?,?,?,?)", 
                            (ic3, itn5, it4, cn, fb, it43))

                # saving data into db
                con.commit()
                messagebox.showinfo("Suit4ess", "Item added to inventory suit4essfully", parent=self.root)
                self.clear()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def clear(self):
        self.var_ic3.set('')
        self.var_itn5.set('')
        self.var_it4.set('')
        self.var_cn.set('')
        self.var_fb.set('')
        self.var_it43.set('')

    def exit(self):
        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
        if option:
            self.root.destroy()
            
if __name__=="__main__":
    root=Tk()
    obj=classorder(root)
    root.mainloop()
