#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 01:59:04 2018

@author: Aryman
"""
# Simple enough, just import everything from tkinter.
from tkinter import *

# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)  
        #creatin the frames
        self.left = Frame(master, width=800, height=720,bg='tomato1')
        self.left.pack(fill=BOTH)
        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Blood Bank Management System")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH)
        
        #heading
        self.heading = Label(self.left, text="मदद", font=("Mangal 40 bold"),fg='red2', bg='tomato1') 
        self.heading.place(x=0, y=0)
        self.heading = Label(self.left, text="- Blood on Demand", font=("Mistral 15 bold"),fg='red2', bg='tomato1') 
        self.heading.place(x=100, y=38)
        
        #Button for Registration 
        self.reg = Button(self.left, text="Registration", width=25, height=2, bg='firebrick1')
        self.reg.place(x=0, y=65)
        
        #Button for Request Blood
        self.req = Button(self.left, text="Request Blood", width=25, height=2, bg='firebrick1')
        self.req.place(x=228, y=65)
        
        #Button for Why donate?
        self.whyd = Button(self.left, text="Why Donate Blood?", width=25, height=2, bg='firebrick1')
        self.whyd.place(x=456, y=65)
        
        #Button for Tips of donatition
        self.tip = Button(self.left, text="Tips on donating", width=25, height=2, bg='firebrick1')
        self.tip.place(x=684, y=65)
        
        #Button for Diagnose Center
        self.dc = Button(self.left, text="Diagnosis Center", width=25, height=2, bg='firebrick1')
        self.dc.place(x=912, y=65)
        
        #Button for Contact Us
        self.cu = Button(self.left, text="Contact Us", width=25, height=2, bg='firebrick1')
        self.cu.place(x=1140, y=65)
        
        #Title Of Entryies
        self.heading = Label(self.left, text="FIND BLOOD", font=("arial 25 bold"),fg='black', bg='tomato1') 
        self.heading.place(x=220, y=130)
        
         #Blood Group
        self.bloodgrp = Label(self.left, text="Blood Group", font=('arial 15 bold'), fg='black', bg='tomato1')
        self.bloodgrp.place(x=80, y=200)
        
        #Donor country
        self.country = Label(self.left, text="Country", font=('arial 15 bold'), fg='black', bg='tomato1')
        self.country.place(x=80, y=240)
        
        #Donor State
        self.state = Label(self.left, text="State", font=('arial 15 bold'), fg='black', bg='tomato1')
        self.state.place(x=80, y=280)
        
        #Donor district
        self.district = Label(self.left, text="District", font=('arial 15 bold'), fg='black', bg='tomato1')
        self.district.place(x=80, y=320)
        
        #Donor city
        self.city = Label(self.left, text="City", font=('arial 15 bold'), fg='black', bg='tomato1')
        self.city.place(x=80, y=360)
        
        #Entries for all the fields
        self.bloodgrp_ent = Entry(self.left, width=30)
        self.bloodgrp_ent.place(x=250, y=200)
        
        self.country_ent = Entry(self.left, width=30)
        self.country_ent.place(x=250, y=240)
        
        self.state_ent = Entry(self.left, width=30)
        self.state_ent.place(x=250, y=280)
        
        self.district_ent = Entry(self.left, width=30)
        self.district_ent.place(x=250, y=320)
        
        self.city_ent = Entry(self.left, width=30)
        self.city_ent.place(x=250, y=360)
        
        #Button for Submit
        self.submit = Button(self.left, text="SUBMIT", width=20, height=2, bg='firebrick1')
        self.submit.place(x=280, y=400)
        

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
#creating the object
root = Tk()
#title of App
root.title("Blood Bank Management System")
b = Window(root)

#resolution of the window
root.geometry('1362x720+0+0')

#preventing he resize feature
root.resizable(True, True)

#end the loop
root.mainloop()
