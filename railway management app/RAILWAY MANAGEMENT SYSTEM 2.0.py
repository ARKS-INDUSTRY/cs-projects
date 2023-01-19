from tkinter import *
import tkinter as tk
import mysql.connector as myc 
from tkinter import messagebox
import random
from tkinter import ttk
import os

#creating main window and title,gemoetr,bg of the window and also the icon for the window
root =tk.Tk()
root.title("RAILWAY MANAGEMENT SYSTEM")
root.iconbitmap("D:\\Computer Science project RAILWAY MANAGEMENT SYSTEM 2022-23\\icon.ico")
root.config(bg="green")
root.geometry("1000x1000")

#background wallpaper for the window and frames
g=PhotoImage(file="D:\\Computer Science project RAILWAY MANAGEMENT SYSTEM 2022-23\\wallpaperflare.com_wallpaper.png")
background_label=Label(root,image=g)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#title of the project as label 
main_lab=Label(root,text='RAILWAY RESERVATION SYSTEM',fg="Dark blue",bg="gray",font=("Italic",30))
main_lab.pack()

#frame for the main buttons
mainframe=Frame(root,bg="gray")
mainframe.place(x=350,y=90,height=350,width=600)

def tree_view():
    global treeview_frame,PNR_entry,trv
    pnr=PNR_entry.get()
   
    s=ttk.Style()
    s.configure('Treeview', rowheight=40,columnheight=40)
    my_con=myc.connect(user="root",host="localhost",database="irctc",password="KR007@12345")
    my_cur=my_con.cursor()
    my_cur.execute("Select * from train")
    e=my_cur.fetchall()
    for i in e:
        if pnr==i[0] and trainname_inside.get()==i[1] and source_inside.get()==i[2] and destination_inside.get()==i[3]:
            showframe.destroy()
            treeview_frame=Frame(root,bg="orange",height=500,width=1500).place(x=0,y=100)
            trv=ttk.Treeview(treeview_frame,selectmode="browse")
            trv.place(x=150,y=150,width=1000,height=400)
            trv['columns']=("1","2","3","4","5","6","7","8","9")
            trv["show"]='headings'
            trv.column("1",width=100,anchor='c')
            trv.column("2",width=100,anchor='c')
            trv.column("3",width=100,anchor='c')
            trv.column("4",width=100,anchor='c')
            trv.column("6",width=60,anchor='c')
            trv.column("7",width=100,anchor='c')
            trv.column("8",width=100,anchor='c')
            trv.column("9",width=100,anchor='c')

            trv.heading("1",text="PNR_No")
            trv.heading("2",text="Train Name")
            trv.heading("3",text="SOurce Station")
            trv.heading("4",text="Destination")
            trv.heading("5",text="Name of the passenger")
            trv.heading("6",text="Gender")
            trv.heading("7",text="Fare")
            trv.heading("8",text="Time of travel")
            trv.heading("9",text="Age")
            trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        elif pnr=="" and trainname_inside.get()=="" and source_inside.get()=="" and destination_inside.get()=="":
            messagebox.showerror("ERROR 420","All fields are required")
        elif pnr!=i[0]:
            messagebox.showwarning("WARNING","Enter a valid PNR number ")
        else:
            print()

def trainnameop():
    global trainname_inside
    trainname_list=["Shatabdi", "Pallavan", "CSF Express", "Vaigai","Hazrat Nizamuddin","Kacheguda","Tejas","Vande Bharat"]
    trainname_inside=tk.StringVar(root)
    trainname_inside.set("Select your source station:")

    trainname_menu=tk.OptionMenu(showframe,trainname_inside,*trainname_list)
    trainname_menu.config(fg="red",bg="blue",font=("Helvetica",16))
    trainname_menu.place(x=90,y=240)


def destinationopt():
    global destination_inside
    destination_list=["Trivandrum-PK","Munnar-M","Seconderabad-SEC","Telangana-Tel"]
    destination_inside=tk.StringVar(root)
    destination_inside.set("Select your source station:")

    destination_menu=tk.OptionMenu(showframe,destination_inside,*destination_list)
    destination_menu.config(fg="red",bg="blue",font=("Helvetica",16))
    destination_menu.place(x=400,y=240)
    

