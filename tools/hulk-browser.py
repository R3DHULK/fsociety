# importing webbrowser module
import webbrowser
# importing all files from tkinter module
from tkinter import *
from tkinter import ttk

# creating root
root = Tk()
# setting GUI title
root.title("HULK-Browser")
#set window color
root.configure(bg='green')
# setting GUI geometry
root.geometry("628x380")
# set maximum window size value
root.maxsize(628, 380)

name = Label(root, text = "Search : ",font="LUCIDA 16 bold", background="pink").place(x = 50,y = 195) 

# function to open linkedin in browser
def linkedin():
    webbrowser.open("www.linkedin.com")
# function to open facebook in browser
def facebook():
    webbrowser.open("www.facebook.com")
# function to open twitter in browser
def twitter():
    webbrowser.open("www.twitter.com")
# function to open youtube in browser
def youtube():
    webbrowser.open("www.youtube.com")
# function to open whatsapp web in browser
def whatsappweb():
    webbrowser.open("web.whatsapp.com")
# function to open instagram in browser
def instagram():
    webbrowser.open("www.instagram.com")
# function to open gmail in browser
def gmail():
    webbrowser.open("www.gmail.com")
def hotstar():
    webbroser.open("www.hotstar.com")
def search():
    
    if(var2.get()==1):
        webbrowser.open("https://www.google.com/search?q="+Term.get(),new=2)
    if(var3.get()==1):
        webbrowser.open("https://www.youtube.com/results?search_query="+Term.get(),new=2)
    if(var4.get()==1):
        webbrowser.open("https://www.imdb.com/find?ref_=nv_sr_fn&q="+Term.get()+"&s=all",new=2)

Label(root, text="HULK-BROWSER", font="Helvtica 24 bold",background='green').place(x=100,y=10)
Label(root,text="(Click on the buttons to open website)",font="LUCIDA 18", background='green').place(x=100,y=50)
#creating button for each functions
# button to call linkedin function
mylinkedin = Button(root,text="LINKEDIN", command=linkedin,font="LUCIDA 15 bold",background="#856ff8").place(x=30, y=100)
# button to call facebook function
myfacebook = Button(root, text="FACEBOOK", command=facebook,font="LUCIDA 15 bold",background="blue").place(x=180, y=100)
# button to call twitter  function
mytwitter = Button(root, text="TWITTER", command=twitter,font="LUCIDA 15 bold",background="sky blue").place(x=344, y=100)
# button to call youtube  function
myyoutube = Button(root, text="YOUTUBE", command=youtube,font="LUCIDA 15 bold",background="red").place(x=485,y=100)
# button to call gmail  function
mygmail= Button(root, text="GMAIL" , command=gmail,font="LUCIDA 15 bold",background="orange").place(x=500,y=300)
# button to call whatsappweb  function
mywhatsapp = Button(root, text="WHATSAPP WEB", command=whatsappweb,font="LUCIDA 15 bold",background="light green").place(x=30, y=300)
# button to call instagram  function
myinstagram = Button(root, text="INSTAGRAM", command=instagram,font="LUCIDA 15 bold",background="#FF6863").place(x=230,y=300)
myhotstar = Button(root, text="Hotstar", command=instagram,font="LUCIDA 15 bold",background="#00008B").place(x=390,y=300)

Term = StringVar(root, value="")
Term_entry=ttk.Entry(root,textvariable=Term,width=50)
Term_entry.place(x=155,y=199)
Term_entry.focus()

submit_button = ttk.Button(root,text="Submit",command=search)
submit_button.place(x=470,y=197)

check=Frame(root).pack(padx=20,pady=20)


var2 = IntVar(root,value=0)
Checkbutton(check, text="Google", variable=var2, background="sky blue").place(x=200,y=240)

var3 = IntVar(root,value=0)
Checkbutton(check, text="Youtube", variable=var3, background="red").place(x=290,y=240)

var4 = IntVar(root,value=0)
Checkbutton(check, text="IMDB", variable=var4,background="yellow").place(x=390,y=240)

Term_entry.bind("<Return>", (lambda event: search()))
#running the mainloop()
root.mainloop()