from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class socialclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Social Media Form")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.focus_force()

        # giving variable for db
        self.var_ic1 = StringVar()
        self.var_itn1 = StringVar()
        self.var_cc = StringVar()
        self.var_cn = StringVar()
        self.var_fb = StringVar()
        self.var_status = StringVar()

        # title label
        self.tittlelabel = Label(self.root, text="Social Media Form", font=("Arial", 33, "bold"), bg="#1c1c1c", fg="white")
        self.tittlelabel.pack(pady=30)

        # item code
        self.ic1 = Label(self.root, text="Item code", font=('Arial', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.ic1.place(x=260, y=120)
        self.ic1_entry = Entry(self.root, textvariable=self.var_ic1, width=30, font=('Arial', 13), bg="#1c1c1c", fg="white")
        self.ic1_entry.place(x=160, y=150)

        # item name
        self.itn1 = Label(self.root, text="Item name", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.itn1.place(x=260, y=200)
        self.itn1_entry = Entry(self.root, textvariable=self.var_itn1, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.itn1_entry.place(x=160, y=230)

        # item type
        self.cc = Label(self.root, text="Customer Conatact", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cc.place(x=260, y=280)
        self.cc_entry = Entry(self.root, textvariable=self.var_cc, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.cc_entry.place(x=160, y=313)

        # customer name
        self.cn = Label(self.root, text="Customer Name", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cn.place(x=240, y=360)
        self.cn_entry = Entry(self.root, textvariable=self.var_cn, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.cn_entry.place(x=160, y=390)
        

        # followed by
        self.fb = Label(self.root, text="Followed By", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.fb.place(x=240, y=440)
        self.fb_entry = Entry(self.root, textvariable=self.var_fb, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.fb_entry.place(x=160, y=470)
    

        # status
        self.status = Label(self.root, text="Status", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.status.place(x=240, y=520)
        self.cp_entry = Entry(self.root, textvariable=self.var_status, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
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
        ic1 = self.var_ic1.get()
        itn1 = self.var_itn1.get()
        cc = self.var_cc.get()
        cn = self.var_cn.get()
        fb = self.var_fb.get()
        status = self.var_status.get()

        if ic1 == '' or itn1 == '' or cc == '' or cn == '' or fb == '' or status == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # establishing connection with db
                con = sqlite3.connect(database="ims1.db")
                cur = con.cursor()

                # inserting values
                cur.execute("insert into socialform(item_code, item_name, customer_name, customer_contact, followed_by, status) values (?,?,?,?,?,?)", 
                            (ic1, itn1, cc, cn, fb, status))

                # saving data into db
                con.commit()
                messagebox.showinfo("Success", "Item added to inventory successfully", parent=self.root)
                self.clear()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def clear(self):
        self.var_ic1.set('')
        self.var_itn1.set('')
        self.var_cc.set('')
        self.var_cn.set('')
        self.var_fb.set('')
        self.var_status.set('')

    def exit(self):
        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
        if option:
            self.root.destroy()
            
if __name__=="__main__":
    root=Tk()
    obj=socialclass(root)
    root.mainloop()
