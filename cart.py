import mysql.connector



# mysql-python connecter
mydb = mysql.connector.connect(host='localhost', user='root', password='Artist0-9')
# print(mydb)
mycursor=mydb.cursor()
def remove():
    print("\n")
    print("$$$$$$$$$$$$ VISUAL FOLKS $$$$$$$$$$$$")
    print("\n")
    global p
    global q
    global pn
    global cb
    n = 0
    p = input("Enter your email :")
    q = input("Enter your password :")
    with open(r"custemor_login_details.txt", 'r+') as fp:
        for i in fp:
            x = i.split()
            # print(x)
            if p in x and q in x:
                n=1
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from cust_cart")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1: 'id_no', 2: 'cust_gmail', 3: 'cust_password', 4: 'cust_name', 5: 'artist_password', 6: 'artist_gmail',
                     7: 'painting_name', 8: 'medium',
                     9: 'size', 10: 'price', 11: 'payment_status', 12: 'artist_name'}
                # print(l)
                dict = {}
                t = 0
                for i in myresult:
                    c = 0
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    #print(dict)
                    if p==dict.get('cust_gmail') and q==dict.get('cust_password') and dict.get('payment_status')=='NOT SELL':
                            c=1
                            row = 6
                            for i in range(row):
                                for j in range(row):
                                    print("****", end="")
                                if i == 0:
                                    print("  ", dict.get('painting_name'), end="")
                                if i == 1:
                                    print("   By", dict.get('artist_name'), end='')
                                if i == 2:
                                    print("   ----------------------------------------", end='')
                                if i == 3:
                                    print("     Size           Medium         ", end='')
                                if i \
                                        == 4:
                                    print("  ", dict.get('size'), " ", dict.get('medium'), " ", end='')
                                if i == 5:
                                    print("   ----------------------------------------", end='')
                                print()
                            print("                           Rs ", dict.get('price'))
                            print("                          ", dict.get('payment_status'))
                            print('\n')
                    dict = {}
                    t = 0
                if c == 0:
                    print('\n')
                    print("     You don't cart anything.....")
                    print('\n')
                    print("press ! to back")
                    s = input("")
                    cart()
                pn = input("Name of painting  :")
                cb = input("created by _____:")
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from cust_cart")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1: 'id_no', 2: 'cust_gmail', 3: 'cust_password', 4: 'cust_name', 5: 'artist_password',
                     6: 'artist_gmail',
                     7: 'painting_name', 8: 'medium',
                     9: 'size', 10: 'price', 11: 'payment_status', 12: 'artist_name'}
                # print(l)
                dict = {}
                t = 0
                for i in myresult:
                    c = 0
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    # print(dict)
                    if p==dict.get('cust_gmail') and q==dict.get('cust_password'):
                        mycursor.execute("use art_gallery")
                        sql = "delete from cust_cart where painting_name=" + "'" + pn + "'" + " and " + "artist_name=" + "'" + cb + "'" + " and " + "payment_status=" + "'NOT SELL'"
                        mycursor.execute(sql)
                        mydb.commit()
                        print(" your cart item is deleted")
                        print("\n")
                        cart()

                    dict = {}
                    t = 0
        if n==0:
                print("An error occurred with log in....")
                remove()

def put_cart():
    mycursor.execute("use art_gallery")
    mycursor.execute("select*from artist_sell")
    myresult = mycursor.fetchall()
    # print(myresult)
    d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'medium', 6: 'size', 7: 'price', 8: 'art_code',
         9: 'sell_or_not', 10: 'user_name'}
    # print(l)
    dict = {}
    t = 0
    c= 0
    for i in myresult:
        for x in i:
            # print(x)
            t = t + 1
            dict.setdefault(d.get(t), x)
        # print(dict)
        if  dict.get('painting_name')==n and  dict.get('user_name')==a:
             gm=dict.get('gmail')
             pwd=dict.get('password')
             m=dict.get('medium')
             s=dict.get('size')
             p=dict.get('price')
             ac=dict.get('sell_or_not')
             s=dict.get('size')
             mycursor.execute("use art_gallery")
             sql = "insert into cust_cart(cust_gmail,cust_password,cust_name,artist_pwd,artist_gmail,painting_name,medium,size,price,payment_status,artist_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             val = [
                 (e,pw,u,pwd,gm,n,m,s,p,ac,a),
             ]
             mycursor.executemany(sql, val)
             mydb.commit()
             print(" your records are carted")
             print("\n")
             view()

        dict = {}
        t = 0
    cart()



