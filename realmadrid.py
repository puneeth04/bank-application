import sqlite3
from random import *
conn = sqlite3.connect("bank.db")
c = conn.cursor()
class rmdbank:
    l = 0
    abc = True
    def register():
            global bank_id
            name = input("enter the username:")
            password  =input("enter the password:")
            bank_id = randint(1,50000)
            print("ur bank id is:",bank_id)
            c.execute("INSERT INTO BANKACC (ID,USERNAME,PASSWORD) VALUES(?,?,?)",(bank_id,name,password))
            conn.commit()
            c.execute("INSERT INTO BANKDET (ID,USERNAME,AMOUNT) VALUES(?,?,?)",(bank_id,name,0))
            conn.commit()
    def login():
            global id
            li = []
            id = int(input("enter the id:"))
            e = input("enter the username:")
            f = input("enter the passwod:")
            c.execute("SELECT ID FROM BANKACC ")
            F = c.fetchall()
            li.append(F)
            if id not in li:
                c.execute("SELECT PASSWORD FROM BANKACC WHERE ID =?",(id,))
                h = c.fetchone()
                H =list(h)
                c.execute("SELECT USERNAME FROM BANKACC WHERE ID =?",(id,))
                D = c.fetchone()
                E =list(D)
                if f == H[0] and e == E[0] :
                    print("login succesful")
                else:
                    print("register if u dont have a bank acc")
                    print("login failed,enter right password and username")
                    rmdbank.abc = False
            else:
                   print("login failed,enter id")
                   rmdbank.abc = False
    def add_deposit(amount):
        c.execute("SELECT AMOUNT FROM BANKDET WHERE ID =?",(id,))
        h = c.fetchone()
        H =list(h)
        a = int(input("enter the deposit amount:"))
        A = int(H[0])
        amount = A+a
        c.execute("UPDATE BANKDET SET AMOUNT = :amount WHERE ID =:id",{'amount':amount,'id':id})
        print("ur deposit money is:",a)
    def withadrawl(amount):
        c.execute("SELECT AMOUNT FROM BANKDET WHERE ID =?",(id,))
        h = c.fetchone()
        H =list(h)
        B =int(H[0])
        b = int(input("enter the withadrawl amount:"))
        amount = B-b
        c.execute("UPDATE BANKDET SET AMOUNT =:amount WHERE ID =:id",{'amount':amount,'id':id})
        print("ur withdrawl money is:",b)
    def transfer(amount):
        c.execute("SELECT AMOUNT FROM BANKDET WHERE ID =?",(id,))
        h = c.fetchone()
        H =list(h)
        B =int(H[0])
        b = int(input("enter the transfer amount:"))
        amount = B-b
        c.execute("UPDATE BANKDET SET AMOUNT =:amount WHERE ID =:id",{'amount':amount,'id':id})
        print("ur transfer money is:",b)
        x=input("enter id to transfer money:")
        c.execute("SELECT AMOUNT FROM BANKDET WHERE ID =?",(x,))
        v = c.fetchone()
        V =list(v)
        m =int(V[0])
        amount1 = m+b
        c.execute("UPDATE BANKDET SET AMOUNT =:amount WHERE ID =:id",{'amount':amount1,'id':x})
    def show_balance(amount):
        c.execute("SELECT AMOUNT FROM BANKDET WHERE ID =?",(id,))
        h = c.fetchone()
        H =list(h)
        amount =int(H[0])
        c.execute("UPDATE BANKDET SET AMOUNT =:amount WHERE ID =:id",{'amount':amount,'id':id})
        print("ur balance money is:",amount)
        
print("welcome to real madrid bank")
class bankacc(rmdbank):
    g = int(input("enter 1)login 2)register:"))
    if g==2:
        rmdbank.register()
        rmdbank.login()
    elif g==1:
        rmdbank.login()
    else:
        print("enter valid number")
    def chk():
                print("press the no for 1)adddeposit 2)withadrawl 3)showbalance 4)quit 5)transfer")
                x = int(input("enter the number:1,2,3,4,5:"))
                if x==1:
                    rmdbank.add_deposit(bankacc)
                elif x==2:
                    rmdbank.withadrawl(bankacc)
                elif x==3:
                    rmdbank.show_balance(bankacc)                
                elif x==4:
                    rmdbank.abc = False
                elif x==5:
                    rmdbank.transfer(bankacc)
                else:  
                    print("enter a valid number")
while rmdbank.abc:
    bankacc.chk()



conn.commit()
conn.close()
