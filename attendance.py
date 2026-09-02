from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime


mydata =[]
class Attendance:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("1350x600")

        
        self.root.title("FACE RECOGNITION MODEL")
        # ======================variables========================/
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()
        
        





        Left_frame = LabelFrame(root,bd=2,relief = RIDGE,text ="Student Details",font =("times new roman",12,"bold"),bg="white")
        Left_frame.place(x = 10,y=0,width=660,height=555)

        

        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief =RIDGE,text="current department",font =("times new roman",12,"bold"))
        current_course_frame.place(x = 0,y=5,width=655,height=540)

        attendanceId_label = Label(current_course_frame,textvariable=self.var_id,text = "Attendence ID",font=("times new roman",12,"bold"))
        attendanceId_label.grid(row=0,column = 0,padx=10,pady= 5,sticky=W)

        attendanceId_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row = 0,column = 1,padx=10,pady= 5,sticky=W)

        

        roll_label = Label(current_course_frame,text = "Roll",font=("times new roman",12,"bold"))
        roll_label.grid(row=0,column = 2,padx=10,pady= 5,sticky=W)

        roll_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        roll_entry.grid(row = 0,column = 3,padx=10,pady= 5,sticky=W)

        

        Name_label = Label(current_course_frame,text = "Name",font=("times new roman",12,"bold"))
        Name_label.grid(row=1,column = 0,padx=10,pady= 5,sticky=W)

        Name_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        Name_entry.grid(row = 1,column = 1,padx=10,pady= 5,sticky=W)

        

        departemt_label = Label(current_course_frame,text = "Department",font=("times new roman",12,"bold"))
        departemt_label.grid(row=1,column = 2,padx=10,pady= 5,sticky=W)

        departemt_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        departemt_entry.grid(row = 1,column = 3,padx=10,pady= 5,sticky=W)

        

        time_label = Label(current_course_frame,text = "Time",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column = 0,padx=10,pady= 5,sticky=W)

        time_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        time_entry.grid(row = 2,column = 1,padx=10,pady= 5,sticky=W)

        Date_label = Label(current_course_frame,text = "Date",font=("times new roman",12,"bold"))
        Date_label.grid(row=2,column = 2,padx=10,pady= 5,sticky=W)

        Date_entry = ttk.Entry(current_course_frame,width = 20,font=("times new roman",12,"bold"))
        Date_entry.grid(row = 2,column = 3,padx=10,pady= 5,sticky=W)

        gender_label = Label(current_course_frame,text = "Attendence Stetus",font=("times new roman",12,"bold"))
        gender_label.grid(row=3,column = 0,padx=10,sticky=W)
                
        gender_combo = ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo['values'] = ("select Attendace","Present","female","other")
        gender_combo.current(0)
        gender_combo.grid(row =3,column = 1,padx=10,pady=5,sticky=W)


        btn_frame = Frame(current_course_frame,bd = 2,relief = RIDGE)
        btn_frame.place(x = 0,y = 468, width = 650, height = 38)

        import_btn = Button(btn_frame,command=self.importCsv,width=17,text="Import",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        import_btn.grid(row = 0,column = 0)

        export_btn = Button(btn_frame,command=self.exportCsv,width=17,text="export",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        export_btn.grid(row = 0,column = 1)

        update_btn = Button(btn_frame,width=17,text="reset",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        update_btn.grid(row = 0,column = 2)

        delete_btn = Button(btn_frame,width=17,command=self.reset_data,text="delete",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        delete_btn.grid(row = 0,column = 3)

        


















        right_frame = LabelFrame(root,bd=2,relief = RIDGE,text ="Student Details",font =("times new roman",12,"bold"),bg="white")
        right_frame.place(x = 680,y=0,width=655,height=555)

        

        scroll_x =ttk.Scrollbar(right_frame,orient =HORIZONTAL)
        scroll_y =ttk.Scrollbar(right_frame,orient =HORIZONTAL)

        self.AttendanceReportTable= ttk.Treeview(right_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department Name")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        

        self.AttendanceReportTable.pack(fill= BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(
                    ("CSV File", "*.csv"),
                    ("ALL File", "*.*")
                ),
                parent=self.root
            )
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("no data","no data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                            initialdir=os.getcwd(),
                            title="Open CSV",
                            filetypes=(
                                ("CSV File", "*.csv"),
                                ("ALL File", "*.*")
                            ),
                            parent=self.root
                        )
            with open(fln,mode="w",newline="") as myfile:
                exp_write= csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.append(i)
                messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)
    def get_cursor(self,event=""):
        cursor_row= self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):

        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")
        

        
        







if __name__=="__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()