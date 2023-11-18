import tkinter as tk
from time import strftime

# Create a tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create a label to display the time
label = tk.Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")

time()  # Start the clock

root.mainloop()
