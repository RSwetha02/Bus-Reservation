#Bus Ticket Booking
from tkinter import*
import mysql.connector
import tkinter.messagebox as tm
from PIL import Image, ImageTk
def connection():
    global mydb,mycursor
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database='swetha_bus_ticket_booking'
    )
    mycursor=mydb.cursor()
    
def starting_page():
    global starting_screen
    starting_screen=Tk()
    starting_screen.title("Welcome to our travels")
    starting_screen.geometry("700x500")
    img1=Image.open("home.jpg")
    test1=ImageTk.PhotoImage(img1)
    img1_lbl=Label(image=test1)
    img1_lbl.image=test1
    img1_lbl.place(x=0,y=0)

    label_0=Label(starting_screen,text="SWETHA TRAVELS",width=32,relief=GROOVE,font=('Helvetica','18','bold'),fg="white",bg="blue4").place(x=100,y=30)
    
    btn1=Button(starting_screen,width=20,text="REGISTER",fg="blue",cursor="hand2",font=('Helvetica','13','bold'),activebackground="white",command=register)
    btn1.place(x=100,y=250)
    btn2=Button(starting_screen,width=20,text="LOGIN",fg="blue",cursor="hand2",font=('Helvetica','12','bold'),activebackground="white",command=login_page)
    btn2.place(x=100,y=320)
def register():
    global register_screen
    register_screen=Toplevel(starting_screen)
    register_screen.title("REGISTER")
    register_screen.geometry("700x500")
    register_screen.config(bg="skyblue")

    img=Image.open("signup.jpg")
    test=ImageTk.PhotoImage(img)
    img1_lbl=Label(register_screen,image=test,relief=FLAT,bg="white")
    img1_lbl.image=test
    img1_lbl.place(x=80,y=30)
    
    label_0=Label(register_screen,text="PASSENGER DETAILS",width=32,relief=GROOVE,font=('Helvetica','18','bold'),fg="white",bg="blue4").place(x=100,y=30)

    global Name,Contact_no,City,Age,Gender,Address,password
    variable=[StringVar() for _ in range(7)]
    Name, Contact_no, City, Age, Gender, Address, password = variable

    font=('Helvetica','11','bold')
    
    LName=Label(register_screen,text="NAME",font=font,bg="white").place(x=190,y=100)
    LPassword=Label(register_screen,text="PASSWORD",font=font,bg="white").place(x=190,y=150)
    LContact_no=Label(register_screen,text="PHONE",font=font,bg="white").place(x=190,y=200)
    LCity=Label(register_screen,text="CITY",font=font,bg="white").place(x=190,y=250)
    LAge=Label(register_screen,text="AGE",font=font,bg="white").place(x=190,y=300)
    LGender=Label(register_screen,text="GENDER",font=font,bg="white").place(x=190,y=350)
    Radiobutton(register_screen,text="MALE",padx=5,variable=Gender,value="male",font=font,bg="white").place(x=290,y=350)
    Radiobutton(register_screen,text="FEMALE",padx=5,variable=Gender,value="female",font=font,bg="white").place(x=370,y=350)
    LAddress=Label(register_screen,text="ADDRESS",font=font,bg="white").place(x=190,y=400)
    
    e1=Entry(register_screen,width=24,textvariable=Name,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=100)
    e1c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=125)
    e2=Entry(register_screen,width=24,textvariable=password,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=150)
    e2c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=175)
    e3=Entry(register_screen,width=24,textvariable=Contact_no,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=200)
    e3c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=225)
    e4=Entry(register_screen,width=24,textvariable=City,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=250)
    e4c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=275)
    e5=Entry(register_screen,width=24,textvariable=Age,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=300)
    e5c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=325)
    e6=Entry(register_screen,width=24,textvariable=Address,font=font,relief=FLAT,bg="white",fg="purple").place(x=290,y=400)
    e6c=Canvas(register_screen,height=2,width=190,bg="blue4").place(x=290,y=425)

    
    sbmitbtn=Button(register_screen,text="REGISTER",font=font,cursor="hand2",fg="blue",command=register_details).place(x=290,y=450)

def register_details():
    a=Name.get()
    b=password.get()
    c=Contact_no.get()
    d=City.get()
    e=Age.get()
    f=Gender.get()
    g=Address.get()
    
    
    connection()

    sql='INSERT INTO register(name,password,contact_no,city,age,gender,address)VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val=(a,b,c,d,e,f,g)
    try:
        mycursor.execute(sql,val)
        mydb.commit()
        tm.showinfo("Success","Registration Success")
        starting_page()
    except:
        mydb.rollback()
    finally:
        mycursor.close()
        mydb.close()