def sourceopt():
    global source_inside
    source_list=["Chennai Egmore-MS","Tiruchirappalli-TPJ","Mangalore-Mn","Madura-MDS","Rameswaram-RMS","Coimbatore-SL","guruvoyur-GV"]
    source_inside=tk.StringVar(root)
    source_inside.set("Select your source station:")

    source_menu=tk.OptionMenu(showframe,source_inside,*source_list)
    source_menu.config(fg="red",bg="blue",font=("Helvetica",16))
    source_menu.place(x=500,y=130)
    

def showtkt():
    global showframe,PNR_entry
    mainframe.destroy()
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute("select * from train")
    e=cur.fetchall()

    showframe=Frame(root,bg="Indigo")
    showframe.place(x=250,y=90,height=400,width=900)
    
    PNR_lab=Label(showframe,text="Enter your PNR_No:",bg="Blue",fg="red",font=("Helvetica",18)).place(x=90,y=90)
    PNR_entry=Entry(showframe,font=("Corbert Condensed Italic",16),bg="lightgray",width=25)
    PNR_entry.place(x=90,y=130)

    source_lab=Label(showframe,text="Select your source station:",bg="Blue",fg="red",font=("Helvetica",18)).place(x=500,y=90)
    sourceopt()
    
    destin_lab=Label(showframe,text="Select your destination",bg="blue",fg="red",font=("Helvetica",18)).place(x=400,y=200)
    destinationopt()

    train_lab=Label(showframe,text="Select your train name:",bg="blue",fg="red",font=("Helvetica",18)).place(x=90,y=200)
    trainnameop()

    search_button=Button(showframe,text=" View my ticket ",bg="Green",fg="lightgray",font=("Helvetica",20),command=tree_view).place(x=600,y=300)
    
