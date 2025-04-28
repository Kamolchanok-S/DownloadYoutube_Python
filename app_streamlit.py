import streamlit as st
import yt_dlp
import os
from pathlib import Path

def download_audio(url):
    status = st.empty()  # create an empty placeholder
    status.write("Downloading audio...")
    # Download the selected stream
    downloads_folder = str(Path.home() / "Downloads")
        
    #download audio
    dlp_opts = {
        'format': 'bestaudio',
        'outtmpl': downloads_folder + '/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(dlp_opts) as ydl:
        ydl.download(url)
    
    status.write("Done")
    
def download_video(url):
    status = st.empty()  # create an empty placeholder
    status.write("Downloading video...")
    
    # Options for resolution selection
    resolutions = ['360p', '480p', '720p', '1080p']
    
    # create resolution options and download video
    if st.button('360p'):
        return
    
    status.write("Done")
    
st.title('Youtube Downloader')
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('URL Link:')
url = st.text_input(label='Put YouTube link here:')

st.subheader('Choose download forms:')
# Create two columns
col1, col2 = st.columns(2)

# Button inside the first column
with col1:
    if st.button('Download Audio'):
        if url:
            download_audio(url)
        else:
            st.warning('Please enter a URL.')

# Button inside the second column
with col2:
    if st.button('Download Video'):
        if url:
            download_video(url)
        else:
            st.warning('Please enter a URL.')

# streamlit run app_streamlit.py