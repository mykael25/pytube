import os
import subprocess

import pytube

link=input("Enter video link: ")
link2="&html5=1"
link=link+link2
yt = pytube.YouTube(link)

vids= yt.streams.all()
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Enter vid Quality option: "))

parent_dir = r"C:\Users\mykael\Desktop\PYTHON\yt"
print("Downloading: ",vids[vnum].title)
vids[vnum].download(parent_dir)