def fare():
    global fare_lab_N,fare1
    #fare label
    fare_label=Label(booktkt_frame,text="Fare of the tkt:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    fare_label.place(x=275,y=415)
    fare1=StringVar(root)
    fare1.set("500")
    # fare2=fare1.get()
    # print(fare2)
    fare_lab_N=Label(booktkt_frame,text="250",textvariable=fare1,bg="lightgray",font=(18))
    fare_lab_N.place(x=275,y=450)

    if value_inside.get()== "Shatabdi":
        fare1.set("400")
    elif value_inside.get() == "Pallavan":
        fare1.set("500")
    elif value_inside.get()=="CSF Express":
        fare1.set("700")
    elif value_inside.get()=="Vaigai":
        fare1.set("800")
    elif value_inside.get()=="Hazrat Nizamuddin":
        fare1.set("900")
    elif value_inside.get()=="Kacheguda":
        fare1.set("1400")
    elif value_inside.get()=="Tejas":
        fare1.set("16000")
    elif value_inside.get()=="Vande Bharat":
        fare1.set("4000")
    


def timeop():
    global time_inside
    time_list=["2:00PM","3:00PM","11:00PM","10:30PM","5:00PM"]
    time_inside=tk.StringVar(root)
    time_inside.set("Select your time:")

    time_menu=tk.OptionMenu(booktkt_frame,time_inside,*time_list)
    time_menu.config(fg="red",bg="yellow",font=("Helvetica",16))
    time_menu.place(x=375,y=350)




def genop():
    global gen_inside
    gen_list=["M","F"]
    gen_inside=tk.StringVar(root)
    gen_inside.set("Select your gender:")

    gen_menu=tk.OptionMenu(booktkt_frame,gen_inside,*gen_list)
    gen_menu.config(fg="red",bg="yellow",font=("Helvetica",16))
    gen_menu.place(x=25,y=350)  
    
def desop():
    global des_inside
    des_list=["Trivandrum-PK","Munnar-M","Seconderabad-SEC","Telangana-Tel"]
    des_inside=tk.StringVar(root)
    des_inside.set("Select you Destination:")
    
    des_menu=tk.OptionMenu(booktkt_frame,des_inside,*des_list)
    des_menu.config(fg="red",bg="yellow",font=("Helvetica",16))
    des_menu.place(x=375,y=165)

def souop():
    global sou_inside
    sou_list=["Chennai Egmore-MS","Tiruchirappalli-TPJ","Mangalore-Mn","Madura-MDS","Rameswaram-RMS","Coimbatore-SL","guruvoyur-GV"]
    sou_inside=tk.StringVar(root)
    sou_inside.set("Select your source station:")
    
    sou_menu=tk.OptionMenu(booktkt_frame,sou_inside,*sou_list)
    sou_menu.config(fg="red",bg="yellow",font=("Helvetica",16))
    sou_menu.place(x=25,y=165)


#variables to store the data entered in textbox
def showop():
    global value_inside

    options_list = ["Shatabdi", "Pallavan", "CSF Express", "Vaigai","Hazrat Nizamuddin","Kacheguda","Tejas","Vande Bharat"]
    
  
# Variable to keep track of the option
# selected in OptionMenu
    value_inside = tk.StringVar(root)
  
# Set the default value of the variable
    value_inside.set("Select the train of your choice")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
    question_menu = tk.OptionMenu(booktkt_frame, value_inside, *options_list)
    question_menu.config(fg="red",bg="yellow",font=('Helvetica',16))
    question_menu.place(x=375,y=65)

# function of the button for deleting the ticket from the database
def deltkt():
    tkt_del=delete_Entry.get()
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute(f"delete from train where PNR_No = '{tkt_del}'")
    print(cur.fetchall())
    con.commit()

    delete_Entry.delete("0","end")
    messagebox.showwarning("Deleted","Your ticket has been successfully deleted!!")

# function for the button to store it in the databse in MYSQL 
def booktkt1():
    if value_inside.get()=="select train of your choice" or sou_inside.get()=="Select your source station" or des_inside.get()=="Select your destination" or namep_entry.get()=="" or gen_inside.get()=="Select your gender" or time_inside.get()=="Select your time" or age_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
        cur=con.cursor()
        tkt_1=str(r)
        name=value_inside.get()
        source=sou_inside.get()
        destin=des_inside.get()
        namep=namep_entry.get()
        gen=gen_inside.get()
        fare=fare1.get()
        time=time_inside.get()
        age=age_entry.get()
         
        cur.execute(f"INSERT INTO train values('{tkt_1}','{name}','{source}','{destin}','{namep}','{gen}','{fare}','{time}','{age}')")
        con.commit()

         

        cur.execute("select PNR_No from train")
        T=cur.fetchall()
        print(T)
        buffer=[]
        for i in T:
            buffer.append(i[0])
        print(buffer)
        state = True 
        while state:
            s=str(random.randint(19876542345600,29876542349000))
            if s not in buffer:
                buffer.append(s)
                state=False
            else:
                state=True
            print(s)
        
        tkt_PNR_Lab.config(text=str(s))
        namep_entry.delete("0","end")
        age_entry.delete("0","end")
        

        messagebox.showinfo("Done!!","Your ticket has been successfully saved to the database")
        
# tabulate function in python is used to tabulate the records and keep a track of the records
        

# The frame to book ticket and the labels and entries for the details  
def booktkt():
    global r,booktkt_frame,con
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute("create table if not exists train(PNR_No varchar(30) primary key,Train_name varchar(50),Source varchar(30),destination varchar(30),name_of_passenger varchar(30),gender char (1),fare varchar(30),time varchar(30),age varchar(30))")
    con.commit()

    global tkt_entry,Name_entry,Source_entry,destin_entry,namep_entry,gender_entry,tkt_PNR_Lab,age_entry
    
    mainframe.destroy()
    booktkt_frame=tk.Frame(root,bg="orange")
    booktkt_frame.place(x=450,y=90,width=700,height=700)
    

    #PNR_No
    r=random.randint(19876542345600,29876542349000)
    tkt_label=Label(booktkt_frame,text="PNR No:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    tkt_label.place(x=25,y=25)

    tkt_PNR_Lab=Label(booktkt_frame,text=r,bg="lightgray",font=(18))
    tkt_PNR_Lab.place(x=25,y=65)


    #Train_Name
    Name_label=Label(booktkt_frame,text="Train Name:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    Name_label.place(x=375,y=25)
    showop()
    
    # Name_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    # Name_entry.place(x=800,y=240)

    #Gender
    Source_label=Label(booktkt_frame,text="Source:",bg="lightgray",font=("Corbert COndensed Italic",18),fg="red")
    Source_label.place(x=25,y=125)
    souop()
    

    #Destination
    destin_label=Label(booktkt_frame,text="Destination:",bg="lightgray",font=("Corbert COndensed Italic",18),fg="red")
    destin_label.place(x=375,y=125)
    desop()

    #Name_of_passernger
    namep_label=Label(booktkt_frame,text="Name of the passenger:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    namep_label.place(x=25,y=225)
    
    namep_entry=Entry(booktkt_frame,font=("Corbert Condensed Italic",16),bg="lightgray",width=25)
    namep_entry.place(x=25,y=265)

    #Gender
    gender_label=Label(booktkt_frame,text="Gender:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    gender_label.place(x=25,y=310)
    genop()

    #signup button
    input_btn=Button(booktkt_frame,text="Book your ticket",bg="Yellow",fg="Red",font=("Corbert Condensed Italic",18),padx=15,pady=15,command=booktkt1)
    input_btn.place(x=25,y=475)

    #show fare btn
    show_fare=Button(booktkt_frame,text="Show fare for the train",padx=5,pady=15,font=("Helvetica",18),fg="Skyblue",bg="Indigo",command=fare)
    show_fare.place(x=400,y=475)
    
    #time button 
    time_lab=Label(booktkt_frame,text="Select your time of journey:",bg="lightgray",fg="red",font=("Helvetica",18))
    time_lab.place(x=375,y=310)
    timeop()

    #Age label
    age_lab=Label(booktkt_frame,text="Enter your age:",bg="lightgray",fg="red",font=("Helvetica",18))
    age_lab.place(x=375,y=225)

    age_entry=Entry(booktkt_frame,font=("Corbert Condensed Italic",16),bg="lightgray",width=25)
    age_entry.place(x=375,y=265)

# the main function for deleting ticket from the table and the frame for it 
def cantkt():
    global delete_Entry
    mainframe.destroy()
    deltkt_frame=tk.Frame(root,bg="pink")
    deltkt_frame.place(x=400,y=90,height=400,width=800)

    delete_btn=Label(root,text="Enter your PNR_No to delete yout ticket:",bg="Yellow",fg="Red",font=("Corbert Condessed Italic",18))
    delete_btn.place(x=550,y=200)

    delete_Entry=Entry(root,font=("Corbert Condensed Italic",18),bg="lightgray",)
    delete_Entry.place(x=550,y=250)

    del_btn=Button(root,text="Delete your ticket",bg="red",fg="skyblue",padx=25,pady=25,font=('Helvetica',16),command=deltkt)
    del_btn.place(x=800,y=300)

# The main buttons for the main functions 
book_tkt_btn=Button(mainframe,text="Book your ticket by clicking here !!",font=("Century Gothic",20),fg="Indigo",bg="light green",command=booktkt)
delete_tkt_btn=Button(mainframe,text="Cancel your ticket !!!",font=("Century Gothic",20),fg="Indigo",bg="light green",command=cantkt)
show_tkt_btn=Button(mainframe,text="View your ticket!!",font=("Century Gothic",20),fg="Indigo",bg="light green",command=showtkt)

# Placing of the buttons at their respective pixels
book_tkt_btn.place(x=45,y=25)
delete_tkt_btn.place(x=45,y=100)
show_tkt_btn.place(x=45,y=175)

 


# The Main function that is required to loop the program till the program ends
root.mainloop()