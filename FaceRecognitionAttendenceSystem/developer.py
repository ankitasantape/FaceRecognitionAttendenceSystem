from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"),
                          bg="Dodgerblue3", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # TOP
        img_top = Image.open("Images/bg1.jpg")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Main Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=515)

        # Developer Image
        img_top1 = Image.open("Images/ankita.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=305, y=0, width=200, height=200)

        # Developer Info
        dev_label = Label(main_frame, text="Hello I'm, Ankita!", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I'm a full stack developer", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0, y=40)

        # Third Image
        img3 = Image.open("Resources/wallpaper.jpg")
        img3 = img3.resize((500, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(main_frame, image=self.photoimg3)
        f_lbl.place(x=0, y=210, width=500, height=300)


if __name__ == '__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()