def login_page():
    
    global Login_screen
    Login_screen=Toplevel(starting_screen)
    Login_screen.title("Login")
    Login_screen.geometry("700x500")
    Login_screen.config(bg="white")
    global username_verify
    global password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    label_0=Label(Login_screen,text="LOGIN",width=32,relief=GROOVE,font=('Helvetica','18','bold'),fg="white",bg="blue4").place(x=100,y=30)
    uname=Label(Login_screen,font=('Helvetica','12','bold'),text="USER NAME",bg="white").place(x=130,y=150)
    password=Label(Login_screen,font=('Helvetica','12','bold'),text="PASSWORD",bg="white").place(x=130,y=190)
    e1=Entry(Login_screen,width=20,font=('Helvetica','12','bold'),relief=FLAT,bg="white",fg="purple",textvariable=username_verify).place(x=250,y=150)
    e1c=Canvas(Login_screen,height=2,width=190,bg="blue4").place(x=250,y=175)
    e2=Entry(Login_screen,width=20,font=('Helvetica','12','bold'),relief=FLAT,bg="white",fg="purple",textvariable=password_verify).place(x=250,y=190)
    e2c=Canvas(Login_screen,height=2,width=190,bg="blue4").place(x=250,y=215)

    img1=Image.open("login.jpg")
    test1=ImageTk.PhotoImage(img1)
    
    sbmitbtn=Button(Login_screen,relief=FLAT,image=test1,bg="white",cursor="hand2",command=Login).place(x=220,y=240)

    img=Image.open("user.jpg")
    test=ImageTk.PhotoImage(img)
    img1_lbl=Label(Login_screen,image=test,relief=FLAT,bg="white")
    img1_lbl.image=test
    img1_lbl.place(x=470,y=140)

    Login_screen.mainloop()
def Login():
    connection()
    if  username_verify.get()==""or password_verify.get()=="":
        tm.showerror("Error","please complete the required fields")
    else:
        mycursor.execute('select*FROM register WHERE name=%s AND password=%s',(username_verify.get(),password_verify.get()))
        if mycursor.fetchone():
            select_place()
            mycursor.close()
            mydb.close()
        else:
            user_not_found()
def user_not_found():
    tm.showerror("Error","Enter a invalid Username and password")
def select_place():
    global  select_place_screen
    select_place_screen=Toplevel(Login_screen)
    select_place_screen.geometry("700x500")
    select_place_screen.title("Journey details")
    select_place_screen.config(bg='white')
    
    label_0=Label(select_place_screen,text="SELECT YOUR JOURNEY",width=32,relief=GROOVE,font=('Helvetica','18','bold'),fg="white",bg="blue4").place(x=100,y=30)
    options_list = ["Chennai", "Madurai", "Dindigul","sivaganga","salem","erode", "Coimbatore","Bangalore","delhi","kerala","kochi","trichy","sivakasi"]
    options_list2=["Madurai","dindigul","bangalore","kodaikanal","salem","sivaganga","erode","hyderabad","delhi","kerala","kochi","trichy","sivakasi"]
    From= StringVar()
    From.set("From")
    To=StringVar()
    To.set("To")
    OptionMenu1= OptionMenu(select_place_screen, From, *options_list)
    OptionMenu1.config(font=('Helvetica','12','bold'),width='10')
    OptionMenu1.place(x=180,y=80)
    OptionMenu2=OptionMenu(select_place_screen, To, *options_list2)
    OptionMenu2.config(font=('Helvetica','12','bold'),width='10')
    OptionMenu2.place(x=380,y=80)
    def print_answers():
        global from_place,to_place
        from_place=From.get()
        to_place=To.get()
        update_place()
    btn= Button(select_place_screen,font=('Helvetica','12','bold'), text='NEXT',cursor="hand2",width='25',fg='blue', command=print_answers).place(x=210,y=400)
    select_place_screen.mainloop()
def update_place():
    connection()
    a1="UPDATE register SET departure=%s,destination=%s WHERE name=%s"
    b1=(from_place,to_place,username_verify.get())
    mycursor.execute(a1,b1)
    mydb.commit()
    seat_selection()
