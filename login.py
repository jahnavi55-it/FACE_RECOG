from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        bg = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\login.jpg")
        bg= bg.resize((1536,840),Image.ANTIALIAS)
        self.photobg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photobg)
        bg_img.place(x=0,y=0,width=1530,height=840)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\log.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started!!",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=135,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=135,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

         #======================Icon Images====================
        img2=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\l1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lbl_img3.place(x=650,y=395,width=25,height=25)

        #Login button
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="red")
        login_btn.place(x=110,y=300,width=120,height=35)

        #register button
        register_btn=Button(frame,text="New User Register Now",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="red",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=15,y=350,width=160)

        #forgot password button
        forgotpassword_btn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassword_btn.place(x=10,y=370,width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Successful","Welcome to Face Recognition Using Survellience System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #====================reset ==========================
    def reset_password(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error","Select security Quesion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,vlue)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","your password as been reset,please login new password",parent=self.root2)
                self.root2.destroy()




    #=====================forget password===============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","you enter the email addres to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror(" My Error","you enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("350x450+610+0")

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="black",bg="lightblue")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Mother's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new font",15,"bold"),command=self.reset_password,fg="white",bg="blue")
                btn.place(x=100,y=300)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #==============Variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #====bg image====================
        bg = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\re.jpg")
        bg= bg.resize((1536,840),Image.ANTIALIAS)
        self.photobg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photobg)
        bg_img.place(x=0,y=0,width=1536,height=840)

        #===========left image==============
        left_img = Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\le.jpeg")
        left_img= left_img.resize((470,550),Image.ANTIALIAS)
        self.photoleft_img=ImageTk.PhotoImage(left_img)

        leftimg=Label(self.root,image=self.photoleft_img)
        leftimg.place(x=50,y=100,width=470,height=550)
        
        #=======main Frame=============
        frame=Frame(self.root,bg="#ffce00")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",24,"bold"),fg="black",bg="#ffce00")
        register_lbl.place(x=20,y=20)

        #===================================label and entry=============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="#ffce00")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #==================row2==========================

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #======================row3===========================

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Mother's Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #==================row4===============

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="#ffce00",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=============checkbox====================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms and Conditions",font=("times new roman",12,"bold"),bg="#ffce00",activebackground="#ffce00",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

         #=============button============================
        img1=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\r1.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",bg="#ffce00",activebackground="#ffce00")
        b1.place(x=330,y=420,width=300)

        img=Image.open(r"C:\Users\Jahnavi\Desktop\Face-Recognition-for-Survelliance\main_face\b1.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.return_login,borderwidth=0,cursor="hand2",bg="#ffce00",activebackground="#ffce00")
        b1.place(x=10,y=420,width=300)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="rootpasswordgiven",database="face_recognizer",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try a valid email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_securityQ.get(),
                                                                                      self.var_securityA.get(),
                                                                                      self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Successful","Register successful")

    def return_login(self):
        self.root.destroy()
            






if __name__=="__main__":
    main()