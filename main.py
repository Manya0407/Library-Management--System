import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
lay=[]


  
def register():
  register_window = Toplevel(root)
  register_window.geometry("600x600")
  register_window.title("DBMS Register Page")
  register_window.bg = ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  register_window.resizable(False, False)
  bg=Label(register_window,image=register_window.bg).place(x=0,y=0, relwidth=1)
  Frame_reg=Frame(register_window,bg="white")
  Frame_reg.place(x=95, y=200, height=300, width=400)
  title=Label(Frame_reg,text="REGISTER", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
            

  lblfrstrow = Label(Frame_reg, text ="Username -", bg="#FFFFFF")   
  lblfrstrow.place(x = 50, y = 100)
  
  Username = Entry(Frame_reg, width = 35, textvariable=myUser2)          
  Username.place(x = 150, y = 100, width = 100)
  un=Username.get()
            
  lblsecrow = Label(Frame_reg, text ="Password -", bg="#FFFFFF")                               
  lblsecrow.place(x = 50, y = 130)
           
  password = Entry(Frame_reg, width = 35, textvariable=myPass2)
  password.place(x = 150, y = 130, width = 100)
  pw=password.get()
  
  lblthirow = Label(Frame_reg, text ="Name -", bg="#FFFFFF")
  lblthirow.place(x = 50, y = 160)
           
  name = Entry(Frame_reg, width = 35, textvariable=myName)
  name.place(x = 150, y = 160, width = 100)
  nm=name.get()

  lblfourow = Label(Frame_reg, text ="Gender -", bg="#FFFFFF")
  lblfourow.place(x = 50, y = 190)
           
  gender = Entry(Frame_reg, width = 35, textvariable=myGender)
  gender.place(x = 150, y = 190, width = 100)
  g=gender.get()
           
  submitbtn = Button(Frame_reg, text ="Register",bg ='#F195AC', command = registeract)
  submitbtn.place(x = 150, y = 225, width = 100)


def registeract():
    db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
    un = myUser2.get()
    pw = myPass2.get()
    nm=myName.get()
    g=myGender.get() 
    cursor = db.cursor()
    mySql_insert_query = "INSERT INTO Reg (UserId, Password, Name, Gender) VALUES (%s, %s, %s, %s)"
    val = (un,pw,nm,g)
    cursor.execute(mySql_insert_query, val)
    db.commit()
    new_loginwindow()



def new_loginwindow():
  login_window = Toplevel(root)
  lay.append(login_window)
  login_window.geometry("600x600")
  login_window.title("DBMS Login Page")
  login_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  login_window.resizable(False, False)
  bg=Label(login_window,image=login_window.bg).place(x=0,y=0)
  Frame_login=Frame(login_window,bg="white")
  Frame_login.place(x=95, y=200, height=300, width=400)
  title=Label(Frame_login,text="LOGIN", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)

  lblfrstrow = Label(Frame_login, text ="Username -", bg="#FFFFFF" )
  lblfrstrow.place(x = 50, y = 100)
       
  Username = Entry(Frame_login, width = 35, textvariable=myUser)
  Username.place(x = 150, y = 100, width = 100)
            
  lblsecrow = Label(Frame_login, text ="Password -", bg="#FFFFFF" )
  lblsecrow.place(x = 50, y = 150)
           
  password = Entry(Frame_login, width = 35, textvariable=myPass)
  password.place(x = 150, y = 150, width = 100)
           
  submitbtn = Button(Frame_login, text ="Login", bg ='#F195AC', command = loginact)
  submitbtn.place(x = 150, y = 205, width = 55)

def loginact():
    top = lay[0]
    top.withdraw()
    db = mysql.connector.connect(host="localhost", user="root", password="manya04", db="libmanagement")
    user = myUser.get()
    passw = myPass.get()
    cursor = db.cursor()
    
    # Use parameterized query to prevent SQL injection
    savequery = "SELECT * FROM Reg WHERE UserID = %s AND Password = %s"
    query_params = (user, passw)
    
    try:
        cursor.execute(savequery, query_params)
        myresult = cursor.fetchall()
        
        if len(myresult) == 0:
            new_loginerrwindow()
        else:
            new_mainwindow()
            
    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error occurred: {err}")
        new_loginerrwindow()
    
    finally:
        cursor.close()
        db.close()
        
def new_loginerrwindow():
    loginerrwindow = Toplevel(root)
    loginerrwindow .geometry("300x300")
    loginerrwindow .title("DBMS Login Error Page")
    lbl = Label(loginerrwindow, text ="Incorrect Login entered", )
    lbl.place(x = 50, y = 20)
    new_loginwindow()
   
    
    
def new_mainwindow():
    mainwindow = Toplevel(root)
    mainwindow.geometry("900x600")
    mainwindow.title("DBMS Main Page")
    mainwindow.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
    mainwindow.resizable(False, False)
    bg=Label(mainwindow,image=mainwindow.bg).place(x=0,y=0, relwidth=1)
    Frame_main=Frame(mainwindow,bg="white")
    Frame_main.place(x=95, y=200, height=300, width=400)
    title=Label(Frame_main,text="LIBRARY", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
    issue_btn = Button(Frame_main, text ="Issue",bg ='#F195AC',command=issuewindow)
    issue_btn.place(x = 50, y = 100, width = 55)
    return_btn = Button(Frame_main, text ="Return", bg ='#F195AC',command=returnwindow)
    return_btn.place(x = 200, y = 100, width = 55)
    delete_btn = Button(Frame_main, text ="Delete Book", bg ='#F195AC',command=deletewindow)
    delete_btn.place(x = 50, y = 150, width = 85)
    addbooks_btn = Button(Frame_main, text ="Add Book", bg ='#F195AC',command=addwindow)
    addbooks_btn.place(x = 200, y = 150, width = 85)
    viewbooks_btn = Button(Frame_main, text ="View Books", bg ='#F195AC',command=viewwindow)
    viewbooks_btn.place(x = 200, y = 200, width = 85)
    exitbooks_btn = Button(Frame_main, text ="Exit", bg ='#F195AC',command=exitact)
    exitbooks_btn.place(x = 50, y = 200, width = 85)

def issuewindow():
  db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
  cursor = db.cursor()
  issue_window = Toplevel(root)
  issue_window.geometry("600x600")
  issue_window.title("DBMS Issue Page")
  issue_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  issue_window.resizable(False, False)
  bg=Label(issue_window,image=issue_window.bg).place(x=0,y=0, relwidth=1)
  Frame_iss=Frame(issue_window,bg="white")
  Frame_iss.place(x=95, y=200, height=300, width=400)
  title=Label(Frame_iss,text="ISSUE", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
            

  lblfrstrow = Label(Frame_iss, text ="Book ID -", bg="#FFFFFF")
  lblfrstrow.place(x = 50, y = 100)
  Bid = Entry(Frame_iss, width = 35, textvariable=myUser3)
  Bid.place(x = 150, y = 100, width = 100)
  

  addbtn = Button(Frame_iss, text ="Issue",bg ='#F195AC', command = issueact)
  addbtn.place(x = 150, y = 230, width = 100)
       


def issueact():
  db = mysql.connector.connect(host ="localhost",user = "root", password = "kakshu", db ="libmanagement")
  cursor = db.cursor()
  bid=myUser3.get()
  allBid=[]
  findavail="select available from Book_available where BookID = "+bid
  try:

        cursor.execute(findavail)
        myresult = cursor.fetchall()

        for i in myresult:
            isAvail=i[0]
            if isAvail == 'TRUE':
                status = True
                print("True")
            else:
                status = False

  except:
        new_isserrwindow()

  updateTable = "update Book_available set available = 'FALSE' where BookID = "+bid
  try:
        if status == True:
            cursor.execute(updateTable)
            db.commit()
            new_mainwindow()
        else:
            new_isserrwindow2()
  except:
        new_isserrwindow()


def new_isserrwindow():
    isserrwindow = Toplevel(root)
    isserrwindow.geometry("300x300")
    isserrwindow.title("DBMS Issue Error Page")
    lbl = Label(isserrwindow, text ="Incorrect BookID entered", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()


def new_isserrwindow2():
    isserrwindow2 = Toplevel(root)
    isserrwindow2.geometry("300x300")
    isserrwindow2.title("DBMS Issue Error Page")
    lbl = Label(isserrwindow2, text ="Book is not available", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()

def returnwindow():
  db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
  cursor = db.cursor()
  return_window = Toplevel(root)
  return_window.geometry("600x600")
  return_window.title("DBMS Return Page")
  return_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  return_window.resizable(False, False)
  bg=Label(return_window,image=return_window.bg).place(x=0,y=0, relwidth=1)
  Frame_ret=Frame(return_window,bg="white")
  Frame_ret.place(x=95, y=200, height=300, width=400)
  title=Label(Frame_ret,text="RETURN", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
            

  lblfrstrow = Label(Frame_ret, text ="Book ID -", bg="#FFFFFF")
  lblfrstrow.place(x = 50, y = 100)
  Bid = Entry(Frame_ret, width = 35, textvariable=myUser4)
  Bid.place(x = 150, y = 100, width = 100)
  

  addbtn = Button(Frame_ret, text ="Return",bg ='#F195AC', command = returnact)
  addbtn.place(x = 150, y = 230, width = 100)

def returnact():
  db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
  cursor = db.cursor()
  bid=myUser4.get()
  allBid=[]
  findavail="select available from Book_available where BookID = "+bid
  try:

        cursor.execute(findavail)
        myresult = cursor.fetchall()

        for i in myresult:
            isAvail=i[0]
            if isAvail == 'FALSE':
                status = True
                print("True")
            else:
                status = False

  except:
        new_reterrwindow()

    
  updateTable = "update Book_available set available = 'TRUE' where BookID = "+bid
  try:
        if status == True:
            cursor.execute(updateTable)
            db.commit()
            new_mainwindow()
        else:
            new_reterrwindow2()
  except:
        new_reterrwindow()


def new_reterrwindow():
    isserrwindow = Toplevel(root)
    isserrwindow.geometry("300x300")
    isserrwindow.title("DBMS Issue Error Page")
    lbl = Label(isserrwindow, text ="Incorrect BookID entered", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()


def new_reterrwindow2():
    isserrwindow2 = Toplevel(root)
    isserrwindow2.geometry("300x300")
    isserrwindow2.title("DBMS Issue Error Page")
    lbl = Label(isserrwindow2, text ="Book is not available", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()

def exitact():
    exit()


def deletewindow():
  delete_window = Toplevel(root)
  delete_window.geometry("600x600")
  delete_window.title("DBMS Delete Page")
  delete_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  delete_window.resizable(False, False)
  bg=Label(delete_window,image=delete_window.bg).place(x=0,y=0)
  Frame_del=Frame(delete_window,bg="white")
  Frame_del.place(x=95, y=300, height=200, width=250)
  title=Label(Frame_del,text="DELETE", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=40,y=30)
  
  lblfrstrow = Label(Frame_del, text ="BookID -", bg="#FFFFFF" )
  lblfrstrow.place(x = 20, y = 100)
    
  BookID = Entry(Frame_del, width = 35, textvariable=myBID2)
  BookID.place(x = 100, y = 100, width = 100)
  BID=BookID.get()

  delbtn = Button(Frame_del, text ="Delete",bg ='#F195AC', command = delact)
  delbtn.place(x = 20, y = 150, width = 100)

def delact():
    db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
    bid = myBID2.get()
    cursor = db.cursor()
    mySql_delete_query = "delete from Books1 where BookID= "+bid
    mySql_delete_query2 = "delete from Book_available where BookID= "+bid
    try:
        cursor.execute(mySql_delete_query)
        cursor.execute(mySql_delete_query2)
        db.commit()
        myresult = cursor.fetchall()
         
    except:
        db.rollback()
        new_delerrwindow()
    
    db.commit()
    new_mainwindow()

def new_delerrwindow():
    delerrwindow = Toplevel(root)
    delerrwindow .geometry("300x300")
    delerrwindow .title("DBMS Delete Error Page")
    lbl = Label(delerrwindow, text ="Incorrect BookID entered", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()

            
def addwindow():
  add_window = Toplevel(root)
  add_window.geometry("600x600")
  add_window.title("DBMS Add Page")
  add_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  add_window.resizable(False, False)
  bg=Label(add_window,image=add_window.bg).place(x=0,y=0, relwidth=1)
  Frame_add=Frame(add_window,bg="white")
  Frame_add.place(x=95, y=200, height=300, width=400)
  title=Label(Frame_add,text="ADD BOOK", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
            

  lblfrstrow = Label(Frame_add, text ="BookID -",  bg="#FFFFFF" )
  lblfrstrow.place(x = 50, y = 100)
       
  BookID = Entry(Frame_add, width = 35, textvariable=myBID)
  BookID.place(x = 150, y = 100, width = 100)
  BID=BookID.get()
            
  lblsecrow = Label(Frame_add, text ="Book Name -", bg="#FFFFFF" )
  lblsecrow.place(x = 50, y = 130)
           
  bkname = Entry(Frame_add, width = 35, textvariable=myBName)
  bkname.place(x = 150, y = 130, width = 100)
  bname=bkname.get()
  
  lblthirow = Label(Frame_add, text ="Genre -", bg="#FFFFFF" )
  lblthirow.place(x = 50, y = 160)
           
  genre = Entry(Frame_add, width = 35, textvariable=myGenre)
  genre.place(x = 150, y = 160, width = 100)
  gn=genre.get()

  lblfourow = Label(Frame_add, text ="Author Name -", bg="#FFFFFF" )
  lblfourow.place(x = 50, y = 190)
           
  auname = Entry(Frame_add, width = 35, textvariable=myAName)
  auname.place(x = 150, y = 190, width = 100)
  aname=auname.get()
           
  addbtn = Button(Frame_add, text ="Add",bg ='#F195AC', command = addact)
  addbtn.place(x = 150, y = 230, width = 100)

def addact():
    db = mysql.connector.connect(host ="localhost",user = "root", password = "manya04", db ="libmanagement")
    bid = myBID.get()
    bname = myBName.get()
    genre=myGenre.get()
    aname=myAName.get() 
    cursor = db.cursor()
    mySql_insert_query = "INSERT INTO Books1 (BookId, BookName, Genre, AuthorName, Status) VALUES (%s, %s, %s, %s, %s)"
    val = (bid, bname, genre, aname, False)
    cursor.execute(mySql_insert_query, val)
    mySql_insert_query2 = "INSERT INTO Book_Available (BookId, available) VALUES (%s, %s)"
    val2 = (bid, 'TRUE')
    cursor.execute(mySql_insert_query2, val2)
    db.commit()
    new_mainwindow()

def viewwindow():
  view_window = Toplevel(root)
  view_window.minsize(width=400,height=400)
  view_window.geometry("600x600")
  view_window.title("DBMS View Page")
  view_window.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
  view_window.resizable(False, False)
  bg=Label(view_window,image=view_window.bg).place(x=0,y=0, relwidth=1)
  Frame_view=Frame(view_window,bg="white")
  Frame_view.place(x=50, y=200, height=300, width=500)
  title=Label(Frame_view,text="VIEW BOOK", font=("Bodoni MT Black", 20), fg="#289499",bg="#F1F093").place(x=50,y=30)
  db = mysql.connector.connect(host ="localhost",user = "root", password = "kakshu", db ="libmanagement")

  y = 0.4
  lbl=Label(Frame_view, text="%-10s%-40s%-30s%-20s"%('BookID','BookName','Genre','AuthorName'),bg='#F195AC',fg='white')
  lbl.place(relx=0.07,rely=0.3)
  getBooks = "select * from Books1"
  cursor = db.cursor()
  try:
    cursor.execute(getBooks)
    myresult = cursor.fetchall()
    db.commit()
    for i in myresult:
        Label(Frame_view,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='#F195AC', fg='white').place(relx=0.07,rely=y)
        y += 0.1
  except:
      new_viewerrwindow()

def new_viewerrwindow():
    viewerrwindow = Toplevel(root)
    viewerrwindow.geometry("300x300")
    viewerrwindow.title("DBMS View Error Page")
    lbl = Label(viewerrwindow, text ="Error occured", )
    lbl.place(x = 50, y = 20)
    new_mainwindow()


      
    
root = Tk()
root.geometry("900x600")
root.title("DBMS Intro Page")
root.resizable(False, False)
root.bg=ImageTk.PhotoImage(file=r"C:\Users\saura\Desktop\Library-Management\picture.jpg")
bg=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
Frame_intro=Frame(root,bg="white")
Frame_intro.place(x=95, y=200, height=300, width=400)
title=Label(Frame_intro,text="WELCOME TO THE LIBRARY", font=("Gabriola", 20), fg="#289499",bg="#F1F093").place(x=66,y=30)

myUser = StringVar()
myPass = StringVar()
myUser2 = StringVar()
myPass2 = StringVar()
myUser3 = StringVar()
myUser4 = StringVar()
myName= StringVar()
myGender= StringVar()
myBID= StringVar()
myBName= StringVar()
myGenre= StringVar()
myAName= StringVar()
myBID2= StringVar()

loginbtn = Button(Frame_intro, text ="Login",bg ='#F195AC', command = new_loginwindow)
loginbtn.place(x = 70, y = 135, width = 55)

regbtn = Button(Frame_intro, text ="Register",bg ='#F195AC', command = register)
regbtn.place(x = 190, y = 135, width = 55)
 

root.mainloop()