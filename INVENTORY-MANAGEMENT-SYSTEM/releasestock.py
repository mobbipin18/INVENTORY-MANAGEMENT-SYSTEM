from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class releaseform:
    def __init__(self,root):
        self.root=root
        self.root.title("Release stock")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.iconbitmap(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\My_project.ico")
        self.root.focus_force()

        # giving variable for db
        self.var_cn1 = StringVar()
        self.var_cc1 = StringVar()
        self.var_ic3 = StringVar()
        self.var_qty = StringVar()
        self.var_add1 = StringVar()
        self.var_remarks = StringVar()

        # title label
        self.tittlelabel = Label(self.root, text="Release stock", font=("Arial", 33, "bold"), bg="#1c1c1c", fg="white")
        self.tittlelabel.pack(pady=30)

        # Customer Name
        self.cn1 = Label(self.root, text="Customer Name", font=('Arial', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cn1.place(x=240, y=120)
        self.cn1_entry = Entry(self.root, textvariable=self.var_cn1, width=30, font=('Arial', 13), bg="#1c1c1c", fg="white")
        self.cn1_entry.place(x=160, y=150)

        # Customer Contact
        self.cc1 = Label(self.root, text="Customer Contact", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cc1.place(x=232, y=200)
        self.cc1_entry = Entry(self.root, textvariable=self.var_cc1, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.cc1_entry.place(x=160, y=230)

        # Item Code
        self.ic3 = Label(self.root, text="Item Code", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.ic3.place(x=262, y=280)
        self.ic3_entry = Entry(self.root, textvariable=self.var_ic3, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.ic3_entry.place(x=160, y=313)

        # Quantity
        self.qty = Label(self.root, text="Quantity", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.qty.place(x=267, y=360)
        self.qty_entry = Entry(self.root, textvariable=self.var_qty, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.qty_entry.place(x=160, y=390)
        

        # Address
        self.add1 = Label(self.root, text="Address", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.add1.place(x=267, y=440)
        self.add1_entry = Entry(self.root, textvariable=self.var_add1, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.add1_entry.place(x=160, y=470)
    

        # remarks
        self.remarks = Label(self.root, text="Remarks", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.remarks.place(x=265, y=520)
        self.remarks_entry = Entry(self.root, textvariable=self.var_remarks, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.remarks_entry.place(x=160, y=550)

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
        cn1 = self.var_cn1.get()
        cc1 = self.var_cc1.get()
        ic3 = self.var_ic3.get()
        qty = self.var_qty.get()
        add1 = self.var_add1.get()
        remarks = self.var_remarks.get()

        if cn1 == '' or cc1 == '' or ic3 == '' or qty == '' or add1 == '' or remarks == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        try:
                # establishing connection with db
                con = sqlite3.connect(database="ims2.db")
                cur = con.cursor()

                # inserting values
                cur.execute("insert into releaseform (customer_name,customer_contact,item_code,quantity, address, remarks) values (?,?,?,?,?,?)", 
                            (cn1, cc1 , ic3, qty, add1, remarks))

                # saving data into db
                con.commit()
                messagebox.showinfo("Success", "Item added to inventory successfully", parent=self.root)
                self.clear()

        except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def clear(self):
        self.var_cn1.set('')
        self.var_cc1.set('')
        self.var_ic3.set('')
        self.var_qty.set('')
        self.var_add1.set('')
        self.var_remarks.set('')

    def exit(self):
        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
        if option:
            self.root.destroy()
            
if __name__=="__main__":
    root=Tk()
    obj=releaseform(root)
    root.mainloop()
