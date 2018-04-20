
from tkinter import *
from tkinter import ttk
from shutil import copyfile
import os
master = Tk()
count = 0


def addrec():
    f = open('rahul.txt', 'a')
    medicine = s1.get()
    disease = s2.get()
    company = s3.get()
    substitude = s4.get()
    price = s5.get()

    f.writelines(medicine.ljust(19) + disease.ljust(19) + company.ljust(19)+substitude.ljust(19) + price.ljust(19)+"\n")
    f.close()

count=0
def nextrec():
    global count
    f = open('rahul.txt', 'r')
    ctr=(1 for q in open('rahul.txt'))
    i = 0
    while (i <= count):
        l = f.readline()
        i = i + 1
    list1 = l.split()
    if list1.__len__() != 0:
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        count = count + 1
    f.close()
    l6.config(text=count)


def prevrec():
    global count
    if count != 1:
        f = open('rahul.txt', 'r')
        i = 0
        count = count - 1
        while (i < count):
            l = f.readline()
            i = i + 1
        list1 = l.split()
        s1.set(list1[0])
        s2.set(list1[1])
        s3.set(list1[2])
        s4.set(list1[3])
        s5.set(list1[4])
        f.close()
        l6.config(text=count)


def deleterec():
    infile = open('rahul.txt', 'r').readlines()
    with open('output.txt', 'w') as outfile:
        for index, line in enumerate(infile):
            if index != count - 1:
                outfile.write(line)
    copyfile("output.txt", "rahul.txt")
    os.remove("output.txt")


def show_entry_fields():
    print("medicine Name: %s\ndisease : %s" % (s1.get(), s2.get()))


s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()

label1 = ttk.Label(master, text="medicine NAME")
label1.grid(row=0,column=1, pady=4)

l2 = Label(master, text="disease")
l2.grid(row=1,column=1, pady=4)

l3 = Label(master, text="COMPANY NAME")
l3.grid(row=2,column=1, pady=4)

l4 = Label(master, text="substitude")
l4.grid(row=3, column=1, pady=4)

l5 = Label(master, text="price")
l5.grid(row=4, column=1, pady=4)

l6 = Label(master, text="select Line")
l6.grid(row=5,column=1, pady=4)

e1 = Entry(master, textvariable=s1)
e1.grid(row=0, column=2, pady=4)

e2 = Entry(master, textvariable=s2)
e2.grid(row=1, column=2, pady=4)

e3 = Entry(master, textvariable=s3)
e3.grid(row=2, column=2, pady=4)

e4 = Entry(master, textvariable=s4)
e4.grid(row=3, column=2,  pady=4)

e5 = Entry(master, textvariable=s5)
e5.grid(row=4, column=2, pady=4)

e6 = Entry(master, textvariable=s6)
e6.grid(row=5, column=2,  pady=4)

Button(master, text='Quit', command=master.quit,height=5,width=10).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='SHOW', command=show_entry_fields,height=5,width=10).grid(row=7, column=2, sticky=W, pady=4)
Button(master, text='ADD', command=addrec,height=5,width=10).grid(row=7, column=4, sticky=W, pady=4)
Button(master, text='Right', command=nextrec,height=5,width=10).grid(row=8, column=0, sticky=W, pady=4)
Button(master, text='left', command=prevrec,height=5,width=10).grid(row=8, column=2, sticky=W, pady=4)
Button(master, text='DELETE', command=deleterec,height=5,width=10).grid(row=8, column=4, sticky=W, pady=4)
master.mainloop()