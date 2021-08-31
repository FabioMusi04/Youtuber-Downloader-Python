#                           -------------LIBRERIE DA IMPORTARE-------------                          #
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
#                 -------------FINE LIBRERIE DA IMPORTARE-------------                          #



#                           -------------INIZIO CODICE-------------                          #

def Download():
    Ytb_Link = UrlInp.get()
    if Ytb_Link == '':
        return
    path_Salva_Video = askdirectory()
    if path_Salva_Video == "":
        return
    Video = YouTube(str(Ytb_Link))
    print("Titolo: " + Video.title)
    print("Numero di Views: " + str(Video.views))
    print("Rating video:  " + str(Video.rating))
    print("Canale:  " + Video.author)
    RisoluzioneVideo = str(Combo.get())
    if RisoluzioneVideo == "":
        return
    try:
        print("Peso del file video:  " + str(Video.streams.filter(res=RisoluzioneVideo).first().filesize))
        Video.streams.filter(res=RisoluzioneVideo).first().download(path_Salva_Video)
        showinfo("SUCCESSO","SCARICATO E SALVATO IN\n"+ path_Salva_Video)
    except:
        showinfo("FALLITO","RISOLUZIONE NON ADATTA O LINK ERRATO")
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
file = PhotoImage(file = "./assets/youtube.png")
Icona = Label(root, image=file)
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
