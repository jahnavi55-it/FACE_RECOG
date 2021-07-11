from tkinter import *
import tkinter
import tkinter.ttk as ttk
from PIL import Image,ImageTk
import os
from employee import Employee
from train import Train
from new import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #img = Image.open(r"C:\Users\megha reddy\Desktop\Face-Recognition-for-survelliance\main_face\face1.jfif")
        #img = img.resize((500,130),Image.ANTIALIAS)
        #self.photoimg=ImageTk.PhotoImage(img)

        #f_lbl=Label(self.root,image=self.photoimg)
        #f_lbl.place(x=0,y=0,width=500,height=130)


        #img1 = Image.open(r"C:\Users\megha reddy\Desktop\Face-Recognition-for-survelliance\main_face\face4.jpg")
        #img1 = img1.resize((500,130),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #f_lbl=Label(self.root,image=self.photoimg1)
        #f_lbl.place(x=500,y=0,width=500,height=130)


        #img2 = Image.open(r"C:\Users\megha reddy\Desktop\Face-Recognition-for-survelliance\main_face\face3.jfif")
        #img2 = img2.resize((500,130),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #f_lbl=Label(self.root,image=self.photoimg2)
        #f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\bg.jpg")
        img3= img3.resize((1536,840),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=840)

        title_lbl=Label(bg_img,text="SURVEILLANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #emp details button
        img4 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\empd.png")
        img4= img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.employee_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="EMPLOYEE DETAILS",command=self.employee_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img5 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\face3.jfif")
        img5= img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Employee Database
        img6 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\attendance.jpg")
        img6= img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="EMPLOYEE DATABASE",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help Button
        img7= Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\help.jpg")
        img7= img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)
        

        #Train Face Button
        img8 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\train.jpg")
        img8= img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Trained Images Button
        img9 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\photos1.jpg")
        img9= img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="TRAINED IMAGES",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer Button
        img10 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\developer.jfif")
        img10= img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit Button
        img11 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\exit.jfif")
        img11= img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this Project",parent=self.root)
        if self.iExit >0:
            self.root.destroy() 
        else:
            return

    ########################Functions Button ##############################
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()