# """write login data in file"""
# file=open("artist_login_details.txt",'w')
# file.write("sanjusanjay23@gmail.com sanju123@""\n"
#  "shamendu12@gmail.com shammu@172""\n"
#  "rajrajan12@gmail.com rajan@142""\n"
# "ganapathi34@gmail.com ganapathi12@""\n"
# "punekae99@gmail.com punness21@""\n"
# "sanjusanju@gmail.com sanju09@""\n"
# "dipti66@gmail.com dipti88@""\n"
# "ghanshyam44@gmail.com ghan23@""\n"
# "nayakghana@gmail.com ghan23@32""\n"
# "rajraj23@gmail.com rajraj@12""\n"
# "paraspp23@gmail.com paras@23""\n"
# "sureshsuresh12@gmail.com susu@01""\n"
# "ganapathi45@gmail.com ganahana@12""\n"
# "babu123@gmail.com babu@123""\n"
# "govind123@gmail.com govi@123""\n")
# file.close()

# """ delete all datas in the file"""
# fp = open('artist_login_details.txt', 'r+')
# fp.truncate(0)
# fp.close()
#
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Artist0-9')
mycursor=mydb.cursor()
# print(mydb)
def update():
    print("\n")
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    e=input("Enter your email :")
    pw=input("Enter your password :")
    # global gmail
    # global pwd
    global username
    if e==gmail and pw==pwd:
          print(gmail,pwd)
          print("\n")
          print("#################### UPDATE YOUR CREATIVITY ####################")
          print("\n")
          X=input("upload your creativity :")
          y=input("name of your painting :")
          z = input("mediam of your painting :")
          s = input("size of your painting :")
          p=input("price of your painting :")
          a = input("Art code of your painting :")
          sell_or_not="SELL"
          mycursor.execute("use art_gallery")
          mycursor.execute("select*from artist")
          myresult = mycursor.fetchall()
          # print(myresult)
          d = {1: 'id_no', 2: 'user_name', 3: 'password', 4: 'contact_no', 5: 'gmail', 6: 'location', 7: 'about'}
          # print(l)
          dict = {}
          t = 0
          for i in myresult:
              for x in i:
                  # print(x)
                  t = t + 1
                  dict.setdefault(d.get(t), x)

              u = dict.get("user_name")
              if gmail==dict.get("gmail") and pwd==dict.get("password"):
                  mycursor.execute("use art_gallery")
                  sql = "insert into artist_sell(gmail,password,painting_name,medium,size,price,art_code,sell_or_not,user_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                  val = [
                          (e, pw, y, z, s, p, a, sell_or_not,u),
                      ]
                  mycursor.executemany(sql, val)
                  mydb.commit()
                  print(" your creativity is uploaded")
                  print("\n")
              dict = {}
              t = 0
    start()
def signup():
    print("$$$$$$$$$$$$ REGISTER $$$$$$$$$$$$")
    print("\n")
    print("kindly fill in this form to register")
    gmail = input("Enter email address: ")
    mob_no=int(input("Enter mobile number"))
    user_name=str(input("Enter user name: "))
    location = input("Enter your location")
    about=input("Enter something about you")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if "@gmail.com" in gmail:
        if  type(mob_no)==int and len(str(mob_no))==10:
            if user_name.isalpha()==True or " " in user_name:
                  if conf_pwd == pwd:
                      x=str(gmail)
                      y=str(pwd)
                      with open(r"artist_login_details.txt", 'r+') as fp:
                          for i in fp:
                              w = i.split()
                              # print(x)
                              if x in w or y in w:
                                  print("This account already exists")
                                  signup()

                          else:
                              with open("artist_login_details.txt", "a") as f:
                                  f.write(x)
                                  f.write(" ")
                                  f.write(y)
                                  f.write("\n")

                              mycursor.execute("use art_gallery")
                              sql = "insert into artist(user_name,password,contact_no,gmail,location,about) values(%s,%s,%s,%s,%s,%s)"
                              val = [
                                  (user_name,pwd,mob_no,gmail,location,about),
                              ]
                              mycursor.executemany(sql, val)
                              mydb.commit()
                              print( " you have successfully registered")
                              print("\n")
                              start()
                  else:
                      print("invalid password")
                      print("\n")
                      signup()
            else:
                print("invalid user name")
                print("user name has only contain alphabets")
                print("\n")
                signup()
        else:
            print("invalied mobile number")
            print("\n")
            signup()
    else:
        print("invalid gmail")
        print("\n")
        signup()
    signup()
def login():
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    # print("kindly fill in this form to register")
    global gmail
    global pwd
    gmail = input("Enter gmail: ")
    pwd = input("Enter password: ")

    n=0
    with open(r"artist_login_details.txt", 'r+') as fp:
        w = str(gmail)
        v=str(pwd)
        for i in fp:
            x=i.split()
            # print(x)
            if w in x and v in x:
                n=1
                print( "\n")
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from artist")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1: 'id_no', 2: 'user_name', 3: 'password', 4: 'contact_no', 5: 'gmail',6:'location',7:'about'}
                # print(l)
                dict = {}
                t = 0
                for i in myresult:
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    # print(dict)
                    # print(dict.get("gmail"),dict.get("password"))
                    if dict.get("gmail")==gmail and dict.get("password")==pwd:
                        row = 4
                        for i in range(row):
                            for j in range(1,row):
                                print("||||", end="")
                            if i == 0:
                                print("  ",dict.get("user_name"),end="")
                            if i == 1:
                                print("  ",dict.get("location"),end="")
                            if i == 2:
                                print("  ",dict.get("about"),end="")

                            print()
                        print("   ----------------------------------------", end='')
                        print("\n","ART WORKS FOR SALE")
                        print("   ---------------------------------------- \n", end='')
                    dict = {}
                    t = 0
                break
        else:
                  print( "An error occurred with log in....")
                  print("\n")
                  login()

    mycursor.execute("use art_gallery")
    mycursor.execute("select*from artist_sell")
    myresult = mycursor.fetchall()
    # print(myresult)
    d = {1: 'id_no', 2: 'gmail', 3: 'password', 4: 'painting_name', 5: 'medium', 6: 'size', 7: 'price',
              8: 'art_code', 9: 'sell_or_not', 10: 'user_name'}
    # print(l)
    dict = {}
    t = 0
    n=0
    for i in myresult:
        for x in i:
            # print(x)
            t = t + 1
            dict.setdefault(d.get(t), x)
        # print(dict)

        if dict.get("gmail") == gmail and dict.get("password") == pwd:
            if dict.get('painting_name')!=None:
                n=1
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
                print("                          ",dict.get('sell_or_not'))
                print('\n')
        dict = {}
        t = 0
    print("Enter * button to upload more works ")
    print("enter space butten for back")
    u=input("")
    if u == "*":
        update()
    if u == " ":
        start()



    # x=input("press space and enter button to go home page")
def start():

    while 1:
        print("********** Login System **********")
        print("\n")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        print("\n")
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            x = input("press space and enter button to go home page")
            from frnd import f
            f()
        else:
            print("Wrong Choice!")

start()
