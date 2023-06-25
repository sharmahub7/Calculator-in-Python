from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def equalsum():
    global operator
    sums=str(eval(operator))
    text_Input.set(sums)
    operator=sums 

cal=Tk()
cal.title("Calculator")
operator="9"
text_Input=StringVar()

txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="gray",justify='right').grid(columnspan=4)

bttn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)

bttn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

bttn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

add=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick('+')).grid(row=1,column=3)

bttn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=2,column=0)

bttn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)

bttn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=2,column=2)

subb=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick('-')).grid(row=2,column=3)

bttn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=3,column=0)

bttn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)

bttn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=3,column=2)

mull=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick('*')).grid(row=3,column=3)

clear=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=btnClearDisplay).grid(row=4,column=0)

bttn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0)).grid(row=4,column=1)

equal=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=equalsum).grid(row=4,column=2)

div=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick('/')).grid(row=4,column=3)

cal.mainloop()
