from pyaudio import PyAudio
import wave
from speech_recognition import Recognizer,AudioFile
from apiclient.discovery import build 
from os import system

CHUNK = 1024
FORMAT = 8
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "output.wav"

DEVELOPER_KEY = "AIXXXXXXXXXX" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY)
                                        
p = PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Say Something to search on Youtube")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Searching....")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

r = Recognizer()
temp_audio = AudioFile(WAVE_OUTPUT_FILENAME)
with temp_audio as source:
	audio = r.record(source)

try:
	output = r.recognize_google(audio)
except:
	print("Error Try again")


if "play" in output:
	output.replace("play","")

search_keyword = youtube.search().list(q = output, part = "id, snippet", 
                                               maxResults = 1).execute()

URLS = f"https://www.youtube.com/watch?v={search_keyword['items'][0]['id']['videoId']}"
print(URLS)

system(f"vlc {URLS} &")

