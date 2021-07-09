import tkinter
from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
import cv2
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        # self.iExit = tkinter
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img1=Image.open("Images/face1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img2 = Image.open("Images/face1.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open("Images/face1.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # bg img
        img4 = Image.open("Images/bg1.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img,text="Face Recognition System Software",font=("times new roman",35,"bold"),bg="white",fg="Dodgerblue3")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #=========== Current Time =========================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background='white',foreground='Dodgerblue3')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # Student Details
        img5 = Image.open("Images/student.jpeg")
        img5 = img5.resize((215, 215), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="Dodgerblue3",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face button
        img6 = Image.open("Images/face rec.jpeg")
        img6 = img6.resize((215, 215), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data ,font=("times new roman", 15, "bold"), bg="Dodgerblue3",fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendence button
        img7 = Image.open("Images/Attendace.png")
        img7 = img7.resize((215, 215), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,command=self.attendance_data, cursor="hand2")
        b1.place(x=800, y=100,width=220, height=220)

        b1_1 = Button(bg_img,text="Attendence",command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="Dodgerblue3",fg="white")
        b1_1.place(x=800, y=300,width=220, height=40)

        # Help Desk
        img8 = Image.open("Images/help.jpeg")
        img8 = img8.resize((215, 215), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,command=self.helper, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk",command=self.helper, cursor="hand2", font=("times new roman", 15, "bold"), bg="Dodgerblue3",
                      fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train Images
        img9 = Image.open("Images/train.png")
        img9 = img9.resize((215, 215), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Image", cursor="hand2", font=("times new roman", 15, "bold"), bg="Dodgerblue3",
                      fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Captured Images
        img10 = Image.open("Images/images.jpg")
        img10 = img10.resize((215, 215), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img )
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Images Collection", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="Dodgerblue3",
                      fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer
        img11 = Image.open("Images/admin.jpeg")
        img11 = img11.resize((215, 215), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,command=self.developer_data, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer",command=self.developer_data,
                      cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="Dodgerblue3",
                      fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit
        img12 = Image.open("Images/exit.jpg")
        img12 = img12.resize((215, 215), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12,command=self.iExit, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit",command=self.iExit, cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="Dodgerblue3",
                      fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    #=============Functions button=====================
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helper(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
