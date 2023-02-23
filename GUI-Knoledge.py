from tkinter import*
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักโปรเเกรม
GUI.title('โปรเเกรมบันทึกข้อมูล') #ชื่อโปรเเกรม
GUI.geometry('800x600') #ขนาดโปรเเกรม


L1 = Label(GUI,text='โปรเเกรมบันทึกความรู้',font=('Angsana New',40),fg='green')
L1.place(x=200,y=0)
####################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่300บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=80,y=80)
B1 =ttk.Button(FB1,text='กรอกชื่อ',command=Button2)
B1.pack(ipadx=35,ipady=10)
#######################
def Button3():
    text = 'pyton 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)
FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=80,y=130)
B2 =ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B2.pack(ipadx=20,ipady=10)
########################

def Button4():
    text = 'ตอนนี้มีเงินในบัญชีอยู่300บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=80,y=180)
B3 =ttk.Button(FB3,text='กรอกชื่อ',command=Button2)
B3.pack(ipadx=35,ipady=10)





GUI.mainloop()

