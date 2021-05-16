from tkinter import*

def btnclick(number):
	global operator
	operator=operator+str(number)
	text_input.set(operator)

def btncleardisplay():
	global operator
	operator=""
	text_input.set("")
	
def btnequal():
	global operator
	sumup=str(eval(operator))
	text_input.set(sumup)
	operator=""
	
	
cal =Tk()
cal.title("calculator")
operator=""
text_input=StringVar()


txtdisplay=Entry(cal,font=('times',20,'bold'),textvariable=text_input,bd=30,insertwidth=5,bg="powderblue",justify='right').grid(columnspan=5)

btn7=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="7",command=lambda:btnclick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="8",command=lambda:btnclick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="9",command=lambda:btnclick(9)).grid(row=1,column=2)

btn4=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="4",command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="5",command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="6",command=lambda:btnclick(6)).grid(row=2,column=2)

btn3=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="3",command=lambda:btnclick(3)).grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="2",command=lambda:btnclick(2)).grid(row=3,column=1)

btn1=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="1",command=lambda:btnclick(1)).grid(row=3,column=2)

btn0=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="0",command=lambda:btnclick(0)).grid(row=4,column=1)

btnac=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="ac",command=btncleardisplay).grid(row=4,column=0)

btnans=Button(cal,padx=16,bd=8,fg="black",font=('times',18,'bold'),text="=",command=btnequal).grid(row=4,column=2)

btnadd=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="+",command=lambda:btnclick("+")).grid(row=1,column=3)

btnsub=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="-",command=lambda:btnclick("-")).grid(row=2,column=3)

btndiv=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="/",command=lambda:btnclick("/")).grid(row=3,column=3)

btnmul=Button(cal,padx=16,bd=8,fg="black",font=('times',20,'bold'),text="*",command=lambda:btnclick("*")).grid(row=4,column=3)

cal.mainloop()


