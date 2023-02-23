from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from instock import addclass
from orderinv import classorder
from releasestock import releaseform
from socialform import socialclass
from instocktree import adddbclass
from socialformtree import socialdbclass
from orderinvtree import classorderdbclass
from releasestocktree import releaseformdbclass
from cont_us import contactus
from bill import billing
from calcular import Calculator
from info import AppInfo
import os



class IMS:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="#000")
        self.root.state("zoomed")
        self.root.title("IMS")
        self.root.iconbitmap(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\My_project.ico")

        #HEAD PART

        self.icon_title=PhotoImage(file=r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\IMSSMALL.png")
        title=Label(self.root, image=self.icon_title, text="HOME | INVENTORY MANAGEMENT SYSTEM", font=("ARIAL BOLD", 40), bg="#6e0211", compound="left", fg="white",height=60,anchor="w",padx=20).place(x=0,y=0,relwidth=5)
        
        #logout button
        Button(self.root, width=15,pady=10,text='LOG OUT',font=('Joy multiplication',15),bg="#36000b", fg='white',border=1,padx=2,cursor="hand2",command=self.logout).place(x=1357,height=60,y=2.5)

        #header
        self.lbl_header=Label(self.root, text="You are in IMS : Team", font=("Arial Bold", 10), bg="#6e0211",  fg="white",height=60)
        self.lbl_header.place(x=0,y=68,relwidth=1,height=20)
        
        
        #MENUBAR FRAME SET

        self.menubar1= Frame(root,bg="#1c1c1c")
        self.menubar1.place(x=0,y=90,width=300,height=300)
        
        self.menubar2= Frame(root,bg="#1c1c1c")
        self.menubar2.place(x=0,y=392,width=300,height=378)
        
        #menubar upper
        Button(self.menubar1,width=30,padx=10,pady=9,text='Adding Stocks',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.instock,cursor="hand2").place(x=0,y=0)


        Button(self.menubar1,width=30,padx=10,pady=9,text='Order Inventory',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.orderinv,cursor="hand2").place(x=0,y=50)


        Button(self.menubar1,width=30,padx=10,pady=9,text='Social Media',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.socialform,cursor="hand2").place(x=0,y=100)
        
        
        Button(self.menubar1,width=30,padx=10,pady=9,text='Release Stock',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.releasestock,cursor="hand2").place(x=0,y=150)
        
        #menubar upper

        # self.menulogo=Image.open("C:\\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\mainlogo1.png")
        # self.menulogo=self.menulogo.resize((300,250),Image.ANTIALIAS)
        # self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        # menubar2_selfmenulogo=Label(self.menubar2,image=self.menulogo)
        # menubar2_selfmenulogo.pack(side=TOP)

        Button(self.menubar2, width=30,padx=10,pady=9,text='Billing Area',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,cursor="hand2",command=self.bill).place(x=0,y=172)

        Button(self.menubar2, width=30,padx=10,pady=9,text='Calculator',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,cursor="hand2",command=self.calcular).place(x=0,y=222)

        Button(self.menubar2,width=30,padx=10,pady=9,text='App Info',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,cursor="hand2",command=self.info).place(x=0,y=272)

        Button(self.menubar2,width=30,padx=10,pady=9,text='Contact us',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,cursor="hand2",command=self.cont_us).place(x=0,y=322)
       
        #footer part
        self.lbl_footer=Label(self.root, text="DEVELOPED AND USED BY TEAM NAMED BDSM | THE INVENTORY MANAGEMENT SYSTEM | COPYRIGHT TO US ONLY", font=("ARIAL BOLD", 10), bg="#6e0211",  fg="white",height=1).pack(side=BOTTOM,fill=X)
        
        #------------------INFO PAGE
        # info= Frame(root,bg="#000")
        # info.place(x=305,y=220,width=1650,height=670)
        
        # def info():
        #     infohead=Label(info,text="HEllO YOU ARE ON INFO PAGE")
        #     infohead.place(x=3,y=2)
        
        #middle button
        midbutton= Frame(root,bg="#000")
        midbutton.place(x=302,y=90,width=1400,height=680)

        heading=Label(midbutton,text="DATA BASE CENTER",bg="#000",fg="white",font=("Arial Bold", 25))
        heading.place(x=400,y=10)


        #imageno1
        # social=PhotoImage(file=r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\ADDING_STOCK.png")
        self.addstock=Image.open(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\ADDING_STOCK.png")
        self.addstock=self.addstock.resize((200,200),Image.ANTIALIAS)
        self.addstock=ImageTk.PhotoImage(self.addstock)
        addstock=Label(midbutton,image=self.addstock)
        addstock.place(x=180,y=80)
        sociallbl1=Button(midbutton, text="ADD STOCKS", font=("Arial Bold", 15), bg="#6e0211",  fg="white",height=1,command=self.instocktree,cursor='hand2')
        sociallbl1.place(x=400,y=100,width=180)
        sociallbl2 = Label(midbutton, text="- Add the item stock.\n- Item details.\n- Stock levels.", bg="black", fg="white",font=("Arial bold", 10),anchor="w")
        sociallbl2.place(x=400,y=150)

        #imageno2
        self.orderst=Image.open(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\ORDERING.png")
        self.orderst=self.orderst.resize((200,200),Image.ANTIALIAS)
        self.orderst=ImageTk.PhotoImage(self.orderst)
        orderst=Label(midbutton,image=self.orderst)
        orderst.place(x=700,y=80)
        stocklbl=Button(midbutton, text="ORDER STOCK", font=("Arial Bold", 15), bg="#6e0211",  fg="white",height=1,command=self.orderinvtree,cursor='hand2')
        stocklbl.place(x=920,y=100)
        sociallbl3 = Label(midbutton, text="-Purchase order creation.\n -Record point setting.\n -Cost tracking and reporting.", bg="black", fg="white",anchor="w",font=("Arial bold", 10))
        sociallbl3.place(x=920,y=150)
        
        
        #imageno3
        self.socialst=Image.open(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\SOCIAL_MEDIA.png")
        self.socialst=self.socialst.resize((200,200),Image.ANTIALIAS)
        self.socialst=ImageTk.PhotoImage(self.socialst)
        socialst=Label(midbutton,image=self.socialst)
        socialst.place(x=180,y=400)
        orderlbl=Button(midbutton, text="SOCIAL MEDIA", font=("Arial Bold", 15), bg="#6e0211",  fg="white",height=1,cursor='hand2',command=self.socialformtree)
        orderlbl.place(x=400,y=420,width=180)
        sociallbl4 = Label(midbutton, text="-Add new product to stocks.\n -Do promotion.\n -Get orders.", bg="black", fg="white",anchor="w",font=("Arial bold", 10))
        sociallbl4.place(x=400,y=473)

        #imageno4
        self.releasest=Image.open(r"C:\Users\Acer\Documents\GitHub\INVENTORY-MANAGEMENT-SYSTEM\RELEASESTOCK.png")
        self.releasest=self.releasest.resize((200,200),Image.ANTIALIAS)
        self.releasest=ImageTk.PhotoImage(self.releasest)
        releasest=Label(midbutton,image=self.releasest)
        releasest.place(x=700,y=400)
        releaselbl=Button(midbutton, text="RELEASE STOCK", font=("Arial Bold", 15), bg="#6e0211",  fg="white",height=1,cursor='hand2',command=self.releasestocktree)
        releaselbl.place(x=920,y=420,width=180)
        sociallbl5 = Label(midbutton, text="-Ensure accuracy and efficiency.\n -Deliver details.\n -Sales order tracking.", bg="black", fg="white",anchor="w",font=("Arial bold", 10))
        sociallbl5.place(x=920,y=473)
        
    def socialform(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=socialclass(self.new_win)
        
    def orderinv(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=classorder(self.new_win) 
        
    def releasestock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=releaseform(self.new_win)
    
    def instock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=addclass(self.new_win) 
        
    def instocktree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=adddbclass(self.new_win) 
        
    def socialformtree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=socialdbclass(self.new_win)

    def orderinvtree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=classorderdbclass(self.new_win)

    def releasestocktree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=releaseformdbclass(self.new_win)

    def cont_us(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=contactus(self.new_win)

    def bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billing(self.new_win)

    def calcular(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Calculator(self.new_win)

    def info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AppInfo(self.new_win)    

    def logout(self):
        root.destroy()
        os.system("python loginn.py")
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
    
