from pytube import YouTube
import os

def BaixarVídeo(self):
    print ("Iniciando...")
    print ("Titulo: "+youtube.title)

    video=youtube.streams.get_highest_resolution(pro)
    video.download()
    print("Baixado")

def BaixarAudio(self):
    print ("Iniciando...")
    print ("Titulo: "+youtube.title)

    video = youtube.streams.get_audio_only()
    arquivoinicial = video.download()
    base, ext = os.path.splitext(arquivoinicial)
    arquivofinal = base + '.mp3'
    os.rename(arquivoinicial, arquivofinal)
    print("Baixado")


url = input("Digite o link do YouTube: ")

youtube = YouTube(url)

resposta=input(print("O que voce deseja baixar? Digite 1 para video / Digite 2 para audio"))

if resposta == '1':
    BaixarVídeo(youtube)

if resposta == '2':
    BaixarAudio(youtube)