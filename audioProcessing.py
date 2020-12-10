import ffmpeg

class AudioProcessor:

    def __init__(self,file_path, bit_rate,file_name):
        super().__init__()
        self.file_Path= file_path 
        self.bit_rate= bit_rate
        self.file_name=file_name

    def convert_video(self):
        input = ffmpeg.input(self.file_Path+'/'+self.file_name+'.mp4')
        audio = input.audio
        #out = ffmpeg.output(audio, 'out.mp3', **{'f':'mp3', 'ab':'320k'})
        path = self.file_Path+'/'+self.file_name+'.mp3'
        out = ffmpeg.output(audio, path, **{'f':'mp3', 'ab':self.bit_rate})
        ffmpeg.run(out)
        print("Audio converted ...")

'''ffmpeg -i teri-mitti.aac  -f wav output4.wav

ffmpeg -i teri-mitti.aac -ab 320k -f mp3 output3.mp3
'''