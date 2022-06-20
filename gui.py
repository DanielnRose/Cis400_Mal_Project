from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import Recommendations
import MAL_Cookbook
import Data_Visualization
client_id = "d1ba6c8f42d9abdc2aa2d84fb61702e5"

#bool newUser = false;

window = tk.Tk() 
window.geometry("720x480")
window.title("Login")
newUser = 0
lst = []


data_set = {}
##json_dump = json. dumps(data_set)
##json_object = json. loads(json_dump)
##print(json_object["key1"])
##
##data_set["key3"] = [1,2,3,5]
##json_dump = json. dumps(data_set)
##json_object = json. loads(json_dump)
##print(json_object["key3"])

#functions for pressing the buttons
def yes():
    global newUser
    newUser=1;
    global lst
    lst.append("New User")
    print (newUser)
    return newUser;
def no():
    global newUser
    newUser = 0;
    global lst
    lst.append("Existing User")
    return newUser;
def username():
    global newUser
    username = u1.get();


    data_set["newUser"] = newUser
    data_set["username"] = username
    json_dump = json. dumps(data_set)
    json_object = json. loads(json_dump)
    print (json_object)
    window.destroy()

    if (newUser == 1):
        win2()
    if (newUser == 0):
        win3(json_object)
    
    return username


    

u1 = Entry(window, width = 12)
u1.grid(row=2, column=2)
l3 = tk.Label(window, text='Username: ', width=8 )
l3.grid(row=2,column=1)

l4 = tk.Label(window, text='Are you a new user? ', width=16 )
l4.grid(row=3,column=1)

b1 = tk.Button(window, text='Yes', command= yes )
b1.grid(row=4,column=1)

b2 = tk.Button(window, text='No', command= no )
b2.grid(row=4,column=2)

b3 = tk.Button(window, text='Login', command=username )
b3.grid(row=8,column=1)



