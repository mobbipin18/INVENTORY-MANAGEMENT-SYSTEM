from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
class classorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Adding Stock Form")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.focus_force()
        
        self.tittlelabel=Label(self.root, text="Order Inventory Form", font=("Arial",33,"bold"),bg="#1c1c1c",fg="white")
        self.tittlelabel.pack(pady=30)

        self.ic=Label(self.root,text="Item code",font=('Arial',13,'bold'),bg="#1c1c1c",fg="white")
        self.ic.place(x=260,y=120)
        self.ic=Entry(self.root,width=30,font=('Arial',13),bg="#1c1c1c",fg="white")
        self.ic.place(x=160,y=150)

        self.itn=Label(self.root, text="Item name" ,font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.itn.place(x=260,y=200)
        self.itn=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.itn.place(x=160,y=230)

        self.it=Label(self.root,text="Item type", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.it.place(x=260,y=280)
        self.it=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.it.place(x=160,y=313)

        self.cn=Label(self.root, text="Customer Name", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.cn.place(x=240,y=360)
        self.cn=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.cn.place(x=160,y=390)

        self.cc=Label(self.root, text="Customer Contact", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.cc.place(x=230,y=440)
        self.cc=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.cc.place(x=160,y=470)

        self.fb=Label(self.root, text="Followed By", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.fb.place(x=255,y=520)
        self.fb=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.fb.place(x=160,y=550)

        self.s=Label(self.root, text="Status", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.s.place(x=270,y=600)
        self.s=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.s.place(x=160,y=630)

        self.btn=Button(self.root, width=8,text='BACK',font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="#FFF",cursor='hand2',command=self.back)
        self.btn.place(x=400,y=680)
        self.btn=Button(self.root,width=8,text="SAVE",font=('Arial Bold)',13,'bold'),bg='#6e0211',fg='#FFF',cursor='hand2')
        self.btn.place(x=500,y=680)
    
    def back(self):
        self.root.destroy()   
        
if __name__=="__main__":
    root=Tk()
    obj=classorder(root)
    root.mainloop()