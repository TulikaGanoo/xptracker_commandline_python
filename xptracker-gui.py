import tkinter as tk
window = tk.Tk()
greeting = tk.Label(
    text="Greetings brave warrior for fighting through another day!",
    fg="white",
    bg="black",
    width=50,
    height=20)
label = tk.Label(text="Name")
entry = tk.Entry()
button = tk.Button(
    text="Submit!",
    width=50,
    height=5,
    bg="grey",
    fg="black",
)
name = entry.get()
greeting.pack()
label.pack()
entry.pack()
button.pack()
window.mainloop()
