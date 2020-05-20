#!/usr/bin/env python3


from time import sleep
from speech_recognition import Recognizer, Microphone, AudioFile
from apiclient.discovery import build 
from os import system

DEVELOPER_KEY = "" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey = DEVELOPER_KEY)
			   
def youtubePlay(output):
	search_keyword = youtube.search().list(q = output, part = "id, snippet",maxResults = 1).execute()
	URLS = f"https://www.youtube.com/watch?v={search_keyword['items'][0]['id']['videoId']}"
	print(URLS)
	system(f"vlc {URLS} &")


# this is called from the background thread
def callback(recognizer, audio):
	# received audio data, now we'll recognize it using Google Speech Recognition
	try:
		output = recognizer.recognize_google(audio)
		print("GSR THINKS: " + output)
		if "play" in output:
			output = output.replace("play","")
			if output!="":
				youtubePlay(output)

	except:
		pass


r = Recognizer()
mic = Microphone()
with mic as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(mic, callback)

# `stop_listening` is now a function that, when called, stops background listening
while True:
	sleep(0.1)

# calling this function requests that the background listener stop listening
#stop_listening(wait_for_stop=False)
