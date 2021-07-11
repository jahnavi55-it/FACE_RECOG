from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===============variables=================
        self.var_dept=StringVar()
        self.var_deptid=StringVar()
        self.var_deptloc=StringVar()
        self.var_empid=StringVar()
        self.var_name=StringVar()
        self.var_deptname=StringVar()
        self.var_gender=StringVar()
        self.var_age=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()

        #bg image
        img3 = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\bg.jpg")
        img3= img3.resize((1536,840),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=840)
        
        title_lbl=Label(bg_img,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1530,height=750)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=720)

        img_left = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\empdet.png")
        img_left = img_left.resize((760,160),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        #department information 
        department_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Department Info",font=("times new roman",12,"bold"))
        department_frame.place(x=5,y=135,width=750,height=150)
       
       
        #department 
        dep_label=Label(department_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(department_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo['values']=("Select Department","Accounts & Finance","HR","Sales & Marketing","Infrastructures","Research & Development","Learning & Development","IT services","Product Development","Quality Assurance","Technical Support","Security & Transport")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #department location

        loc_label=Label(department_frame,text="Department Location",font=("times new roman",12,"bold"),bg="white")
        loc_label.grid(row=0,column=2,padx=10,sticky=W)

        loc_combo=ttk.Combobox(department_frame,textvariable=self.var_deptloc,font=("times new roman",12,"bold"),width=17,state="read only")
        loc_combo['values']=("Select Dept Location","Bangalore","Chennai","Hyderabad","Visakhapatnam","New Delhi","Mumbai")
        loc_combo.current(0)
        loc_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #department Id
        id_label=Label(department_frame,text="Department ID",font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=1,column=0,padx=10,sticky=W)

        id_combo=ttk.Combobox(department_frame,textvariable=self.var_deptid,font=("times new roman",12,"bold"),width=17,state="read only")
        id_combo['values']=("Select Dept ID","EM001","EM002","EM003","EM004","EM005","EM006","EM007","EM008","EM009","EM010","EM011","EM012","EM013","EM014","EM015","EM016","EM017","EM018","EM019","EM020","EM021","EM022","EM023","EM024","EM025","EM026","EM027","EM028")
        id_combo.current(0)
        id_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        #Employee Information
        employee_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        employee_frame.place(x=5,y=300,width=750,height=380)

        #employee id

        EmployeeId_label=Label(employee_frame,text="Employee ID:",font=("times new roman",13,"bold"),bg="white")
        EmployeeId_label.grid(row=0,column=0,padx=10,sticky=W)

        EmployeeId_entry=ttk.Entry(employee_frame,textvariable=self.var_empid,width=20,font=("times new roman",13,"bold"))
        EmployeeId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #employee name
        Employeename_label=Label(employee_frame,text="Employee Name:",font=("times new roman",13,"bold"),bg="white")
        Employeename_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Employeename_entry=ttk.Entry(employee_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        Employeename_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #department name
        depn_label=Label(employee_frame,text="Department Name",font=("times new roman",13,"bold"),bg="white")
        depn_label.grid(row=1,column=0,padx=10,sticky=W)

        depn_combo=ttk.Combobox(employee_frame,textvariable=self.var_deptname,font=("times new roman",12,"bold"),width=20,state="read only")
        depn_combo['values']=("Select Department","Accounts & Finance","HR","Sales & Marketing","Infrastructures","Research & Development","Learning & Development","IT services","Product Development","Quality Assurance","Technical Support","Security & Transport")
        depn_combo.current(0)
        depn_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #gender
        gen_label=Label(employee_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gen_label.grid(row=1,column=2,padx=10,sticky=W)

        gen_combo=ttk.Combobox(employee_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="read only")
        gen_combo['values']=("Select Gender","Male","Female","Others")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #age
        Employeeage_label=Label(employee_frame,text="Age:",font=("times new roman",13,"bold"),bg="white")
        Employeeage_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Employeeage_entry=ttk.Entry(employee_frame,textvariable=self.var_age,width=20,font=("times new roman",13,"bold"))
        Employeeage_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Designation
        Employeedes_label=Label(employee_frame,text="Designation:",font=("times new roman",13,"bold"),bg="white")
        Employeedes_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Employeedes_entry=ttk.Entry(employee_frame,textvariable=self.var_designation,width=20,font=("times new roman",13,"bold"))
        Employeedes_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Employeemail_label=Label(employee_frame,text="Email Id:",font=("times new roman",13,"bold"),bg="white")
        Employeemail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Employeemail_entry=ttk.Entry(employee_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Employeemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #ph no
        Employeeph_label=Label(employee_frame,text="Phone Number:",font=("times new roman",13,"bold"),bg="white")
        Employeeph_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Employeeph_entry=ttk.Entry(employee_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        Employeeph_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        Employeeadd_label=Label(employee_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        Employeeadd_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Employeeadd_entry=ttk.Entry(employee_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Employeeadd_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #salary
        Employeesal_label=Label(employee_frame,text="Salary:",font=("times new roman",13,"bold"),bg="white")
        Employeesal_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Employeesal_entry=ttk.Entry(employee_frame,textvariable=self.var_salary,width=20,font=("times new roman",13,"bold"))
        Employeesal_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=8,column=0)

        radionbtn2=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=8,column=1)

        #bbutons frame
        btn_frame=Frame(employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=745,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=270,width=745,height=70)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=36,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=36,font=("times new roman",13,"bold"),bg="Gray",fg="black")
        update_photo_btn.grid(row=1,column=1)

        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=730,height=720)

        img_right = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\empd2.jpeg")
        img_right = img_right.resize((760,210),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=130)

        ###############SEARCH SYSTEM#####################
        #search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=130,width=720,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="indigo",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=20,state="read only")
        search_combo['values']=("Select","Employee ID","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=720,height=485)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dept","deptid","deptloc","empid","name","deptname","gender","age","designation","email","phone","address","salary","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


        self.employee_table.heading("dept",text="Department")
        self.employee_table.heading("deptid",text="DepartmentID")
        self.employee_table.heading("deptloc",text="DepartmentLoc")
        self.employee_table.heading("empid",text="EmployeeID")
        self.employee_table.heading("name",text="EmpName")
        self.employee_table.heading("deptname",text="DeptName")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("age",text="Age")
        self.employee_table.heading("designation",text="Designation")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("phone",text="PhoneNumber")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("salary",text="Salary")
        self.employee_table.heading("photo",text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

        self.employee_table.column("dept",width=100)
        self.employee_table.column("deptid",width=100)
        self.employee_table.column("deptloc",width=100)
        self.employee_table.column("empid",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("deptname",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("age",width=100)
        self.employee_table.column("designation",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.column("photo",width=150)




        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ###########################Function Declaration##########################
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_empid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            
                                                                                                              self.var_dept.get(),
                                                                                                              self.var_deptid.get(),
                                                                                                              self.var_deptloc.get(),
                                                                                                              self.var_empid.get(),
                                                                                                              self.var_name.get(),
                                                                                                              self.var_deptname.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_age.get(),
                                                                                                              self.var_designation.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_salary.get(),
                                                                                                              self.var_radio1.get()

                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #===================fetch data======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_deptid.set(data[1]),
        self.var_deptloc.set(data[2]),
        self.var_empid.set(data[3]),
        self.var_name.set(data[4]),
        self.var_deptname.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_age.set(data[7]),
        self.var_designation.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_salary.set(data[12]),
        self.var_radio1.set(data[13])

    # update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_empid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update employee set Department=%s,DepartmentID=%s,DepartmentLoc=%s,EmpName=%s,DeptName=%s,Gender=%s,Age=%s,Designation=%s,Email=%s,PhoneNumber=%s,Address=%s,Salary=%s,PhotoSample=%s where EmployeeID=%s",(
                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                 self.var_dept.get(),
                                                                                                                                                                                                                 self.var_deptid.get(),
                                                                                                                                                                                                                 self.var_deptloc.get(),
                                                                                                                                                                                                                
                                                                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                                                                 self.var_deptname.get(),
                                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                                 self.var_age.get(),
                                                                                                                                                                                                                 self.var_designation.get(),
                                                                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                 self.var_salary.get(),
                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                 self.var_empid.get()
                                                                                                                                                                                                                 
                                                                                                                                                                                                            
                                                                                                                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #====================delete function====================
    def delete_data(self):
        if self.var_empid.get=="":
            messagebox.showerror("Error","employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("employee Delete Page","Do you want to delete this employee",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor()
                    sql="delete from employee where EmployeeID=%s"
                    val=(self.var_empid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_deptid.set("select dept id")
        self.var_deptloc.set("select dept loc")
        self.var_empid.set("")
        self.var_name.set("")
        self.var_deptname.set("Dept Name")
        self.var_gender.set("Male")
        self.var_age.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_salary.set("")
        self.var_radio1.set("")

    #========== Generate data set or Take photo Sample===================
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_empid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update employee set Department=%s,DepartmentID=%s,DepartmentLoc=%s,EmpName=%s,DeptName=%s,Gender=%s,Age=%s,Designation=%s,Email=%s,PhoneNumber=%s,Address=%s,Salary=%s,PhotoSample=%s where EmployeeID=%s",(
                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                 self.var_dept.get(),
                                                                                                                                                                                                                 self.var_deptid.get(),
                                                                                                                                                                                                                 self.var_deptloc.get(),
                                                                                                                                                                                                                
                                                                                                                                                                                                                 self.var_name.get(),
                                                                                                                                                                                                                 self.var_deptname.get(),
                                                                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                                                                 self.var_age.get(),
                                                                                                                                                                                                                 self.var_designation.get(),
                                                                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                                                                 self.var_address.get(),
                                                                                                                                                                                                                 self.var_salary.get(),
                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                 self.var_empid.get()==id+1
                                                                                                                                                                                                        
                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==============load predefined data on face frontals from opencv===========
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!!!",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                                                                                                                                                                                                             
                                                                                                                                                                                                            
                                                    
                
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
