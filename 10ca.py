

from pydub import AudioSegment
import os
import os.path
from os import path
from tkinter import Tk
from tkinter.filedialog import askdirectory


# root = 10thElevatorMusic (work folder)
# shows dialog box and return the root
root = askdirectory(title='Select Folder')


for subdir, dirs, files in os.walk(root):
    for dir in dirs:
        configFilePath = root + "/" + dir
        with open(configFilePath + "/config.cpp", "w") as myfile:
            myfile.write('''

class CfgPatches
{
		class ''' + dir + '''
	{
		units[] = {};
		weapons[] = {};
		requiredVersion = 0.1;
		requiredAddons[] = {};
	};
};

class CfgMusicClasses
{
		class ''' + dir + '''
	{
		displayName = "::::''' + dir + '''::::"
	};
};

class CfgMusic
{''')
            # https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
            for subdir, dirs, files in os.walk(configFilePath):
                counter = 1
                for i in files:
                    if i.endswith(".ogg"):
                        audio = AudioSegment.from_file(
                            configFilePath + "/" + i)
                        myfile.write('''
		class ''' + dir[0:7] + '''_''' + str(counter) + '''
	{
		name = "''' + i[0:-4] + '''";
		sound[] = {"''' + dir + '''\\''' + i + '''",1,1};
		theme = "''' + dir + '''";
		duration = "''' + str(int(audio.duration_seconds)) + '''";
		musicClass = "''' + dir + '''";
	};
''')
                        counter += 1

                myfile.write('''

};''')
