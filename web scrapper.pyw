from bs4 import BeautifulSoup
import requests
from tkinter import *


def get_URL(url):
    global html
    html = requests.get(url)

def get_ID(id,html):
    global results
    s = BeautifulSoup(html.content,'html.parser')
    results = s.find(id = id)

def get_CLASS(results,type,classVar):
    global country_title
    country_title = results.find_all(type,class_=classVar)

def get_RESULT(country_title):
    for country in country_title:
        with open("scrapper.txt","a") as f:
            f.write(country.text + "\n")

##########tkinter functions##############
def url_button_func():
    url = url_entry.get()            
    get_URL(url)

def id_button_func():
    id = label_id_entry.get()
    get_ID(id,html)

def class_button_func():
    classVar = label_class_entry.get()
    get_CLASS(results,type,classVar)

def type_button_func():
    global type
    type = label_type_entry.get()

def get_result_button_func():
    get_RESULT(country_title)
##########################################


screen = Tk(className = " WEB Scrapper")
screen.geometry("600x270")

url_entry = Entry(width = 34,font="Verdana 14 bold")
url_entry.place(x=30,y=30)

url_button = Button(width=4,font="Verdana 14 bold",text="Done",command = url_button_func)
url_button.place(x=530,y=20)

label_id = Label(text = "Write the id",font="Verdana 14 bold")
label_id.place(x=50,y=100)

label_id_entry = Entry(font="Verdana 14 bold",width=5)
label_id_entry.place(x=50,y=130)

label_entry_button = Button(width=4,font="Verdana 14 bold",text="Done",command=id_button_func,height=1)
label_entry_button.place(x=140,y=127)

label_class = Label(text = "Write the class",font="Verdana 14 bold")
label_class.place(x=400,y=100)

label_class_entry = Entry(font="Verdana 14 bold",width=5)
label_class_entry.place(x=400,y=130)

label_class_entry_button = Button(width=4,font="Verdana 14 bold",text="Done",command=class_button_func,height=1)
label_class_entry_button.place(x=490,y=127)

label_type = Label(text = "Write the type",font="Verdana 14 bold")
label_type.place(x=220,y=100)

label_type_entry = Entry(font="Verdana 14 bold",width=5)
label_type_entry.place(x=230,y=130)

label_type_entry_button = Button(width=4,font="Verdana 14 bold",text="Done",command=type_button_func,height=1)
label_type_entry_button.place(x=320,y=127)

get_result_button = Button(text = "Scrape",font="Verdana 14 bold",command = get_result_button_func)
get_result_button.place(x=250,y=200)


screen.mainloop()