def seat_selection():
    global top
    top=Toplevel(select_place_screen)
    global seat_var, seat_chk
    
    #VARIABLE TYPE
    variable=[IntVar() for _ in range(30)]
    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30=variable

    seat_var=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30]
    seat_chk=["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15","c16","c17","c18","c19","c20","c21","c22","c23","c24","c25","c26","c27","c28","c29","c30"]
    for i in seat_var:
        i=IntVar()
    top.geometry("700x500")
    top.title("seat selection")
    label_0=Label(top,text="SELECT YOUR SEATS",width=50,font=('bold',15),bg="blue4",fg="white").pack()
    x=y=50
    for count in range(30):
        
        seat_chk[count]=Checkbutton(top,text="",onvalue=1,offvalue=0,height=2,variable=seat_var[count]).place(x=x,y=y)
        #aligning right seats
        if(x>=240):
            x=x+30
            if(x==300):
                x=240
                y=y+30
        #aligning left seats
        if(x<=110):
            x=x+30
            if(x==140):
                x=50
                y=y+30
        if(y==230):
            x=240
            y=50
    Button(top,text="Submit",width=20,fg='blue',command=seat_confirmation).place(x=100,y=270)
    label=Label(top,text="A").place(x=10,y=58)
    label=Label(top,text="B").place(x=10,y=90)
    label=Label(top,text="C").place(x=10,y=120)
    label=Label(top,text="D").place(x=10,y=150)
    label=Label(top,text="E").place(x=10,y=180)
    label=Label(top,text="F").place(x=10,y=210)
    label=Label(top,text="1").place(x=50,y=30)
    label=Label(top,text="2").place(x=80,y=30)
    label=Label(top,text="3").place(x=110,y=30)
    label=Label(top,text="4").place(x=245,y=30)
    label=Label(top,text="5").place(x=275,y=30)
    top.mainloop()
def seat_confirmation():
    global s_name,Amount
    seat_name=["A1","A2","A3","B1","B2","B3","C1","C2","C3","D1","D2","D3","E1","E2","E3","F1","F2","F3","A4","A5","B4","B5","C4","C5","D4","D5","E4","E5","F4","F5"]
    s_name=""
    Amount=0
    for count in range(30):
        x=seat_var[count]
        
        if (x.get()==1):
            s_name+=seat_name[count]+", "
            Amount+=200
    print(s_name,Amount)

    connection()
    a1="UPDATE register SET seat_no=%s,Ticket_price=%s WHERE name=%s"
    b1=(s_name,Amount,username_verify.get())
    mycursor.execute(a1,b1)
    mydb.commit()
    fetch_details()
def fetch_details():
    connection()
    a3='select name,contact_no,gender FROM register WHERE name=%s'
    a4=(username_verify.get(),)
    try:
        mycursor.execute(a3,a4)
        for a1 in mycursor:
                for a2 in range(len(a1)):
                    print(a1[a2])
        global b1,c1,d1
        b1=a1[0]
        c1=a1[1]
        d1=a1[2]
        print(b1,c1,d1)
    except:
        mydb.rollback()
    final_details()
def final_details():
    global final_details_screen
    final_details_screen=Toplevel(top)
    final_details_screen.title("CHECKOUT DETAILS")
    final_details_screen.geometry("700x500")
    font=('Helvetica','11','bold')
    font1=('Helvetica','9','bold')
    label_0=Label(final_details_screen,text="CHECKOUT DETAILS",width=50,font=('bold',15),bg="blue4",fg="white").pack()
    Name=Label(final_details_screen,text="NAME:",font=font1).place(x=220,y=50)
    Contact_no=Label(final_details_screen,text="CONTACT:",font=font1).place(x=220,y=100)
    Seat_no=Label(final_details_screen,text="SEAT NO.:",font=font1).place(x=220,y=150)
    From=Label(final_details_screen,text="DEPARTURE:",font=font1).place(x=220,y=200)
    Destiny=Label(final_details_screen,text="DESTINATION:",font=font1).place(x=220,y=250)
    Gender=Label(final_details_screen,text="GENDER:",font=font1).place(x=220,y=300)
    Ticket_amount=Label(final_details_screen,text="TICKET PRICE:",font=font1).place(x=220,y=350)
    e1=Label(final_details_screen,text=b1,font=font).place(x=320,y=50)
    e2=Label(final_details_screen,text=c1,font=font).place(x=320,y=100)
    e3=Label(final_details_screen,text=s_name,font=font).place(x=320,y=150)
    e4=Label(final_details_screen,text=from_place,font=font).place(x=320,y=200)
    e5=Label(final_details_screen,text=to_place,font=font).place(x=320,y=250)
    e6=Label(final_details_screen,text=d1,font=font).place(x=320,y=300)
    e7=Label(final_details_screen,text=Amount,font=font).place(x=320,y=350)
    sbmitbtn=Button(final_details_screen,text="SUBMIT",font=font,command=ticket_booked).place(x=240,y=400)
def ticket_booked():
    tm.showinfo("confirmed","ticket booked successfully")
starting_page()
