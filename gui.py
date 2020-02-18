import PySimpleGUI as sg
from run import Run
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return wrapped

@background
def download(url,folder):
    run = Run()
    run.execute(url,folder)

def beforeSubmit(url,folder,bit_rate,error):
    if(len(url)<=0 or len(folder)<=0 or len(bit_rate)<=0):
        return False
    else:
        return True

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Youtube url', size=(15, 1)), sg.InputText(key='-url-')],
            [sg.Text('Download folder', size=(15, 1)), sg.InputText(key='-folder-')],
            [sg.Text('Bit Rate', size=(15, 1)), sg.Combo(['128k','192k','256k','320k'], key='-bitrate-')],
            [sg.Submit(), sg.Button('Cancel')]
             ]

# Create the Window
window = sg.Window('Youtube Song Converter', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    else:
        url=values['-url-']
        folder=values['-folder-']
        bit_rate=values['-bitrate-']
        
        flag=beforeSubmit(url,folder,bit_rate,"")
        if(flag):
            download(url,folder)
        else:
            sg.Popup('Fill out all fields')  
        

window.close()


