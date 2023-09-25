import mysql.connector

#mysql-python connecter
mydb=mysql.connector.connect(host='localhost',user='root',password='Artist0-9')
# print(mydb)
mycursor=mydb.cursor()
# mycursor.execute("use art_gallary")
# mycursor.execute("select*from artist")
# myresult = mycursor.fetchall()
# print(myresult)
def search():
    A = str(input(">>>>>>>>>>>"))
    s=A.upper()
    mycursor.execute("use art_gallery")
    mycursor.execute("select*from artist_sell")
    myresult = mycursor.fetchall()
    # print(myresult)
    d={1:'id_no',2:'gmail',3:'password',4:'painting_name',5:'medium',6:'size',7:'price',8:'art_code',9:'sell_or_not',10:'user_name'}
    # print(l)
    dict={}
    t=0
    none = 1
    for i in myresult:
        for x in i:
            # print(x)
            t=t+1
            dict.setdefault(d.get(t),x)
        # print(dict)
        c=dict.get('painting_name')
        if c!=None:
            p=c.upper()
            if s==p or s in p :
                none=0
                row = 6
                for i in range(row):
                    for j in range(row):
                        print("****", end="")
                    if i==0:
                        print("  ",c,end="")
                    if i==1:
                        print("   By",dict.get('user_name'),end='')
                    if i==2:
                        print("   ----------------------------------------",end='')
                    if i==3:
                        print("     Size           Medium         Art Code",end='')
                    if i == 4:
                         print("  ",dict.get('size')," ",dict.get('medium')," ",dict.get('art_code'), end='')
                    if i==5:
                        print("   ----------------------------------------",end='')
                    print()
                print("                           Rs ",dict.get('price'),"                    ","Buy Now")
                print("                          ",dict.get('sell_or_not'))
                print("                           Delivery time: 5-7 bussiness days")
                print('\n')
            dict={}
            t=0
    x = input("press space and enter button to go home page")
    from frnd import f
    f()
    if none==1:
        print("No Records Found")
        x = input("press space and enter button to go home page")
        from frnd import f
        f()

search()