import cv2
import face_recognition as frcn
import os
import numpy as np
import pickle
import customtkinter as tk
from PIL import Image, ImageTk
import attendence as ac
import openpyxl as ox
import datetime as dt
import subprocess
import exporter

current_date = dt.date.today()
import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
person =str()
attendease_path = 'Data/Attandease'
images = []
attendease_name = []
images_list = os.listdir(attendease_path)
for photos in images_list:
    current_image = cv2.imread(f'{attendease_path}/{photos}')
    images.append(current_image)
    attendease_name.append(os.path.splitext(photos)[0])
known_face_encodings = []
try:
    with open('Data/processing/known_face_encodings.pkl', 'rb') as file:
        known_face_encodings = pickle.load(file)
except FileNotFoundError:
    print('Pickle file not found. Please run Program encoder to create known face encodings.')
def recognition():
    def registrationapp():
        subprocess.Popen(["python", "registration.py"])
    def exportapp():
        subprocess.Popen(["python", "exporter.py"])
    def capture():
        try:
            with open('Data/processing/known_face_encodings.pkl', 'rb') as file:
                known_face_encodings = pickle.load(file)
        except FileNotFoundError:
            print('Pickle file not found. Please run Program encoder to create known face encodings.')
        success, cam = cap.read()
        if success:
            imgS = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
            cam_img_loc = frcn.face_locations(imgS)
            cam_image_encodings = frcn.face_encodings(imgS, cam_img_loc)
            cam_image_encodings = [np.array(enc) for enc in cam_image_encodings]
            for encode_face, face_loc in zip(cam_image_encodings, cam_img_loc):
                check_match = frcn.compare_faces(known_face_encodings, cam_image_encodings[0])
                face_dis = frcn.face_distance(known_face_encodings, encode_face)
                # print(face_dis)
                match_index = np.argmin(face_dis)
                if check_match[match_index]:
                    global person
                    name = attendease_name[match_index].upper()
                    person =name
                    y1, x2, y2, x1 = face_loc
                    cv2.rectangle(cam, (x1, y1), (x2, y2), (52, 32, 79), 3)
                    cv2.putText(cam, name, (x1-6, y2+6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            frame_rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk=tk.CTkImage(img,size=(875,500))
            # imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.image = imgtk
            present_taker()
            if not recognition.stopped:
                tpl.after(10, capture)
    def stop_capture(count=2):
        start_button.configure(state='normal')
        # attadance_button.configure(state='disabled')
        if count > 0:
            # Load your image
            display.configure(state='normal')
            display.configure(state='disabled')
            video_label.configure(image=u)
            tpl.update_idletasks()
            recognition.stopped = True
            display.configure(state='normal')
            display.delete(1.0,tk.END)
            display.insert(1.0,"Press Start Capture to Activate")
            display.configure(state='disabled')
            tpl.after(10, stop_capture, count - 1)
    def start_capture():
        stop_button.configure(state='normal')
        display.configure(state='normal')
        display.delete(1.0, tk.END)
        display.insert(1.0,"Press Stop to Activate")
        display.configure(state='disabled')
        recognition.stopped = False
        start_button.configure(state='disabled')
        capture()
    def person_exists(name):
        file_path = f'Data/Attandance_list/Present_list_{current_date}.xlsx'
        if os.path.exists(file_path):
            wb = ox.load_workbook(file_path)
            ws = wb.active
            for row in ws.iter_rows(min_row=3, max_col=1, values_only=True):
                if row[0] == name:
                    return True
        return False
    
    def present_taker():
        try:
            if person !='':
                if not person_exists(person):
                    gett=f'Attandance taken {person}'
                    ac.present(person)
                    # print(f'Present taken {person}')
                else:
                    print(f'{person} already marked present')
                    gett='already marked present'
            else:
                gett = "No person specified"
        except Exception as e:
            print(e)
            gett = "Face not detected properly!"
        display.configure(state='normal')
        display.delete(1.0, tk.END)
        display.insert(1.0, gett)
        display.configure(state='disabled')    
    # recognition.stopped = False
    def restore_main_window():
        cap.release()
        cv2.destroyAllWindows()
        tpl.destroy()



    cap = cv2.VideoCapture(0)
    tpl = tk.CTk()
    tpl.lift()
    tpl.title("A.E.F.T.  -  Autonomus Employee Face Tracker ")
    screen_width = tpl.winfo_screenwidth()
    screen_height = tpl.winfo_screenheight()
    # Calculate the default tpl size (e.g., 60% of the screen width and height)
    default_width = int(screen_width )
    default_height = int(screen_height )
    # Set the default tpl size
    # tpl.geometry(f"{default_width}x{default_height}")
    tpl.minsize(default_width,default_height)
    # tpl.resizable(False,False)

    bg_image = Image.open("Data\\processing\\bgimg.jpg")  # Change "background.png" to your image file
    bg_image = tk.CTkImage(bg_image,size=(screen_width,screen_height))  # Change "background.png" to your image file

    # Create a Label widget to hold the background image
    bg_label = tk.CTkLabel(tpl, image=bg_image)
    bg_label.place(relwidth=1, relheight=1) 


    logo_label=tk.CTkLabel(tpl,width=30,height=20,text='A.E.F.T',text_color='white',font=("Lucida Handwriting", 24),fg_color="#007F7F")
    logo_label.place(relx=0.15,rely=0.08,anchor='center')



    video_frame = tk.CTkFrame(tpl, width=875, height=500, bg_color='gray')
    video_frame.place(relx=0.1,rely=0.55,anchor='w')
    u = Image.open('Data/processing/banner.jpg')
    u = tk.CTkImage(u,size=(875,500))
    video_label = tk.CTkLabel(video_frame,text='',image=u)
    video_label.pack(fill='both',anchor='center')

    display=tk.CTkTextbox(tpl,height=38,width=875,font=tk.CTkFont(family='cursive',size=16,weight='bold'),fg_color='#013864')
    display.place(relx=0.1,rely=0.88,anchor='w')
    display.insert(1.0,"Press Start Capture to Activate")
    display.configure(state='disabled')


    radio_var=tk.IntVar()
    start_button = tk.CTkRadioButton(tpl, text="Start Capture", command=start_capture,variable=radio_var, value=1,fg_color='white',text_color='white',bg_color='#01053D',height=15,width=15,font=tk.CTkFont(size=16))
    start_button.place(relx=0.5, rely=0.23, anchor='center')

    stop_button = tk.CTkRadioButton(tpl, text="Stop Capture", command=stop_capture,variable=radio_var, value=1,fg_color='white',text_color='white' ,bg_color='#01053D',height=15,width=15,font=tk.CTkFont(size=16))
    stop_button.place(relx=0.63, rely=0.23, anchor='center')
    # stop_button.configure(state='disabled')


    register_button=tk.CTkButton(tpl,text='Register Employee',width=200,height=35,fg_color='#013864',font=tk.CTkFont(size=17,weight='bold',family='Segoe UI Black'),text_color='white',command=registrationapp)
    register_button.place(relx=0.87,rely=0.1,anchor='center')

    export_button=tk.CTkButton(tpl,text='Export Excel',width=200,height=35,fg_color='#013864',font=tk.CTkFont(size=17,weight='bold',family='Segoe UI Black'),text_color='white',command=exportapp)
    export_button.place(relx=0.87,rely=0.2,anchor='center')

    
    tpl.protocol("WM_DELETE_WINDOW",restore_main_window)
    tpl.mainloop()

if __name__=='__main__':
    recognition()