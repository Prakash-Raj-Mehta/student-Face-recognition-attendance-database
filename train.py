from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("1180x500")

        
        self.root.title("TRAIN DATA SET")


        img = Image.open(r"train_images\face_scan.jpg")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img = img.resize((230, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0,y=0,width = 230,height = 120)
        
        img1 = Image.open(r"train_images\face_recognition.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img1 = img1.resize((900, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg1 = ImageTk.PhotoImage(img1)
                
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x = 230,y=0,width = 1000,height = 120)

        img3 = Image.open(r"train_images\model_train.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img3 = img3.resize((430, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg3 = ImageTk.PhotoImage(img3)
                
        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x = 1130,y=0,width = 430,height = 120)


        #background image
        img5 = Image.open(r"student_images\back_page.jpg")
        img5 = img5.resize((1690, 710), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
                                
        bg_img = Label(self.root,image = self.photoimg5)
        bg_img.place(x = 0,y=120,width = 1690,height = 710)
        
        title_lbl = Label(bg_img,text ="STUDENT MANAGMENT SYSTEM PAGE",font=("COPPERPLATE GOTHIC BOLI",35,"bold"),bg="lightgray",fg="darkgreen")
        title_lbl.place(x=0,y=0,width = 1180,height=45)

        b1 = Button(bg_img ,command=self.train_classifier,text="TRAIN DATA",cursor ="hand2",font=("COPPERPLATE GOTHIC BOLI",15,"bold"))
        b1.place(x =500,y=150,width = 180,height=30)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces =[]
        ids =[]
        for image in path:
            img = Image.open(image).convert('L') #gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)




        # ==========================train the classifier=======================================
        clf = cv2.face.LBPHFaceRecognizer_create()
        # clf = cv2.faces.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets complete!!!")


        



if __name__=="__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()
    