from pytube import YouTube
import urllib2
from bs4 import BeautifulSoup
import os.path
import time
from pydub import AudioSegment
import ssl
import Tkinter as tk
import ttk

class downloader:
    @classmethod
    def dowload(self, path, playlist):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        ssl._create_default_https_context = ssl._create_unverified_context

        page = urllib2.urlopen(playlist, context=ctx)
        soup = BeautifulSoup(page, 'lxml')
        list = soup.find_all("a", class_="pl-video-title-link")

        length = len(list)

        popup = tk.Toplevel()
        tk.Label(popup, text="Files being downloaded").grid(row=0, column=0)

        progress = 0
        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=length)
        progress_bar.grid(row=1, column=0)#pack(fill=tk.X, expand=1, side=tk.BOTTOM)
        #grid(row=1, column=0)
        label = tk.Label(popup, text=str(0) + "/" + str(length) + " songs downloaded")
        label.grid(row=2, column = 0)
        popup.pack_slaves()



        for n in list:
            current = list.index(n)
            label["text"] = str(current) + "/" + str(length) + " songs downloaded"
            popup.update()

            progress = current
            progress_var.set(progress)
            print current,"/",length
            link = "https://www.youtube.com/" + n.get("href")
            yt = YouTube(link)
            yt.set_filename("video")
            video = yt.get("mp4", '360p')
            video.download(path)
            filename = path + "video" + ".mp4"

            AudioSegment.converter = r"c:\ffmpeg\bin\ffmpeg.exe"
            AudioSegment.ffmpeg = r"c:\ffmpeg\bin\ffmpeg.exe"

            while not os.path.exists(filename):
                time.sleep(1)

            yt = YouTube(link)

            if (os.path.exists(filename)):
                AudioSegment.from_file(filename, "mp4").export(path + yt.filename + ".mp3", format='mp3')
                os.remove(filename)

        popup.destroy()



