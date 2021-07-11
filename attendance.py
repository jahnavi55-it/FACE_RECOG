from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==============variables===============
        #self.var_atten_DatabaseID=StringVar()
        self.var_atten_EmpName=StringVar()
        self.var_atten_DepartmentID=StringVar()
        self.var_atten_Gender=StringVar()
        self.var_atten_EmpID=StringVar()
        self.var_atten_Time=StringVar()
        self.var_atten_Date=StringVar()
        self.var_atten_Status=StringVar()


        #bg image
        img3 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\access.jpg")
        img3= img3.resize((1536,840),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=840)
        

        title_lbl=Label(self.root,text="DATABASE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1530,height=750)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Access Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=720)

        img_left = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\aces.jpg")
        img_left = img_left.resize((860,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=20,width=850,height=150)

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=20,y=180,width=750,height=460)

        #Label and entry
        # Database id
        #attendanceId_label=Label(left_inside_frame,text="Database ID:",font="comicsansns 13 bold",bg="white")
        #attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_DatabaseID,font="comicsansns 13 bold")
        #attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # empname
        nameLabel=Label(left_inside_frame,text="EmpName:",bg="white",font="comicsansns 13 bold")
        nameLabel.grid(row=0,column=0,padx=4,pady=8,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_EmpName,font="comicsansns 13 bold")
        atten_name.grid(row=0,column=1,pady=8,sticky=W)

        # deptid
        nameLabel=Label(left_inside_frame,text="DepartmentID:",bg="white",font="comicsansns 13 bold")
        nameLabel.grid(row=1,column=0,padx=4,pady=8,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_DepartmentID,font="comicsansns 13 bold")
        atten_name.grid(row=1,column=1,pady=8,sticky=W)

        #gender
        genLabel=Label(left_inside_frame,text="Gender",font="comicsansns 13 bold",bg="white")
        genLabel.grid(row=1,column=2,padx=10,sticky=W)

        self.gender_combo=ttk.Combobox(left_inside_frame,font="comicsansns 13 bold",width=20,textvariable=self.var_atten_Gender,state="read only")
        self.gender_combo['values']=("Select Gender","Male","Female","Others")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=1,column=3,pady=8,sticky=W)

        # EmpID
        EmpIDLabel=Label(left_inside_frame,text="EmpID:",bg="white",font="comicsansns 13 bold")
        EmpIDLabel.grid(row=2,column=0,padx=4,pady=8,sticky=W)

        atten_ID=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_EmpID,font="comicsansns 13 bold")
        atten_ID.grid(row=2,column=1,pady=8,sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 13 bold")
        timeLabel.grid(row=2,column=2,padx=4,pady=8,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_Time,font="comicsansns 13 bold")
        atten_time.grid(row=2,column=3,pady=8,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 13 bold")
        dateLabel.grid(row=3,column=0,padx=4,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_Date,font="comicsansns 13 bold")
        atten_date.grid(row=3,column=1,pady=8,sticky=W)

        # status
        attendanceLabel=Label(left_inside_frame,text="Access Status",font="comicsansns 13 bold",bg="white")
        attendanceLabel.grid(row=3,column=2,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,font="comicsansns 13 bold",width=20,textvariable=self.var_atten_Status,state="read only")
        self.atten_status['values']=("Status","Detected","UnknownUserDetected")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=3,pady=8,sticky=W)

        #bbutons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=400,width=800,height=35)

        save_btn=Button(btn_frame,text="Import Csv",command=self.importCsv,width=18,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export Csv",command=self.exportCsv,width=18,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Upload",width=18,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)






        


        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Access Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=750,height=720)

        img_right = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\Control.jpg")
        img_right = img_right.resize((760,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=180)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=200,width=730,height=460)

        #============scroll bar table======================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("EmpName","DepartmentID","Gender","EmpID","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        #self.AttendanceReportTable.heading("DatabaseID",text="DatabaseID")
        self.AttendanceReportTable.heading("EmpName",text="EmpName")
        self.AttendanceReportTable.heading("DepartmentID",text="DepartmentID")
        self.AttendanceReportTable.heading("Gender",text="Gender")
        self.AttendanceReportTable.heading("EmpID",text="EmpID")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Status",text="Status")

        self.AttendanceReportTable["show"]="headings"

        #self.AttendanceReportTable.column("DatabaseID",width=100)
        self.AttendanceReportTable.column("EmpName",width=100)
        self.AttendanceReportTable.column("DepartmentID",width=100)
        self.AttendanceReportTable.column("Gender",width=100)
        self.AttendanceReportTable.column("EmpID",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Status",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==================fetch data=================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     #importCsv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row) 
        rows=content['values']
        #self.var_atten_DatabaseID.set(rows[0])
        self.var_atten_EmpName.set(rows[0])
        self.var_atten_DepartmentID.set(rows[1])
        self.var_atten_Gender.set(rows[2])
        self.var_atten_EmpID.set(rows[3])
        self.var_atten_Time.set(rows[4])
        self.var_atten_Date.set(rows[5])
        self.var_atten_Status.set(rows[6])

    def reset_data(self):
        #self.var_atten_DatabaseID.set("")
        self.var_atten_EmpName.set("")
        self.var_atten_DepartmentID.set("")
        self.var_atten_Gender.set("")
        self.var_atten_EmpID.set("")
        self.var_atten_Time.set("")
        self.var_atten_Date.set("")
        self.var_atten_Status.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()