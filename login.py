
import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'admin' and password == 'kenshingwapo':
        messagebox.showinfo("Login Successfully", "Welcome, Pogi")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid Username Or Password!")
        root.destroy()

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("300x200")
    dashboard.resizable(False, False)
    welcome_label = tk.Label(dashboard, text="Yes")
    welcome_label.pack(pady=50)
    dashboard.mainloop()
    button = tk.Button(dashboard, text="Click Me")
    button.pack()
    

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
