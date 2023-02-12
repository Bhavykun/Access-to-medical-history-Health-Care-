from tkinter import *
import mysql.connector
 
def Ok():
    global myresult
    pid= e1.get()
    sno= e2.get()
    name = e3.get()
    age=e4.get()
    phone=e5.get()
    gender=e6.get()
    dob=e7.get()
    address=e8.get()
    height=e9.get()
    weight=e10.get()
    disease=e11.get()
    admit_date=e12.get()
    discharge_date=e13.get()
    guardian_name=e14.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="pavithra",database="oo")
    mycursor=mysqldb.cursor()
 
    try:
        
        mycursor.execute("SELECT * FROM hospital where pid = '" + name + "'")
        myresult = mycursor.fetchall()
        for x in myresult:
            print('x')
        e2.delete(0, END)
        e2.insert(END, x[1])
        e3.delete(0, END)
        e3.insert(END, x[2])
        e4.delete(0,END)
        e4.insert(END,x[3])
        e5.delete(0,END)
        e5.insert(END,x[4])
        e6.delete(0,END)
        e6.insert(END,x[5])
        e7.delete(0,END)
        e7.insert(END,x[6])
        e8.delete(0,END)
        e8.insert(END,x[7])
        e9.delete(0,END)
        e9.insert(END,x[8])
        e10.delete(0,END)
        e10.insert(END,x[9])
        e11.delete(0,END)
        e11.insert(END,x[10])
        e12.delete(0,END)
        e12.insert(END,x[11])
        e13.delete(0,END)
        e13.insert(END,x[12])
        e14.delete(0,END)
        e14.insert(END,x[13])
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
root = Tk()
root.title("HOSPITAL RECORDS")
root.geometry("1400x1400")

Label(root, text="Patient ID").place(x=10, y=10)
Button(root, text="Search", command=Ok ,height = 1, width = 13).place(x=580, y=40)

Label(root, text="Sno").place(x=10, y=80)
Label(root, text="Name").place(x=10, y=120)
Label(root, text="Age").place(x=10, y=160)
Label(root, text="phone").place(x=10, y=200)
Label(root, text="gen]der").place(x=10, y=240)
Label(root, text="DOB").place(x=10, y=280)
Label(root, text="Address").place(x=10, y=320)
Label(root, text="Height").place(x=10, y=360)
Label(root, text="Weight").place(x=10, y=400)
Label(root, text="Disease").place(x=10, y=440)
Label(root, text="Admit Date").place(x=10, y=480)
Label(root, text="Discharge Date").place(x=10, y=520)
Label(root, text="Guardian name").place(x=10, y=560)

e1 = Entry(root)
e1.place(x=580, y=10)
 
e2 = Entry(root)
e2.place(x=580, y=80)
 
e3 = Entry(root)
e3.place(x=580, y=120)

e4 = Entry(root)
e4.place(x=580, y=160)

e5 = Entry(root)
e5.place(x=580, y=200)

e6 = Entry(root)
e6.place(x=580, y=240)

e7 = Entry(root)
e7.place(x=580, y=280)

e8 = Entry(root)
e8.place(x=580, y=320)

e9 = Entry(root)
e9.place(x=580, y=360)

e10 = Entry(root)
e10.place(x=580, y=400)

e11 = Entry(root)
e11.place(x=580, y=440)

e12 = Entry(root)
e12.place(x=580, y=480)

e13 = Entry(root)
e13.place(x=580, y=520)

e14 = Entry(root)
e14.place(x=580, y=560)

root.mainloop()
