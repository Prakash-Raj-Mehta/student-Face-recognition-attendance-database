from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("600x600")

        
        img5 = Image.open(r"attendence_images\developer_back.jpg")
        img5 = img5.resize((600, 600), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
                                
        bg_img = Label(self.root,image = self.photoimg5)
        bg_img.place(x = 0,y=0,width = 600,height = 600)


        img3 = Image.open(r"attendence_images\02.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img3 = img3.resize((150, 200), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg3 = ImageTk.PhotoImage(img3)
                
        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x = 225,y=50,width = 150,height = 200)


        right_frame = LabelFrame(root,bd=2,relief = RIDGE,text ="info",font =("times new roman",12,"bold"),bg="white")

        right_frame.place(x = 100,y=300,width=400,height=225)

        email_label = Label(right_frame,text = "Name",font=("times new roman",12,"bold"))
        email_label.grid(row=0,column = 0,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "PRAKASH KUMAR",font=("times new roman",12,"bold"))
        email_label.grid(row=0,column = 1,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "Email",font=("times new roman",12,"bold"))
        email_label.grid(row=1,column = 0,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "prakashkuswaha2008@gmail.com",font=("times new roman",10,"bold"))
        email_label.grid(row=1,column = 1,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "Contact",font=("times new roman",12,"bold"))
        email_label.grid(row=2,column = 0,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "+91 9508824749",font=("times new roman",12,"bold"))
        email_label.grid(row=2,column = 1,padx=10,pady= 5,sticky=W)


if __name__=="__main__":
    root=Tk()
    obj = Developer(root)
    root.mainloop()