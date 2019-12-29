
import sys
from downloader import Downloader
from audioProcessing import AudioProcessor

class Run:
    def __init__(self):
        super().__init__()


    def execute(self,youtube_url, download_folder):
        #youtube_url = input("Enter Youtube url\n")
        #download_folder = input("Enter the download folder\n")    
        dw=Downloader(youtube_url,download_folder)
        print('Downloading the songs ...')
        yt=dw.execute()
        print("Starting the conversion to mp3 ...")
        print(yt.folder_location)
        print(yt.file_name)
        au = AudioProcessor(yt.folder_location,'320k',yt.file_name)
        au.convert_video()


