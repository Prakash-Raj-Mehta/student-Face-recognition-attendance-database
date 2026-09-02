from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class help_desk:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("600x400")
        right_frame = LabelFrame(root,bd=2,relief = RIDGE,text ="Help Section",font =("times new roman",12,"bold"),bg="white")
        
        right_frame.place(x = 100,y=100,width=400,height=225)

        email_label = Label(right_frame,text = "Send a email if you face any \nproblem in thish strudent attendance ,\nface recognition software",font=("times new roman",14,"bold"))
        email_label.grid(row=0,column = 0,padx=10,pady= 5,sticky=W)
        email_label = Label(right_frame,text = "Email",font=("times new roman",12,"bold"))
        email_label.grid(row=1,column = 0,padx=10,pady= 5,sticky=W)

        email_label = Label(right_frame,text = "prakashkuswaha2008@gmail.com",font=("times new roman",10,"bold"),fg='green')
        email_label.grid(row=2,column = 0,padx=10,pady= 5,sticky=W)

        
        

if __name__=="__main__":
    root=Tk()
    obj = help_desk(root)
    root.mainloop()