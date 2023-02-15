from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
from instock import addclass
from orderinv import classorder
from releasestock import classrelease
from socialform import socialclass
from instocktree import adddbclass
from socialformtree import socialdbclass



class IMS:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="#000")
        self.root.state("zoomed")
        self.root.title("INVENTORY MANAGEMENT PAGE")
        
        
   
        #HEAD PART
        self.icon_title=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\mainlogo.png")
        title=Label(self.root, image=self.icon_title, text="HOME | INVENTORY MANAGEMENT SYSTEM", font=("ARIAL BOLD", 40), bg="#6e0211", compound="left", fg="white",height=60,anchor="w",padx=20).place(x=0,y=0,relwidth=5)
        
        #logout button
        Button(self.root, width=15,pady=10,text='LOG OUT',font=('Joy multiplication',15),bg="#36000b", fg='white',border=1,padx=2,cursor="hand2").place(x=1600,height=60,y=2.5)
        #header
        self.lbl_header=Label(self.root, text="You are in IMS : Team", font=("Arial Bold", 10), bg="#6e0211",  fg="white",height=60)
        self.lbl_header.place(x=0,y=70,relwidth=1,height=20)
        
        
        #MENUBAR FRAME SET

        self.menubar1= Frame(root,bg="#1c1c1c")
        self.menubar1.place(x=0,y=100,width=300,height=300)
        
        self.menubar2= Frame(root,bg="#1c1c1c")
        self.menubar2.place(x=0,y=420,width=300,height=700)
        
        #menubar upper
        Button(self.menubar1,width=30,padx=10,pady=9,text='Social Media',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.socialform).place(x=0,y=0)


        Button(self.menubar1,width=30,padx=10,pady=9,text='Adding Stocks',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.instock).place(x=0,y=50)


        Button(self.menubar1,width=30,padx=10,pady=9,text='Order Inventory',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.orderinv).place(x=0,y=100)
        
        
        Button(self.menubar1,width=30,padx=10,pady=9,text='Release Stock',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command=self.releasestock).place(x=0,y=150)
        
        #menubar upper
        self.menulogo=Image.open("D:\education\SOFTWARICA\INVENTORY\mainlogo1.png")
        self.menulogo=self.menulogo.resize((300,250),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        menubar2_selfmenulogo=Label(self.menubar2,image=self.menulogo)
        menubar2_selfmenulogo.pack(side=TOP)
        Button(self.menubar2, width=30,padx=10,pady=9,text='Fun Zone',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0).place(x=0,y=320)

        Button(self.menubar2, width=30,padx=10,pady=9,text='App Gallery',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0).place(x=0,y=370)

        Button(self.menubar2,width=30,padx=10,pady=9,text='Info',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0).place(x=0,y=420)

        Button(self.menubar2,width=30,padx=10,pady=9,text='About',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0).place(x=0,y=470)

        Button(self.menubar2,width=30,padx=10,pady=9,text='Contact us',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0).place(x=0,y=520)


        
        #footer part
        self.lbl_footer=Label(self.root, text="DEVELOPED AND USED BY TEAM NAMED BDSM | THE INVENTORY MANAGEMENT SYSTEM | COPYRIGHT TO US ONLY", font=("ARIAL BOLD", 10), bg="#6e0211",  fg="white",height=1).pack(side=BOTTOM,fill=X)
        
        #middle button
        midbutton= Frame(root,bg="#000")
        midbutton.place(x=305,y=100,width=1650,height=875)
        
        
        #imageno1
        social=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\stock.png")
        socialbtn=Button(midbutton,image=social,bd=0,cursor='hand2',command=self.instocktree)
        socialbtn.place(x=300,y=500)
        sociallbl1=Button(midbutton, text="SOCIAL MEDIA", font=("Arial Bold", 20), bg="#6e0211",  fg="white",height=1,command=self.instocktree)
        sociallbl1.place(x=370,y=375)
        
        #imageno2
        stock=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\stock.png")
        stockbtn=Button(midbutton,image=stock,bd=0,cursor='hand2')
        stockbtn.place(x=900,y=90)
        stocklbl=Button(midbutton, text="ADD STOCKS", font=("Arial Bold", 20), bg="#6e0211",  fg="white",height=1,command=self.socialformtree,cursor='hand2')
        stocklbl.place(x=970,y=375)
        
        
        #imageno3
        order=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\stock.png")
        orderbtn=Button(midbutton,image=order,bd=0,cursor='hand2')
        orderbtn.place(x=300,y=90)
        orderlbl=Label(midbutton, text="ORDER STOCK", font=("Arial Bold", 20), bg="#6e0211",  fg="white",height=1)
        orderlbl.place(x=370,y=785)
        
        #imageno4
        release=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\stock.png")
        releasebtn=Button(midbutton,image=release,bd=0,cursor='hand2')
        releasebtn.place(x=900,y=500)
        releaselbl=Label(midbutton, text="RELEASE STOCK", font=("Arial Bold", 20), bg="#6e0211",  fg="white",height=1)
        releaselbl.place(x=970,y=785)
        
    def socialform(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=socialclass(self.new_win)
        
    def orderinv(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=classorder(self.new_win) 
        
    def releasestock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=classrelease(self.new_win)
    
    def instock(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=addclass(self.new_win) 
        
    def instocktree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=adddbclass(self.new_win) 
        
    def socialformtree(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=socialdbclass(self.new_win)
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
    
