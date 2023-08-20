

from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfile
from yt_dlp import YoutubeDL as yDL
from pydub import AudioSegment
import os

# shows dialog box and return the songFolder path
# returns textFile object NOT PATH

# need to keep songFolder EMPTY, or else formatting will overwrite everything?
print(os.getcwd())
songFolder = askdirectory(initialdir=os.getcwd(), title='Select Folder To Save Songs In')
textFileObject = askopenfile(initialdir=os.getcwd(), title='Select text file with YT URLs')


URLs = textFileObject.readlines()

# https://github.com/yt-dlp/yt-dlp
# ^ use this: download speeds are much better, youtube_dl is shit


ydl_opts = {
    'outtmpl': songFolder + '/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }],
    'noplaylist': True
}

audio_downloader = yDL(ydl_opts)

# downloads all files to songFolder
audio_downloader.download(URLs)


# step 2: convert all formats in songFolder to .ogg, 16 bit, 192 kbps, & keep stereo
# https://stackoverflow.com/questions/1246131/python-library-for-converting-files-to-mp3-and-setting-their-quality
for subdir, dirs, files in os.walk(songFolder):
    for i in files:
        sound = AudioSegment.from_file(
            songFolder + "/" + i, sample_width=2, channels=2, frame_rate=44100)
        sound.export(songFolder + "/" +
                     i[0:-4] + ".ogg", format="ogg", codec="libvorbis", bitrate="192k")

    for i in files:
        if i.endswith(".ogg") or i.endswith(".cpp"):
            continue
        else:
            os.remove(os.path.join(songFolder, i))

# ffmpeg error
# https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/