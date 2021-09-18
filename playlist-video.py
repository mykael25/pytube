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
	#print("Streams: ", video.streams.filter(fps= 30,res="720p", mime_type="video/mp4"))
	video.streams.get_by_itag(22).download()
	#video.streams.filter(res='720p').download()
	#video.streams.first().download()

	#Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video"
	
#vids[vnum].download(r"C:\Users\mykael\Desktop\yt-playlist-master")
	#default_filename = video.streams.first().default_filename
	
	#new_filename = input("Enter filename (including extension): ") # e.g. new_filename.mp3



print('done ALL')