
import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'admin' and password == 'kenshingwapo':
        messagebox.showinfo("Login Successfully", "Welcome, Pogi")
    else:
        messagebox.showerror("Login Failed", "Invalid Username Or Password!")
        root.destroy()

root = tk.Tk()
root.title("Login Ah")
root.geometry("300x200")
root.resizable(False, False)

username_label = tk.Label(root, text='Enter Your Username')
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text='Enter Your Password')
password_label.pack(pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

login_button = tk.Button(root, text='Login', command=validate_login)
login_button.pack(pady=10)

root.mainloop()
