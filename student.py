from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class student:
    def __init__(self,root):
        self.root=root
        # self.root.geometry("900x700+0+0")
        self.root.geometry("1530x900")

        
        self.root.title("student data base")


        # ************************variables*********************************
        self.var_dep=StringVar()
        self.var_course =StringVar()  
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
       
        img = Image.open(r"student_images\girl_student.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img = img.resize((200, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x = 0,y=0,width = 200,height = 120)
        
        img1 = Image.open(r"student_images\studentdetails.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img1 = img1.resize((1000, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg1 = ImageTk.PhotoImage(img1)
                
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x = 200,y=0,width = 1000,height = 120)

        img3 = Image.open(r"student_images\data.png")
        # img = img.resize((500,130),Image.ANTIALIAS)
        img3 = img3.resize((330, 120), Image.Resampling.LANCZOS)
        # self.photoimg = imageTk.PhotoImage(img)
        self.photoimg3 = ImageTk.PhotoImage(img3)
                
        f_lbl = Label(self.root,image = self.photoimg3)
        f_lbl.place(x = 1200,y=0,width = 330,height = 120)


        #background image
        img5 = Image.open(r"student_images\back_page.jpg")
        img5 = img5.resize((1690, 710), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
                                
        bg_img = Label(self.root,image = self.photoimg5)
        bg_img.place(x = 0,y=120,width = 1690,height = 710)
        
        title_lbl = Label(bg_img,text ="STUDENT MANAGMENT SYSTEM PAGE",font=("COPPERPLATE GOTHIC BOLI",35,"bold"),bg="lightgray",fg="darkgreen")
        title_lbl.place(x=0,y=0,width = 1530,height=45)




        overlay = Image.new("RGBA", (1500, 650), (255, 255, 255, 100))
        self.overlay_img = ImageTk.PhotoImage(overlay)

        main_frame = Label(bg_img, image=self.overlay_img, bd=2)
        main_frame.place(x=20, y=55, width=1500, height=600)


        Left_frame = LabelFrame(main_frame,bd=2,relief = RIDGE,text ="Student Details",font =("times new roman",12,"bold"),bg="white")
        Left_frame.place(x = 100,y=10,width=660,height=580)

        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief =RIDGE,text="current department",font =("times new roman",12,"bold"))
        current_course_frame.place(x = 0,y=5,width=655,height=250)

        #department
        dep_label = Label(current_course_frame,text = "Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column = 0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values'] = ("select Department","Computer","IT","Civil","Mechanical","Bio","Manegment")
        dep_combo.current(0)
        dep_combo.grid(row =0,column = 1,padx=2,pady=10,sticky=W)


        #department
        course_label = Label(current_course_frame,text = "Cource",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column = 2,padx=10,sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo['values'] = ("select Cource","B tech","BCA","BBA","Nursing","MBBS","MBA","MCA","M Tech")
        course_combo.current(0)
        course_combo.grid(row =0,column = 3,padx=2,pady=10,sticky=W)


        #department
        year_label = Label(current_course_frame,text = "Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column = 0,padx=10,sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo['values'] = ("select Department","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028")
        year_combo.current(0)
        year_combo.grid(row =1,column = 1,padx=2,pady=10,sticky=W)

        #department
        semester_label = Label(current_course_frame,text = "Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column = 2,padx=10,sticky=W)
                
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo['values'] = ("select Semester","Computer","1st","2nd","3rd","Last Year")
        semester_combo.current(0)
        semester_combo.grid(row =1,column = 3,padx=2,pady=10,sticky=W)


        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief =RIDGE,text="Class Student information",font =("times new roman",12,"bold"))
        class_student_frame.place(x = 0,y=250,width=655,height=300)

        # student id
        student_id_label = Label(class_student_frame,text = "ID",font=("times new roman",12,"bold"))
        student_id_label.grid(row=0,column = 0,padx=10,pady= 5,sticky=W)

        student_entry = ttk.Entry(class_student_frame,textvariable=self.var_id,width = 20,font=("times new roman",12,"bold"))
        student_entry.grid(row = 0,column = 1,padx=10,pady= 5,sticky=W)



        student_name_label = Label(class_student_frame,text = "Name",font=("times new roman",12,"bold"))
        student_name_label.grid(row=0,column = 2,padx=10,pady= 5,sticky=W)
        
        student_nametry = ttk.Entry(class_student_frame,textvariable=self.var_name,width = 20,font=("times new roman",12,"bold"))
        student_nametry.grid(row = 0,column = 3,padx=10,pady= 5,sticky=W)



        # class_div_label = Label(class_student_frame,text = "Division",font=("times new roman",12,"bold"))
        # class_div_label.grid(row=1,column = 0,padx=10,pady= 5,sticky=W)
        
        # class_divtry = ttk.Entry(class_student_frame,textvariable=self.var_div,width = 20,font=("times new roman",12,"bold"))
        # class_divtry.grid(row = 1,column = 1,padx=10,pady= 5,sticky=W)


        class_div_label = Label(class_student_frame,text = "Division",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column = 0,padx=10,sticky=W)
                
        class_div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        class_div_combo['values'] = ("select division","A","B","C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row =1,column = 1,padx=10,pady=5,sticky=W)




        student_id_label = Label(class_student_frame,text = "Roll no",font=("times new roman",12,"bold"))
        student_id_label.grid(row=1,column = 2,padx=10,pady= 5,sticky=W)
        
        student_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width = 20,font=("times new roman",12,"bold"))
        student_entry.grid(row = 1,column = 3,padx=10,pady= 5,sticky=W)


        

        # gender_label = Label(class_student_frame,text = "Gender",font=("times new roman",12,"bold"))
        # gender_label.grid(row=2,column = 0,padx=10,pady= 5,sticky=W)
        
        # gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,width = 20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row = 2,column = 1,padx=10,pady= 5,sticky=W)
        gender_label = Label(class_student_frame,text = "Gender",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column = 0,padx=10,sticky=W)
                
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo['values'] = ("select gender","Male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row =2,column = 1,padx=10,pady=5,sticky=W)

        dob_label = Label(class_student_frame,text = "Date of Birth",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column = 2,padx=10,pady= 5,sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width = 20,font=("times new roman",12,"bold"))
        dob_entry.grid(row = 2,column = 3,padx=10,pady= 5,sticky=W)
        email_label = Label(class_student_frame,text = "Email",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column = 0,padx=10,pady= 5,sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width = 20,font=("times new roman",12,"bold"))
        email_entry.grid(row = 3,column = 1,padx=10,pady= 5,sticky=W)
        
        
        phone_label = Label(class_student_frame,text = "Phone nu",font=("times new roman",12,"bold"))
        
        
        phone_label.grid(row=3,column = 2,padx=10,pady= 5,sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width = 20,font=("times new roman",12,"bold"))
        phone_entry.grid(row = 3,column = 3,padx=10,pady= 5,sticky=W)

        address_label = Label(class_student_frame,text = "Address",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column = 0,padx=10,pady= 5,sticky=W)
                
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width = 20,font=("times new roman",12,"bold"))
        address_entry.grid(row = 4,column = 1,padx=10,pady= 5,sticky=W)

        teacher_label = Label(class_student_frame,text = "Class Teacher Name",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column = 2,padx=10,pady= 5,sticky=W)
                
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width = 20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row = 4,column = 3,padx=10,pady= 5,sticky=W)



        #radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable = self.var_radio1, text="Face sample",value="Yes")
        radiobtn1.grid(row = 6,column=0)

        
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable = self.var_radio1, text="No Face sample",value="No")
        radiobtn2.grid(row = 6,column=1)


        #button frame
        btn_frame = Frame(class_student_frame,bd = 2,relief = RIDGE)
        btn_frame.place(x = 0,y = 210, width = 720, height = 38)

        

        save_btn = Button(btn_frame,width=17,text="save",command = self.add_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        save_btn.grid(row = 0,column = 0)

        update_btn = Button(btn_frame,width=17,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        update_btn.grid(row = 0,column = 1)

        delete_btn = Button(btn_frame,width=17,text="delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        delete_btn.grid(row = 0,column = 2)

        reset_btn = Button(btn_frame,width=17,text="reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row = 0,column = 3)

        btn_frame1 = Frame(class_student_frame,bd = 2,relief = RIDGE)
        btn_frame1.place(x = 0,y = 248, width = 720, height = 38)

        update_btn = Button(btn_frame1,width=35,text="Update face sample",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        update_btn.grid(row = 0,column = 1)
        
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,width=35,text="Take face sample",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        take_photo_btn.grid(row = 0,column = 0)

        

        




















#  ***********************************right box main **************************************************       
        
        right_frame = LabelFrame(main_frame,bd=2,relief = RIDGE,text ="Student Details",font =("times new roman",12,"bold"),bg="white")
        right_frame.place(x = 770,y=10,width=660,height=580)
# ===================================search bar =============================================
        search_frame = LabelFrame(right_frame,bd =2,bg="white",relief = RIDGE,text="search box")
        search_frame.place(x=5,y = 5,width = 650,height= 70)

        search_label = Label(search_frame,text = "search bar",font=("times new roman",12,"bold"))
        search_label.grid(row=0,column = 0,padx=10,pady= 5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo['values'] = ("select","roll no","phone nu")
        search_combo.current(0)
        search_combo.grid(row =0,column = 1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width = 20,font=("times new roman",12,"bold"))
        search_entry.grid(row = 0,column = 2,padx=10,pady= 5,sticky=W)

        search_btn = Button(search_frame,width=8,text="search",font=("times new roman",12,"bold"),bg="white",fg="black")
        search_btn.grid(row = 0,column = 3)
        
        showall_btn = Button(search_frame,width=8,text="show all",font=("times new roman",12,"bold"),bg="white",fg="black")
        showall_btn.grid(row = 0,column = 4)



        # ======================table frame ====================
        table_frame = Label(right_frame,bd =2,bg="white",relief = RIDGE,text="search box")
        table_frame.place(x=5,y = 75,width = 650,height= 480)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # scroll_x.config(command=self.student_table.xview)
        # scroll_y.config(command=self.student_table.yview)

        self.student_table = ttk.Treeview(table_frame,
                                          columns = ("dep","course","year","semester","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),
                                          xscrollcommand = scroll_x.set,
                                          yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        


        self.student_table.heading("dep",text= "Department")
        self.student_table.heading("course",text= "course")
        self.student_table.heading("year",text= "Year")
        self.student_table.heading("semester",text= "Semester")
        self.student_table.heading("id",text= "Student ID")
        self.student_table.heading("name",text= "Name")
        self.student_table.heading("div",text= "Division")
        self.student_table.heading("roll",text= "Roll no")
        self.student_table.heading("gender",text= "Gender")
        self.student_table.heading("dob",text= "Date of Birth")
        self.student_table.heading("email",text= "Email Id")
        self.student_table.heading("phone",text= "Contact")
        self.student_table.heading("address",text= "address")
        self.student_table.heading("teacher",text= "calss teacher")
        self.student_table.heading("photo",text= "Face sample Status")
        
        self.student_table["show"]="headings"

        self.student_table.pack(side=LEFT, fill=BOTH, expand=1)
        self.student_table.column("dep",width= 100)
        self.student_table.column("course",width= 100)
        self.student_table.column("year",width= 100)
        self.student_table.column("semester",width= 100)
        self.student_table.column("id",width= 100)
        self.student_table.column("name",width= 100)
        self.student_table.column("div",width= 100)
        self.student_table.column("roll",width= 100)
        self.student_table.column("gender",width= 100)
        self.student_table.column("dob",width= 100)
        self.student_table.column("email",width= 100)
        self.student_table.column("phone",width= 100)
        self.student_table.column("address",width= 100)
        self.student_table.column("teacher",width= 100)
        self.student_table.column("photo",width= 100)

        self.student_table.pack(side=LEFT, fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # /////////////////////////////////////////////FUNCTION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Warrnig","All Fields are compulsary",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                        
                                        
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()


                messagebox.showinfo("successful","all details are subbmited",parent=self.root)
                messagebox.showinfo("thank","you",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


        # ===================fetch data===================
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_data")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values = i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_focus =self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data =content['values']

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Warrnig","All Fields are compulsary",parent=self.root)
        else:
            try:
                Upadate = messagebox .askyesno("Updade","Do u want to update this student_data details",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student_data set Dep = %s,course = %s,Year=%s,Semester=%s,Name=%s,Division= %s,Roll=%s,Gender=%s,Dob = %s,Email= %s,Phone= %s,Adderss=%s,Teacher=%s,Photosample=%s where id =%s",(
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            # self.var_id.get(),
                                            self.var_name.get(),
                                            self.var_div.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_radio1.get(),
                                            self.var_id.get()
                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Sudent details successfully update compale",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f" Due To:{str(es)}",parent=self.root)


    # delete function/////////////////

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must be requered ", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Dalele page","Do you want to delete this student Details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
                    my_cursor = conn.cursor()
                    sql = "delete from student_data where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f" Due To:{str(es)}",parent=self.root)

    # reset function =================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ==================generate photo sample==================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Warrnig","All Fields are compulsary",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(host = "localhost",user = "root",password="Prakashcoder14$",database="attendence_data")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student_data")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student_data set Dep = %s,course = %s,Year=%s,Semester=%s,Name=%s,Division= %s,Roll=%s,Gender=%s,Dob = %s,Email= %s,Phone= %s,Adderss=%s,Teacher=%s,Photosample=%s where id =%s",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            # self.var_id.get(),
                                                            self.var_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_radio1.get(),
                                                            self.var_id.get()==id+1
                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ==========================load predifiend data from face =====================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    #minimum Neightbor = 5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,155,0),2)
                        cv2.imshow("Croped face",face)
                    if cv2.waitKey(1)==13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","Generating data sets compled!!!!")
            except Exception as es:
                messagebox.showerror("Error",f" Due To:{str(es)}",parent=self.root)



        
        
        







        
        
               






        
        
                
        
                

        






if __name__=="__main__":
    root=Tk()
    obj = student(root)
    root.mainloop()