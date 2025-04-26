from tkinter import *
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(url):
    # print(url)
    # Download the YouTube video at the highest resolution
    youtube = YouTube(url, on_progress_callback = on_progress)
    mp4 = youtube.streams.get_highest_resolution()
    mp4.download()
    
root = Tk()
root.title("Youtube Downloader")

canvas = Canvas(root, width=400, height=200)
canvas.pack()

# app title
app_title = Label(root, text="Youtube Downloader", font=('Arial', 20, 'bold'))
canvas.create_window(200, 30, window=app_title)

# input url link
input_lb = Label(root, text="Enter url:")
canvas.create_window(200, 80, window=input_lb)

url_input = Entry(root, width=60)
canvas.create_window(200, 100, window=url_input)

# send url to download function with parameter
btn = Button(text="Download", command=lambda: download(url_input.get()))
canvas.create_window(200, 150, window=btn)


root.mainloop()