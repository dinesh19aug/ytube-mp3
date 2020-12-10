

from pytube import YouTube

class Downloader:
    
    
    def __init__(self, youtube_url, folder_location):
        super().__init__()
        self.youtube_url= youtube_url
        self.folder_location = folder_location
        self.file_name=''

    def execute(self):
        youtube_obj=self.download_audio()
        return self
        

    def complete_func(self,stream,file_handle):
        print("Download completed")
        

    def download_audio(self):
        print("Started ...")
        youtube_obj = YouTube(self.youtube_url)
        #youtube_obj.register_on_complete_callback(self.complete_func)
        self.file_name=str(youtube_obj.title).rsplit(' ')[0]
        
        youtube_obj.streams \
        .filter(mime_type='audio/mp4', only_audio=True ) \
        .first() \
        .download(self.folder_location,self.file_name)
        
        
    
    
  