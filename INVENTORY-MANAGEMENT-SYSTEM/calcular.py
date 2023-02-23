from tkinter import *
from subprocess import call
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.config(bg="#1c1c1c")
        self.root.focus_force()
        self.root.geometry("400x400+600+205")
        self.root.iconbitmap(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\My_project.ico")
        expression = ""
        input_text = StringVar()

        # Update the input field whenever a number is entered
        def btn_press(item):
            nonlocal expression
            expression = expression + str(item)
            input_text.set(expression)

        # Clear the last input
        def btn_clear_last():
            nonlocal expression
            expression = expression[:len(expression) - 1]
            input_text.set(expression)

        # Clear the input field
        def btn_clear():
            nonlocal expression
            expression = ""
            input_text.set("")

        # Calculate the expression present in input field
        def btn_equal():
            nonlocal expression

            try:
                result = str(eval(expression))
                input_text.set(result)
            except:
                input_text.set("Error")
                expression = ""

        # Creating a Frame for the input field
        input_frame = Frame(root)
        input_frame.pack(fill=X, padx=5, pady=5)

        # Creating an input field inside the 'Frame'
        input_field = Entry(input_frame, font=('arial', 16, 'bold'),
                            textvariable=input_text, bd=2)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10, fill=X)

        # Creating another Frame for the button below the 'input_frame'
        btns_frame = Frame(root, bg="grey")
        btns_frame.pack(padx=5)

        # First row
        clear_btn = Button(btns_frame, text="CLEAR ALL", fg="white", width=21, height=3, bd=1,
                           bg="#6e0211", cursor="hand2", command=btn_clear)
        clear_btn.grid(row=0, columnspan=2)
        divide_btn = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1,
                            bg="#eee", cursor="hand2", command=lambda: btn_press("/"))
        divide_btn.grid(row=0, column=2)
        clear_last_btn = Button(btns_frame, text="C1", fg="black", width=10, height=3, bd=1,
                                bg="#eee", cursor="hand2", command=btn_clear_last)
        clear_last_btn.grid(row=0, column=3)

        # Second row
        seven_btn = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=1,
                           bg="#fff", cursor="hand2", command=lambda: btn_press("7"))
        seven_btn.grid(row=1, column=0)
        eight_btn = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=1,
                           bg="#fff", cursor="hand2", command=lambda: btn_press("8"))
        eight_btn.grid(row=1, column=1)
        nine_btn = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=1,
                          bg="#fff", cursor="hand2", command=lambda: btn_press("9"))
        nine_btn.grid(row=1, column=2)

        multiply_btn = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=1, 
            bg="#eee", cursor="hand2", command=lambda: btn_press("*"))
        multiply_btn.grid(row=1, column=3)

        # Third row
        four_btn = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("4"))
        four_btn.grid(row=2, column=0)
        five_btn = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("5"))
        five_btn.grid(row=2, column=1)
        six_btn = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("6"))
        six_btn.grid(row=2, column=2)
        minus_btn = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, 
            bg="#eee", cursor="hand2", command=lambda: btn_press("-"))
        minus_btn.grid(row=2, column=3)

        # Fourth row
        one_btn = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("1"))
        one_btn.grid(row=3, column=0)
        two_btn = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("2"))
        two_btn.grid(row=3, column=1)
        three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("3"))
        three.grid(row=3, column=2)
        plus_btn = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, 
            bg="#eee", cursor="hand2", command=lambda: btn_press("+"))
        plus_btn.grid(row=3, column=3)

        # Fifth row
        zero_btn = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=1, 
            bg="#fff", cursor="hand2", command=lambda: btn_press("0"))
        zero_btn.grid(row=4, columnspan=2)
        point_btn = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, 
            bg="#eee", cursor="hand2", command=lambda: btn_press("."))
        point_btn.grid(row=4, column=2)
        equal_btn = Button(btns_frame, text="=", width=10, height=3, bd=1, 
            bg="#6e0211",fg="white", cursor="hand2", command=btn_equal)
        equal_btn.grid(row=4, column=3)


if __name__=="__main__":
    root=Tk()
    obj=Calculator(root)
    root.mainloop()