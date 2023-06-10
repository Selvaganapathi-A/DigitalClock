from tkinter import Label, Tk

window: Tk = Tk()
window.title("Digital Clock")
window.geometry("640x320")
window.configure(bg="orangered")

label: Label = Label(
    window, text="Welcome", font=("Poppins", 28, "bold"), bg="orangered", fg="white"
)
label.pack(padx=10, pady=10)
window.mainloop()
