import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("485x700+290+10")
root.configure(background = "#333333")
root.resizable(False, False)
mixer.init()


def AddMusic():
    path =filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
         
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name =Playlist.get(ACTIVE)
    print(Music_Name)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    

lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0,y=400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Menu = PhotoImage(file="menu.png")
Label(root,image = Menu).place(x=0 , y=580, width = 485, height = 100)

Frame_Music = Frame(root, bd=2,relief= RIDGE)
Frame_Music.place(x=0 , y=585 , width = 485, height = 100)

ButtonPlay = PhotoImage(file = "play.png")
Button(root , image = ButtonPlay, bg= "#FFFFFF",bd =0 , height = 60, width = 60, command = PlayMusic).place(x=215,y=487) 

ButtonStop = PhotoImage(file = "stop.png")
Button(root , image = ButtonStop, bg="#FFFFFF", bd=0 , height=60 , width= 60, command = mixer.music.stop).place(x=130, y=487)

ButtonPause = PhotoImage(file = "pause.png")
Button(root , image= ButtonPause, bg="#FFFFFF", bd=0 , height=60 , width= 60, command = mixer.music.stop).place(x=300, y=487)

Volume1 = PhotoImage(file="volume.png")
panel = Label(root , image=Volume1).place(x=20,y=487)

music1 = PhotoImage(file="m1.png")
panel = Label(root , image=music1).place(x=0,y=0)

Button(root, text ="Browse Music", width = 49, height = 1, font =("calubri",12,"bold"), fg= "Black", bg="#FFFFFF", command = AddMusic).place(x=0 , y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music , width = 100 , font = ("Times new roman",10),bg = "#333333",fg = "grey", selectbackground="lightblue",cursor="hand2",bd = 0,yscrollcommand= Scroll.set)

Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill=Y)
Playlist.pack(side = RIGHT, fill = BOTH)

root.mainloop()