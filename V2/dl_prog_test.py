from YTDL_classes import *

def on_progress(obj1,obj2,prog):
    size = vid.get_file_size()
    current_progress = (size-prog)/size * 60
    print("current progress in %:\t"+str(current_progress))

vid = video("https://youtu.be/E9-F83up6gw",on_progress)
vid.download(Aud=True)