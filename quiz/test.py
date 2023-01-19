from tkinter import *
from tkinter import ttk
import random
import mysql.connector

#mysql.connector
con = mysql.connector.connect(user = 'root', host = 'localhost', password = '1234')
cur = con.cursor()
def score_db():
    global name, score,diff_lev
    db_name = username
    db_score = score
    db_diff_lev = diff_lev
    print(db_diff_lev,db_name,db_score)
    cur.execute("CREATE DATABASE IF NOT EXISTS quiz")
    cur.execute("USE quiz")
    cur.execute("CREATE TABLE IF NOT EXISTS score(Name VARCHAR(90),Score INT,Difficulty_level VARCHAR(90))")
    cur.execute(f"INSERT INTO SCORE VALUES('{db_name}',{db_score},' {db_diff_lev}')")
    cur.execute("SELECT * FROM SCORE ORDER BY SCORE DESC")
    m=cur.fetchall()
    con.commit()
    for i in m:
        print(i)
    con.close()

#Tkinter
root = Tk()
root.title("SOLO LEVELING")
root.configure(bg = '#1EC1C8')
root.geometry('1200x512')
frame = Frame(root)
frame.configure(bg = '#1EC1C8')
frame.pack()
style = ttk.Style(frame)
style.theme_use('clam')
#'clam', 'alt', 'default', 'classic'


score=0
q = []
qm = []
qe = []


def score_check(quiz_block, option):
    global score
    ans = quiz_block[0]
    if option == ans:
        score = score + 1
    else:
        pass


def diff_lv_check(a):
    global diff_lev
    if a == 1:
        diff_lev = "Elite"
        qe1()
    elif a == 2:
        diff_lev = "Knight"
        qm1()
    elif a == 0:
        diff_lev = "Commander"
        q1()


def level_pg():
    global username,name
    username = name.get()
    for widget in frame.winfo_children():
        widget.destroy()
    
    Label(frame, text = " SELECT DIFFICULTY ", fg = 'white', font = ("MATURASC", 30, "bold"), bg = '#1EC1C8').grid(row = 0, column = 1, pady = 100)
    elite = Button(frame, text = " ELITE ", font = ("MATURASC", 15, "bold"), width = 20, command = lambda : diff_lv_check(1))
    elite.grid(row = 1, column = 1, pady = 10)
    knight = Button(frame, text = " KNIGHT ", font = ("MATURASC", 15, "bold"), width = 20, command = lambda : diff_lv_check(2))
    knight.grid(row = 2, column = 1, pady = 10)
    commander = Button(frame, text = " COMMANDER ", font = ("MATURASC", 15, "bold"), width = 20, command = lambda : diff_lv_check(0))
    commander.grid(row = 3, column = 1, pady = 10)


def hard():
        m=open("quizhard.txt")
        l=[]
        buff = []
        e=0
        x=0
        v=98
        for i in range(0,v):
            w=m.readline()
            r=w.rstrip('\n')
            l.append(r)
        l2=[0,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105]
        for f in range(11):
                state=True
                while state:
                    p=random.randint(0,14)
                    if p not in buff:
                        e=l2[p]
                        x=e+7  
                        for i in l[e:x]:
                            q.append(i)
                        buff.append(p)
                        state =False
                    else:
                        state=True            
        for widget in frame.winfo_children():
              widget.destroy()

def op1(list_ops,op):
    score_check(list_ops,op)
    q2()
def op2(list_ops,op):
    score_check(list_ops,op)
    q3()        
def op3(list_ops,op):
    score_check(list_ops,op)
    q4()   
def op4(list_ops,op):
    score_check(list_ops,op)
    q5() 
def op5(list_ops,op):
    score_check(list_ops,op)
    q6() 
def op6(list_ops,op):
    score_check(list_ops,op)
    q7()
def op7(list_ops,op):
    score_check(list_ops,op)
    q8()  
def op8(list_ops,op):
    score_check(list_ops,op)
    q9()
def op9(list_ops,op):
    score_check(list_ops,op)
    q10()
def op10(list_ops,op):
    global final
    final = score_check(list_ops,op) 
    crt_ans(1)

