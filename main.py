import pygame as p
from tkinter import *
from pygame import mixer
import os
from tkinter import filedialog

Playlist=[]
def add():
	path=filedialog.askdirectory()
	if path:
		os.chdir(path)
		songs=os.listdir(path)
		for song in songs:
			if song.endswith("mp3"):
				Playlist.insert(END,song)

def play():
	music=Playlist[0]
	mixer.music.load(music)
	mixer.music.play()
		







#main window
root=Tk()
root.geometry("400x300+10+20")
root.configure(bg="red")
root.title("*****************Music Player*********************")
l1=Label(root,text="MUSIC PLAYER",font="BOLD",bg="pink",fg="black")
l2=Label(root,text="CONTROLS",font="BOLD",bg="blue",fg="black")
l2.place(x=157,y=150)
l1.place(x=150,y=0)
b1=Button(root,bg="green",text="Add Songs",fg="white",command=add())
b1.place(x=160,y=90)
b2=Button(root,bg="yellow",fg="black",text="        PLAY         ",command=play())
b2.place(x=10,y=150)
b3=Button(root,bg="violet",fg="white",text="     PAUSE    ")
b3.place(x=160,y=200)
b4=Button(root,bg="purple",fg="white",text="     STOP     ")
b4.place(x=300,y=150)
mainloop()


#function for the controls


