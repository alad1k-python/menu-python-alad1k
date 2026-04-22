from customtkinter import *
from tkinter import messagebox

set_appearance_mode("dark")
set_default_color_theme("blue")
win = CTk()
win.geometry("340x380")
win.title("Register")

title_label = CTkLabel(win, text="Register", font = CTkFont(size = 22, weight = "bold"))
title_label.pack(pady = (40, 20))
entry_name = CTkEntry(win, placeholder_text = "Enter your NAME", width = 240, height = 35)
entry_name.pack(pady = 10)
entry_host = CTkEntry(win, placeholder_text = "Enter your IP", width = 240, height = 35)
entry_host.pack(pady = 10)
entry_port = CTkEntry(win, placeholder_text = "Enter your PORT", width = 240, height = 35)
entry_port.pack(pady = 10)
def register():
    name = entry_name.get().strip()
    host = entry_host.get().strip()
    port = entry_port.get().strip()
    if not name or not host or not port:
        messagebox.showerror("Error", "Please fill all fields")
        return
    messagebox.showinfo("Success", "Registered successfully")
register_button = CTkButton(win, text = "Register", command = register, width = 180, height = 35)
register_button.pack(pady = (20,10))


win.mainloop()