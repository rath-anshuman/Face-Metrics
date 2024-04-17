import cv2 
import face_recognition as frcn
import os 
import numpy as np
import pickle
import customtkinter as tk
from tkinter import messagebox
import os
import sys
base_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
attendease_path='Data/Attandease'
known_face_encodings=[]
images=[]
attendease_name=[]
images_list=os.listdir(attendease_path)
for photos in images_list:
    current_image=cv2.imread(f'{attendease_path}/{photos}')
    images.append(current_image)
    attendease_name.append(os.path.splitext(photos)[0])
def create_encodings(images):
    encodinglist=[]
    for idx, image in enumerate(images):
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        current_image_encoding=frcn.face_encodings(image)[0]
        encodinglist.append(current_image_encoding)
        print(f'{attendease_name[idx]} face encoded')
    return encodinglist

def encode_again():
    known_face_encodings=create_encodings(images)
    known_face_encodings=[np.array(enc) for enc in known_face_encodings]
    pickle_file = "Data/processing/known_face_encodings.pkl"
    with open(pickle_file, 'wb') as file:
        pickle.dump(known_face_encodings, file)

# encode_again()