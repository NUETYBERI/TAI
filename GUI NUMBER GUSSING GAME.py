from tkinter import *
import random

window = Tk()
window.title("GAME")
window.geometry("300x200")
window.resizable(0,0)

attempts=10
ans=random.randint(1,99)
def checkans():
    global attempts
    global text
    attempts-=1
    guess=int(entry.get())
    if ans==guess:
        text.set("YOU WIN!")
    elif guess<ans:
        text.set("YOU HAVE "+str(attempts)+" LEFT")
    elif guess>ans:
        text.set("YOU HAVE "+str(attempts)+" LEFT")
    else:
        text.set("YOU ARE OUT OF ATTEMPTS")
        
    if attempts == 0:
        btn.config(state="disabled") 


frame = Frame(window,height=300,width=200)
frame.pack()
label=Label(frame,text="GUESS A NUMBER BETWEEN 1 TO 99")
label.pack()
entry=Entry(frame,width=30,borderwidth=4)
entry.pack(pady=20)
btn=Button(frame,text="CHECK",command=checkans)
btn.pack()


text=StringVar()
text.set("YOU HAVE 10 ATTEMPTS LEFT ! ")
guess_attempts=Label(frame,textvariable=text)
guess_attempts.pack(pady=10)


    
