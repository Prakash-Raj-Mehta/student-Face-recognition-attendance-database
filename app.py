from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import help_desk
from tkinter import messagebox

class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("1530x900")

        
        self.root.title("face Recognition System")

        img = Image.open("attendence_images/welcome.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img = img.resize((400, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0,y=0,width = 400,height = 120)

        img1 = Image.open("attendence_images/student_attendece.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img1 = img1.resize((500, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x = 400,y=0,width = 500,height = 120)

        img3 = Image.open("attendence_images/and.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img3 = img3.resize((200, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x = 900,y=0,width = 200,height = 120)

        img4 = Image.open("attendence_images/data_base.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img4 = img4.resize((400, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg4 = ImageTk.PhotoImage(img4)
                
        f_lbl = Label(self.root,image = self.photoimg4)
        f_lbl.place(x = 1100,y=0,width = 400,height = 120)




        #background image
        img5 = Image.open("attendence_images/home_back1.jpg")
        img5 = img5.resize((1690, 710), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
                        
        bg_img = Label(self.root,image = self.photoimg5)
        bg_img.place(x = 0,y=120,width = 1690,height = 710)

        title_lbl = Label(bg_img,text ="FACE RECOGNITION ATTENDANCE SYSTEM PAGE",font=("COPPERPLATE GOTHIC BOLI",35,"bold"),bg="lightgray",fg="red")
        title_lbl.place(x=0,y=0,width = 1530,height=45)


        # student button1
        img6 = Image.open("attendence_images/button.png")
        img6 = img6.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img ,image =self.photoimg6,command = self.student_details,cursor ="hand2")
        b1.place(x =180,y=100,width = 180,height=150)

        b1_1 = Button(bg_img ,text="Student Details",command = self.student_details,cursor ="hand2",font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_1.place(x =180,y=250,width = 180,height=40)

        # student button2
        img7 = Image.open("attendence_images/face_recognition.png")
        img7 = img7.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b2 = Button(bg_img ,image =self.photoimg7,cursor ="hand2",command=self.Face_recognition)
        b2.place(x =430+60,y=100,width = 180,height=150)
        b1_2 = Button(bg_img ,text="Face Rcognition",cursor ="hand2",command=self.Face_recognition,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_2.place(x =430+60,y=250,width = 180,height=40)




        # student button3
        img8 = Image.open("attendence_images/attendence.png")
        img8 = img8.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b3 = Button(bg_img ,image =self.photoimg8,cursor ="hand2",command=self.attendance_data)
        b3.place(x =680+90,y=100,width = 180,height=150)
        b1_3 = Button(bg_img ,text="Attendence",cursor ="hand2",command=self.attendance_data,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_3.place(x =680+90,y=250,width = 180,height=40)

        # student button
        img9 = Image.open("attendence_images/help_desk.png")
        img9 = img9.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b4 = Button(bg_img ,image =self.photoimg9,cursor ="hand2",command=self.help_sec)
        b4.place(x =930+120,y=100,width = 180,height=150)
        b1_4 = Button(bg_img ,text="Help Desk",cursor ="hand2",command=self.help_sec,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_4.place(x =930+120,y=250,width = 180,height=40)


        # student button down 5

        # student button down 5
        # student button down 5
        img10 = Image.open("attendence_images/Train_data.png")
        img10 = img10.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b5 = Button(bg_img ,image =self.photoimg10,cursor ="hand2",command=self.Train_data)
        b5.place(x =180,y=400,width = 180,height=150)
        b1_5 = Button(bg_img ,text="Train Data",cursor ="hand2",command=self.Train_data,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_5.place(x =180,y=550,width = 180,height=40)


        # student button2
        img11 = Image.open("attendence_images/pics.png")
        img11 = img11.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b6 = Button(bg_img ,image =self.photoimg11,cursor ="hand2",command=self.open_img)
        b6.place(x =430+60,y=400,width = 180,height=150)
        b1_6 = Button(bg_img ,text="Photos",cursor ="hand2",command=self.open_img,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_6.place(x =430+60,y=550,width = 180,height=40)


        # student button3
        img12 = Image.open("attendence_images/developer.png")
        img12 = img12.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg17 = ImageTk.PhotoImage(img12)
        b7 = Button(bg_img ,image =self.photoimg17,cursor ="hand2",command=self.developer_page)
        b7.place(x =680+90,y=400,width = 180,height=150)
        
        b1_7 = Button(bg_img ,text="Developer",cursor ="hand2",command=self.developer_page,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_7.place(x =680+90,y=550,width = 180,height=40)


        img13 = Image.open("attendence_images/exit.png")
        img13 = img13.resize((180, 150), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img13)
        b8 = Button(bg_img ,image =self.photoimg12,cursor ="hand2",command=self.iExit)
        b8.place(x =930+120,y=400,width = 180,height=150)
                
        b1_8 = Button(bg_img ,text="Exit",cursor ="hand2",command=self.iExit,font=("COPPERPLATE GOTHIC BOLI",15,"bold"),bg="lightgray",fg="red")
        b1_8.place(x =930+120,y=550,width = 180,height=40)


    def open_img(self):
        os.startfile("data")




        # ///////////////////////////////FUNCTION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
                

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app =Train(self.new_window)

    def Face_recognition(self):
        self.new_window =Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
    def attendance_data(self):
        self.new_window =Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    def help_sec(self):
        self.new_window = Toplevel(self.root)
        self.app = help_desk(self.new_window)
    def iExit(self):
        self.iExit = messagebox.askyesno(
    "Face Recognition",
    "Are you sure exit this page?"
)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
                
        
        



if __name__=="__main__":
    root=Tk()
    obj = Face_recognition_System(root)
    root.mainloop()
