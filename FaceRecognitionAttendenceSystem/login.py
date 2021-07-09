from main import Face_Recognition_System
from Register import Register
import tkinter
from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import time
import datetime
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("1530x780+0+0")
        self.root.geometry("1600x900+0+0")
        self.root.title("Login")

        self.bg = ImageTk.PhotoImage(file=r"Images/bg1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # frame
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open("Images/login.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1,bg="white",borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="Dodgerblue3",bg="white")
        get_str.place(x=95,y=100)

        #label
        #username
        username = lbl=Label(frame,text="Username", font=("times new roman",15,"bold"),fg="Dodgerblue3",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #password
        password = lbl = Label(frame, text="Password", font=("times new roman",15,"bold"), fg="Dodgerblue3", bg="white")
        password.place(x=70, y=225)

        self.txtpass =ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250,width=270)

        #=============== Icon Images ===============
        img2 = Image.open("Images/login.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimg2, bg="Dodgerblue3", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("Images/lock.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimg3, bg="Dodgerblue3", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # login button
        loginbtn = Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="Dodgerblue3",activeforeground="white",activebackground="Dodgerblue3")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # New User Register button
        registerbtn = Button(frame,command=self.register_window, text="New User Register", font=("times new roman", 10, "bold"),borderwidth=0,fg="Dodgerblue3",bg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=20, y=350, width=120)

        # Forgetpassword button
        registerbtn = Button(frame,command=self.forgot_password_window, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0 ,fg="Dodgerblue3",bg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=12.5, y=370, width=120)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="Ankita" and self.txtpass.get()=="abcd1":
            messagebox.showinfo("success","Welcome to student portal")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Ankita$99",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))

            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.root)
                else:
                    if not open_main:
                        return
            conn.commit()
           # self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")


    #============ Reset Password ================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Ankita$99",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpassword.get(),self.txtuser.get())
                    my_cursor.execute(query,value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #============ Forgot Password ===============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Ankita$99",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Reset Password", font=("times new roman", 20, "bold"), fg="white", bg=""
                                                                                                                  "Dodgerblue3")
                l.place(x=0, y=10, relwidth=1)

                # ------------ row3
                security_Q = Label(self.root2, text="Select Security Questions: ", font=("times new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q['values'] = ("Select", "Your BirthPlace", "Your Father's Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer: ", font=("times new roman", 15, "bold"), bg="white",
                                   fg="black")
                security_A.place(x=50, y=150)

                self.txt_security_A = ttk.Entry(self.root2,
                                                font=("times new roman", 15, "bold"))
                self.txt_security_A.place(x=50, y=180, width=250)

                # New Password
                newpassword = Label(self.root2, text="Enter New Password: ", font=("times new roman", 15, "bold"),
                                   bg="white",
                                   fg="black")
                newpassword.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2,
                                                font=("times new roman", 15, "bold"))
                self.txt_newpassword.place(x=50, y=250, width=250)

                # Reset Button
                resetbtn = Button(self.root2,command=self.reset_pass, text="Reset", font=("times new roman", 15, "bold"),
                                    bg="white",
                                    fg="black")
                resetbtn.place(x=120, y=290)


#============= Register Class ===========
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register")

        #========== Variables ===========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        #======== bg image ======================
        self.bg = ImageTk.PhotoImage(file=r"Images/bg1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #=========== left image =======================
        self.bg1 = ImageTk.PhotoImage(file=r"Images/face_detect.jpg")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=50, y=100, width=470, height=550)

        #============= Main frame ========================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100,width=800,height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="Dodgerblue3", bg="white")
        register_lbl.place(x=60, y=20)

        # ============ label and entry =====================
        # ------------ row1
        # First Name
        firstname = Label(frame, text="First Name", font=("times new roman", 15, "bold") ,bg="white",fg="black")
        firstname.place(x=50, y=100)

        self.firstname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        self.firstname_entry.place(x=50,y=130,width=250)

        # Last Name
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # ------------ row2
        # Contact Number
        contact = Label(frame, text="Contact No: ", font=("times new roman", 15, "bold"), bg="white",fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email: ", font=("times new roman", 15, "bold"), bg="white",fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # ------------ row3
        security_Q = Label(frame, text="Select Security Questions: ", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"),state="readonly" )
        self.combo_security_Q['values'] = ("Select", "Your BirthPlace", "Your Father's Name", "Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer: ",font=("times new roman", 15, "bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
        self.txt_security_A.place(x=370,y=270,width=250)

        #--------------------row4
        pswd=Label(frame,text="Password: ", font=("times new roman", 15, "bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password: ", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #========= Check button =========================
        self.var_check = IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions ",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #============= Buttons ============================
        img=Image.open("Images/Register.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1 = Image.open("Images/login-b.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=330, y=420, width=200)

        #================= Funtion Declaration ==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Ankita$99",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","Registration done Successfully!!")








if __name__ == '__main__':
    main()