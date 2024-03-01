import sqlite3
import random
import re
import time 

# DataBase class to controll the database
class DataBase:
    def __init__(self) :
        self.db = sqlite3.connect("logins.db")
        self.cr = self.db.cursor()

    # method to create database if not exist
        
    def CreateDatabase(self):
    
        # Create Tables in dataBase
        self.cr.execute("CREATE TABLE if not exists User(user_id integer,user_name text,password text)")

    # method that Inserting Data Come from User

    def InsertingDataBase(self,data):

        self.cr.execute(f"insert into User values({data[0]},'{data[1]}','{data[2]}')")

        # saving process
        self.db.commit()
    
    #  Method to delete and User from database
    def deletingData(self):
        deleted_accout = input("Enter your Email to delete it\n")

        email_pass = input("Enter your password\n")
        try:

            if email_pass == self.cr.execute(f"SELECT password from User where user_name = '{deleted_accout}'").fetchone()[0] :
                self.cr.execute(f"delete from User where user_name ='{deleted_accout}'")
                
                print("Your accout deleted")


            self.db.commit()

        except:
            print("Invalid Input or the data you entered not exist")

    #  Method to update data from user Username or password
            
    def UpdataingData(self):
        dataUpdated = input("What do want to update User_name or password\n")

        if dataUpdated == 'User_name' :

            try:
                old_userNm = input("Enter your old User_name\n")
                
                new_userNm = input("Enter the new UserName\n")
                
                self.cr.execute(f"update User set user_name = '{new_userNm}' where user_name ='{old_userNm}' ")
                
                self.db.commit()
                
                print("Your Data Has been updated\n")

            except :
                print("Invalid Input or the data you entered not exist")

        elif dataUpdated == 'password' :
            try:
                
                userName = input("Enter your Email\n")
                
                old_pass = input("Enter your old password\n")
                
                new_pass = input("Enter the new password\n")
                
                self.cr.execute(f"update User set password = '{new_pass}' where user_name = '{userName}' ")
                
                self.db.commit()
                
                print("Your Data Has been updated")

            except:
                print("Invalid Input or the data you entered not exist")

        else:
            
            print("invalid input")
            self.UpdataingData()


user_id = random.randint(1,99)

Existing_Email = input("Do you have an email ")

Existing_Email.lower()

if Existing_Email == 'yes' :
    
    user_name = input('Enter Your login account \n')
    
    password = input('Enter your Password \n')

    Exciting_db_accoubt = DataBase()

    Exciting_db_accoubt.UpdataingData()

    Exciting_db_accoubt.deletingData()
    

elif Existing_Email == 'no':
    
    Create_account = input("Sign Up with an account \n")

    Sigh_up_pass = input("Enter your password\n")

    Create_db = DataBase()

    data = [user_id,Create_account,Sigh_up_pass]

    Create_db.CreateDatabase()
    
    Create_db.InsertingDataBase(data)

    Create_db.UpdataingData()
    
    Create_db.deletingData()

else :
    print("Invalid Input")
