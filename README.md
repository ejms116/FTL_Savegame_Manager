# FTL_Savegame_Manager
The FTL Savegamer Manager is a tool to keep track of your savegames in a FTL run. After a full run you end up with a folder that has a savegame from every beacon. The intention was to collect interesting/bad fights and use those as training to get better at handling those.

# Credits
The code that reads the continue.sav file is based on Vhati's profile editor and the python implementation by whiskeythecat.

https://github.com/Vhati/ftl-profile-editor

https://github.com/whiskeythecat/ftl_twitch

# Setup
If you just want to use the program. The only thing you need is to download the standalone.zip file.

* Download the zip file and extract it 
* you should end up with a directory that includes 2 folders (current and saves), a config.ini and the ftl_savegame_manager.exe
* now you need to configure the config.ini file:
  * target_path: this has to be the location where FTL stores the continue.sav
  * saves_db_path: this should point to the saves folder
  * saves_new_path: this should point to the current folder
  * update_frequency: this is the intervall for checking new continue.sav files, the default is 2000
* run the ftl_savegame_manager.exe

# Usage

* Load Save: This copies the chosen file into the FTL directory. This also renames the file so you can rename your saved games if you want.
* Save Last File: This copies the latest saved game into the saves folder, if tracking is active. It opens a prompt so you can choose to rename the file.
* Open Saves Folder: Opens the saves folder
* Open Current Folder: Opens the current folder
* Toggle Tracking: If this is active (indicated by the color of the button; green=active, red=not active) the program checks every 2 seconds (default) if the continue.sav has changed and creates a copy of the file in the current directory. The program also creates a folder for every new run. The filenames include the current beacon, sector and the ship name, so it should be easy to identify the file you're looking for.
