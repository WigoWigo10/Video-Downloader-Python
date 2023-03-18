from pytube import YouTube
import os

def baixar_video(youtube):
    print("Iniciando.")
    print("Título: " + youtube.title)

    video = youtube.streams.get_highest_resolution()
    video.download()
    print("Baixado")

def baixar_audio(youtube):
    print("Iniciando...")
    print("Título: " + youtube.title)

    video = youtube.streams.get_audio_only()
    arquivo_inicial = video.download()
    base, ext = os.path.splitext(arquivo_inicial)
    arquivo_final = base + ".mp3"
    os.rename(arquivo_inicial, arquivo_final)
    print("Baixado")

url = input("Digite o link do YouTube: ")
youtube = YouTube(url)

resposta = input("O que você deseja baixar? Digite 1 para vídeo / Digite 2 para áudio: ")
if resposta == "1":
    baixar_video(youtube)
elif resposta == "2":
    baixar_audio(youtube)
else:
    print("Opção inválida.")

