from tkinter import*
from datetime import datetime

# create the main self.root
class contactus:
    def __init__(self,root):
        self.root = root
        self.root.title("Contact Us")
        self.root.geometry("400x400+600+205")
        self.root.config(bg="#1c1c1c")

        # create the labels and entry fields
        name_label = Label(self.root, text="Name:", font=("Arial Bold", 12), bg="#1c1c1c",fg="white")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        name_entry = Entry(self.root, width=30, font=("Arial Bold", 12))
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        email_label = Label(self.root, text="Email:", font=("Arial Bold", 12), bg="#1c1c1c",fg="white")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        email_entry = Entry(self.root, width=30, font=("Arial Bold", 12))
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        message_label = Label(self.root, text="Message:", font=("Arial Bold", 12), bg="#1c1c1c",fg="white")
        message_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        message_entry = Text(self.root, width=30, height=10, font=("Arial Bold", 12))
        message_entry.grid(row=2, column=1, padx=10, pady=5)

        # create the submit button
        def submit():
            # get the current date and time
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

            # get the entered contact information
            name = name_entry.get()
            email = email_entry.get()
            message = message_entry.get("1.0", "end")

            # create the contact string
            contact = f"{dt_string} | {name} | {email} | {message}"

            # save the contact information to the database file
            with open("contacts.txt", "a") as f:
                f.write(contact + "\n")

            # clear the entry fields
            name_entry.delete(0, END)
            email_entry.delete(0, END)
            message_entry.delete("1.0", END)

        submit_button = Button(self.root, text="Submit", font=("Arial Bold", 12), bg="#36000b", fg="white", command=submit)
        submit_button.grid(row=3, column=1, padx=10, pady=5)

if __name__=="__main__":
    root=Tk()
    obj=contactus(root)
    root.mainloop()
