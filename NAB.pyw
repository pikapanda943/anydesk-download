import tkinter as tk
import subprocess
from tkinter import messagebox

root = tk.Tk()
root.title("Not a bomb")
root.configure(bg="black")
root.overrideredirect(True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

time_left = 10 * 60  # 10 minutes in seconds
running = False
pin = "1524"


def update_time():  # detonation
    global time_left, running
    if time_left > 0 and running:
        minutes, seconds = divmod(time_left, 60)
        time_left -= 1
        time_left_str = "{:02d}:{:02d}".format(minutes, seconds)
        label.configure(text=time_left_str, fg="red", bg="black")
        root.after(1000, update_time)
    elif time_left == 0:
        label.configure(text="Detonating...", fg="red", bg="black")
        running = False
        root.destroy()
        subprocess.run(["C:/Users/Admin/Desktop/NAB/(deto)/Deto.exe"])  # exe used to detonate


def start_timer():
    global running
    entered_pin = pin_entry.get()
    if entered_pin == pin:
        running = True
        start_button.configure(text="Stop", command=stop_timer)
        pin_entry.delete(0, tk.END)
        update_time()
    else:
        messagebox.showwarning("Wrong Pin", "The pin you entered is incorrect.")


def stop_timer():
    global running
    entered_pin = pin_entry.get()
    if entered_pin == pin:
        running = False
        start_button.configure(text="Start", command=start_timer)
        pin_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Wrong Pin", "The pin you entered is incorrect.")


def change_time():
    global time_left
    entered_pin = pin_entry.get()
    if entered_pin == pin:
        time_left = 0
        start_timer()
        minutes, seconds = divmod(time_left, 60)
        time_left_str = "{:02d}:{:02d}".format(minutes, seconds)
        label.configure(text=time_left_str, fg="red", bg="black")
        pin_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Wrong Pin", "The pin you entered is incorrect.")


label = tk.Label(root, font=("times", 160), bg="black", fg="red")
label.pack(expand=True)

pin_entry = tk.Entry(root, font=("times", 40), show="*", width=4, bg="gray90")
pin_entry.pack(expand=True)

start_button = tk.Button(root, text="Start", command=start_timer, bg="black", fg="red", font=("times", 40))
start_button.pack(expand=True)

change_time_button = tk.Button(root, text="Detonate", command=change_time, bg="black", fg="red", font=("times", 40))
change_time_button.pack(expand=True)


def kill_program():
    entered_pin = pin_entry.get()
    if entered_pin == pin:
        root.destroy()


# create a button to kill the program
kill_button = tk.Button(root, text="", command=kill_program, bg="black", fg="black", font=("times", 1), relief="flat")
kill_button.pack(side="left", anchor="sw")

root.mainloop()
