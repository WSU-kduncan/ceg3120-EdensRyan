Setup
	
To get a bot up and running multiple tasks have to be completed
First a discord account must be created and a server/guild must be generated
Then on the discord developer site a new application must be created 
From the new application a new Bot must be created, this can be done with the menu on the left side of the screen.
The Bot must then be added to the guild. Stay on the application page and select OAuth2 directly above the new Bot option.
This will bring you to two sections called "Scopes" and "Bot". In Scopes select bot and in Bot select administrator.
Click the copy button located at the bottom of the "Scopes" section. Paste this into a browser.
After following the copied link a window that will open with a drop down menu. Select the chosen guild from the menu and click "Authorize"
The bot is now a memeber of the guild but doesn't actually do anything yet.

To create code for the bot the following must be in the system
python3
pip3
discord.py
python-dotenv
 
Once the above is complied with a .py file with instructions for the bot can be created.
This program will identify as the bot by using it's OAuth token which can be copied from the application page in the discord developer site.
For security reasons instead of placing the token directly into the code it will be placed in a file called .env which the code will access.

Usage

My changes to the code were fairly simple and straightforward. I changed all of the Brooklyn 99 quotes to Dresden Files quotes and the Hitchhikers guide quotes to 
quotes from The Name of the Wind. The commands became Dresden and Wind instead of towel!. The biggest change I did was creating an elif statement that accepted a
second command, radomly selected from the other set of quotes and sent it as a response. 

So to be clear the bot will respond to two commands
"Dresden" will make the bot respond with a quote from Jim Butchers Dresden Files
"Wind" will make the bot respond with a quote from Patrick Rothfuss' Name of the Wind

Research

There are a few ways to keep the bot running whithout stopping me from using my computer. The first and easist I think would be to simply have it running in it's own tap in MobaXterm. I could also (as has been demonstrated) create a screen and detach it from it's source so that it runs in the background or create a "package" that has all of the requisite programs and information and have it run somewhere else. I found what I believe to be a version of this where you could use the site replit
to host the bot with a modifier in the code that made it act occasionally and avoid timing out on the site. 
