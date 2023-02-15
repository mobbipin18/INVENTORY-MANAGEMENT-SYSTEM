from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class addclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Adding Stock Form")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.focus_force()

        # giving variable for db
        self.var_ic = StringVar()
        self.var_itn = StringVar()
        self.var_it = StringVar()
        self.var_ip = StringVar()
        self.var_avo = StringVar()
        self.var_cp = StringVar()

        # title label
        self.tittlelabel = Label(self.root, text="ADD STOCKS", font=("Arial", 33, "bold"), bg="#1c1c1c", fg="white")
        self.tittlelabel.pack(pady=30)

        # item code
        self.ic = Label(self.root, text="Item code", font=('Arial', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.ic.place(x=260, y=120)
        self.ic_entry = Entry(self.root, textvariable=self.var_ic, width=30, font=('Arial', 13), bg="#1c1c1c", fg="white")
        self.ic_entry.place(x=160, y=150)

        # item name
        self.itn = Label(self.root, text="Item name", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.itn.place(x=260, y=200)
        self.itn_entry = Entry(self.root, textvariable=self.var_itn, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.itn_entry.place(x=160, y=230)

        # item type
        self.it = Label(self.root, text="Item type", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.it.place(x=260, y=280)
        self.it_entry = Entry(self.root, textvariable=self.var_it, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.it_entry.place(x=160, y=313)

        # item price
        self.ip = Label(self.root, text="Item Price", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.ip.place(x=240, y=360)
        self.ip_entry = Entry(self.root, textvariable=self.var_ip, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        self.ip_entry.place(x=160, y=390)

        # availability
        self.avo = Label(self.root, text="Availability", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.avo.place(x=230, y=440)
        self.avo_combo = ttk.Combobox(self.root, textvariable=self.var_avo, width=28, state="readonly", values=("SELECT", "STOCK AVAILABLE", "OUT OF STOCK", "ORDERED"),font=('Arial Bold)', 13), background="#1c1c1c", foreground="white")
        self.avo_combo.current(0)
        self.avo_combo.place(x=160, y=470)

        # cost price
        self.cp = Label(self.root, text="Cost Price", font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        self.cp.place(x=240, y=520)
        self.cp_entry = Entry(self.root, textvariable=self.var_cp, width=30, font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
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
        ic = self.var_ic.get()
        itn = self.var_itn.get()
        it = self.var_it.get()
        ip = self.var_ip.get()
        avo = self.var_avo.get()
        cp = self.var_cp.get()

        if ic == '' or itn == '' or it == '' or ip == '' or avo == '' or cp == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # establishing connection with db
                con = sqlite3.connect(database="ims.db")
                cur = con.cursor()

                # inserting values
                cur.execute("insert into instock (item_code, item_name, item_type, item_price, availability, cost_price) values (?,?,?,?,?,?)", 
                            (ic, itn, it, ip, avo, cp))

                # saving data into db
                con.commit()
                messagebox.showinfo("Success", "Item added to inventory successfully", parent=self.root)
                self.clear()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_ic.set('')
        self.var_itn.set('')
        self.var_it.set('')
        self.var_ip.set('')
        self.var_avo.set('')
        self.var_cp.set('')

    def exit(self):
        option = messagebox.askyesno("Confirm Exit", "Do you really want to exit?", parent=self.root)
        if option:
            self.root.destroy()
            
if __name__=="__main__":
    root=Tk()
    obj=addclass(root)
    root.mainloop()
