from speech_recognition import Recognizer, Microphone, AudioFile
from time import sleep
from apiclient.discovery import build 
from os import system
import vlclib

r = Recognizer()
mic = Microphone()



DEVELOPER_KEY = "AIzaSyDeyCcahQ5EDOFcfZ25TzTSQqcUW9IM98w" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey = DEVELOPER_KEY)
	


def RecordnSave():
	with mic as source:
		print("Listening..")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	with open("microphone-results.wav", "wb") as f:
		f.write(audio.get_wav_data())


def youtubePlay(output):
	search_keyword = youtube.search().list(q = output, part = "id, snippet",maxResults = 1).execute()
	URLS = f"https://www.youtube.com/watch?v={search_keyword['items'][0]['id']['videoId']}"
	print(URLS)
	return URLS
   

def VLC_COMMANDS(output):

	if "play" in output:
		output = output.replace("play","")
		if output!="":
			URLS = youtubePlay(output)
			play = vlclib.add(URLS)
			
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
		
	if "decrease volume" == output:
		voldown = vlclib.voldown()
		
	if "show volume" == output:
		volume = vlclib.volume()
		print(f"Volume is {volume}")
	if "next" == output:
		vlclib.next()
	if "previous" == output:
		vlclib.prev()
	if "clear playlist" == output:
		vlclib.clear()
	if "stop" == output:
		vlclib.stop()

def start():
	RecordnSave()    
	temp_audio = AudioFile("microphone-results.wav")
	with temp_audio as source:
		audio = r.record(source)
	try:
		output = r.recognize_google(audio)
		print("WE THINKS: " + output)
		
		with open("logs.txt","a") as f:
			f.write(f"{output}\r\n")
			f.close()
			
		VLC_COMMANDS(output)
	except:
		print("-")



def main():
	vlclib.connect()
	while True:
		start()
		sleep(0.1)	


if __name__ == "__main__": 
    main() 
