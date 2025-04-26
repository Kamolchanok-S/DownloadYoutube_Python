# This version will let user choose resolutions of video to download

from tkinter import *
from tkinter import ttk
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from pathlib import Path

def selectedVideo(url):
    # print(url)
    yt = YouTube(url, on_progress_callback = on_progress)
    
    # Get all the available streams (filter only video streams and ordered from highest to lowest)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Print available resolutions
    resolution_stream = []
    resolution_num = []
    for stream in video_streams:
        resolution_stream.append(stream)
        resolution_num.append(stream.resolution)
        # print(f"Resolution: {stream.resolution}, FPS: {stream.fps}, Mime type: {stream.mime_type}")
        
    # let user choose resolution
    # Create popup window
    popup = Toplevel(root)
    popup.title("Select Resolution")
    popup.geometry("300x200")
    
    Label(popup, text="Choose resolution:", font=('Arial', 12)).pack(pady=10)

    # Dropdown menu
    selected = StringVar()
    combobox = ttk.Combobox(popup)
    combobox['values'] = resolution_num
    combobox.pack(pady=10)
    # Shows highest resolution as a default value 
    combobox.current(0)  
    
    def download_selected():
        choice = combobox.current()
        selected_stream = resolution_stream[choice]
        # print(f"Resolution: {selected_stream.resolution}, FPS: {selected_stream.fps}, Mime type: {selected_stream.mime_type}")
        # Download the selected stream
        downloads_folder = str(Path.home() / "Downloads")  # Path to the real Downloads folder
        selected_stream.download(output_path=downloads_folder)
        popup.destroy()
    
    # Download button inside popup
    Button(popup, text="Download", command=download_selected).pack(pady=10)
    
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
btn = Button(text="Go!", command=lambda: selectedVideo(url_input.get()))
canvas.create_window(200, 150, window=btn)


root.mainloop()