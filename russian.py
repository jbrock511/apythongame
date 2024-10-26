import tkinter as tk
import time
import sys
import os
from random import randint

#dont run in codespaces!! completely safe to run on any computer :]

chambers = int(6)
BulletPosition = randint(1, chambers)
file_path = sys.argv[0]
TimesShot = 0

window = tk.Tk()
window.title("Russian Roulette")
window.geometry("300x300")

message_label = tk.Label(window,
                         text="",
                         font=("Helvetica", 16),
                         wraplength=400)
message_label.pack(pady=20)

hello = tk.Label(text="Let's play Russian Roulette!")
hello.pack()
hello1 = tk.Label(text="Trigger pulls: " + str(TimesShot))
hello1.pack()


def type_text(label, text, delay=0.05):
  #simulate typing text
  label.config(text="")
  for char in text:
    label.config(text=label.cget("text") + char)
    window.update()
    time.sleep(delay)


def Shoot():
  global BulletPosition
  if BulletPosition == 1:
    SpinButton.config(state='disabled')
    ShootButton.config(state='disabled')

    type_text(message_label, "You hesitate for a second...")
    time.sleep(2)  #wait 2 seconds before continuing
    type_text(message_label, "1...")
    time.sleep(2)
    type_text(message_label, "2...")
    time.sleep(2)
    type_text(message_label, "3!!!")

    window.destroy()
    os.remove(file_path)
  else:
    global TimesShot
    TimesShot += 1
    hello1.config(text="Trigger pulls: " + str(TimesShot))
    hello1.pack()

    ShootButton.config(state='disabled')
    ShootButton.after(1500, lambda: ShootButton.config(state='active'))
    SpinButton.config(state='disabled')
    SpinButton.after(1500, lambda: SpinButton.config(state='active'))

    type_text(message_label, "Click!")
    time.sleep(0.4)
    type_text(message_label, "You lived... for now!")

    BulletPosition -= 1
    hello1.update()


def Spin():
  SpinButton.config(state='disabled')
  SpinButton.after(1500, lambda: SpinButton.config(state='active'))
  ShootButton.config(state='disabled')
  ShootButton.after(1500, lambda: ShootButton.config(state='active'))
  global BulletPosition
  BulletPosition = randint(1, chambers)
  type_text(message_label, "You spin the chamber...")


ShootButton = tk.Button(text="Shoot!", command=Shoot)
SpinButton = tk.Button(text="Spin!", command=Spin)

ShootButton.pack()
SpinButton.pack()

tk.mainloop()

#end of program :)
