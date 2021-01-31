from tkinter import *

from tkinter import messagebox

screen=Tk()
screen.geometry("1100x650+110+20")
screen.title("LOGIN PAGE")
screen.resizable(0,0)
screen.configure(background='floral white')
us=StringVar("")
ps=StringVar("")

def page():
    global us
    global ps

    if i1.get()=='Username' and i2.get()=='Password':
        messagebox.showerror('Error','Please fill out these fields')
        
    elif i1.get()=='Username':
        messagebox.showerror('Error','Please enter your username') 

    elif i2.get()=='Password':
        messagebox.showerror('Error','Please enter your password')

    elif i1.get()=='yash' and i2.get()=='123456':
        messagebox.showinfo('Congrats','you id is : yash and pass is :123456')

    elif i1.get()!='yash' or i2.get()!='123456':
         messagebox.showinfo('Error','Please enter your correct username or password')

frame1=Frame(screen,height=480,width=760,bg='white')
frame1.place(x=150,y=100)

t1=Label(frame1,text='Member Login',font=("Arial",22),bg='white',fg='black')
t1.place(x=390,y=130)

def on_entry_click(event):
    if i1.get()=='Username':
        i1.delete(0,"end")
        i1.insert(0,'')
        i1.configure(fg='black')

def on_focusout(event):
    if i1.get()=='':
        i1.insert(0,'Username')
        i1.configure(fg='grey')

def on_entry_click1(event):
    if i2.get()=='Password':
        i2.delete(0,"end")
        i2.insert(0,'')
        i2.configure(fg='black')

def on_focusout1(event):
    if i2.get()=='':
        i2.insert(0,'Password')
        i2.configure(fg='grey')
        
i1=Entry(frame1,bg='white',fg='grey',font=("Arial",15),width=15)
i1.insert(0,'Username')
i1.place(x=405,y=190)
i1.bind('<FocusIn>',on_entry_click)
i1.bind('<FocusOut>',on_focusout)

i2=Entry(frame1,bg='white',fg='grey',font=("Arial",15),width=15)
i2.insert(0,'Password')
i2.place(x=405,y=240)
i2.bind('<FocusIn>',on_entry_click1)
i2.bind('<FocusOut>',on_focusout1)


t2=Button(frame1,text='Forget Password/Username',font=("Arial",8),bg='white',fg='red',bd=0,cursor='hand2')
t2.place(x=420,y=350)

img1=PhotoImage(file="tr2.png")

t=Label(frame1,image=img1,bg='white',bd=0)
t.place(x=50,y=70)

img=PhotoImage(file="lt.png")
b1=Button(frame1,image=img,bg='white',bd=0,cursor='hand2',command=page)
b1.place(x=445,y=290)

screen.mainloop()
