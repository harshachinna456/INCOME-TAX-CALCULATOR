from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")     #creating root window
root.title("Income Tax Calculator")
root.configure(bg="#e0b21b")
#creating frame to place the calculator
f1=Frame(root,bg="#823574",relief="groove",bd=3)
f1.place(x=50,y=50,width=300,height=300)
f2=Frame(f1,bg="#823574")
f2.place(x=50,y=110,width=200,height=200)
#creating a exit calculator alert
def closewindow():
    result=messagebox.askokcancel("Quit","Do you want to close the window")
    if result:
        quit()
root.protocol("WM_DELETE_WINDOW",closewindow)
#function to calculate
def taxamount():
    a2=int(a1.get())
    if a2>=250001 and a2<500000:
        tax=5
        return entryer.set(str(a2 * (tax/100)))
    elif a2 >=500001 and a2 <750000:
        tax=10
        return entryer.set(str((a2 * (tax/100)+12500)))
    elif a2 >=750001 and a2<=1000000:
        tax=15
        return entryer.set(str((a2 * (tax / 100) + 37500)))
    elif a2 >= 1000001 and a2 <= 1250000:
        tax = 20
        return entryer.set(str((a2 * (tax / 100) + 75000)))
    elif a2 >= 1250001 and a2 <= 1500000:
        tax = 25
        return entryer.set(str((a2 * (tax / 100) + 125000)))
    elif a2 >= 1500001:
        tax =30
        return entryer.set(str((a2 * (tax / 100) + 187500)))
    else:
        return entryer.set("0")
#create lable to take input from user
a = Label(f2, text="amount",background="#3bd9bc",foreground="#e01b6d")
a.grid(row=0,column=0)
#create a entry to take input from user
a1 = Entry(f2,background="SkyBlue2",foreground="blue4")
a1.grid(row=0,column=1,columnspan=2)
#button when clicked will display output
button = Button(f2,text="submit", bg="blue4", font=("bold", 10), fg="PaleTurquoise1", command=taxamount)
button.grid(row=1,column=1)

#taking tax amount and displaying it
entryer = StringVar()
entryer.set(0)

totaltax=Label(f2, textvariable=entryer,bg="LightYellow2",fg="blue4")
totaltax.grid(row=2,column=1)

#listbx=Listbox(f2)
#listbx.insert(0,"income tax slab            -      tax applicable as per new regime")
#listbx.insert(1,"Rs.0 - Rs.250000           -          nill")

#listbx.insert(2,"Rs.250001 - Rs.500000      -          5.00%")
#lstbx.insert(3,"Rs.500001 - Rs.750000      -          12500+10%")
#listbx.insert(4,"Rs.750001 - Rs.1000000     -          37500+15%")
#listbx.insert(5,"Rs.1000001 - Rs.1250000    -          75000+20%")
#listbx.insert(6,"Rs.1250001 - Rs.1500000    -          125000+25%")
#listbx.insert(7,"Rs.1500001                 -          125000+30%")
#listbx.grid(row=3,column=0,columnspan=3)
root.mainloop()
