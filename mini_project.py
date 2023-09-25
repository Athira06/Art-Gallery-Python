import mysql.connector

# from sketchpy import library as lib
# import cv2

# mysql-python connecter
mydb = mysql.connector.connect(host='localhost', user='root', password='Artist0-9')
# print(mydb)
from frnd import f
mycursor = mydb.cursor()
def start():
    l=1
    for l in range(0,3):
        choise = int(input("ENTER THE CHOISE:"))
        if choise == 1:
            from search import search
            search()
            f()
            # x=input("press space and enter button to go home page")
        if choise == 2:
            from artist_login_signup import start
            start()
            f()
            choise = int(input("ENTER THE CHOISE:"))
        if choise == 3:
            from cut_signin_login import start
            f()
            choise = int(input("ENTER THE CHOISE:"))
        if choise == 4:
            from drowing import drow
            f()
            choise = int(input("ENTER THE CHOISE:"))
        if choise == 5:
            from compitition import play
            f()
            choise = int(input("ENTER THE CHOISE:"))

start()

