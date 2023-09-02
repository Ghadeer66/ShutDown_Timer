from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
from tkinter import font as tkFont
import os
#####################
root = Tk()
root.title("Shutdown Timer")
root.geometry("400x400+500+150") 
root.iconphoto(False,PhotoImage("icon.ico"))
style = ttk.Style()
style.configure("BW.TLabel", background="white")
root.tk.call('source', 'breeze/breeze.tcl')
root.resizable(False, False)
style.theme_use('breeze')
###################
bg = ImageTk.PhotoImage(Image.open("background.jpg")) 
bIm = Label(root , image=bg).place(x=0,y=0)
###################
def grab():
    h=hSpin. get()
    m=mSpin. get()
    s=sSpin. get()
    oo=selectOpt.get()
    hh=int(h)
    print(hh)
    mm=int(m)
    print(m)
    print(mm)
    ss=int(s)
    res = (hh*3600)+(mm*60)+ss
    print(res)
    if oo =='Shutdown':
     messagebox.showwarning("Warning", "Your computer will be shutdown after {} Hours and {} Minutes {} Seconds".format(h,m,s))
     os. system("Shutdown -s -t {}".format(res))
    elif oo == 'Restart':
        messagebox.showwarning("Warninig", "Your computer will be restart after {} Hours and {} Minutes {} Seconds".format(h,m,s))
        os. system("Shutdown /r -t {}".format(res))
#####################
def canc():
    oo=selectOpt.get()
    os. system("shutdown -a ")
    messagebox.showinfo("Info", "Operation cancelled")
#####################
def selected(event):
    la=Label(root,text=clicked.get(),font=("Courier",8)).place(x=200,y = 550)
#####################
oLabel=Label(root,text="Select Operation:",bg="lavender",font=("adoody",18)).place(x=50,y=60)
#####################
selectOpt = StringVar(value='Shutdown')
oBox=ttk.Combobox(root,textvariable=selectOpt,width=10)
oBox['values'] = ('Shutdown','Restart')
oBox.place(x = 250,y =60)
oBox['state'] = 'readonly'
 #####################
hLabel =Label(root,text="Hours:",font=("adoody",18)).place(x=260,y=140)
hValue = StringVar(value=0)
hSpin =ttk.Spinbox(root,from_=0,to=1000,textvariable=hValue,width=3,wrap=True)
hSpin.place(x = 275,y=200)
#-----#
mLabel =Label(root,text="Minutes:",font=("adoody",18)).place(x=150,y=140)
mValue = StringVar(value=0)
mSpin =ttk.Spinbox(root,from_=0,to=59,textvariable=mValue,width=3,wrap=True)
mSpin.place(x = 175,y = 200)
#---#
sLabel =Label(root,text="Seconds:",font=("adoody",18)).place(x=40,y=140)
sValue = StringVar(value=0)
sSpin =ttk.Spinbox(root,from_=0,to=59,textvariable=sValue,width=3,wrap=True)
sSpin.place(x = 75,y=200)
#####################
h_button = Button(root,text="Submit",command = grab,bg="springgreen",font=("adoody",18))
h_button. place(x = 250,y=270)
#####################
c_button = Button(root,text="Cancel",command = canc,bg="orangered",font=("adoody",18))
c_button. place(x = 60,y=270)
#####################
root. mainloop()