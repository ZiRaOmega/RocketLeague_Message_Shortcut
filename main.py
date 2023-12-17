import tkinter as tk
from tkinter import simpledialog
import json
import keyboard
import pyautogui
import time
import pygetwindow as gw

# Function to check if Rocket League is the active window
def is_rocket_league_active():
    try:
        return gw.getWindowsWithTitle('Rocket League')[0].isActive
    except IndexError:
        return False

# Function to send a message in Rocket League
def send_rocket_league_message(message):
    if is_rocket_league_active():
        pyautogui.press('t')
        time.sleep(0.5)
        pyautogui.write(message)
        pyautogui.press('enter')
    else:
        print("Rocket League is not active")

# Load shortcuts from a JSON file
def load_shortcuts():
    try:
        with open("shortcuts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save shortcuts to a JSON file
def save_shortcuts(shortcuts):
    with open("shortcuts.json", "w") as file:
        json.dump(shortcuts, file)

# Add a new shortcut
def add_shortcut():
    shortcut = simpledialog.askstring("Input", "Enter the shortcut (e.g., ctrl+shift+d):")
    message = simpledialog.askstring("Input", "Enter the message:")
    if shortcut and message:
        shortcuts[shortcut] = message
        save_shortcuts(shortcuts)
        update_listbox()
        keyboard.add_hotkey(shortcut, lambda: send_rocket_league_message(message))

# Delete the selected shortcut
def delete_shortcut():
    selected = listbox.curselection()
    if selected:
        shortcut = listbox.get(selected[0])
        del shortcuts[shortcut]
        save_shortcuts(shortcuts)
        update_listbox()

# Update the listbox with the current shortcuts
def update_listbox():
    listbox.delete(0, tk.END)
    for shortcut in shortcuts:
        listbox.insert(tk.END, shortcut)

# GUI setup
root = tk.Tk()
root.title("Rocket League Shortcut Manager")

listbox = tk.Listbox(root)
listbox.pack()

add_button = tk.Button(root, text="Add Shortcut", command=add_shortcut)
add_button.pack()

delete_button = tk.Button(root, text="Delete Shortcut", command=delete_shortcut)
delete_button.pack()

shortcuts = load_shortcuts()
update_listbox()

for shortcut, message in shortcuts.items():
    keyboard.add_hotkey(shortcut, lambda: send_rocket_league_message(message))

root.mainloop()
