import sounddevice as sd
import soundfile as sf
from tkinter import *

def vrc():
    fs = 48000
    # seconds
    duration = 5
    myrec = sd.rec(int(duration * fs),samplerate=fs, channels=2)
    sd.wait()

    #save as flac at correct sampling rate
    return sf.write('my_audio_file.flac', myrec,fs)

master = Tk()
Label(master, text="Voice recorder : ").grid(row=0,stick=W,rowspan=5)
but=Button(master,text="Start", command=vrc)
but.grid(row=0,column=2,columnspan=2, rowspan=2,padx=5,pady=5)
mainloop()