import pytube
import os
import subprocess
from pytube import Playlist, YouTube
#yt = pytube.YouTube("https://youtube.com/playlist?list=PLJAYqRa04szE3FfiUnUlTFo3StziFXbGf")
#p = Playlist('https://youtube.com/playlist?list=PLHm-yTb5V0AorFOdYoII2GgQG_kbiVOYv')
link=input("Enter Playlist Link: ")
p = Playlist(link)
print(f'Downloading: {p.title}')

for video in p.videos:
	print("Downloading: ", video.title)
	video.streams.first().download()
	
#vids[vnum].download(r"C:\Users\mykael\Desktop\yt-playlist-master")
	default_filename = video.streams.first().default_filename
	default_filename1=default_filename.strip(".mp4")
	#new_filename = input("Enter filename (including extension): ") # e.g. new_filename.mp3
	new_filename = default_filename1+".mp3"
	parent_dir = r"C:\Users\mykael\Desktop\PYTHON\yt"
	#vids[vnum].download(parent_dir)

	#default_filename = video.streams.first().default_filename  # get default name using pytube API
	subprocess.run([
	    'ffmpeg',
	    '-i', os.path.join(parent_dir, default_filename),
	    os.path.join(parent_dir, new_filename)
	    
	])
	os.remove(default_filename)
	print('done converting')


print('done ALL')