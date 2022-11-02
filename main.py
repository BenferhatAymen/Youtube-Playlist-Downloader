import os 
from pytube import YouTube,Playlist
import time
from random import randint

#------------------------------------------------------
Header = """\
      $$\     $$\                $$$$$$$$\        $$\                        $$$$$$\                      $$\            $$\     
      \$$\   $$  |               \__$$  __|       $$ |                      $$  __$$\                     \__|           $$ |    
       \$$\ $$  /$$$$$$\  $$\   $$\ $$ |$$\   $$\ $$$$$$$\   $$$$$$\        $$ /  \__| $$$$$$$\  $$$$$$\  $$\  $$$$$$\ $$$$$$\   
        \$$$$  /$$  __$$\ $$ |  $$ |$$ |$$ |  $$ |$$  __$$\ $$  __$$\       \$$$$$$\  $$  _____|$$  __$$\ $$ |$$  __$$\\_$$  _|  
         \$$  / $$ /  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |       \____$$\ $$ /      $$ |  \__|$$ |$$ /  $$ | $$ |    
          $$ |  $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|      $$\   $$ |$$ |      $$ |      $$ |$$ |  $$ | $$ |$$\ 
          $$ |  \$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\       \$$$$$$  |\$$$$$$$\ $$ |      $$ |$$$$$$$  | \$$$$  |
          \__|   \______/  \______/ \__| \______/ \_______/  \_______|       \______/  \_______|\__|      \__|$$  ____/   \____/ 
                                                                                                              $$ |               
                                                                                                              $$ |               
                                                                                                              \__|               
                                                                                        By : Hadjaymen Baroud
    """
for line in Header.splitlines() :
    print(line)
    time.sleep(0.07)
url = input("Input The Playlists's Url : ")
playlistVideos = Playlist(url)
path = os.path.abspath(os.getcwd())
if playlistVideos !=[]:

    try : 
        os.makedirs(path+"\Playlist")
    except : 
        os.makedirs(path+"\Playlist"+str(randint(0,3000)))
    print("Starting ... ")
    time.sleep(2)
    for i in playlistVideos : 
        print(f"Downloading : {YouTube(i).title} ...")
        YouTube(i).streams.get_highest_resolution().download(path+"\Playlist")
        print("Video Downloaded")
    print("Playlist Downloaded \n Enjoy !")
else :
    print("Empty Playlist")


