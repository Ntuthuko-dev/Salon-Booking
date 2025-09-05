#This project is about booking an appoinment in a solo salon
#I will need a database,add a client, delete a client and update the client
#A chart to display monthly constumers
#Input for name,surame,number,email and hair-Style Time and date they want to visit the salon
#Responses to the client
#Display The client user base
#Save the data to a file like a document

import sqlite3
import string
import matplotlib.pyplot as plt
from datetime import datetime

conn=sqlite3.connect("client_database.db",detect_types=sqlite3.PARSE_DECLTYPES)
cursor=conn.cursor();

create_table_sql="""

CREATE TABLE IF NOT EXISTS clients_detail(
        client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NULL,
        email TEXT NULL,
        gender TEXT NULL,
        phone_number TEXT NULL,
        hair_style TEXT NULL,
        booked_time TEXT NULL,
        day_to_visit TEXT NULL,
        time_visit TEXT NULL

);
"""
cursor.execute(create_table_sql)
#INSERTING USERS TO THE DATABASE CODE
print("============================================================")

print("WELCOME TO THANDO'S & MPUMELELO SALON")
print("============================================================")
name=input("Enter name: ");
last_name=input("Enter last Name: ");
email=input("Enter your Email Address/Gmail: ").lower();
gender=input("Enter Gender: ").lower();
phone_number=input("Enter Phone Number: ");
hair_style=input("Enter hair style you want: ").lower();
booked_time=datetime.now();
day_to_visit=input("Enter the day to come to Salon: ").lower();
print("\nPLEASE NOTE THAT THE Salon OPENS at 8h00am and CLOSES at 18h00pm\n","8-11 is AM 12-18 is PM\n");
time_visit=input("Enter Time You wish to come by Please be mindful: ");

insert_query="""

INSERT INTO clients_detail(name,last_name,email,gender,phone_number,hair_style,booked_time,day_to_visit,time_visit) VALUES(?,?,?,?,?,?,?,?,?)

"""

input_values=(name,last_name,email,gender,phone_number,hair_style,booked_time,day_to_visit,time_visit);

cursor.execute(insert_query,input_values);
conn.commit();

display_Database = """SELECT * FROM clients_detail;"""
cursor.execute(display_Database)
rows=cursor.fetchall()


with open("bookings.txt","a") as f:
    for row in rows:
        data_strings=''.join(map(str,row))
        print(row,"\n")
        f.write(data_strings+"\n")

f=open("bookings.txt","r")
print(f.read(),"\n");

print("THANK YOU FOR USING OUR SERVICE ")

#Summing  Gender'

#male_average="""SELECT SUM(gender) FROM clients_detail WHERE gender='male'"""
#cursor.execute(male_average)
#male=cursor.fetchone()[0];
#female_average="""SELECT SUM(gender) FROM clients_detail WHERE gender='female'"""
#cursor.execute(female_average)
#female=cursor.fetchone()[0];
#regular_visitors=["Male","Female"];
#average_gender=[male,female];

#plt.bar(regular_visitors,average_gender)
#plt.xlabel(regular_visitors);
#plt.ylabel(average_gender);
#plt.title("Regular Visitors Per WEEK:")
#plt.show();
           


conn.close()