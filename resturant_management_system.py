from tkinter import*
import random
import time


root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root, bg="light green", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#..................TIME........................

localtime=time.asctime(time.localtime(time.time()))
time.sleep(1)


#.................................***...........................................................

lbfo = Label(Tops, font=('aria', 30, 'bold'), text="RESTAURANT MANAGEMENT SYSTEM", fg="dark green", bd=10, anchor='ne')
lbfo.grid(row=0, column=0)
lbfo = Label(Tops, font=('aria', 20, 'bold'), text=localtime, fg="black", anchor=W)
lbfo.grid(row=1, column=0)

#---------------Calculator------------------

text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7 , bg="white",justify='right')
txtdisplay.grid(columnspan=4)


def  btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(0,100000000)
    randomRef = str(x)
    rand.set(randomRef)

    colf = float(Largefries.get())
    cob = float(Burger.get())
    cov = float(Vegmeal.get())
    con = float(Nonvegmeal.get())
    cot = float(Thakalifood.get())
    cod = float(Drinks.get())

    costoflargefries = colf * 30
    costofburger = cob * 25
    costofveg = cov * 60
    costofnonveg = con * 80
    costofthakali = cot * 65
    costofdrinks = cod * 40

    costoffood = "Rs.", str('%.2f' % (costoflargefries + costofburger + costofveg + costofnonveg + costofthakali + costofdrinks))
    Totalcost = (costoflargefries + costofburger + costofburger + costofveg + costofnonveg + costofthakali + costofdrinks)
    PayTax = ((costoflargefries + costofburger + costofburger + costofveg + costofnonveg + costofthakali + costofdrinks) * 0.33)
    ServiceCharge = ((costoflargefries + costofburger + costofveg + costofnonveg + costofthakali + costofdrinks) / 99)
    Service = "Rs.", str('%.2f' % ServiceCharge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + ServiceCharge)
    PaidTax = "Rs.", str('%.2f' % PayTax)

    Servicecharge.set(Service)
    Cost.set(costoffood)
    Tax.set(PayTax)
    Subtotal.set(costoffood)
    Total.set(OverAllCost)



def reset():
    rand.set("")
    Cost.set("")
    Largefries.set("")
    Burger.set("")
    Vegmeal.set("")
    Nonvegmeal.set("")
    Subtotal.set("")
    Total.set("")
    Thakalifood.set("")
    Servicecharge.set("")
    Drinks.set("")
    Tax.set("")

    #Costoffood.set("")

def Exit():
    root.destroy()


#...............................Buttons...................................


btn7=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16, pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Add=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Add.grid(row=2,column=3)

#......................................................................................................

btn4=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Sub=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Sub.grid(row=3,column=3)

#.........................................................................................

btn1=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multi=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: btnclick("*") )
multi.grid(row=4,column=3)

#.........................................................................................................

btn0=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="white", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Div=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Div.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="By Amit Kumar",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#................................................................................................


