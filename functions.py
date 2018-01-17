import os, random, psutil, subprocess, time
from Socket import openSocket, sendMessage
from settings import *
demolist = []
# demo directory creation
def updateDemos():
	demolist.clear()
	#rewrite to use webdir from Settings.py
	openfile = open(WEBDIR+"/index.html", "a")
	open(WEBDIR+"/index.html", 'w').close()
	TableTop = '<table style="width:100%">\n<tr>\n<th align="left">Demo ID</th>\n<th align="left">Demo Name</th>\n</tr>\n'
	openfile.write(TableTop)
	#rewrite to use gamedir and moddir from Settings.py
	path = "GAMEDIR + "/" + MODDIR + "/demos""
	dirs = os.listdir ( path )
	for filenumber in range(len(dirs)):
		demoname = dirs[filenumber].rsplit('.', 1)
		demonumber = filenumber + 0
		demoid = "<tr>\n<td>" + str(demonumber) + "</td>\n<td>" + demoname[0] + "</td>\n</tr>\n"
		openfile.write(demoid)
		demolist.append(demoname[0])
	openfile.write("</tr>\n</table>\n")
	
# Updates the Queue File with Current Queue
	
def queueUpdate():
	untailQueue()
	updateDemos()
	queueInit()
	#rewrite to use webdir from Settings.py
	queuefile = open(WEBDIR+"/queue.html", "a")
	for idx in currentQueue:
		queuefile.write("\t<tr>\n\t\t<td>" + idx + "</td>\n")
	queuefile.close()
	tailQueue()	

# Adds end of table to queue file
	
def tailQueue():
	#rewrite to use webdir from Settings.py
	queuefile = open(WEBDIR+"/queue.html", "a")
	queuefile.write("\n\t</tr>\n</table>")
	queuefile.close()
	
# Removes end of table from queue file so file can be written to
	
def untailQueue():
	#rewrite to use webdir from Settings.py
	queuefile = open(WEBDIR+"/queue.html", "r")
	lines = queuefile.readlines()
	queuefile.close()
	#rewrite to use webdir from Settings.py
	queuefile = open(WEBDIR+"/queue.html", "w")
	queuefile.writelines([item for item in lines[:-2]])
	queuefile.close()

# intializes currentQueue and adds random demo, updates queue.html
	
currentQueue = []
def queueInit():
	#rewrite to use webdir from Settings.py
	queuefile = open(WEBDIR+"/queue.html", "a")
	#rewrite to use webdir from Settings.py
	open(WEBDIR+"/queue.html", 'w').close()
	TableTop = '<table style="width:100%">\n\t<tr>\n\t\t<th align="left">Demo Name</th>\n\t</tr>\n'
	queuefile.write(TableTop)
	queuefile.close()
	
# Adds a random demo to current Queue and updates
	
def randomQueue():
	currentQueue.append(random.choice(demolist))
	queueUpdate()

# add chatQueue to the current queue and update queue.html

def queueAdd(chatQueue):
	currentQueue.append(chatQueue)
	queueUpdate()
	print(currentQueue)

def gameRunning(exeName):
	# write an if statement for detecting linux, pull from ps if so
    process = subprocess.Popen( 
        'tasklist.exe /FO CSV /FI "IMAGENAME eq %s"' % exeName,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True )
    out, err = process.communicate()    
    try : return out.split("\n")[1].startswith('"%s"' % exeName)
    except : return False	
	
# game launcher
def launchGame():
	if gameRunning(GAMEBIN) == False:
		if len(currentQueue) == 0:
			randomQueue()
		global launchdemo
		launchdemo = currentQueue.pop(0)
		#rewrite to use gamedir from Settings.py
		obsfile = open(GAMEDIR + "/upcomming.txt", "w")
		obsfile.write(" " + launchdemo + " ")
		obsfile.close()
		time.sleep(20)
		print("Launching game with demo:" + launchdemo)
		#rewrite to use gamedir and gamebin from Settings.py
		subprocess.Popen((GAMEDIR + "/" + GAMEBIN + " +set fs_basepath " + GAMEDIR + " +demo" + "\"" + launchdemo.rstrip() + "\""  +" +set nextdemo quit"), cwd=GAMEDIR)
		queueUpdate()
