from asyncio import streams
from pytube import YouTube
import os




def mp4(LINK:str):
    print('TéLéchargement de la vidéo...')
    YouTube(f'{LINK}').streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path='./Video')
    print('Téléchargement terminé!!')

def mp3(LINK:str):
    print("TéLéchargement de l'audio...")
    YouTube(f'{LINK}').streams.filter(only_audio=True).first().download(output_path='./Audio')
    
    print('Téléchargement terminé!!')


selection = input('Veuillez choisir une option: \n 1: Télécharger une vidéo \n 2: Télécharger un audio \n 3: Quitter\n--> ')
if selection == '1':
    mp4(str(input('Youtube Video Link: ')))
elif selection == '2':
    mp3(str(input('Youtube Video Link: ')))
elif selection == '3':
    print('Au revoir')
    quit()


