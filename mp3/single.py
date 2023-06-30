import os
import subprocess

import pytube

link=input("Enter video link: ")
link2="&html5=1"
link=link+link2
yt = pytube.YouTube(link)

print("Downloading: ", yt.title)
# https://youtu.be/XFkzRNyygfk

parent_dir = r"/data/data/com.termux/files/home/storage/shared/pytube/pytube/mp3"

yt.streams.get_by_itag(251).download()

default_filename = yt.streams.get_by_itag(251).default_filename
default_filename1=default_filename.strip(".webm")
new_filename = default_filename1+".mp3"



subprocess.run([
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])
os.remove(default_filename)
print('done')