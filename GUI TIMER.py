from tkinter import *
import time

def start_timer():
    global running
    global start_time
    running = True
    start_time = time.time()
    update_timer()
    start_button.config(state="disabled")
    stop_button.config(state="normal")

def stop_timer():
    global running
    running = False
    start_button.config(state="normal")
    stop_button.config(state="disabled")

def update_timer():
    if running:
        elapsed_time = time.time() - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
        timer_label.config(text=time_str)
        window.after(1000, update_timer)  
    else:
        timer_label.config(text="00:00:00")

window = Tk()
window.title("Timer")

timer_label = Label(window, text="00:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

start_button = Button(window, text="Start", command=start_timer)
start_button.pack(pady=10)

stop_button = Button(window, text="Stop", command=stop_timer, state="disabled")
stop_button.pack(pady=10)

running = False
start_time = None


