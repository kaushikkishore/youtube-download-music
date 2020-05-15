from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

to_download = {"https://www.youtube.com/watch?v=adyjwFgXRNY","https://www.youtube.com/watch?v=nwRoHC83wx0"}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for item in to_download:
        ydl.download([item])
        print("completed "+ item)

print("All Completed")