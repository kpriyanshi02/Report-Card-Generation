# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:27:09 2020

@author: dell
"""
#IMPORTING NECESSARY FILES AND PACKAGES
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="priyanshi",database="records")
if mycon.is_connected():
    print("Connection Successful")
else:
    print("Connection Failed")
cursor=mycon.cursor()
    
    
#LOGIN ID AND PASSWORD
userid=18106632
passwd="loginnow"


#FUNCTION DISPLAY_RECORDS
def display_records():
    Roll_No=int(input("""Enter student's roll number whose data you want to display
                      (from 23670608 to 23670617):"""))
    string="select * from marksheet where Sr_No=%s" %(Roll_No,)
    cursor.execute(string)
    data=cursor.fetchall()
    print(data)
    

#FUNCTION INSERT_RECORDS
def insert_records():
    Roll_No=int(input("""Enter student's roll number whose data you want to insert
                      ('data already inserted from 23670608 to 23670617') please:"""))
    Name=input("Enter student's name please:")
    Physics=int(input("Enter marks in Physics(out of 100):"))
    Chemistry=int(input("Enter marks in Chemistry(out of 100):"))
    Maths=int(input("Enter marks in Maths(out of 100):"))
    English=int(input("Enter marks in English(out of 100):"))
    Comp_Science=int(input("Enter marks in Comp_Science(out of 100):"))
    Phy_Edu=int(input("Enter marks in Phy_Edu(out of 100):"))
    string="""insert into marksheet(Sr_No,Name,Physics,Chemistry,Maths,English,Comp_Science,Phy_Edu)
              values ({},'{}',{},{},{},{},{},{})""".format(Roll_No,Name,Physics,Chemistry,Maths,English,Comp_Science,Phy_Edu)
    cursor.execute(string)
    string="select * from marksheet where Sr_No=%s" %(Roll_No,)
    cursor.execute(string)
    data=cursor.fetchall()
    print(data)    
    mycon.commit()
    
    
#FUNCTION DELETE_RECORDS 
def delete_records():
    Roll_No=int(input("""Enter student's roll number whose data you want to delete
                      (from 23670608 to 23670617):"""))
    string="delete from marksheet where Sr_No=%s" %(Roll_No,)
    cursor.execute(string)
    mycon.commit()
    
    
#FUNCTION UPDATE_RECORDS
def update_records():
    Roll_No=int(input("""Enter student's roll number whose data you want to update
                      (from 23670608 to 23670617):"""))
    subject=input("""Enter which subject marks you want to change
                  (physics/chemistry/maths/english/com_science/phy_edu:""")
    marks=int(input("Enter marks of student (out of 100):"))
    change=(marks,Roll_No)
    if subject=="physics":        
        string="update marksheet set Physics=%s where Sr_no=%s"
        cursor.execute(string,change)
    elif subject=="chemistry":        
        string="update marksheet set Chemistry=%s where Sr_no=%s"
        cursor.execute(string,change)
    elif subject=="maths":        
        string="update marksheet set Maths=%s where Sr_no=%s"
        cursor.execute(string,change)
    elif subject=="english":        
        string="update marksheet set English=%s where Sr_no=%s"
        cursor.execute(string,change)
    elif subject=="comp_science":        
        string="update marksheet set Comp_Science=%s where Sr_no=%s"
        cursor.execute(string,change)
    else:
        string="update marksheet set Phy_Edu=%s where Sr_no=%s"
        cursor.execute(string,change)
    mycon.commit()
    

#ACTION TO BE PERFORMED BY KEYS:
def choice():
    choice1="yes"
    while choice1=="yes":        
        key=int(input("Enter key of your choice 1/2/3/4/5/6 :"))
        if key==1:
            display_records()
        elif key==2:
            insert_records()
        elif key==3:
            delete_records()
        elif key==4:
            update_records()
        elif key==5:
            percent()
        else:
            break
        choice1=input("Do you want to perform any other task(yes/no):" )
        if choice1=="yes":
            menu()
        else:
            break
        

#FUNCTION MENU
def menu():
    print("PRESS FOLLOWING KEYS ACCORDING TO YOUR CHOICE.")
    print("1.DISPLAY STUDENT RECORDS")
    print("2.INSERT NEW RECORDS")
    print("3.DELETE RECORDS")
    print("4.UPDATE RECORDS")
    print("5.CALCULATE PERCENTAGE")
    print("6.EXIT")         
    choice()
    
        
             
#FUNCTION PERCENT (CALCULATING AGGREGATE PERCENTAGE OF STUDENT):
def percent():
    choice="yes"
    while choice=="yes":
        Roll_No=int(input("""Enter student's roll number whose percentage you want to calculate
                          (from 23670608 to 2367617):"""))
        string="select * from marksheet where Sr_No=%s"%(Roll_No,)
        cursor.execute(string)
        data=cursor.fetchall()
        print(data)
        x=0
        count=0
        y=len(data[0])
        z=data[0][2:y]
        #print(y,z)
        for i in z:
            if i==None:
                continue
            x=x+i
            count=count+1
        percentage=(x/(count*100))*100
        print("Student's percentage is", percentage,"%")
        choice=input("Do you want to display any other student's percentage(yes/no):")
    else:   
        exit()        

        
#PRE INSERTING DATA INTO TABLE:MARKSHEET
def preinsert_data():
    Row1="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670608,"AMIT SHUKLA",88,86,89,82,80,90)
    cursor.execute(Row1)
    Row2="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670609,"PRIYA TIWARI",86,86,83,80,87,92)
    cursor.execute(Row2)
    Row3="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670610,"VISHWAJEET SINGH PAL",84,85,81,82,86,93)
    cursor.execute(Row3)
    Row4="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670611,"ABHISEKH TIWARI",81,85,87,80,82,91)
    cursor.execute(Row4)
    Row5="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670612,"SATYAM KUMAR",83,85,87,87,90,94)
    cursor.execute(Row5)
    Row6="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670613,"ADITYA DWIVEDI",84,85,87,81,87,88)
    cursor.execute(Row6)
    Row7="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670614,"DIVYANSHU CHOWDHARY",83,82,81,82,83,86)
    cursor.execute(Row7)
    Row8="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670615,"SUMIT PANDEY",88,81,83,82,89,85)
    cursor.execute(Row8)
    Row9="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science)
        values({},'{}',{},{},{},{},{})""".format(23670616,"PRIYANSHI KUSHWAHA",99,98,100,96,100)
    cursor.execute(Row9)
    Row10="""insert into marksheet(Sr_No, Name, Physics,Chemistry,Maths,English,Comp_Science, Phy_Edu)
        values({},'{}',{},{},{},{},{},{})""".format(23670617,"ANKUR TALUKDAR",88,89,89,90,90,92)
    cursor.execute(Row10)
    mycon.commit()
    
    
#CALLING PREINSERT_DATA:
#preinsert_data()
   
    
#MAIN FUNCTION LOGIN
def login():
    Userid=int(input("Enter a valid userid please:" ))
    Passwd=input("Enter password please:")
    if (Userid==userid and Passwd==passwd):
        print("WELCOME TO REPORT CARD GENERATION PROGRAM!!!")
        print("MENU DRIVEN PROGRAM")
        menu()
        print("THANKS FOR USING STUDENT REPORT CARD GENERATION PROGRAM!!!")                
    else:
        print("Retry")
        
        
#CALLING FUNTION LOGIN
login()
































