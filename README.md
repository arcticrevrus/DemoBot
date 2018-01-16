# DemoBot

This script will run a queue controlled by a twitch chat of demo files for quake 3 engine games.
Example: http://twitch.tv/CPMAReplays

# Requirements

Python 3
Twitch account for bot.

Twitch account for channel. (could optionally use bot account)

Game client that can launch demo from command line and close after demo playback

Web Server with directory accessible from user running python script to host demo index and queue file

*possible*

Windows, the python script has not been tested on linux. Currently the script detects when the game finishes by scanning the output of tasksel.exe. This can be rewritten to use the output of ps, but currently isnt.


* Note 
This will not run on most VPS services, as a GPU is required to run the game. VPS with GPU is possible, however extremely expensive for this purpose. I recommend a spare PC or server that can take a video card, especially if you have the ability to colocate it in a datacenter.
