from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("Error", "Invalid username or password")
    elif usernameEntry.get()=='123'and passwordEntry.get()=='123':
        messagebox.showinfo("Error", "Login is successful")
        root.destroy()
        import ems
        
    else:
        messagebox.showerror("Error", "invalid username or password")


root=CTk()
root.geometry("930x480")
root.resizable(0,0)
root.title("Login Page")
image=CTkImage(Image.open("cover.jpg"),size=(930,478))
imageLabel=CTkLabel(root,image=image,text="")
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text="Employee Management system",bg_color="#FAFAFA",font=("Times New Roman",20,'bold'))
headinglabel.place(x=20,y=100)
print()
usernameEntry= CTkEntry(root,placeholder_text="Enter Username",width=180,bg_color="#FAFAFA")
usernameEntry.place(x=100,y=150)
print()
passwordEntry= CTkEntry(root,placeholder_text="Enter Password",width=180,bg_color="#FAFAFA",show="*")
passwordEntry.place(x=100,y=200)
LoginButton=CTkButton(root,text="Login",cursor="hand2",bg_color="#FAFAFA",command=login)
LoginButton.place(x=100,y=250)
root.mainloop()