def price():
    root=Tk()
    root.geometry("500x350+0+0")
    root.title("Price List")

    labelinfo = Label(root, font=('aria', 15, 'bold'), text=" FOOD ITEMS", fg="dark green", bd=5)
    labelinfo.grid(row=0, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Large Fries", fg="black", bd=5)
    labelinfo.grid(row=1, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Burger", fg="black", bd=5)
    labelinfo.grid(row=2, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Veg Meal", fg="black", bd=5)
    labelinfo.grid(row=3, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Non VegMeal", fg="black", bd=5)
    labelinfo.grid(row=4, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Thakali Food", fg="black", bd=5)
    labelinfo.grid(row=5, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Drinks", fg="black", bd=5)
    labelinfo.grid(row=6, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Momos", fg="black", bd=5)
    labelinfo.grid(row=7, column=0)

    labelinfo = Label(root, font=('aria', 10, 'bold'), text="Chowmins", fg="black", bd=5)
    labelinfo.grid(row=8, column=0)

    labelinfo = Label(root, font=('aria', 15, 'bold'), text="                         ", fg="black", bd=5)
    labelinfo.grid(row=0, column=1)

    labelinfo = Label(root, font=('aria', 15, 'bold'), text="PRICE", fg="dark green", bd=5)
    labelinfo.grid(row=0,column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="30", fg="black", bd=5)
    labelinfo.grid(row=1, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="25", fg="black", bd=5)
    labelinfo.grid(row=2, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="60", fg="black", bd=5)
    labelinfo.grid(row=3, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="80", fg="black", bd=5)
    labelinfo.grid(row=4, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="65", fg="black", bd=5)
    labelinfo.grid(row=5, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="30", fg="black", bd=5)
    labelinfo.grid(row=6, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="30", fg="black", bd=5)
    labelinfo.grid(row=7, column=2)

    labelinfo = Label(root, font=('aria', 13, 'bold'), text="25", fg="black", bd=5)
    labelinfo.grid(row=8, column=2)


    root.mainloop()

rand = StringVar()
Largefries = StringVar()
Burger = StringVar()
Vegmeal = StringVar()
Nonvegmeal = StringVar()
Subtotal = StringVar()
Total = StringVar()
Servicecharge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Thakalifood = StringVar()



lblRef=Label(f1,font=( 'aria' ,15, 'bold' ),text="Order_No.",bd=10,anchor='w')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1,font=('ariel', 15 ,'bold'), textvariable=rand ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtRef.grid(row=0,column=1)

lbllrgfries=Label(f1,font=( 'aria' ,15, 'bold' ),text="Large fries",bd=10,anchor='w')
lbllrgfries.grid(row=1,column=0)
txtlrgfries=Entry(f1,font=('ariel', 15 ,'bold'), textvariable=Largefries ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtlrgfries.grid(row=1,column=1)

lblBurger=Label(f1,font=( 'aria' ,15, 'bold' ),text="Burger",bd=10,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('ariel', 15 ,'bold'), textvariable=Burger ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtBurger.grid(row=2,column=1)

lblVegmeal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Veg meal",bd=10,anchor='w')
lblVegmeal.grid(row=3,column=0)
txtVegmeal=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Vegmeal ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtVegmeal.grid(row=3,column=1)

lblNonVegmeal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Non vegmeal",bd=10,anchor='w')
lblNonVegmeal.grid(row=4,column=0)
txtNonVegmeal=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Nonvegmeal ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtNonVegmeal.grid(row=4,column=1)

lblThakali=Label(f1,font=( 'aria' ,15, 'bold' ),text="Thakali food",bd=10,anchor='w')
lblThakali.grid(row=5,column=0)
txtThakali=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Thakalifood ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtThakali.grid(row=5,column=1)

#................................................................................................

lblDrinks=Label(f1,font=( 'aria' ,15, 'bold' ),text="Drinks",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Drinks, insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost=Label(f1,font=( 'aria' ,15, 'bold' ),text="cost",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost=Entry(f1,font=('ariel', 15 ,'bold'),textvariable = Cost, insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtcost.grid(row=1,column=3)

lblservice=Label(f1,font=( 'aria' ,15, 'bold' ),text="Service charge",bd=10,anchor='w')
lblservice.grid(row=2,column=2)
txtservice=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Servicecharge ,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtservice.grid(row=2,column=3)

lblstate=Label(f1,font=( 'aria' ,15, 'bold' ),text="Tax",bd=10,anchor='w')
lblstate.grid(row=3,column=2)
txtstate=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Tax,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtstate.grid(row=3,column=3)

lblsubtotal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Subtotal",bd=10,anchor='w')
lblsubtotal.grid(row=4,column=2)
txtsubtotal=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Subtotal,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtsubtotal.grid(row=4,column=3)

lbltotalcost=Label(f1,font=( 'aria' ,15, 'bold' ),text="Total",bd=10,anchor='w')
lbltotalcost.grid(row=5,column=2)
txttotalcost=Entry(f1,font=('ariel', 15 ,'bold'),textvariable=Total,insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txttotalcost.grid(row=5,column=3)


#..............................Buttons..........................................................


lblspace = Label(f1,text="                  ",fg="white")
lblspace.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="light yellow",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="yellow",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=Exit)
btnexit.grid(row=7, column=3)


btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="light green",command=price)
btnprice.grid(row=7, column=0)


root.mainloop()

