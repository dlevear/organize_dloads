# organize_dloads 
Run this script to organize the folder `~/dloads`. The idea is to move all files into an archive folder labeled by yesterday's date, unless there is evidence that this already happened once today. 

This means that yes, the script is idempotent. 

I suggest setting this up as a "Login Item"

# Login Items Mac
Currently it works as follows. You have to make an Automator script which runs this python script. Then add this as a "Login Item" under Uses & Groups in System Preferences. 

# Login Items PC
I believe I found that you have to use Windows Task Scheduler. 