def q1():
        hard()
        global q1
        q1=[]
        i1=0
        for i1 in range(0,7):
           q1.append(q[i1])
           i1=i1+1
        label = Label(frame, text = f'{q1[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q1[1]}", width = 20, height = 3, font = (30), command = lambda : op1(q1,q1[1]))
        button2 = Button(frame, text = f"{q1[2]}", width = 20, height = 3, font = (30), command = lambda : op1(q1,q1[2]))
        button3 = Button(frame, text = f"{q1[3]}", width = 20, height = 3, font = (30), command = lambda : op1(q1,q1[3]))
        button4 = Button(frame, text = f"{q1[4]}", width = 20, height = 3, font = (30), command = lambda : op1(q1,q1[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q2():
        hard()
        global q2
        q2=[]
        i2=0
        for i2 in range(7,14):
             q2.append(q[i2])
             i2=i2+1
        label = Label(frame, text = f'{q2[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q2[1]}", width = 20, height = 3, font = (30), command = lambda : op2(q2,q2[1]))
        button2 = Button(frame, text = f"{q2[2]}", width = 20, height = 3, font = (30), command = lambda : op2(q2,q2[2]))
        button3 = Button(frame, text = f"{q2[3]}", width = 20, height = 3, font = (30), command = lambda : op2(q2,q2[3]))
        button4 = Button(frame, text = f"{q2[4]}", width = 20, height = 3, font = (30), command = lambda : op2(q2,q2[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q3():
        hard()
        global q3
        q3=[]
        i3=0
        for i3 in range(14,21):
             q3.append(q[i3])
             i3=i3+1
        label = Label(frame, text = f'{q3[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q3[1]}", width = 20, height = 3, font = (30), command = lambda : op3(q3,q3[1]))
        button2 = Button(frame, text = f"{q3[2]}", width = 20, height = 3, font = (30), command = lambda : op3(q3,q3[2]))
        button3 = Button(frame, text = f"{q3[3]}", width = 20, height = 3, font = (30), command = lambda : op3(q3,q3[3]))
        button4 = Button(frame, text = f"{q3[4]}", width = 20, height = 3, font = (30), command = lambda : op3(q3,q3[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q4():
         hard()
         global q4
         q4=[]
         i4=0
         for i4 in range(21,28):
              q4.append(q[i4])
              i4=i4+1
         label = Label(frame, text = f'{q4[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
         button1 = Button(frame, text = f"{q4[1]}", width = 20, height = 3, font = (30), command = lambda : op4(q4,q4[1]))
         button2 = Button(frame, text = f"{q4[2]}", width = 20, height = 3, font = (30), command = lambda : op4(q4,q4[2]))
         button3 = Button(frame, text = f"{q4[3]}", width = 20, height = 3, font = (30), command = lambda : op4(q4,q4[3]))
         button4 = Button(frame, text = f"{q4[4]}", width = 20, height = 3, font = (30), command = lambda : op4(q4,q4[4]))
         button1.grid(row = 2, column = 1, pady = 20)
         button2.grid(row = 2, column = 3, pady = 20)
         button3.grid(row = 3, column = 1, pady = 20)
         button4.grid(row = 3, column = 3, pady = 20)

def q5():
        hard()
        global q5
        q5=[]
        i5=0
        for i5 in range(28,35):
              q5.append(q[i5])
              i5=i5+1
        label = Label(frame, text = f'{q5[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q5[1]}", width = 20, height = 3, font = (30), command = lambda : op5(q5,q5[1]))
        button2 = Button(frame, text = f"{q5[2]}", width = 20, height = 3, font = (30), command = lambda : op5(q5,q5[2]))
        button3 = Button(frame, text = f"{q5[3]}", width = 20, height = 3, font = (30), command = lambda : op5(q5,q5[3]))
        button4 = Button(frame, text = f"{q5[4]}", width = 20, height = 3, font = (30), command = lambda : op5(q5,q5[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q6():
        hard()
        global q6
        q6=[]
        i6=0
        for i6 in range(35,42):
             q6.append(q[i6])
             i6=i6+1
        label = Label(frame, text = f'{q6[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q6[1]}", width = 20, height = 3, font = (30), command = lambda : op6(q6,q6[1]))
        button2 = Button(frame, text = f"{q6[2]}", width = 20, height = 3, font = (30), command = lambda : op6(q6,q6[2]))
        button3 = Button(frame, text = f"{q6[3]}", width = 20, height = 3, font = (30), command = lambda : op6(q6,q6[3]))
        button4 = Button(frame, text = f"{q6[4]}", width = 20, height = 3, font = (30), command = lambda : op6(q6,q6[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q7():
        hard()
        global q7
        q7=[]
        i7=0
        for i7 in range(42,49):
           q7.append(q[i7])
           i7=i7+1
        label = Label(frame, text = f'{q7[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q7[1]}", width = 20, height = 3, font = (30), command = lambda : op7(q7,q7[1]))
        button2 = Button(frame, text = f"{q7[2]}", width = 20, height = 3, font = (30), command = lambda : op7(q7,q7[2]))
        button3 = Button(frame, text = f"{q7[3]}", width = 20, height = 3, font = (30), command = lambda : op7(q7,q7[3]))
        button4 = Button(frame, text = f"{q7[4]}", width = 20, height = 3, font = (30), command = lambda : op7(q7,q7[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q8():
        hard()
        global q8
        q8=[]
        i8=0
        for i8 in range(49,56):
           q8.append(q[i8])
           i8=i8+1
        label = Label(frame, text = f'{q8[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700 ).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q8[1]}", width = 20, height = 3, font = (30), command = lambda : op8(q8,q8[1]))
        button2 = Button(frame, text = f"{q8[2]}", width = 20, height = 3, font = (30), command = lambda : op8(q8,q8[2]))
        button3 = Button(frame, text = f"{q8[3]}", width = 20, height = 3, font = (30), command = lambda : op8(q8,q8[3]))
        button4 = Button(frame, text = f"{q8[4]}", width = 20, height = 3, font = (30), command = lambda : op8(q8,q8[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q9():
        hard()
        global q9
        q9 = []
        i9=0
        for i9 in range(56,63):
             q9.append(q[i9])
             i9=i9+1
        label = Label(frame, text = f'{q9[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q9[1]}", width = 20, height = 3, font = (30), command = lambda : op9(q9,q9[1]))
        button2 = Button(frame, text = f"{q9[2]}", width = 20, height = 3, font = (30), command = lambda : op9(q9,q9[2]))
        button3 = Button(frame, text = f"{q9[3]}", width = 20, height = 3, font = (30), command = lambda : op9(q9,q9[3]))
        button4 = Button(frame, text = f"{q9[4]}", width = 20, height = 3, font = (30), command = lambda : op9(q9,q9[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)

def q10():
        hard()
        global q10
        q10=[]
        i10=0
        for i10 in range(63,70):
           q10.append(q[i10])
           i10=i10+1
        label = Label(frame, text = f"{q10[5]}", font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 2, pady = 50)
        button1 = Button(frame, text = f"{q10[1]}", width = 20, height = 3, font = (30), command = lambda : op10(q10,q10[1]))
        button2 = Button(frame, text = f"{q10[2]}", width = 20, height = 3, font = (30), command = lambda : op10(q10,q10[2]))
        button3 = Button(frame, text = f"{q10[3]}", width = 20, height = 3, font = (30), command = lambda : op10(q10,q10[3]))
        button4 = Button(frame, text = f"{q10[4]}", width = 20, height = 3, font = (30), command = lambda : op10(q10,q10[4]))
        button1.grid(row = 2, column = 1, pady = 20)
        button2.grid(row = 2, column = 3, pady = 20)
        button3.grid(row = 3, column = 1, pady = 20)
        button4.grid(row = 3, column = 3, pady = 20)


def medium():
    mm=open("quizmed.txt")
    lm=[]
    buffm = []
    em=0
    xm=0
    vm=105
    for i in range(0,vm):
        wm=mm.readline()
        rm=wm.rstrip('\n')
        lm.append(rm)
    lm2=[0,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126]
    for f in range(11):
        state=True
        while state:
            pm=random.randint(0,15)
            if pm not in buffm:
                em=lm2[pm]
                xm=em+7  
                for i in lm[em:xm]:
                    qm.append(i)
                buffm.append(pm)
                state =False
            else:
                    state=True
    for widget in frame.winfo_children():
        widget.destroy()

def opm1(list_ops,op):
    score_check(list_ops,op)
    qm2()
def opm2(list_ops,op):
    score_check(list_ops,op)
    qm3()        
def opm3(list_ops,op):
    score_check(list_ops,op)
    qm4()   
def opm4(list_ops,op):
    score_check(list_ops,op)
    qm5() 
def opm5(list_ops,op):
    score_check(list_ops,op)
    qm6() 
def opm6(list_ops,op):
    score_check(list_ops,op)
    qm7()
def opm7(list_ops,op):
    score_check(list_ops,op)
    qm8()  
def opm8(list_ops,op):
    score_check(list_ops,op)
    qm9()
def opm9(list_ops,op):
    score_check(list_ops,op)
    qm10()
def opm10(list_ops,op):
    global final
    final = score_check(list_ops,op)
    crt_ans(2)

def qm1():
    medium()
    global qm1
    qm1=[]
    im1=0
    for im1 in range(0,7):
         qm1.append(qm[im1])
         im1=im1+1
    label = Label(frame, text = f'{qm1[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm1[1]}", width = 20, height = 3, font = (30), command = lambda : opm1(qm1,qm1[1]))
    button2 = Button(frame, text = f"{qm1[2]}", width = 20, height = 3, font = (30), command = lambda : opm1(qm1,qm1[2]))
    button3 = Button(frame, text = f"{qm1[3]}", width = 20, height = 3, font = (30), command = lambda : opm1(qm1,qm1[3]))
    button4 = Button(frame, text = f"{qm1[4]}", width = 20, height = 3, font = (30), command = lambda : opm1(qm1,qm1[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm2():
    medium()
    global qm2
    qm2=[]
    im2=0
    for im2 in range(7,14):
         qm2.append(qm[im2])
         im2=im2+1
    label = Label(frame, text = f'{qm2[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm2[1]}", width = 20, height = 3, font = (30), command = lambda : opm2(qm2,qm2[1]))
    button2 = Button(frame, text = f"{qm2[2]}", width = 20, height = 3, font = (30), command = lambda : opm2(qm2,qm2[2]))
    button3 = Button(frame, text = f"{qm2[3]}", width = 20, height = 3, font = (30), command = lambda : opm2(qm2,qm2[3]))
    button4 = Button(frame, text = f"{qm2[4]}", width = 20, height = 3, font = (30), command = lambda : opm2(qm2,qm2[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm3():
    medium()
    global qm3
    qm3=[]
    im3=0
    for im3 in range(14,21):
         qm3.append(qm[im3])
         im3=im3+1
    label = Label(frame, text = f'{qm3[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm3[1]}", width = 20, height = 3, font = (30), command = lambda : opm3(qm3,qm3[1]))
    button2 = Button(frame, text = f"{qm3[2]}", width = 20, height = 3, font = (30), command = lambda : opm3(qm3,qm3[2]))
    button3 = Button(frame, text = f"{qm3[3]}", width = 20, height = 3, font = (30), command = lambda : opm3(qm3,qm3[3]))
    button4 = Button(frame, text = f"{qm3[4]}", width = 20, height = 3, font = (30), command = lambda : opm3(qm3,qm3[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm4():
    medium()
    global qm4
    qm4=[]
    im4=0
    for im4 in range(21,28):
         qm4.append(qm[im4])
         im4=im4+1
    label = Label(frame, text = f'{qm4[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm4[1]}", width = 20, height = 3, font = (30), command = lambda : opm4(qm4,qm4[1]))
    button2 = Button(frame, text = f"{qm4[2]}", width = 20, height = 3, font = (30), command = lambda : opm4(qm4,qm4[2]))
    button3 = Button(frame, text = f"{qm4[3]}", width = 20, height = 3, font = (30), command = lambda : opm4(qm4,qm4[3]))
    button4 = Button(frame, text = f"{qm4[4]}", width = 20, height = 3, font = (30), command = lambda : opm4(qm4,qm4[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm5():
    medium()
    global qm5
    qm5=[]
    im5=0
    for im5 in range(28,35):
        qm5.append(qm[im5])
        im5=im5+1
    label = Label(frame, text = f'{qm5[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm5[1]}", width = 20, height = 3, font = (30), command = lambda : opm5(qm5,qm5[1]))
    button2 = Button(frame, text = f"{qm5[2]}", width = 20, height = 3, font = (30), command = lambda : opm5(qm5,qm5[2]))
    button3 = Button(frame, text = f"{qm5[3]}", width = 20, height = 3, font = (30), command = lambda : opm5(qm5,qm5[3]))
    button4 = Button(frame, text = f"{qm5[4]}", width = 20, height = 3, font = (30), command = lambda : opm5(qm5,qm5[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm6():
    medium()
    global qm6
    qm6=[]
    im6=0
    for im6 in range(35,42):
        qm6.append(qm[im6])
        im6=im6+1
    label = Label(frame, text = f'{qm6[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm6[1]}", width = 20, height = 3, font = (30), command = lambda : opm6(qm6,qm6[1]))
    button2 = Button(frame, text = f"{qm6[2]}", width = 20, height = 3, font = (30), command = lambda : opm6(qm6,qm6[2]))
    button3 = Button(frame, text = f"{qm6[3]}", width = 20, height = 3, font = (30), command = lambda : opm6(qm6,qm6[3]))
    button4 = Button(frame, text = f"{qm6[4]}", width = 20, height = 3, font = (30), command = lambda : opm6(qm6,qm6[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm7():
    medium()
    global qm7
    qm7=[]
    im7=0
    for im7 in range(42,49):
        qm7.append(qm[im7])
        im7=im7+1
    label = Label(frame, text = f'{qm7[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm7[1]}", width = 20, height = 3, font = (30), command = lambda : opm7(qm7,qm7[1]))
    button2 = Button(frame, text = f"{qm7[2]}", width = 20, height = 3, font = (30), command = lambda : opm7(qm7,qm7[2]))
    button3 = Button(frame, text = f"{qm7[3]}", width = 20, height = 3, font = (30), command = lambda : opm7(qm7,qm7[3]))
    button4 = Button(frame, text = f"{qm7[4]}", width = 20, height = 3, font = (30), command = lambda : opm7(qm7,qm7[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm8():
    medium()
    global qm8
    qm8=[]
    im8=0
    for im8 in range(49,56):
        qm8.append(qm[im8])
        im8=im8+1
    label = Label(frame, text = f'{qm8[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm8[1]}", width = 20, height = 3, font = (30), command = lambda : opm8(qm8,qm8[1]))
    button2 = Button(frame, text = f"{qm8[2]}", width = 20, height = 3, font = (30), command = lambda : opm8(qm8,qm8[2]))
    button3 = Button(frame, text = f"{qm8[3]}", width = 20, height = 3, font = (30), command = lambda : opm8(qm8,qm8[3]))
    button4 = Button(frame, text = f"{qm8[4]}", width = 20, height = 3, font = (30), command = lambda : opm8(qm8,qm8[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qm9():
    medium()
    global qm9
    qm9=[]
    im9=0
    for im9 in range(56,63):
        qm9.append(qm[im9])
        im9=im9+1
    label = Label(frame, text = f'{qm9[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm9[1]}", width = 20, height = 3, font = (30), command = lambda : opm9(qm9,qm9[1]))
    button2 = Button(frame, text = f"{qm9[2]}", width = 20, height = 3, font = (30), command = lambda : opm9(qm9,qm9[2]))
    button3 = Button(frame, text = f"{qm9[3]}", width = 20, height = 3, font = (30), command = lambda : opm9(qm9,qm9[3]))
    button4 = Button(frame, text = f"{qm9[4]}", width = 20, height = 3, font = (30), command = lambda : opm9(qm9,qm9[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)
 
def qm10():
    medium()
    global qm10
    qm10=[]
    im10=0
    for im10 in range(63,70):
        qm10.append(qm[im10])
        im10=im10+1
    label = Label(frame, text = f'{qm10[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qm10[1]}", width = 20, height = 3, font = (30), command = lambda: opm10(qm10,qm10[1]))
    button2 = Button(frame, text = f"{qm10[2]}", width = 20, height = 3, font = (30), command = lambda: opm10(qm10,qm10[2]))
    button3 = Button(frame, text = f"{qm10[3]}", width = 20, height = 3, font = (30), command = lambda: opm10(qm10,qm10[3]))
    button4 = Button(frame, text = f"{qm10[4]}", width = 20, height = 3, font = (30), command = lambda: opm10(qm10,qm10[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)


def easy():
         me=open("quizeasy.txt")
         le=[]
         buffe = []
         ee=0
         xe=0
         ve=98
         for i in range(0,ve):
              we=me.readline()
              re=we.rstrip('\n')
              le.append(re)
         le2=[0,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105]
         for f in range(11):
             state=True
             while state:
                  pe=random.randint(0,14)
                  if pe not in buffe:
                        ee=le2[pe]
                        xe=ee+7  
                        for i in le[ee:xe]:
                             qe.append(i)
                        buffe.append(pe)
                        state =False
                  else:
                       state=True
         for widget in frame.winfo_children():
              widget.destroy()

def ope1(list_ops,op):
    score_check(list_ops,op)
    qe2()
def ope2(list_ops,op):
    score_check(list_ops,op)
    qe3()        
def ope3(list_ops,op):
    score_check(list_ops,op)
    qe4()   
def ope4(list_ops,op):
    score_check(list_ops,op)
    qe5() 
def ope5(list_ops,op):
    score_check(list_ops,op)
    qe6() 
def ope6(list_ops,op):
    score_check(list_ops,op)
    qe7()
def ope7(list_ops,op):
    score_check(list_ops,op)
    qe8()  
def ope8(list_ops,op):
    score_check(list_ops,op)
    qe9()
def ope9(list_ops,op):
    score_check(list_ops,op)
    qe10()
def ope10(list_ops,op):
    global final
    final = score_check(list_ops,op)
    crt_ans(3)

def qe1():
    easy()
    global qe1
    qe1=[]
    ie1=0
    for ie1 in range(0,7):
         qe1.append(qe[ie1])
         ie1=ie1+1
    label = Label(frame, text = f'{qe1[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe1[1]}", width = 20, height = 3, font = (30), command = lambda : ope1(qe1,qe1[1]))
    button2 = Button(frame, text = f"{qe1[2]}", width = 20, height = 3, font = (30), command = lambda : ope1(qe1,qe1[2]))
    button3 = Button(frame, text = f"{qe1[3]}", width = 20, height = 3, font = (30), command = lambda : ope1(qe1,qe1[3]))
    button4 = Button(frame, text = f"{qe1[4]}", width = 20, height = 3, font = (30), command = lambda : ope1(qe1,qe1[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe2():
    easy()
    global qe2
    qe2=[]
    ie2=0
    for ie2 in range(7,14):
         qe2.append(qe[ie2])
         ie2=ie2+1
    label = Label(frame, text = f'{qe2[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe2[1]}", width = 20, height = 3, font = (30), command = lambda : ope2(qe2,qe2[1]))
    button2 = Button(frame, text = f"{qe2[2]}", width = 20, height = 3, font = (30), command = lambda : ope2(qe2,qe2[2]))
    button3 = Button(frame, text = f"{qe2[3]}", width = 20, height = 3, font = (30), command = lambda : ope2(qe2,qe2[3]))
    button4 = Button(frame, text = f"{qe2[4]}", width = 20, height = 3, font = (30), command = lambda : ope2(qe2,qe2[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe3():
    easy()
    global qe3
    qe3=[]
    ie3=0
    for ie3 in range(14,21):
        qe3.append(qe[ie3])
        ie3=ie3+1
    label = Label(frame, text = f'{qe3[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe3[1]}", width = 20, height = 3, font = (30), command = lambda : ope3(qe3,qe3[1]))
    button2 = Button(frame, text = f"{qe3[2]}", width = 20, height = 3, font = (30), command = lambda : ope3(qe3,qe3[2]))
    button3 = Button(frame, text = f"{qe3[3]}", width = 20, height = 3, font = (30), command = lambda : ope3(qe3,qe3[3]))
    button4 = Button(frame, text = f"{qe3[4]}", width = 20, height = 3, font = (30), command = lambda : ope3(qe3,qe3[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe4():
    easy()
    global qe4
    qe4=[]
    ie4=0
    for ie4 in range(21,28):
        qe4.append(qe[ie4])
        ie4=ie4+1
    label = Label(frame, text = f'{qe4[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe4[1]}", width = 20, height = 3, font = (30), command = lambda : ope4(qe4,qe4[1]))
    button2 = Button(frame, text = f"{qe4[2]}", width = 20, height = 3, font = (30), command = lambda : ope4(qe4,qe4[2]))
    button3 = Button(frame, text = f"{qe4[3]}", width = 20, height = 3, font = (30), command = lambda : ope4(qe4,qe4[3]))
    button4 = Button(frame, text = f"{qe4[4]}", width = 20, height = 3, font = (30), command = lambda : ope4(qe4,qe4[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe5():
    easy()
    global qe5
    qe5=[]
    ie5=0
    for ie5 in range(28,35):
        qe5.append(qe[ie5])
        ie5=ie5+1
    label = Label(frame, text = f'{qe5[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe5[1]}", width = 20, height = 3, font = (30), command = lambda : ope5(qe5,qe5[1]))
    button2 = Button(frame, text = f"{qe5[2]}", width = 20, height = 3, font = (30), command = lambda : ope5(qe5,qe5[2]))
    button3 = Button(frame, text = f"{qe5[3]}", width = 20, height = 3, font = (30), command = lambda : ope5(qe5,qe5[3]))
    button4 = Button(frame, text = f"{qe5[4]}", width = 20, height = 3, font = (30), command = lambda : ope5(qe5,qe5[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe6():
    easy()
    global qe6
    qe6=[]
    ie6=0
    for ie6 in range(35,42):
        ie6=ie6+1
        qe6.append(qe[ie6])
    label = Label(frame, text = f'{qe6[4]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe6[0]}", width = 20, height = 3, font = (30), command = lambda : ope6(qe6,qe6[0]))
    button2 = Button(frame, text = f"{qe6[1]}", width = 20, height = 3, font = (30), command = lambda : ope6(qe6,qe6[1]))
    button3 = Button(frame, text = f"{qe6[2]}", width = 20, height = 3, font = (30), command = lambda : ope6(qe6,qe6[2]))
    button4 = Button(frame, text = f"{qe6[3]}", width = 20, height = 3, font = (30), command = lambda : ope6(qe6,qe6[3]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)  

def qe7():
    easy()
    global qe7
    qe7=[]
    ie7=0
    for ie7 in range(42,49):
        qe7.append(qe[ie7])
        ie7=ie7+1
    label = Label(frame, text = f'{qe7[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe7[1]}", width = 20, height = 3, font = (30), command = lambda : ope7(qe7,qe7[1]))
    button2 = Button(frame, text = f"{qe7[2]}", width = 20, height = 3, font = (30), command = lambda : ope7(qe7,qe7[2]))
    button3 = Button(frame, text = f"{qe7[3]}", width = 20, height = 3, font = (30), command = lambda : ope7(qe7,qe7[3]))
    button4 = Button(frame, text = f"{qe7[4]}", width = 20, height = 3, font = (30), command = lambda : ope7(qe7,qe7[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe8():
    easy()
    global qe8
    qe8=[]
    ie8=0
    for ie8 in range(49,56):
        qe8.append(qe[ie8])
        ie8=ie8+1
    label = Label(frame, text = f'{qe8[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe8[1]}", width = 20, height = 3, font = (30), command = lambda : ope8(qe8,qe8[1]))
    button2 = Button(frame, text = f"{qe8[2]}", width = 20, height = 3, font = (30), command = lambda : ope8(qe8,qe8[2]))
    button3 = Button(frame, text = f"{qe8[3]}", width = 20, height = 3, font = (30), command = lambda : ope8(qe8,qe8[3]))
    button4 = Button(frame, text = f"{qe8[4]}", width = 20, height = 3, font = (30), command = lambda : ope8(qe8,qe8[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe9():
    easy()
    global qe9
    qe9=[]
    ie9=0
    for ie9 in range(56,63):
        qe9.append(qe[ie9])
        ie9=ie9+1
    label = Label(frame, text = f'{qe9[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe9[1]}", width = 20, height = 3, font = (30), command = lambda : ope9(qe9,qe9[1]))
    button2 = Button(frame, text = f"{qe9[2]}", width = 20, height = 3, font = (30), command = lambda : ope9(qe9,qe9[2]))
    button3 = Button(frame, text = f"{qe9[3]}", width = 20, height = 3, font = (30), command = lambda : ope9(qe9,qe9[3]))
    button4 = Button(frame, text = f"{qe9[4]}", width = 20, height = 3, font = (30), command = lambda : ope9(qe9,qe9[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)

def qe10():
    easy()
    global qe10
    qe10=[]
    ie10=0
    for ie10 in range(63,70):
        qe10.append(qe[ie10])
        ie10=ie10+1
    label = Label(frame, text = f'{qe10[5]}', font = ("MATURASC", 20), bg = '#1EC1C8', fg = 'white', wraplength = 700).grid(row = 1, column = 1, pady = 50)
    button1 = Button(frame, text = f"{qe10[1]}", width = 20, height = 3, font = (30), command = lambda : ope10(qe10,qe10[1]))
    button2 = Button(frame, text = f"{qe10[2]}", width = 20, height = 3, font = (30), command = lambda : ope10(qe10,qe10[2]))
    button3 = Button(frame, text = f"{qe10[3]}", width = 20, height = 3, font = (30), command = lambda : ope10(qe10,qe10[3]))
    button4 = Button(frame, text = f"{qe10[4]}", width = 20, height = 3, font = (30), command = lambda : ope10(qe10,qe10[4]))
    button1.grid(row = 2, column = 1, pady = 20)
    button2.grid(row = 2, column = 3, pady = 20)
    button3.grid(row = 3, column = 1, pady = 20)
    button4.grid(row = 3, column = 3, pady = 20)


def cont():
    for widget in frame.winfo_children():
        widget.destroy()
    
    Label(frame, text = ' ENTER YOUR NAME ', font = (50), bg = '#1EC1C8', fg = 'White').grid(row = 0, pady = 100 )
    global name
    name = Entry(frame, font = (50), width = 20)
    name.grid(row = 0, column = 1)
    enter_btn = Button(frame, text = " ENTER THE QUIZ ", font = ("MATURASC", 10, "bold"), foreground= 'Blue', command = lambda : level_pg())
    enter_btn.grid(row = 2, column = 1)


def exit():
    global exit_window
    exit_window = Tk()
    exit_window.configure(bg = '#1EC1C8')
    exit_window.title("EXIT")
    
    exit_label = Label(exit_window, text = " DO YOU WANT TO EXIT? ", bg = '#1EC1C8')
    exit_label.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 2)

    yes_button = Button(exit_window, text = " YES ", foreground = "red", borderwidth = 2, command = lambda : destroy_app(1))
    yes_button.grid(row = 1, column = 0, padx = 2, pady = 2)

    no_button = Button(exit_window, text = " NO ", foreground = "green", borderwidth = 2, command = lambda : destroy_app(0))
    no_button.grid(row = 1, column = 1, padx = 2, pady = 2)


def destroy_app(a):
    if a == 1:
        root.destroy()
        exit_window.destroy()
        quit()
    else:
        exit_window.destroy()


def crt_ans(e):
    score_db()
    for widget in frame.winfo_children():
        widget.destroy()
    tree = ttk.Treeview(frame, column = ("q", "a", "b", "c", "d", "crt"), show = 'headings', height = 10)
    tree.column("#1", anchor = CENTER)
    tree.heading("# 1", text="Question")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Option A")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Option B")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Option C")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Option D")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Correct answer")
    
    if e == 1:
        tree.insert('', 'end', text = "1", values = (f'{q1[5]}', f'{q1[1]}', f'{q1[2]}', f'{q1[3]}', f'{q1[4]}', f'{q1[0]}'))
        tree.insert('', 'end', text = "2", values = (f'{q2[5]}', f'{q2[1]}', f'{q2[2]}', f'{q2[3]}', f'{q2[4]}', f'{q2[0]}'))
        tree.insert('', 'end', text = "3", values = (f'{q3[5]}', f'{q3[1]}', f'{q3[2]}', f'{q3[3]}', f'{q3[4]}', f'{q3[0]}'))
        tree.insert('', 'end', text = "4", values = (f'{q4[5]}', f'{q4[1]}', f'{q4[2]}', f'{q4[3]}', f'{q4[4]}', f'{q4[0]}'))
        tree.insert('', 'end', text = "5", values = (f'{q5[5]}', f'{q5[1]}', f'{q5[2]}', f'{q5[3]}', f'{q5[4]}', f'{q5[0]}'))
        tree.insert('', 'end', text = "6", values = (f'{q6[5]}', f'{q6[1]}', f'{q6[2]}', f'{q6[3]}', f'{q6[4]}', f'{q6[0]}'))
        tree.insert('', 'end', text = "7", values = (f'{q7[5]}', f'{q7[1]}', f'{q7[2]}', f'{q7[3]}', f'{q7[4]}', f'{q7[0]}'))
        tree.insert('', 'end', text = "8", values = (f'{q8[5]}', f'{q8[1]}', f'{q8[2]}', f'{q8[3]}', f'{q8[4]}', f'{q8[0]}'))
        tree.insert('', 'end', text = "9", values = (f'{q9[5]}', f'{q9[1]}', f'{q9[2]}', f'{q9[3]}', f'{q9[4]}', f'{q9[0]}'))
        tree.insert('', 'end', text ="10", values=  (f'{q10[5]}', f'{q10[1]}', f'{q10[2]}', f'{q10[3]}', f'{q10[4]}', f'{q10[0]}'))
    
    if e == 2:
        tree.insert('', 'end', text = "1", values = (f'{qm1[5]}', f'{qm1[1]}', f'{qm1[2]}', f'{qm1[3]}', f'{qm1[4]}', f'{qm1[0]}'))
        tree.insert('', 'end', text = "2", values = (f'{qm2[5]}', f'{qm2[1]}', f'{qm2[2]}', f'{qm2[3]}', f'{qm2[4]}', f'{qm2[0]}'))
        tree.insert('', 'end', text = "3", values = (f'{qm3[5]}', f'{qm3[1]}', f'{qm3[2]}', f'{qm3[3]}', f'{qm3[4]}', f'{qm3[0]}'))
        tree.insert('', 'end', text = "4", values = (f'{qm4[5]}', f'{qm4[1]}', f'{qm4[2]}', f'{qm4[3]}', f'{qm4[4]}', f'{qm4[0]}'))
        tree.insert('', 'end', text = "5", values = (f'{qm5[5]}', f'{qm5[1]}', f'{qm5[2]}', f'{qm5[3]}', f'{qm5[4]}', f'{qm5[0]}'))
        tree.insert('', 'end', text = "6", values = (f'{qm6[5]}', f'{qm6[1]}', f'{qm6[2]}', f'{qm6[3]}', f'{qm6[4]}', f'{qm6[0]}'))
        tree.insert('', 'end', text = "7", values = (f'{qm7[5]}', f'{qm7[1]}', f'{qm7[2]}', f'{qm7[3]}', f'{qm7[4]}', f'{qm7[0]}'))
        tree.insert('', 'end', text = "8", values = (f'{qm8[5]}', f'{qm8[1]}', f'{qm8[2]}', f'{qm8[3]}', f'{qm8[4]}', f'{qm8[0]}'))
        tree.insert('', 'end', text = "9", values = (f'{qm9[5]}', f'{qm9[1]}', f'{qm9[2]}', f'{qm9[3]}', f'{qm9[4]}', f'{qm9[0]}'))
        tree.insert('', 'end', text ="10", values=  (f'{qm10[5]}', f'{qm10[1]}', f'{qm10[2]}', f'{qm10[3]}', f'{qm10[4]}', f'{qm10[0]}'))
    
    if e == 3:
        tree.insert('', 'end', text = "1", values = (f'{qe1[5]}', f'{qe1[1]}', f'{qe1[2]}', f'{qe1[3]}', f'{qe1[4]}', f'{qe1[0]}'))
        tree.insert('', 'end', text = "2", values = (f'{qe2[5]}', f'{qe2[1]}', f'{qe2[2]}', f'{qe2[3]}', f'{qe2[4]}', f'{qe2[0]}'))
        tree.insert('', 'end', text = "3", values = (f'{qe3[5]}', f'{qe3[1]}', f'{qe3[2]}', f'{qe3[3]}', f'{qe3[4]}', f'{qe3[0]}'))
        tree.insert('', 'end', text = "4", values = (f'{qe4[5]}', f'{qe4[1]}', f'{qe4[2]}', f'{qe4[3]}', f'{qe4[4]}', f'{qe4[0]}'))
        tree.insert('', 'end', text = "5", values = (f'{qe5[5]}', f'{qe5[1]}', f'{qe5[2]}', f'{qe5[3]}', f'{qe5[4]}', f'{qe5[0]}'))
        tree.insert('', 'end', text = "6", values = (f'{qe6[4]}', f'{qe6[0]}', f'{qe6[1]}', f'{qe6[2]}', f'{qe6[3]}', f'{qe6[0]}'))
        tree.insert('', 'end', text = "7", values = (f'{qe7[5]}', f'{qe7[1]}', f'{qe7[2]}', f'{qe7[3]}', f'{qe7[4]}', f'{qe7[0]}'))
        tree.insert('', 'end', text = "8", values = (f'{qe8[5]}', f'{qe8[1]}', f'{qe8[2]}', f'{qe8[3]}', f'{qe8[4]}', f'{qe8[0]}'))
        tree.insert('', 'end', text = "9", values = (f'{qe9[5]}', f'{qe9[1]}', f'{qe9[2]}', f'{qe9[3]}', f'{qe9[4]}', f'{qe9[0]}'))
        tree.insert('', 'end', text ="10", values=  (f'{qe10[5]}', f'{qe10[1]}', f'{qe10[2]}', f'{qe10[3]}', f'{qe10[4]}', f'{qe10[0]}'))

    tree.grid()
    label = Label(frame, text = "CONTINUE?", bg = '#1EC1C8', font = ('MATURASC',30, 'bold')).grid()
    button1 = Button(frame, text = " YES ",font = (20), height = 2, width = 20, command = lambda : cont())
    button1.grid()
    button2 = Button(frame, text = " NO ",font = (20), height = 2, width = 20, command = lambda : exit())
    button2.grid()


gname = Label(frame, text = " QUIZ CORNER ", font = ("8514oem", 100, "bold"), bg = '#1EC1C8', fg = 'white', height = 2).pack()
cont_btn = Button(frame, text = " PLAY ", font = ("MATURASC", 10, "bold"), foreground="green", width = 25, height = 3, command = lambda : cont())
cont_btn.pack(side = LEFT)
exit_btn = Button(frame, text = " QUIT GAME ", font = ("MATURASC", 10, "bold"), foreground="red", width = 25, height = 3, command= lambda : exit())
exit_btn.pack(side= RIGHT)


root.mainloop()