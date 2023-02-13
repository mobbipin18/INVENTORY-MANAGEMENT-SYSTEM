from tkinter import*
from form import formclass
from subprocess import call

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="#33353b")
        self.root.state("zoomed")
        self.root.title("INVENTORY MANAGEMENT PAGE")
        
        #HEAD OF THE APP 
        frame1= Frame(self.root,bg="#1c1c1c")
        frame1.place(x=0,y=0,width=1950,height=70)

        frame2= Frame(self.root,bg="#1c1c1c")
        frame2.place(x=0,y=75,width=300,height=320)

        frame3= Frame(self.root,bg="#1c1c1c")
        frame3.place(x=0,y=400,width=300,height=700)

        frame4= Frame(self.root,bg="#33353b")
        frame4.place(x=305,y=75,width=1650,height=977)

        Button(frame2,width=30,padx=10,pady=9,text='Social Media',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command='lambda').place(x=0,y=0)


        Button(frame2,width=30,padx=10,pady=9,text='Adding Stocks',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command='lambda').place(x=0,y=50)


        Button(frame2,width=30,padx=10,pady=9,text='Order Inventory',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command='lambda').place(x=0,y=100)


        Button(frame2,width=30,padx=10,pady=9,text='Release Stock',font=('Microsoft YaHei UI Light',14),bg='#1c1c1c',fg='white',border=0,command='lambda').place(x=0,y=150)

        Button(frame3, width=30,padx=10,pady=9,text='Fun Zone',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,command='lambda').place(x=0,y=350)

        Button(frame3, width=30,padx=10,pady=9,text='App Gallery',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,command='lambda').place(x=0,y=400)

        Button(frame3,width=30,padx=10,pady=9,text='Info',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,command='lambda').place(x=0,y=450)

        Button(frame3,width=30,padx=10,pady=9,text='About',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,command='lambda').place(x=0,y=500)

        Button(frame3,width=30,padx=10,pady=9,text='Contact us',font=('Microsoft YaHei UI Light',14),bg="#1c1c1c",fg='white',border=0,command='lambda').place(x=0,y=550)

        heading=Label(frame1,text='BDSM INVENTORY MANAGEMENT', fg='white',bg='#1c1c1c',font=('Arial Bold',16))
        heading.place(x=0,y=20)

        Button(frame1, width=15,pady=10,text='+  ADD',font=('Microsoft YaHei UI Light',9),bg="#acd658", fg='black',border=1).place(x=1700,y=2.5)
        
        #----------------------------SEARCH BUTTON-----------------------#
        # searchimg=PhotoImage(file=r"C:\Users\Acer\Desktop\BDSM\newpython\searchbtn.png")
        # search_btn= Button(frame1,image=searchimg,bg='#1c1c1c',bd=0,cursor='hand2')
        # search_btn.place(x=1560,y=10)

        stocklbl=Label(frame4, text='Stock/inventory',fg='Black',bg='White',font=('Arial Bold',14),cursor='hand2')
        # stckbtn=Button(frame4,)
        stocklbl.place(x=375,y=375)

        stock=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\stock.png")
        stockbtn=Button(frame4,image=stock,bg='#fff',bd=0,cursor='hand2')
        stockbtn.place(x=300,y=90)

        delivery=PhotoImage(file=r"D:\education\SOFTWARICA\INVENTORY\delivery.png")
        deliverybtn=Button(frame4,image=delivery,bg='#fff',bd=0,cursor='hand2')
        deliverybtn.place(x=800,y=90)





        def on_enter(e):
            code.delete(0,END)
        def on_leave(l):
            name=code.get()
            if name=='':
                code.insert(0,'Search order inventory')
        code= Entry(frame1,width=50,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',15))
        code.place(x=1000,y=15)
        code.insert(0,'Search order inventory')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)

        
    def form(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=formclass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
