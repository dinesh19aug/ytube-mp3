# ytube-mp3
This app downloads the youtube files and converts them to mp3. You can download the youtube video and convert them to 128k/192/256/320k.

## Installer
### Windows:
Windows exe app can be found under installer/dist - gui.exe

### Mac:
If you need to create a mac installer, then follow the below steps:
- fork the project
- Create a new python environment using conda or pipenv
- Use requirements.txt or requirements.yml file inside the project to set up and install all the dependencies.
- Change dir to installer. Remove all folder dist/build. 
- Run command 
```pyinstaller --onefile --windowed <path to gui.py file>\gui.py```
- This will create the dmg file under 'dist' folder.
## Why:
I wanted to download few videos from youtube, which I did using firefox and chrome plugin. However, I only wanted the audio, so that I could hear on my ipod/phone while driving. The video size was too big and extracting audio required me to push the video files to some online websites which were either too unreliable or were charging too much fees.

## Language
This app is built using the following 
- python
- pysimplegui - Used to create the gui
- ffmpeg - Used to convert the music file to bit rate of your choice.
- pytube - Used to download the file from youtube.