def add_to_cart():
    print("<<<<<<<<<< PURCHASE YOUR PRODUCT >>>>>>>>>>")
    global n
    global a
    n = str(input("Name of painting :"))
    a = str(input("created by _____:"))
    mycursor.execute("use art_gallery")
    mycursor.execute("select*from artist_sell")
    myresult = mycursor.fetchall()
    # print(myresult)
    d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'medium', 6: 'size', 7: 'price', 8: 'art_code',
         9: 'sell_or_not', 10: 'user_name'}
    # print(l)
    dict = {}
    t = 0
    none = 1
    for i in myresult:
        for x in i:
            # print(x)
            t = t + 1
            dict.setdefault(d.get(t), x)
            if dict.get('sell_or_not') == 'NOT SELL' and n==dict.get('painting_name') and a==dict.get('user_name'):
                row = 6
                for i in range(row):
                    for j in range(row):
                        print("****", end="")
                    if i == 0:
                        print("  ", dict.get('painting_name'), end="")
                    if i == 1:
                        print("   By", dict.get('user_name'), end='')
                    if i == 2:
                        print("   ----------------------------------------", end='')
                    if i == 3:
                        print("     Size           Medium         ", end='')
                    if i == 4:
                        print("  ", dict.get('size'), " ", dict.get('medium'), " ", end='')
                    if i == 5:
                        print("   ----------------------------------------", end='')
                    print()
                print("                           Rs ", dict.get('price'))
                print('\n')
        dict = {}
        t = 0
    print("1=>BUY     2=>ADD TO CART     3=>BACK")
    c=int(input("choose your plane:"))
    while c!=0:
        if c==2:
            global e
            global pw
            global u
            e = input("Enter your email :")
            pw = input("Enter your password :")
            u= input("Enter your name:")
            put_cart()
        elif c==1:
            print("********** BUY PRODUCT **********")
            print("\n")
            print("------------------------------------------------")
            print("painting name:",n)
            print("created by:",a)
            row = 6
            for i in range(row):
                for j in range(row):
                    print("****", end="")
                print()
            print("------------------------------------------------")
            em = input("enter your gmal:")
            cpw = input("enter your password:")
            un=input("enter your name:")
            sn=input("enter your state:")
            sd=input("enter your district:")
            ua=input("enter your adress:")
            pc=input("enter your pin code:")
            um=input("enter your current mobile number:")
            print("1=>Cash on delivery           2=>Online paiment")
            s=int(input("choose your option: "))
            while s!=0:
                if s==1:
                    print("Painting name :",a)
                    print("Artist name :", n)
                    print("Customer name :",un)
                    print("custemer gmail id :",em)
                    print("State :",sn)
                    print("District :",sd)
                    print("Adress :",ua)
                    print("Pin code :",pc)
                    print("Mobile number :",um)
                    print("\n")
                    cnfrm=input("press @ button to conform")
                    if cnfrm=='@':
                        print("********** Your product has been delivered **********")
                        print("Delivered up to 5-7 days")
                        print("for more updates contact related artist")

                        mycursor.execute("use art_gallery")
                        sql = "insert into buy(painting_name,artist_name,user_name,state,district,address,pin_code,mob_num) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = [
                            (n, a, un, sn, sd, ua, pc, um),
                        ]
                        mycursor.executemany(sql, val)
                        mydb.commit()
                        mycursor.execute("use art_gallery")
                        mycursor.execute("select*from artist_sell")
                        myresult = mycursor.fetchall()
                        # print(myresult)
                        d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'medium', 6: 'size',
                             7: 'price', 8: 'art_code', 9: 'sell_or_not', 10: 'user_name'}
                        # print(l)
                        dict = {}
                        t = 0
                        none = 1
                        for i in myresult:
                            for x in i:
                                # print(x)
                                t = t + 1
                                dict.setdefault(d.get(t), x)
                            # print(dict)
                            if dict.get('painting_name')==n and dict.get('user_name')==a:
                                apw=dict.get('password')
                                agm=dict.get('gmail')
                                mid=dict.get('medium')
                                ss= dict.get('size')
                                ps=dict.get('price')
                                mycursor.execute("use art_gallery")
                                sql = "insert into cust_cart(cust_gmail,cust_password,cust_name,artist_pwd,artist_gmail,painting_name,medium,size,price,payment_status,artist_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                val = [
                                    (em,cpw,un,apw,agm,n,mid,ss,ps,'PAID',a),
                                ]
                                mycursor.executemany(sql, val)
                                mydb.commit()

                                c = dict.get('painting_name')
                                mycursor.execute("use art_gallery")
                                sql = "update  artist_sell set sell_or_not='SELL' WHERE painting_name=" + "'" +n+ "'"+" and "+"user_name="+"'"+a+"'"
                                # sql="update test set salary='3456' where salary='1234'"
                                mycursor.execute(sql)
                                mydb.commit()
                                x=input("press * to back")
                                if x=='*':
                                    cart()

                            dict={}
                            t=0
                elif s==2:
                    print("Painting name :", a)
                    print("Artist name :", n)
                    print("Customer name :", un)
                    print("State :", sn)
                    print("District :", sd)
                    print("Adress :", ua)
                    print("Pin code :", pc)
                    print("Mobile number :", um)
                    print("\n")
                    bnk= input("press @ button to connect your bank")
                    print("LOADING..........")
                    x = input("press * to back")
                    if x == '*':
                        cart()



        elif c==3:
            cart()

        elif c>3:
            print("wrong option")
            add()



