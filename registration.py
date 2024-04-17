import customtkinter as tk
from customtkinter import filedialog
from PIL import Image ,ImageTk
import shutil
import os
from tkinter import messagebox
import subprocess
import os
import sys
import encoder_refresh
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
file_path = ''
tpl = tk.CTk()
tpl.title('Employee Registration')
def file_find():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        update_photo_label()
        enable_entry()
def enable_entry():
    entry_box.configure(state='normal')
def update_photo_label():
    if file_path:
        # notify(tpl,'Enter the name for the person',5)
        temp_Photo = Image.open(file_path)
        temp_Photo=tk.CTkImage(temp_Photo,size=(250,250))
        photo_label.configure(image=temp_Photo)
        photo_label.update()
        open_button.configure(state='disabled')
        entry_box.configure(state='normal')

def change_and_copy():
    new_file_name = entry_box.get()
    if file_path and new_file_name:
        file_dir, file_ext = os.path.splitext(file_path)
        new_path = f'Data/Attandease/{new_file_name}{file_ext}'
        destination_folder = os.path.dirname(new_path)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.copy(file_path, new_path)
        encoder_refresh.encode_again()
        tpl.destroy()
def restore_main_window():
    subprocess.Popen(["python", "app.pyw"])

default_image = Image.open('Data/processing/user.jpg')
default_image = tk.CTkImage(default_image,size=(250, 255))  # Resize the default image
photo_label = tk.CTkLabel(tpl, text='', image=default_image)
photo_label.pack()
entry_box = tk.CTkEntry(tpl, placeholder_text='Persons name...', width=110)
entry_box.pack()
entry_box.configure(state='disabled')
# entry_box.configure(state='normal')
open_button = tk.CTkButton(tpl, text='Select File', command=file_find)
open_button.pack()
copy_button = tk.CTkButton(tpl, text='Register', command=change_and_copy)
copy_button.pack()
# notify(tpl,'Select image than add name in the box',7)
# tpl.protocol("WM_DELETE_WINDOW",restore_main_window)

if __name__=='__main__':
    tpl.mainloop()