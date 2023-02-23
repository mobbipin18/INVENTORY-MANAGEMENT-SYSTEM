from tkinter import *

class AppInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("App Gallery And Info")
        self.root.geometry("400x800")
        self.root.config(bg="#1c1c1c")
        
        # Create widgets
        self.label0=Label(self.root,text="ABOUT APP", font=("Arial Bold", 20),fg="White", bg="#1c1c1c")
        self.label0.place(x=1,y=0)
        self.label = Label(self.root, text="Welcome to our app! We understand the busy lives of modern day individuals, and that's why we've created a one-stop-shop to help make your life easier. Our app is filled with useful resources and tools that will help you manage your day-to-day tasks, give you access to personalized advice and support. We are constantly striving to improve our app We want to make sure that you are able to use our app to its fullest potential, so we have included comprehensive tutorials and guidance in our help centre. We value your feedback, so please don’t hesitate to get in touch with us if you have any questions or suggestions. We want to make sure that our app is constantly improving and meeting the needs of our users. Thank you for choosing our app and we hope you find it useful!", font=("Arial Bold", 12), fg="White", bg="#1c1c1c",wraplength=350)
        self.label.place(x=1,y=35)
        
        self.label1=Label(self.root,text="ABOUT IMS",font=("Arial Bold", 20),fg="White", bg="#1c1c1c")
        self.label1.place(x=2,y=400)
        
        self.label2= Label(self.root, text="An inventory management app is a software program that helps businesses manage their inventory and stock levels. This type of application helps businesses automate the tracking of inventory, ensuring that the correct amount of stock is always available. It can also help businesses improve their inventory forecasting and planning, as well as optimize their inventory and stock levels. The app can also be used to manage pricing, promotions, and discounts. Additionally, an inventory management app can help businesses maintain accurate records of their inventory and stock levels, track shipments and deliveries, and easily monitor warehouse capacity.", font=("Arial Bold", 12), fg="White", bg="#1c1c1c",wraplength=350,anchor="e")
        self.label2.place(x=1,y=435)
        
if __name__ == '__main__':
    root = Tk()
    app = AppInfo(root)
    root.mainloop()
