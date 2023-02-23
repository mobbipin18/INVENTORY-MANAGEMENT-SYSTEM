import tkinter
from tkinter import*
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox




    
class billing:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="#1c1c1c")
        self.root.title("BILLING AREA")
        
        def clear_item():
            qty_spinbox.delete(0, tkinter.END)
            qty_spinbox.insert(0, "1")
            itemname_entry.delete(0, tkinter.END)
            price_spinbox.delete(0, tkinter.END)
            price_spinbox.insert(0, "0.0")

        invoice_list = []
        def add_item():
            qty = int(qty_spinbox.get())
            itemname = itemname_entry.get()
            price = float(price_spinbox.get())
            line_total = qty*price
            invoice_item = [qty, itemname, price, line_total]
            tree.insert('',0, values=invoice_item)
            clear_item()
            
            invoice_list.append(invoice_item)

            
        def new_invoice():
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            phone_entry.delete(0, tkinter.END)
            clear_item()
            tree.delete(*tree.get_children())
            
            invoice_list.clear()
            
        def generate_invoice():
            doc = DocxTemplate("invoice_template.docx")
            name = first_name_entry.get()+last_name_entry.get()
            phone = phone_entry.get()
            subtotal = sum(item[3] for item in invoice_list) 
            salestax = 0.1
            total = subtotal*(1-salestax)
            
            doc.render({"name":name, 
                    "phone":phone,
                    "invoice_list": invoice_list,
                    "subtotal":subtotal,
                    "total":total})
            
            doc_name = "Bill of" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
            doc.save(doc_name)
            
            messagebox.showinfo("Invoice Complete", "Invoice Complete")
            
            new_invoice()

        frame = tkinter.Frame(self.root,bg="#1c1c1c")
        frame.pack(padx=20, pady=10)

        first_name_label = tkinter.Label(frame, text="First Name",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        first_name_label.grid(row=0, column=0)
        last_name_label = tkinter.Label(frame, text="Last Name",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        last_name_label.grid(row=0, column=1)

        first_name_entry = tkinter.Entry(frame,font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        last_name_entry = tkinter.Entry(frame,font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        first_name_entry.grid(row=1, column=0)
        last_name_entry.grid(row=1, column=1)

        phone_label = tkinter.Label(frame, text="Phone",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        phone_label.grid(row=0, column=2)
        phone_entry = tkinter.Entry(frame,font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        phone_entry.grid(row=1, column=2)

        qty_label = tkinter.Label(frame, text="Quantity",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        qty_label.grid(row=2, column=0)
        qty_spinbox = tkinter.Spinbox(frame, from_=1, to=100,font=('Arial Bold)', 13,), bg="#1c1c1c", fg="white")
        qty_spinbox.grid(row=3, column=0)

        itemname_label = tkinter.Label(frame, text="Item Name",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        itemname_label.grid(row=2, column=1)
        itemname_entry = tkinter.Entry(frame,font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        itemname_entry.grid(row=3, column=1)

        price_label = tkinter.Label(frame, text="Unit Price",font=('Arial Bold)', 13, 'bold'), bg="#1c1c1c", fg="white")
        price_label.grid(row=2, column=2)
        price_spinbox = tkinter.Spinbox(frame, from_=0.0, to=500, increment=0.5,font=('Arial Bold)', 13), bg="#1c1c1c", fg="white")
        price_spinbox.grid(row=3, column=2)

        add_item_button = tkinter.Button(frame, text = "Add item", command = add_item,font=('Arial Bold)', 13), bg="#6e0211", fg="white")
        add_item_button.grid(row=4, column=2, pady=5)

        columns = ('qty', 'itemname', 'price', 'total')
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.heading('qty', text='Qty')
        tree.heading('itemname', text='Item Name')
        tree.heading('price', text='Unit Price')
        tree.heading('total', text="Total")

            
        tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)


        save_invoice_button = tkinter.Button(frame, text="Import Bill", command=generate_invoice,font=('Arial Bold)', 13), bg="#6e0211", fg="white")
        save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
        new_invoice_button = tkinter.Button(frame, text="Create New Bill", command=new_invoice,font=('Arial Bold)', 13), bg="#6e0211", 
                              fg="white")
        new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)


if __name__=="__main__":
    root=Tk()
    obj=billing(root)
    root.mainloop()