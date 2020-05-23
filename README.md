# YoutubeAutomation
Play Youtube Videos from terminal to VLC with SpeechRecognition and YoutubeAPI v3

# Install All the requirements from requirements.txt
pip3/pip install -r requirements.txt


# We will also need VLC TO PLAY THE VIDEO


# This is the demo for voice automation to search for a youtube video and play on the vlc without using browser
# This requires the Youtube API v3 Key which you need to add in the code and then run the file

# You can find the key using google account

Before you start
You need a Google Account to access the Google API Console, request an API key, and register your application.

Create a project in the Google Developers Console and obtain authorization credentials so your application can submit API requests.

After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:

Go to the API Console and select the project that you just registered.
Visit the Enabled APIs page. In the list of APIs, make sure the status is ON for the YouTube Data API v3.
If your application will use any API methods that require user authorization, read the authentication guide to learn how to implement OAuth 2.0 authorization.For more infomation visit https://developers.google.com/youtube/v3/getting-started


# TO RUN VOICE CONTROLLED
open terminal and run vlc 

--intf telnet --telnet-password admin &


and then run python3 AddedVoiceControl.py

