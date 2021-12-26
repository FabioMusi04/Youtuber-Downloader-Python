#                           -------------LIBRERIE DA IMPORTARE-------------                          #
import os
import ffmpeg
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
#                 -------------FINE LIBRERIE DA IMPORTARE-------------                          #



#                           -------------INIZIO CODICE-------------                          #

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(f"{liveprogress}%")

def Download():
    Video = 0
    Ytb_Link = UrlInp.get()
    if Ytb_Link == '':
        return
    path_Salva_Video = askdirectory()
    if path_Salva_Video == "":
        return
    try:
        Video = YouTube(str(Ytb_Link), on_progress_callback=on_progress)
    except:
        showinfo("Errore", "link non valido")
        return
    print("Titolo: " + Video.streams.first().default_filename.split('.')[0])
    print("Numero di Views: " + str(Video.views))
    #print("Rating video:  " + str(Video.rating))
    print("Canale:  " + Video.author)

    RisoluzioneVideo = Combo.get()
    if RisoluzioneVideo == "":
        showinfo("Seleziona", "Seleziona Risoluzione")
        return

    if Video.streams.filter(resolution=RisoluzioneVideo, only_video=True).first() == None:
        showinfo("Errore", "risoluzione video o link errato")
        return

    print("Peso del file video:  " + str(Video.streams.filter(resolution=RisoluzioneVideo, only_video=True).first().filesize))

    if os.path.exists(f"{path_Salva_Video}/video.mp4"): #se file esiste elimino
        os.remove(f"{path_Salva_Video}/video.mp4")
    video = Video.streams.filter(res=RisoluzioneVideo, only_video=True).first().download(f'{path_Salva_Video}')
    os.rename(video, f'{path_Salva_Video}/video.mp4')

    if os.path.exists(f"{path_Salva_Video}/audio.mp4"): #se file esiste elimino
        os.remove(f"{path_Salva_Video}/audio.mp4")
    audio = Video.streams.filter(only_audio=True).first().download(f'{path_Salva_Video}')    
    os.rename(audio, f'{path_Salva_Video}/audio.mp4')
    input_video = ffmpeg.input(f'{path_Salva_Video}/video.mp4')
    input_audio = ffmpeg.input(f'{path_Salva_Video}/audio.mp4')

    nome = input("Nome del video: ")
    if nome == "": #Nome non valido
        showinfo("DEVI SCRIVERE IL NOME DEL FILE 111!!!", "Nome non valido.")
        return
    try:  #try-catch in caso utente smanettasse nei file  
        ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'{path_Salva_Video}/{nome}.mp4').run()
        os.remove(f"{path_Salva_Video}/audio.mp4")
        os.remove(f"{path_Salva_Video}/video.mp4")
        showinfo("FINITO", "VIDEO SCARICATO CON SUCCESSO")
    except:
        showinfo("Errrore", "file non trovati o non è stato possibile unire i video")
        return
        


#                           -------------FINE CODICE-------------                          #





#                           -------------LAYOUT-------------                          #
     
root = Tk()
root.resizable(False, False)
root.title("YTB DOWNLOADER  1.0V")
root.iconbitmap("./assets/youtube.ico")
root.geometry("600x450")
font = ('verdana', 20)

# Icona
File = PhotoImage(file = "./assets/youtube.png")
Icona = Label(root, image=File)
Icona.pack(side=TOP, pady=3)
# Input URL
UrlInp = Entry(root, font=font, justify=CENTER)
UrlInp.pack(side=TOP, fill=X, padx=10)
UrlInp.focus()
# Download Btn
downloadBtn = Button(root, text="Download Video", font=font, relief='ridge', command=Download)
downloadBtn.pack(side=TOP, pady=20)
# ComboBox 

box_value=StringVar()
Combo = ttk.Combobox(root, textvariable=box_value, state='readonly')
Combo.pack(pady=20)
Combo["values"] = ["144p","360p","480p","720p","1080p","1440p","2160p","4320p"]

root.mainloop()
#                           -------------FINE LAYOUT-------------                          #                       
