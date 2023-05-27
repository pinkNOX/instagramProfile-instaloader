import tkinter
import instaloader
from tkinter import *
from instaloader import *
import urllib
from urllib.request import urlopen
# pip install pillow
from PIL import Image, ImageTk
import io
import tkinter.messagebox


#---------please log in (Error)
def errorsmsg1(ms):
    if ms == 'error':
        tkinter.messagebox.showerror("error", "Please log in to your Instagram account first")
def get_image():
    try:
        L= instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, f"{userName.get()}")
        a= urlopen(profile.get_profile_pic_url())
        data= a.read()
        a.close()
        image= Image.open(io.BytesIO(data))
        pic= ImageTk.PhotoImage(image)
        label.config(image=pic)
        label.image = pic
        label.pack()
    except:
         errorsmsg1("error")


#------------login button
def login_button():
    window1=Toplevel()
    window1.title('login')
    window1.geometry("400x200")
    window1.resizable(width=False, height=False)
    Label(window1, text= 'your user name :').pack()
    myUserName = Entry(window1, width=20)
    myUserName.pack()
    Label(window1, text='your password :').pack()
    myPass = Entry(window1, width=20)
    myPass.pack()
    loginEndbtn= Button(window1, text='login', width=12, height=3, bg="SkyBlue4", fg="floral white", font=('Vani', 10),
           cursor="arrow")

#---login error
    def errorsmsg(ms):
        if ms=='error':
            tkinter.messagebox.showerror("error", "user name or password is wrong")
    def loginEnd():
        try:
            L2 = instaloader.Instaloader()
            L2.login(f"{myUserName}", f"{myPass}")
        except:
            errorsmsg("error")

    loginEndbtn.config(command=loginEnd)
    loginEndbtn.pack()
    Button(window1,text="close", command=window1.destroy).pack(pady=10)

#------------first window
window= Tk()
window.title("instagram Profile downloader - راد")
window.geometry("400x600")
window.resizable(width=False, height=False)
window.configure(bg="#ECF8F9")

#------------label in first window
Label(window, text="hi !", font=('Times', 14),bg= "#ECF8F9", fg="#068DA9").pack()
Label(window, text="welcome to instagram downloader", font=('Times', 12),bg= "#ECF8F9", fg="#068DA9").pack()
Label(window, text="type your main instagram ID", font=('Times', 12),bg= "#ECF8F9", fg="#068DA9").pack(pady=20)

userName = Entry(window, width=30, bg='bisque2', insertbackground="SkyBlue4")
userName.pack()
label = Label(window)

#------------download button
button = Button(window, text='click here to start download', width=22, height=1, bg="#E55807",fg="#ECF8F9", font=('Vani', 13), cursor="shuttle")
button.config(command=get_image)
button.pack(pady=10)
Button(window, text='login to your instagram', command=login_button,bg="#7E1717",fg="#ECF8F9" ,font=('times', 10)).pack()


#------------Close button
closeBTN= Button(window, text="close", command=window.destroy, bg="#7E1717", fg="#ECF8F9", font=('times', 10))
closeBTN.pack()

window.mainloop()


