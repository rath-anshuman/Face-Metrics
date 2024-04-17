import customtkinter as tk


def start_button_clicked():
    print("START button clicked")

def stop_button_clicked():
    print("STOP button clicked")


main = tk.CTk()
main.maxsize(600,600)
main.minsize(600,600)
main.resizable(False,False)


radio_var = tk.IntVar()

start_button = tk.CTkRadioButton(main, text='START', variable=radio_var, value=1,fg_color='green',text_color='green', command=start_button_clicked)
start_button.place(relx=0.4, rely=0.5, anchor='center')

stop_button = tk.CTkRadioButton(main, text='STOP', variable=radio_var, value=0,fg_color ='red',text_color='red', command=stop_button_clicked)
stop_button.place(relx=0.6, rely=0.5, anchor='center')

main.mainloop()