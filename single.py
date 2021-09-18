import os
import subprocess

import pytube

link=input("Enter video link: ")
link2="&html5=1"
link=link+link2
yt = pytube.YouTube(link)

print("Downloading: ", yt.title)
vids= yt.streams.first().download()

default_filename = yt.streams.first().default_filename
default_filename1=default_filename.strip(".mp4")
#new_filename = input("Enter filename (including extension): ") # e.g. new_filename.mp3
new_filename = default_filename1+".mp3"
parent_dir = r"C:\Users\mykael\Desktop\PYTHON\yt"

subprocess.run([
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])
os.remove(default_filename)
print('done')