def view():
    print("\n")
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    e = input("Enter your email :")
    pw = input("Enter your password :")
    with open(r"custemor_login_details.txt", 'r+') as fp:
        n=0
        for i in fp:
            x = i.split()
            # print(x)
            if e in x and pw in x:
                n=1
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from customer")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1: "id", 2: "cust_name", 3: "GMAIL", 4: "PASSWORD", 5: "MOBILE_NUMBER"}
                # print(l)
                dict = {}
                t = 0
                for i in myresult:
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    # print(dict)
                    if e == dict.get("GMAIL") and pw == dict.get("PASSWORD"):
                        print("-----------------------------------------------------")
                        print(dict.get("cust_name"))
                        print(dict.get("GMAIL"))
                        print("-----------------------------------------------------")
                        print("\n")
                    dict = {}
                    t = 0
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from cust_cart")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1: 'id_no', 2: 'cust_gmail', 3: 'cust_password', 4: 'cust_name', 5: 'artist_password', 6: 'artist_gmail', 7: 'painting_name', 8: 'medium',
                     9: 'size', 10: 'price',11:'payment_status',12:'artist_name'}
                # print(l)
                dict = {}
                t = 0
                c=0
                for i in myresult:
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    # print(dict)
                    if e==dict.get('cust_gmail') and pw==dict.get('cust_password'):
                            c=1
                            row = 6
                            for i in range(row):
                                for j in range(row):
                                    print("****", end="")
                                if i == 0:
                                    print("  ", dict.get('painting_name'), end="")
                                if i == 1:
                                    print("   By", dict.get('artist_name'), end='')
                                if i == 2:
                                    print("   ----------------------------------------", end='')
                                if i == 3:
                                    print("     Size           Medium         ", end='')
                                if i \
                                        == 4:
                                    print("  ", dict.get('size'), " ", dict.get('medium'), " ", end='')
                                if i == 5:
                                    print("   ----------------------------------------", end='')
                                print()
                            print("                           Rs ", dict.get('price'))
                            print("                          ", dict.get('payment_status'))
                            print('\n')

                    dict = {}
                    t = 0
                print("press @ to add product")
                print("press # to delete product")
                print("press * to back")
                a = input(" ")
                if a == '@':
                    add()
                elif a == '#':
                    remove()
                elif a=='*':
                    cart()


                if c==0:
                        print("               you dont cart enithing")
                        print("\n")
                        # a=input("press @ to add product")
                        # if c=='@':
                        #     add()

                        print("\n")



        if n == 0:
                print("An error occurred with log in....")
                view()
def add():
    mycursor.execute("use art_gallery")
    mycursor.execute("select*from artist_sell")
    myresult = mycursor.fetchall()
    # print(myresult)
    d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'medium', 6: 'size', 7: 'price', 8: 'art_code',
         9: 'sell_or_not', 10: 'user_name'}
    # print(l)
    dict = {}
    t = 0
    none = 1
    for i in myresult:
        for x in i:
            # print(x)
            t = t + 1
            dict.setdefault(d.get(t), x)
        if dict.get('sell_or_not')=='NOT SELL':
            # print(dict)
            row = 6
            for i in range(row):
                for j in range(row):
                    print("****", end="")
                if i == 0:
                    print("  ", dict.get('painting_name'), end="")
                if i == 1:
                    print("   By", dict.get('user_name'), end='')
                if i == 2:
                    print("   ----------------------------------------", end='')
                if i == 3:
                    print("     Size           Medium         Art Code", end='')
                if i == 4:
                    print("  ", dict.get('size'), " ", dict.get('medium'), " ", dict.get('art_code'), end='')
                if i == 5:
                    print("   ----------------------------------------", end='')
                print()
            print("                           Rs ", dict.get('price'), "                    ", "Buy Now")
            print("                          ", dict.get('sell_or_not'))
            print("                           Delivery time: 5-7 bussiness days")
            print('\n')
        dict = {}
        t = 0
    print("press + button to purchase your product")
    print("press # to  go back")
    x=input("")
    if x=='+':
        add_to_cart()
    elif x=='#':
        cart()




def cart():
    cart = {}
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    while True:
        print()
        print("Please type in one of these")
        print("1. Add item ")
        print("2. View cart ")
        print("3. Remove Item ")
        print("4. exit")

        select = int(input(" Type in a number to go on : "))

        if select == 1:
            add()



        if select == 2:
            view()


        if select == 3:
            remove()

        if select == 4:
            from cut_signin_login import start
            start()
            break


cart()
