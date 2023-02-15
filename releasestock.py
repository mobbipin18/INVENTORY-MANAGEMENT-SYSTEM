from tkinter import*
from subprocess import call
from PIL import Image, ImageTk
class classrelease:
    def __init__(self,root):
        self.root=root
        self.root.title("Release Stock Form")
        self.root.config(bg="#1c1c1c")
        self.root.geometry("700x600+500+10")
        self.root.minsize(600,750)
        self.root.maxsize(600,750)
        self.root.focus_force()
        
        self.tittlelabel=Label(self.root, text="Release Stock Form", font=("Arial",33,"bold"),bg="#1c1c1c",fg="white")
        self.tittlelabel.pack(pady=30)

        self.cn=Label(self.root,text="Customer Name",font=('Arial',13,'bold'),bg="#1c1c1c",fg="white")
        self.cn.place(x=260,y=120)
        self.cn=Entry(self.root,width=30,font=('Arial',13),bg="#1c1c1c",fg="white")
        self.cn.place(x=160,y=150)

        self.cc=Label(self.root, text="Customer Contact" ,font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.cc.place(x=260,y=200)
        self.cc=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.cc.place(x=160,y=230)

        self.ic=Label(self.root,text="Item Code", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.ic.place(x=260,y=280)
        self.ic=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.ic.place(x=160,y=313)

        self.qty=Label(self.root, text="Quantity", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.qty.place(x=240,y=360)
        self.qty=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.qty.place(x=160,y=390)

        self.adr=Label(self.root, text="Address", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.adr.place(x=230,y=440)
        self.adr=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.adr.place(x=160,y=470)

        self.fb=Label(self.root, text="Followed By", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.fb.place(x=255,y=520)
        self.fb=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.fb.place(x=160,y=550)

        self.re=Label(self.root, text="Remarks", font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="white")
        self.re.place(x=270,y=600)
        self.re=Entry(self.root,width=30,font=('Arial Bold)',13),bg="#1c1c1c",fg="white")
        self.re.place(x=160,y=630)

        self.btn=Button(self.root, width=8,text='BACK',font=('Arial Bold)',13,'bold'),bg="#1c1c1c",fg="#FFF",cursor='hand2',command=self.back)
        self.btn.place(x=400,y=680)
        self.btn=Button(self.root,width=8,text="SAVE",font=('Arial Bold)',13,'bold'),bg='#6e0211',fg='#FFF',cursor='hand2')
        self.btn.place(x=500,y=680)
    
    def back(self):
        self.root.destroy()   
        
if __name__=="__main__":
    root=Tk()
    obj=classrelease(root)
    root.mainloop()