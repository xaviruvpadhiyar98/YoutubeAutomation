from telnetlib import Telnet


def connect():
	server='localhost'
	port = 4212
	timeout = 5
	password = "admin"
	global telnet
	telnet = Telnet()
	telnet.open(server,port,timeout)

	result = telnet.expect([r"VLC media player ([\d.]+)".encode("utf-8")])

	telnet.read_until("Password: ".encode("utf-8"))
	telnet.write(password.encode("utf-8"))
	telnet.write("\n".encode("utf-8"))

	result = telnet.expect(["Password: ".encode("utf-8"),">".encode("utf-8")])

	if "Welcome" in str(result[2]):
		print("Connection Succesful")


def send_command(line):
    telnet.write((line + "\n").encode("utf-8"))
    return telnet.read_until(">".encode("utf-8"))[1:-3]
    
    
def help():
        """Returns the full command reference"""
        return send_command("help")

def info():
    """information about the current stream"""
    return send_command("info")


def raw(*args):
    """Send a raw telnet command"""
    return send_command(" ".join(args))

#
# Playlist
#
def add(filename):
    """
    Add a file to the playlist and play it.
    This command always succeeds.
    """
    return send_command('add {0}'.format(filename))

def enqueue(filename):
    """
    Add a file to the playlist. This command always succeeds.
    """
    return send_command("enqueue {0}".format(filename))

def seek(second):
    """
    Jump to a position at the current stream if supported.
    """
    return send_command("seek {0}".format(second))

def play():
    """Start/Continue the current stream"""
    return send_command("play")

def pause():
    """Pause playing"""
    return send_command("pause")

def stop():
    """Stop stream"""
    return send_command("stop")

def rewind():
    """Rewind stream"""
    return send_command("rewind")

def next():
    """Play next item in playlist"""
    return send_command("next")

def prev():
    """Play previous item in playlist"""
    return send_command("prev")

def clear():
    """Clear all items in playlist"""
    return send_command("clear")

def loop():
    """Toggle loop"""
    return send_command("loop")

def repeat():
    """Toggle repeat of a single item"""
    return send_command("repeat")

def random():
    """Toggle random playback"""
    return send_command("random")

#
# Volume
#
def volume(vol=None):
    """Get the current volume or set it"""
    if vol:
        return send_command("volume {0}".format(vol))
    else:
        return send_command("volume").strip()

def volup(steps=1):
    """Increase the volume"""
    return send_command("volup {0}".format(steps))

def voldown(steps=1):
    """Decrease the volume"""
    return send_command("voldown {0}".format(steps))
    
    
def main():
	connect()
	add("https://www.youtube.com/watch?v=gOsM-DYAEhY")
	

if __name__ == "__main__": 
    main() 
