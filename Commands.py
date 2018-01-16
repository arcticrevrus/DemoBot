import subprocess, re, psutil
from Socket import openSocket, sendMessage
from functions import *

commands = {"!help", "!add", "!demolist", "!commands", "!queue", "!download", "!upload", "!current", "!report" }

def commandHelp(s, message):
	helped = ""
	if re.search(r'^!help !add$', message.rstrip()) is not None:
		sendMessage(s, "Adds a demo to the queue with a given demo ID. Usage: \"!add 36\"")
		helped = "True"
	if re.search(r'^!help !demolist$', message.rstrip()) is not None:
		sendMessage(s, "Sends a link to the list of available demos.")
		helped = "True"
	if re.search(r'^!help !commands$', message.rstrip()) is not None:
		sendMessage(s, "Lists available commands")
		helped = "True"
	if re.search(r'^!help !queue$', message.rstrip()) is not None:
		sendMessage(s, "Sends a link to the current demo queue.")
		helped = "True"
	if re.search(r'^!help !download$', message.rstrip()) is not None:
		sendMessage(s, "Sends a link to download the currently running demo.")
		helped = "True"
	if re.search(r'^!help !upload$', message.rstrip()) is not None:
		sendMessage(s, "Sends information on how to upload your own demos.")
		helped = "True"
	if re.search(r'^!help !current$', message.rstrip()) is not None:
		sendMessage(s, "Shows the currently running demo name and ID.")
		helped = "True"
	if re.search(r'^!help !report$', message.rstrip()) is not None:
		sendMessage(s, "Reports the current demo. Please use in case of demos with long pauses or warmup times. Usage: \"!report 36\"")
		helped = "True"
	if helped != "True":
		sendMessage(s, "Gives information about a particular command. Usage: \"!help !add\"")

		

def commandAdd(s, message):
	from functions import demolist, currentQueue
	if re.search(r'!add \d+$', message.rstrip()) is not None:
		if 0 <= int(re.search(r'(\d+)(?!.*\d)', message).group(0)) < len(demolist):
			chatQueue = demolist[int(re.search(r'\d+$', message.rstrip()).group(0))]
			queueAdd(chatQueue) 
			sendMessage(s, "Added Demo: " + demolist[int(re.search(r'\d+$', message.rstrip()).group(0))] + ".")
		else:
			sendMessage(s, "Invalid ID")
	else:
		sendMessage(s, "Invalid Format. Example: !demo 36")
		
def commandUpdatedemos(s):
	sendMessage(s, "Updated demos file.")
	updateDemos()
	
def commandDemolist(s):
	#rewrite to use URL from Settings.py
	sendMessage(s, "You can see the list of Demos and Demo ID's at http://arcticrevr.us/")

def commandCommands(s):
	sendMessage(s, "The following commands are available for use: " + str(commands) )
	
def commandRandomadd(s):
	from functions import demolist
	chatQueue = random.choice(demolist)
	sendMessage(s, chatQueue + " has been added to the queue. ")
	queueAdd(chatQueue)
	
def commandTest(s):
	sendMessage(s, "No, you suck!")
	
def commandQueue(s):
	#rewrite to use URL from Settings.py
	sendMessage(s, "You can see the current Queue at http://arcticrevr.us/queue.html")
	
def commandDownload(s):
	from functions import launchdemo
	#rewrite to use URL from Settings.py
	sendMessage(s, "You can download the current Demo at http://arcticrevr.us/demos/" + launchdemo + ".dm_68")
	
def commandUpload(s):
	#rewrite to use URL from Settings.py
	sendMessage(s, "You can upload your own demos by FTP'ing .dm_68 files to ftp://arcticrevr.us/")
	
def commandCurrent(s):
	from functions import launchdemo
	print(launchdemo)
	for idx, item in enumerate(demolist):
		if item == launchdemo:
			demoidx = idx
	sendMessage(s, "The current demo is: " + launchdemo + " . Demo ID is: " + str(demoidx))
	
def commandReport(s, message):
	from functions import demolist
	if re.search(r'!report \d+$', message.rstrip()) is not None:
		if 0 <= int(re.search(r'(\d+)(?!.*\d)', message).group(0)) < len(demolist):
			#rewrite to use GAMEDIR from Settings.py
			reportfile = open("E:\quake\shitdemos.txt", "a")
			reportfile.write(demolist[int(re.search(r'\d+$', message.rstrip()).group(0))] + "\n")
			reportfile.close()
			sendMessage(s, "Reported Demo: " + demolist[int(re.search(r'\d+$', message.rstrip()).group(0))] + ".")
		else:
			sendMessage(s, "Invalid ID")
	else:
		sendMessage(s, "Invalid Format. Example: !demo 36")
		
def commandStats(s):
	# Use UDT to dump stats to JSON and parse for Final stats.
	pass