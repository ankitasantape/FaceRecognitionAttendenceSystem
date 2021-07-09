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
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="TRAINING DATASET", font=("times new roman", 35, "bold"),
                          bg="Dodgerblue3", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # TOP
        img_top = Image.open("Images/trainn.png")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=75, width=1530, height=325)

        #Button
        b1_btn = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2"
                        ,width=17,
        font=("times new roman", 30, "bold"), bg="white", fg="Dodgerblue3")
        b1_btn.place(x=0, y=400,width=1530,height=60)

        # BOTTOM
        img_bottom = Image.open("Images/bg1.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=460, width=1530, height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #Gray Scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========Train the classifier and save ===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")



         
if __name__ == '__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()