x=0
y=0
z=0
userRec=0
def win2():
    def complete():
        #data_set["top5"] = [options.get(),options2.get(),options3.get(),options4.get(),options4.get()]
        #json_dump = json. dumps(data_set)
        #json_object = json. loads(json_dump)
        #data_set["Weights"] = [("Year",x),("Genre",y),("Length",z)("UserRecommended", userRec)]
        #json_dump = json. dumps(data_set)
        #json_object = json. loads(json_dump)
        genres = [options.get(),options2.get(),options3.get(),options4.get(),options5.get()]
        Recommendations.getRecommendationsNewUser(genres, x/100, y/100, userRec/100, z/100)
        #window2.destroy()
        #win3(json_object)
    window2 = tk.Tk() 
    window2.geometry("720x480")
    window2.title("New User")


    options = tk.StringVar(window2)
    options.set("Select")
    options2 = tk.StringVar(window2)
    options2.set("Select")
    options3 = tk.StringVar(window2)
    options3.set("Select")
    options4 = tk.StringVar(window2)
    options4.set("Select")
    options5 = tk.StringVar(window2)
    options5.set("Select")


    #Labels for the ui
    l5 = tk.Label(window2, text='Select your top 5 genres: ', width=20 )
    l5.grid(row=2,column=1)

    l5 = tk.Label(window2, text='#1', width=5 )
    l5.grid(row=3,column=1)

    l5 = tk.Label(window2, text='#2', width=5 )
    l5.grid(row=4,column=1)
    l5 = tk.Label(window2, text='#3', width=5 )
    l5.grid(row=5,column=1)
    l5 = tk.Label(window2, text='#4', width=5 )
    l5.grid(row=3,column=4)
    l5 = tk.Label(window2, text='#5', width=5 )
    l5.grid(row=4,column=4)

    om1 =tk.OptionMenu(window2, options, "Action","Adventure", "Comedy", "Drama","Fantasy","Horror","Mystery","Romance","Slice of Life","Sci-Fi","Sports")
    om1.grid(row=3,column=2)

    om2 =tk.OptionMenu(window2, options2, "Action","Adventure", "Comedy", "Drama","Fantasy","Horror","Mystery","Romance","Slice of Life","Sci-Fi","Sports")
    om2.grid(row=4,column=2)
    om3 =tk.OptionMenu(window2, options3, "Action","Adventure", "Comedy", "Drama","Fantasy","Horror","Mystery","Romance","Slice of Life","Sci-Fi","Sports")
    om3.grid(row=5,column=2)

    om4 =tk.OptionMenu(window2, options4, "Action","Adventure", "Comedy", "Drama","Fantasy","Horror","Mystery","Romance","Slice of Life","Sci-Fi","Sports")
    om4.grid(row=3,column=5)
    om5 =tk.OptionMenu(window2, options5, "Action","Adventure", "Comedy", "Drama","Fantasy","Horror","Mystery","Romance","Slice of Life","Sci-Fi","Sports")
    om5.grid(row=4,column=5)


    my_text = str(x)
    #Functions that happen when you hit the plus and minus buttons
    def plus():
        global x
        print (x);
        global y
        global z
        global userRec
        if (x >= 0):
            if ((x+y+z+userRec) <100):
                x = x+5
                global my_text
                u5.config(text = str(x))

    def minus():
        global x
        global y
        global z
        global userRec
        if (x >= 5):
            if ((x+y+z+userRec) <=100):
                x = x-5
                global my_text
                u5.config(text = str(x))
     

    my_text2 = str(y)

    def plus2():
        global x
        global y
        global z
        global userRec
        if (y >= 0):
            if ((x+y+z+userRec) <100):
                y = y+5
                global my_text2
                u6.config(text = str(y))

    def minus2():
        global x
        global y
        global z
        global userRec
        if (y >= 5):
            if ((x+y+z+userRec) <=100):
                y = y-5
                global my_text2
                u6.config(text = str(y))
     

    my_text3 = str(z)

    def plus3():
        global x
        global y
        global z
        global userRec
        if (z >= 0):
            if ((x+y+z+userRec) <100):
                z = z+5
                global my_text3
                u7.config(text = str(z))

    my_text4 = str(userRec)

    def minus3():
        global x
        global y
        global z
        global userRec
        if (z >= 5):
            if ((x+y+z+userRec) <=100):
                z = z-5
                global my_text3
                u7.config(text = str(z))

    def plus4():
        global x
        global y
        global z
        global userRec
        if (z >= 0):
            if ((x+y+z+userRec) <100):
                userRec = userRec+5
                global my_text4
                u8.config(text = str(userRec))

    def minus4():
        global x
        global y
        global z
        global userRec
        if (userRec >= 5):
            if ((x+y+z+userRec) <=100):
                userRec = userRec-5
                global my_text4
                u8.config(text = str(userRec))



    l5 = tk.Label(window2, text='Weights: ', width=10 ).grid(row=6,column=1)
    l5 = tk.Label(window2, text='Year', width=10 ).grid(row=7,column=1)
    l5 = tk.Label(window2, text='Genre', width=10 ).grid(row=8,column=1)
    l5 = tk.Label(window2, text='Length', width=10 ).grid(row=9,column=1)
    l5 = tk.Label(window2, text='User Rec', width=10 ).grid(row=7,column=7)

    b4 = tk.Button(window2, text='-', command=minus ).grid(row=7,column=2)
    b4 = tk.Button(window2, text='+', command=plus ).grid(row=7,column=4)
    u5 = Label(window2, text='0', width = 6)
    u5.grid(row=7, column=3)

    b4 = tk.Button(window2, text='-', command=minus2 ).grid(row=8,column=2)
    b4 = tk.Button(window2, text='+', command=plus2 ).grid(row=8,column=4)
    u6 = Label(window2, text='0', width = 6)
    u6.grid(row=8, column=3)

    b4 = tk.Button(window2, text='-', command=minus3 ).grid(row=9,column=2)
    b4 = tk.Button(window2, text='+', command=plus3 ).grid(row=9,column=4)
    u7 = Label(window2, text='0', width = 6)
    u7.grid(row=9, column=3)

    b4 = tk.Button(window2, text='-', command=minus4 ).grid(row=7,column=8)
    b4 = tk.Button(window2, text='+', command=plus4 ).grid(row=7,column=10)
    u8 = Label(window2, text='0', width = 6)
    u8.grid(row=7, column=9)


    b1 = tk.Button(window2, text='Complete', command= complete )
    b1.grid(row=10,column=1)


