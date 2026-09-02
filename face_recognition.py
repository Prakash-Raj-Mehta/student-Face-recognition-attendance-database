from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_recognition:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("300x600")

        
        self.root.title("FACE RECOGNITION MODEL")

        title_lbl = Label(root,text ="Face Recognition Model",font=("COPPERPLATE GOTHIC BOLI",5,"bold"),bg="lightgray",fg="darkgreen")
        title_lbl.place(x=0,y=0,width =205,height=20)



        img5 = Image.open(r"student_images\face_scan.jpg")
        img5 = img5.resize((300, 600), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
                                
        bg_img = Label(root,image = self.photoimg5)
        bg_img.place(x = 0,y=0,width = 300,height = 600)

        b1 = Button(root ,text="click hear",command=self.face_recog,cursor ="hand2",font=("COPPERPLATE GOTHIC BOLI",10,"bold"))
        b1.place(x =75,y=500,width = 150,height=30)

    # ==================================attendence==============================
    def mark_attendance(self,i,r,n,d):
        with open("kran.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry =line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

                                                                   
                                                                   



        # ==============face recognition=================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
                my_cursor = conn.cursor()
                # my_cursor.execute("select Name from student_data where id="+str(id))
                # n= my_cursor.fetchone()
                # # result= my_cursor.fetchone()
                # n="+".join(n)
                # my_cursor.execute("select Roll from student_data where id="+str(id))
                # r= my_cursor.fetchone()
                # r="+".join(r)

                # my_cursor.execute("select Dep from student_data where id="+str(id))
                # d= my_cursor.fetchone()
                # d="+".join(d)
                # my_cursor.execute("select id from student_data where id="+str(id))
                # i= my_cursor.fetchone()
                # i="+".join(i)
                my_cursor.execute(
                    "SELECT id, Name, Roll, Dep FROM student_data WHERE id = %s",
                    (id,)
                )
                result = my_cursor.fetchone()

                if result and confidence > 77:

                    i, n, r, d = result

                    i = str(i)
                    n = str(n)
                    r = str(r)
                    d = str(d)

                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        f"Department:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    self.mark_attendance(i, r, n, d)

                else:

                    cv2.rectangle(
                        img,
                        (x, y),
                        (x + w, y + h),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3
                    )

                    coord = [x, y, w, h]


                my_cursor.close()
                conn.close()

                
                

                

                # if confidence > 77:
                    
                #     # cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     # cv2.putText(img,f"Roll:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     # cv2.putText(img,f"Name:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     # cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                #     self.mark_attendance(i,r,n,d)
                # else:
                #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                #     cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     coord=[x,y,w,h]
                # my_cursor.close()
                # conn.close()
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Wlcome To face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




                        
                        






if __name__=="__main__":
    root=Tk()
    obj = Face_recognition(root)
    root.mainloop()
