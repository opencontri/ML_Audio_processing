import tkinter as tk
from tkVideoPlayer import TkinterVideo
import customtkinter as ctk
import os 
import torch
import vlc
import torchaudio
import IPython
import soundfile
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

app = tk.Tk()
app.geometry("600x550")
app.title("Rap God v2.0")
ctk.set_appearance_mode("dark") 

promptFrame = tk.Frame()
promptFrame.pack(padx=10, pady=10)
buttonFrame = tk.Frame()
buttonFrame.pack()

prompt = ctk.CTkEntry(promptFrame, height=40, width=300, text_font=("Arial", 20), text_color="black", fg_color="white")
prompt.pack(side='left', padx=10)
lyrics = ctk.CTkEntry(height=240, width=500, text_font=("Arial", 20), text_color="black", fg_color="white")
lyrics.pack()

def generateText():	
	if os.path.exists('generated.wav'):
		 p = vlc.MediaPlayer('file:///generated.wav')
		

def generateAudio(): 
    voice_samples, conditioning_latents = load_voice('stormzy', extra_voice_dirs=['stormzy_samples'])  
    tts = TextToSpeech()
    gen = tts.tts_with_preset(prompt.get(), voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset='ultra_fast') 
    torchaudio.save('generated.wav', gen.squeeze(0).cpu(), 24000) 

def playAudio(): 
    if os.path.exists('generated.wav'): 
        p = vlc.MediaPlayer('file:///generated.wav') 
        p.play()
    
videoplayer = TkinterVideo(master=app, scaled=True, keep_aspect=True)    
def generateVideo(): 
    os.system("xcopy /y generated.wav .\MakeItTalk\examples")
    os.system("cd MakeItTalk & python generate.py") 

    if os.path.exists('generated.wav'): 
        p = vlc.MediaPlayer('file:///generated.wav') 
        p.play()
           
genAudioButton =ctk.CTkButton(promptFrame,height=40, width=120, text_font=("Arial", 20), text_color="black", text="Generate Audio", command=generateAudio)
genAudioButton.pack(side='right')
playAudioButton =ctk.CTkButton(promptFrame,height=40, width=120, text_font=("Arial", 20), text_color="black", text="Play Audio", command=playAudio)
playAudioButton.pack(side='right')
genTextButton =ctk.CTkButton(promptFrame, height=40, width=120, text_font=("Arial", 20), text_color="black", text="Generate", command=generateText)
genTextButton.pack(side='right')
 
app.mainloop()