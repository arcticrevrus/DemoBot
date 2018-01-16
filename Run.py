import string, subprocess, random, re, psutil, threading, time, datetime
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from functions import *
from Commands import *
from threading import Thread
#from commands import *
# Connect to IRC/Channel and start listening

s = openSocket()
joinRoom(s)

readbuffer = ""
lastping = datetime.datetime.now()

# demo directory creation
updateDemos()

# set up the queue
queueInit()
randomQueue()	

def quake():
	while True:
		launchGame()
		
def reconnect():
	while True:
		if lastping < datetime.datetime.now()-datetime.timedelta(minutes=6):
			joinRoom(s)
			
# bot commands and shit
	
if __name__ == "__main__":
	t1 = Thread(target = quake)
	t1.setDaemon(True)
	t1.start()
	t2 = Thread(target = reconnect)
	t2.setDaemon(True)
	t2.start()
	while True:
		readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
		temp = str.split(readbuffer, "\n")
		readbuffer = temp.pop()
	
		
		for line in temp:
			print(line)
			# reply to IRC PING's so we dont get disconnected
			if "PING" in line:
				s.sendall(bytes("PONG :tmi.twitch.tv\r\n", "UTF-8" ))
				lastping = datetime.datetime.now()
				break
			user = getUser(line)
			message = getMessage(line)
			print (user + " typed :" + message)
			# test command
			if re.search(r'^!suck', message, re.IGNORECASE):
				commandTest(s)
				break
			# test command to launch game with specified demo number
			if re.search(r'^!add ', message):
				commandAdd(s, message)
				break
			if re.search(r'^!add$', message.rstrip()):
				sendMessage(s, "Invalid Format. Example: !demo 36")
				break
			#command to update the demo list
			if re.search(r'^!updatedemos', message):
				commandUpdatedemos(s)
				break
			#post link to demo directory
			if re.search(r'^!demolist', message):
				commandDemolist(s)
				break
			#post list of commands
			if re.search(r'^!commands', message):
				commandCommands(s)
				break
			#add a random demo to the queue
			if re.search(r'^!randomadd', message):
				commandRandomadd(s)
				break
			#give link to queue
			if re.search(r'^!queue', message):
				commandQueue(s)
				break
			if re.search(r'^!download', message):
				commandDownload(s)
				break
			if re.search(r'^!report ', message):
				commandReport(s, message)
				break
			if re.search(r'^!report$', message.rstrip()):
				sendMessage(s, "Invalid Format. Example: !report 36")
				break
			if re.search(r'^!current', message):
				commandCurrent(s)
				break
			if re.search(r'^!upload', message):
				commandUpload(s)
				break
			if re.search(r'^!help', message):
				commandHelp(s, message)
				break
		pass
