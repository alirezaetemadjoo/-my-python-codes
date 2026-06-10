#--------------------stater---------------------

from tkinter import*
import tkinter.messagebox

#--------------------setting--------------------

call = Tk()
call.title("Calculator")
call.geometry("350x450")
call.resizable(False,False)
color = "black"
call.configure(bg = color)
PhotoImage(file = "calculator-3d-application-icon-png")
p = PhotoImage(file = "calculator-3d-application-icon-png")
icon = call.iconphoto(False,p)

#-------------------defline----------------------
#------------------frames------------------------

f1 = Frame(call,width =400,height = 50,bg = "white")
f1.pack()

f2 = Frame(call,width = 400,height = 50,bg = "white")
f2.pack()

f3 = Frame(call,width = 400,height = 50,bg ="white")
f3.pack()

f4 = Frame(call,width = 400,height = 50,bg = "white")
f4.pack()

f5 = Frame(call,width = 400,height= 50 ,bg = "white")
f5,pack()

f6 = Frame(call,width =400,height = 50,bg = "white")
f6.pack()

f7 = Frame(call,width =400,height = 50,bg = "white")
f7.pack()

f8 = Frame(call,width =400,height = 50,bg = "white")
f8.pack()

f9 = Frame(call,width =400,height = 50,bg = "white")
f9.pack()

f10 = Frame(call,width =400,height = 50,bg = "white")
f10.pack()

f11 = Frame(call,width =400,height = 50,bg = "white")
f11.pack()

f12 = Frame(call,width =400,height = 50,bg = "white")
f12.pack()

f13 = Frame(call,width =400,height = 50,bg = "white")
f13.pack()

f14 = Frame(call,width =400,height = 50,bg = "white")
f14.pack()

f15 = Frame(call,width =400,height = 50,bg = "white")
f15.pack()

f16 = Frame(call,width =400,height = 50,bg = "white")
f16.pack()

f17 = Frame(call,width =400,height = 50,bg = "white")
f17.pack()

f18 = Frame(call,width =400,height = 50,bg = "white")
f18.pack()

f19 = Frame(call,width =400,height = 50,bg = "white")
f19.pack()

f20 = Frame(call,width =400,height = 50,bg = "white")
f20.pack()

f21 = Frame(call,width =400,height = 50,bg = "white")
f21.pack()
f22 = Frame(call,width =400,height = 50,bg = "white")
f22.pack()

f23 = Frame(call,width =400,height = 50,bg = "white")
f23.pack()

f24 = Frame(call,width =400,height = 50,bg = "white")
f24.pack()

#------------------button------------------------

btn1 = Button(f1 , text = "%" , width=30 , command =%)
btn1.Pack(padx = 4 , pady = 4)

btn2 = Button(f2 , text = "CE" , width=30 , command = CE)
btn2.Pack(padx = 4 , pady = 4)

btn3 = Button(f3 , text = "C" , width=30 , command = C)
btn3.Pack(padx = 4 , pady = 4)

btn4 = Button(f4 , text = "back" , width=30 , command = back)
btn4.Pack(padx = 4 , pady = 4)

btn5 = Button(f5 , text = "1/x" , width=30 , command = 1/x)
btn5.Pack(padx = 4 , pady = 4)

btn6 = Button(f6 , text = "x2" , width=30 , command = x2)
btn6.Pack(padx = 4 , pady = 4)

btn7 = Button(f7 , text = "-/x" , width=30 , command = -/x)
btn7.Pack(padx = 4 , pady = 4)

btn8 = Button(f8 , text = "//" , width=30 , command = //)
btn8.Pack(padx = 4 , pady = 4)

btn9 = Button(f9 , text = "7" , width=30 , command = 7)
btn9.Pack(padx = 4 , pady = 4)

btn10 = Button(f10 , text = "8" , width=30 , command = 8)
btn10.Pack(padx = 4 , pady = 4)

btn11 = Button(f11 , text = "9" , width=30 , command = 9)
btn11.Pack(padx = 4 , pady = 4)

btn12 = Button(f12 , text = "x" , width=30 , command = x)
btn12.Pack(padx = 4 , pady = 4)

btn13 = Button(f13 , text = "4" , width=30 , command = 4)
btn13.Pack(padx = 4 , pady = 4)

btn14 = Button(f14 , text = "5" , width=30 , command = 5)
btn14.Pack(padx = 4 , pady = 4)

btn15 = Button(f15 , text = "6" , width=30 , command = 6)
btn15.Pack(padx = 4 , pady = 4)

btn16 = Button(f16 , text = "-" , width=30 , command = -)
btn16.Pack(padx = 4 , pady = 4)

btn17 = Button(f17 , text = "1" , width=30 , command = 1)
btn17.Pack(padx = 4 , pady = 4)

btn18 = Button(f18 , text = "2" , width=30 , command = 2)
btn18.Pack(padx = 4 , pady = 4)

btn19 = Button(f19 , text = "3" , width=30 , command = 3)
btn19.Pack(padx = 4 , pady = 4)

btn20 = Button(f20 , text = "+" , width=30 , command = +)
btn20.Pack(padx = 4 , pady = 4)

btn21 = Button(f21 , text = "+/-" , width=30 , command = +/-)
btn21.Pack(padx = 4 , pady = 4)

btn22 = Button(f22 , text = "0" , width=30 , command = 0)
btn22.Pack(padx = 4 , pady = 4)

btn23 = Button(f23 , text = "." , width=30 , command = .)
btn23.Pack(padx = 4 , pady = 4)

btn24 = Button(f24 , text = "=" , width=30 , command = =)
btn24.Pack(padx = 4 , pady = 4)










