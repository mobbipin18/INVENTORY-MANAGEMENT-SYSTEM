from tkinter import*

# create the main self.root
class contactus:
    def __init__(self,root):
        self.root = Tk()
        self.root.title("Contact Us")
        self.root.geometry("400x400")
        self.root.config(bg="#000")

        # create the labels and entry fields
        name_label = Label(self.root, text="Name:", font=("Arial Bold", 12),fg="White", bg="#000")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        name_entry = Entry(self.root, width=30, font=("Arial Bold", 12))
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label = Label(self.root, text="Email:", font=("Arial Bold", 12), fg="White", bg="#000")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        email_entry = Entry(self.root, width=30, font=("Arial Bold", 12))
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        message_label = Label(self.root, text="Message:", font=("Arial Bold", 12), fg="White", bg="#000")
        message_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        message_entry = Text(self.root, width=30, height=10, font=("Arial Bold", 12))
        message_entry.grid(row=2, column=1, padx=10, pady=5)

        # create the submit button
        def submit():
            name = name_entry.get()
            email = email_entry.get()
            message = message_entry.get("1.0", "end")
            print("Name:", name)
            print("Email:", email)
            print("Message:", message)

        submit_button = Button(self.root, text="Submit", font=("Arial Bold", 12), bg="#36000b", fg="white", command=submit)
        submit_button.grid(row=3, column=1, padx=10, pady=5)

if __name__=="__main__":
    root=Tk()
    obj=contactus(root)
    root.mainloop()
