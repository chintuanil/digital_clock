import tkinter as tm
import time
window=tm.Tk()
def start_clock():
    hours=time.strftime("%I")
    minutes=time.strftime("%M")
    seconds=time.strftime("%S")
    am_pm=time.strftime("%p")
    actual_time=hours +":"+minutes +":"+seconds+":" +am_pm
    clock_label.config(text=actual_time)
    clock_label.after(1000,start_clock)
clock_label=tm.Label(window, text="00:00:00", font="Arial 90 bold")
clock_label.pack()
start_clock()
window.mainloop()
