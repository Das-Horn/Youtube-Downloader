import eel
import pytube
import time
import os
import threading
import sys
import shutil
import subprocess
from mhmovie import Movie
from mhmovie import Music


#Declare Global Variables here
#%%
url = " "
mp3Toggle = False
vidToggle = False
Hdirect = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
path = Hdirect+'\\YTDL Videos'
Check = os.path.isdir(path)
audioPath = path+'\\audio'
vidPath = path+'\\vid'
#%%
#Get Youtube video info
#---------------------------------------------
@eel.expose
def getYTTitle(id):
    youtube = pytube.YouTube(id)
    video = youtube.streams
    video = video.filter(adaptive=True).first()
    Vidtitle = video.title
    print(Vidtitle)
    return Vidtitle


#Functionality thread functions below
#They handle all the background processing
def checkFileStruc():
    eel.LChecks("Checking File structure..",False)()
    print('Checking File structure')    
    if Check == False :
        print('Creating directorys')
        os.mkdir(path)
        os.mkdir(path+'\\vid')
        os.mkdir(path+'\\audio')
        os.mkdir(path+'\\Assets')
        imgRecover()
    eel.LChecks("Checking Assets...",False)()
#    if not os.path.isfile(path+'\\Assets\\icon.png'):
#        print("Downloading Img")                           From Tkinter version need to change
#        imgRecover()

    print("Changing Directories")
    os.chdir(path)
    eel.sleep(1)
    return

def imgRecover():
    eel.LChecks("Downloading Assets..",False)()
    os.chdir(path+'\\Assets')
    os.system('curl https://i.ibb.co/dBG1KRb/icon.png --output icon.png')
    os.chdir(path)
    eel.sleep(3)
    return

def check_ffmpeg():
#    """Windows only"""
    eel.LChecks("Checking FFMPEG installation..",False)()
    files = ("ffmpeg", "ffprobe", "ffplay")
    if not all([shutil.which(f) for f in files]): # Return the path to an executable which would be run if the given cmd was called. If no cmd would be called, return None.
        print("FFmpeg install not found")
        return False
    else:
        print("FFmpeg install found")
        eel.sleep(1)
        return True 

def youtubeVidDl():
    #set Variables
    print("\nURL:\t"+url+"\nMP3:\t"+str(mp3Toggle)+"\nVID::\t"+str(vidToggle))

    #Download Video
    if not url or url == '' or url == ' ':
        eel.LoadingScreen(0)
        return
    if mp3Toggle == 1:
        videoToMp3()
        return
    print("Begining video download")
    youtube = pytube.YouTube(url)
    video = youtube.streams
    video.get_audio_only().download(audioPath)
    Audtitle = video.get_audio_only().default_filename
    video = video.filter(adaptive=True).first()
    Vidtitle = video.default_filename
    video.download(vidPath)
    eel.setProgressBar("35%")
    #post proccessing
    FFmpegPost(vidPath+'\\'+Vidtitle,audioPath+'\\'+Audtitle,path+"\\"+Vidtitle)
    eel.setProgressBar("65%")
    print("Finished Rendering the video...Begining audio processing")
    VToMp3Post(Audtitle)
    #Loading screen Progress
    eel.setProgressBar("100%")
    eel.sleep(2)
    eel.LoadingScreen(0)
    eel.sleep(1)
    eel.setProgressBar("0%")
    return

def videoToMp3():
    print("Will download and convert audio file now.")
    if not url:
        return
    youtube = pytube.YouTube(url)
    video = youtube.streams
    video.get_audio_only().download(audioPath)
    Audtitle = video.get_audio_only().default_filename
 #   Audtitle2 = video.get_audio_only().title
    #post proccessing
    eel.setProgressBar("75%")
    VToMp3Post(Audtitle)
    eel.setProgressBar("100%")
    eel.sleep(2)
    eel.LoadingScreen(0)
    eel.sleep(1)
    eel.setProgressBar("0%")
    return

#Post Processing for ffmpeg videos
def FFmpegPost(Film,Aud,Out):
    os.system('ffmpeg -i "'+Film+'" -i "'+Aud+'" -c:v copy -c:a aac "'+Out+'"')
    return

#Audio processing functions
def VToMp3Post(Audtitle):
    #Here we will process all audio clips to mp3 versions
    cwd = os.getcwd()
    if cwd != audioPath:
        os.chdir(audioPath)
    Audtitle2 = Audtitle
    if Audtitle2.endswith('.mp4'):
        Audtitle2 = Audtitle2[:-4]
    print('We have recieved the variables '+Audtitle+' and '+Audtitle2)
    mu = Music(audioPath+'\\'+Audtitle)
    mu.save(Audtitle2+".mp3")
    cmd1 = 'ren extract.mp3 "'+Audtitle2+'.mp3"'
    eel.setProgressBar("85%")
    os.system('dir /w')
    os.system(cmd1)
    os.chdir(path)
    fileCleanup()
    print("Finished all processes")
    return

def fileCleanup():
    #Function to clean unessecary files
    cmd = "del *.mp4"
    cwd = os.getcwd()

    if cwd != audioPath:
        os.chdir(audioPath)
    os.system(cmd)

    if vidToggle == 1:
        os.chdir(vidPath)
        os.system(cmd)
    os.chdir(path)
    return

@eel.expose
def openFileLocation():
    print("Opening File explorer, path:\t"+path)
    os.system(r'explorer \select,"'+path+'"')
#    subprocess.Popen(r'explorer /select,"'+path+r'\"')
    return

#UI thread functions below
#Have all the front end user interactions  
@eel.expose  
def setUrl(urlIn,mp3State,vidState):
    #Write Global Var's

    global url
    global mp3Toggle
    global vidToggle
    print("Updating variables")
    url = urlIn
    mp3Toggle = mp3State
    vidToggle = vidState

    #Start threading
    vidDL = threading.Thread(target=youtubeVidDl,args=())
    print("Starting BC thread")
    vidDL.start()
    print("\nJoining BC thread")
    vidDL.join()
    return

def uiInit():
    eel.start('index.html', block=False)
    eel.sleep(5)
    eel.spawn(LoadInit)
    KeepLive()
    return

def KeepLive():
    while True:
        print("Thread Check")
        eel.sleep(60)
    return

def LoadInit():
    FFMpeg = check_ffmpeg()
    if FFMpeg == False:
        sys.exit(0)
    checkFileStruc()
    eel.LChecks("",True)()
    return

#main function's

def jsUpdate():
    print("updatetasks")
#    eel._import_js_function("LChecks")
    print("--------------------------------")
    print(eel._js_functions) # it print []
    print("--------------------------------")
    return

def startUI():
    x = threading.Thread(target=uiInit,args=())
    print("Starting UI thread")
    x.start()
    print("Joining UI thread")
    x.join()
    return

def main():
    eel.init('www')
    jsUpdate()
    startUI()
    return


if __name__ == "__main__":
    main()
    sys.exit(1)
# %%
