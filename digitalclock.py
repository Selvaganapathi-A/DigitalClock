from tkinter import Label, Tk

import datetime
import threading

window: Tk = Tk()
window.title("Digital Clock")
window.geometry("640x320")
window.configure(bg="orangered")

label: Label = Label(window, font=("Poppins", 50, "bold"), bg="orangered", fg="white")
label.pack(padx=10, pady=10)


def clock():
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    label.configure(text=time)
    label.after(500, clock)


t1 = threading.Thread(target=clock)
t1.daemon = True
# t1.setDaemon(True)
t1.start()

window.mainloop()
