# 10thElevatorAutomatic

Move to directory containing 10aud.py and/or 10con.py
    e.g. Set-location -Path "Path"

Execute files in command line 
    e.g. py 10aud.py

What is 10aud.py (10audio)

    10aud.py downloads YT videos and converts them to .ogg audio files (192kbps, 16 bit depth, stereo, 44.1khz sample rate)

    10aud.py will prompt 2 inputs
        where to store the audio files (referred to as song folder from now on)
        the .txt file that contains YT URLs, with one URL per line

    it is recommended that the song folder be empty before execution
        it will convert any pre-existing audio file to .ogg
        it will then delete any file that is not .ogg or .cpp


What is 10con.py (10config)

    10con.py creates a config.cpp file in every sub/genre folder that contains .ogg audio files
    the name of the genre folder will be the name of the genre folder in Zeus
    the name of the audio file will be the name found inside the genre folder

    10con.py will prompt 1 input
        select the root folder that contains all of the genre subfolders, which each contains .ogg files & a .cpp file
        i.e. rootFolder/genreFolder/config.cpp

        the program only needs to be run once to create config.cpp files for every genre folder

    