def win3(json_object):
    window3 = tk.Tk() 
    window3.geometry("720x480")
    window3.title("Main")

    options4 = tk.StringVar(window3)
    options4.set("Select")

    def stop():
        window3.destroy()
        #print(json_object)
        #return (json_object)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(json_object, f, ensure_ascii=False, indent=4)

    my_text = str(x)

    def plus():
        global x
        global y
        global z
        global userRec
        if (x >= 0):
            if ((x+y+z+userRec) <100):
                x = x+5
                global my_text
                u5.config(text = str(x))

    def minus():
        global x
        global y
        global z
        global userRec
        if (x >= 5):
            if ((x+y+z+userRec) <=100):
                x = x-5
                global my_text
                u5.config(text = str(x))
     

    my_text2 = str(y)

    def plus2():
        global x
        global y
        global z
        global userRec
        if (y >= 0):
            if ((x+y+z+userRec) <100):
                y = y+5
                global my_text2
                u6.config(text = str(y))

    def minus2():
        global x
        global y
        global z
        global userRec
        if (y >= 5):
            if ((x+y+z+userRec) <=100):
                y = y-5
                global my_text2
                u6.config(text = str(y))
     

    my_text3 = str(z)

    def plus3():
        global x
        global y
        global z
        global userRec
        if (z >= 0):
            if ((x+y+z+userRec) <100):
                z = z+5
                global my_text3
                u7.config(text = str(z))

    def minus3():
        global x
        global y
        global z
        global userRec
        if (z >= 5):
            if ((x+y+z+userRec) <=100):
                z = z-5
                global my_text3
                u7.config(text = str(z))

    my_text4 = str(userRec)

    def plus4():
        global x
        global y
        global z
        global userRec
        if (z >= 0):
            if ((x+y+z+userRec) <100):
                userRec = userRec+5
                global my_text4
                u8.config(text = str(userRec))

    def minus4():
        global x
        global y
        global z
        global userRec
        if (z >= 5):
            if ((x+y+z+userRec) <=100):
                userRec = userRec-5
                global my_text4
                u8.config(text = str(userRec))

    blockList = [];
    #This function runs when you hit the finish button
    def finish():
        data_set["Blocked"] = [blockList]
        json_dump = json. dumps(data_set)
        json_object = json. loads(json_dump)
        print(json_object)
        recs = Recommendations.getRecommendations(data_set["username"], yearw=x/100, genrew = y/100, userRecSW = userRec/100, lengthw = z/100)

    def add():
        #global blockList
        blockList.append(options4.get())
        u10.config(text = blockList)
        print(blockList)

    def remove():
        for item in blockList:
            if options4.get() == item:
                blockList.remove(item)
        u10.config(text = blockList)
        print(blockList)

    #Simple labels and buttons for the weights
    l5 = tk.Label(window3, text='Weights: ', width=10 ).grid(row=1,column=1)
    l5 = tk.Label(window3, text='Year', width=10 ).grid(row=2,column=1)
    l5 = tk.Label(window3, text='Genre', width=10 ).grid(row=3,column=1)
    l5 = tk.Label(window3, text='User Rec', width=10 ).grid(row=2,column=5)
    l5 = tk.Label(window3, text='Length', width=10 ).grid(row=4,column=1)

    b4 = tk.Button(window3, text='-', command=minus ).grid(row=2,column=2)
    b4 = tk.Button(window3, text='+', command=plus ).grid(row=2,column=4)
    u5 = Label(window3, text=my_text, width = 6)
    u5.grid(row=2, column=3)

    b4 = tk.Button(window3, text='-', command=minus2 ).grid(row=3,column=2)
    b4 = tk.Button(window3, text='+', command=plus2 ).grid(row=3,column=4)
    u6 = Label(window3, text=my_text2, width = 6)
    u6.grid(row=3, column=3)

    b4 = tk.Button(window3, text='-', command=minus3 ).grid(row=4,column=2)
    b4 = tk.Button(window3, text='+', command=plus3 ).grid(row=4,column=4)
    u7 = Label(window3, text=my_text3, width = 6)
    u7.grid(row=4, column=3)

    b4 = tk.Button(window3, text='-', command=minus4 ).grid(row=2,column=6)
    b4 = tk.Button(window3, text='+', command=plus4 ).grid(row=2,column=10)
    u8 = Label(window3, text=my_text4, width = 6)
    u8.grid(row=2, column=7)

    u15 = Label(window3, text="Block List:", width = 12)
    u15.grid(row=5, column=1)

    u10 = Label(window3, text=blockList, width = 20)
    u10.grid(row=6, column=5)


    om5 =tk.OptionMenu(window3, options4, "Action","Adventure", "Comedy", "Sci-Fi")
    om5.grid(row=6,column=1)
    b5 = tk.Button(window3, text="Add", command=add ).grid(row=6,column=2)

    
    b5 = tk.Button(window3, text="Remove", command=remove ).grid(row=6,column=3)

    
    b1 = tk.Button(window3, text='Finish', command= finish )
    b1.grid(row=6,column=4)
    
    
    b1 = tk.Button(window3, text='Quit', command= stop )
    b1.grid(row=7,column=1)




    window3.mainloop()
