from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="blue")
        #title_lbl.place(x=5,y=0,width=1500,height=50)


        img_top=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\ph2.jpg")
        img_top=img_top.resize((1530,840),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1580,height=840)
        #button
        #title_lbl=Label(self.root,text="PHOTO SAMPLE TESTING",font=("times new roman",35,"bold"),bg="white",fg="blue")
        #title_lbl.place(x=5,y=5,width=1530,height=60)

        b1_1=Button(self.root,text="PHOTO SAMPLE TRAINING",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=0,width=1530,height=60)

        #f_lbl=Label(self.root,image=self.photoimg_top)
        #f_lbl.place(x=0,y=0,width=1280,height=640)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            #C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\data\user.1.1.jpg
            #0                                                                 1

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        ##### train the classifier ######
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
