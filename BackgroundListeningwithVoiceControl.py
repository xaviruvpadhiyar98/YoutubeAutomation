#!/usr/bin/env python3


from time import sleep
from speech_recognition import Recognizer, Microphone, AudioFile
from apiclient.discovery import build 
from os import system
import vlclib
from time import sleep



DEVELOPER_KEY = "AIzaSyDeyCcahQ5EDOFcfZ25TzTSQqcUW9IM98w" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey = DEVELOPER_KEY)


#def startVLC():		
	#system("vlc --intf telnet --telnet-password admin &")
	#sleep(2)
vlc = VLCClient("::1")		
vlc.connect()
print("VLC STARTED.....")	   
			   
def youtubePlay(output):
	search_keyword = youtube.search().list(q = output, part = "id, snippet",maxResults = 1).execute()
	URLS = f"https://www.youtube.com/watch?v={search_keyword['items'][0]['id']['videoId']}"
	print(URLS)
	return URLS
	

def VLC_COMMANDS(output):

	if "play" in output.split()[0].lower():
		output = output.replace("play","")
		if output!="":
			URLS = youtubePlay(output)
			vlclib.add(URLS)
			
	if "add" in output:
		output = output.replace("add","")
		if output!="":
			URLS = youtubePlay(output)
			add = vlclib.enqueue(URLS)
			
	if "pause" == output:
		pause = vlclib.pause()
		
	if "resume" == output:
		resume = vlclib.play()
		
	if "increase volume" == output:
		volup = vlclib.volup()
		volume = vlclib.volume()
		print(f"Volume increased to {int(volume)}")
		
	if "decrease volume" == output:
		voldown = vlclib.voldown()
		volume = vlclib.volume()
		print(f"Volume decreased to {int(volume)}")
		
	if "show volume" == output:
		volume = vlclib.volume()
		print(f"Volume is {int(volume)}")
	if "next" == output:
		vlclib.next()
	if "previous" == output:
		vlclib.prev()
	if "clear playlist" == output:
		vlclib.clear()
	if "stop" == output:
		vlclib.stop()





# this is called from the background thread
def callback(recognizer, audio):
	# received audio data, now we'll recognize it using Google Speech Recognition
		
		'''
		if "play" in output:
			output = output.replace("play","")
			if output!="":
				URLS = youtubePlay(output)
				play = vlc.add(URLS)
				
		if "add" in output:
			output = output.replace("add","")
			if output!="":
				URLS = youtubePlay(output)
				add = vlc.enqueue(URLS)
				
		
		if "pause" == output:
			vlc.pause()
		if "resume" == output:
			vlc.play()
		if "increase volume" == output:
			vlc.volup()
		if "decrease volume" == output:
			vlc.voldown()
		if "show volume" == output:
			volume = vlc.volume()
			print(f"Volume is {volume}")
		if "play next" == output:
			vlc.next()
		if "play previous" == output:
			vlc.prev()
		if "clear playlist" == output:
			vlc.clear()

			'''
	try:
		output = recognizer.recognize_google(audio)
		print("WE THINKS: " + output)			
			
		with open("backgroundAudioListen.txt","a") as f:
			f.write(f"{output}\r\n")
			f.close()
			
		VLC_COMMANDS(output)
	except:
		pass




r = Recognizer()
mic = Microphone()
vlclib.connect()
with mic as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(mic, callback)

# `stop_listening` is now a function that, when called, stops background listening
while True:
	sleep(0.1)

# calling this function requests that the background listener stop listening
#stop_listening(wait_for_stop=False)
