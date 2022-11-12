print("NOTIFY ME APP")
import mysql.connector as py 
import datetime
from plyer import notification

import string
import random
 
# initializing size of string
N = 7
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
 
# print result

while True:
    mydb = py.connect(
        host="localhost",
        user="root",
        passwd="AWSgargatharv2010@gmail.com",
        database = "NotifyMe",
    )
    # print("Date and Time in Integer Format:",int(current_date.strftime("%Y%m%d%H%M%S")))
    mycursor = mydb.cursor()
    check = input("Enter What To Wait Or Add:")
    def createDB(name):
        mycursor.execute(f"CREATE DATABASE {name}")

    def add(h,d,hour,min):
        formula = "INSERT INTO NotifyAdd(heading,description,timeH,timeM,ID) VALUES (%s,%s,%s,%s,%s)"
        
        data = (
            h,
            d,
            hour,
            min,
            random.randint(0,99999),
            
            
        )
        mycursor.execute(formula,data)
        mydb.commit()
    if check == "Wait":
        print("Ok Your Notification Will Occur")

    elif check == "Add":
        print("Ok")
        heading = input("Enter The Heading:")
        desc = input("Enter The Description:")
        timeH = int(input("Enter The Hour in Whole:"))
        timeMin = int(input("Enter The Minute in Whole:"))

        add(heading,desc,timeH,timeMin)
        
    def get ():

        formula2 = "SELECT * FROM NotifyAdd"
        mycursor.execute(formula2)
        myresult = mycursor.fetchall()
        all =[]
        for result in myresult:
            all.append(result)
            

        for i in range(len(all)):
            # print(type(time.strftime("%H")))
            a = all[i]
            
            while True:

                b = datetime.datetime.now()
                
                # if a[2] != time.strftime("%H") and  a[3]!=time.strftime("%M"):
                #     print("A")
                #     b
                # else:
                if a[2] == b.hour and a[3]==b.minute:
                    print("Notify")
                    if __name__=="__main__":
                    
                            notification.notify(
                                title = a[0],
                                message=a[1] ,

                                # displaying time
                                timeout=5
                    )
                    formula = f"DELETE FROM NotifyAdd WHERE ID={a[4]}"
                    mycursor.execute(formula)
                    mydb.commit()
                    break
                else:
                    continue
                # print(a[2] == x.hour and  a[3]!=x.minute)
                #     continue

            
    get()