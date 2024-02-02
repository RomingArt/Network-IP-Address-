# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:06:22 2023

Programmer: Saul Ascencio
Professor: Benoit
Class: Informatics 201
Section: 10
Semester Spring 2023

"""


from tkinter import *
import sqlite3 as sq
from tkinter import messagebox as msg
import socket
import time 


"""Begining of the program """
root=Tk() #TO CREATE AND PASS WINDOW TO A FEW PARAMETERS
root.geometry('457x370') #DEFINE WINDOW SIZE
root.title('Webpage Scanner') #SIMPLE TITLE ON TOP


"""Text box area""" 
txt_web_name = StringVar() #YOU NEED TO TEST HERE  
ent_w_name = Entry(root, width=30, font=('none 12 bold'), textvar = txt_web_name)
ent_w_name.pack()
ent_w_name.place(x=170, y=80)


"""Create table even if it doesn't exist """
db = sq.connect('Networks.db') 
point = db.cursor() 
point.execute("CREATE TABLE IF NOT EXISTS Network_List(Network_Name TEXT, IP_Address TEXT, Date TEXT)")
db.commit()



"""Create a function"""
def ld_info():
    if "www" in txt_web_name.get()[0:3]:
        apnd()
        #msg.showinfo(title="RIGHT",message ="You entered the correct informaiton!")
        # WORKS print(socket.gethostbyname(txt_web_name.get())) 
        #txt_web_name.set("")
    else:
        msg.showwarning(title="Warning",message="Email needs to start with WWW") 
        txt_web_name.set("Please enter a new website ")
        #time.sleep(4)
        txt_web_name.set("")


"""Database connection"""
def apnd():
    ntwork_name = txt_web_name.get()
    hst_name = socket.gethostbyname(txt_web_name.get())

    conct = sq.connect('Networks.db')
    with conct:
        point = conct.cursor()
        point.execute('INSERT INTO Network_List(Network_Name,IP_Address,Date) VALUES (?,?,?)', (ntwork_name,hst_name,time.strftime('%m-%d-%Y %I:%M:%S %p')))  
        db.close()
        txt_web_name.set('')



"""Button details"""
btn_add = Button(root, padx=25, pady=5, text='Analyze', command=ld_info, font= ('none 12 bold')) 
btn_add.pack()
btn_add.place(x= 25, y= 70)
btn_add.config(relief='raised') #BUTTON INFO NEEDS TO BE ADDED HERE OR FUNCTIO NOT RECOGNIZED


root.mainloop() #This allows the window to show until the program is closed

