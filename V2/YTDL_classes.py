import pytube
import json
import os
import tempfile
from pathlib import Path

class video:
    def __init__(self,link=str()) -> None:
        self.__link = link
        self.__tmp_path = tempfile.TemporaryDirectory().name
        self.__main_path = os.path.join(str(Path.home()), "Videos", "YTDL")
        self.Title = str()
        self.__yt = pytube.YouTube(self.__link)
    
    # Init Methods     
    def __init_file_sys(self):
        if os.path.isdir(self.__main_path):
           print("File checks complete.")
        else:
            try:
                os.mkdir(self.__main_path)
            except Exception as e:
                print("Encountered an exception while creating file system:\t"+e) 
    
    #Downloading methods
    def download(self,Aud=bool()):

        return
    
    def __audio_dl(self):
        return
    
    def __video_dl(self):
        return
    
    #IO Methods
    def get_link(self):
        return self.__link
    
    def change_link(self,link=str()):
        self.__link = link
    
    def get_temp_dir(self):
        return self.__tmp_path
    
    def get_main_dir(self):
        return self.__main_path

class settings:
    def __init__(self) -> None:
        #init vars
        self.__data_path = "Data.json"
        self.__data = dict()
        
        #init methods
        self.__fetch_data()
        pass

    #   Methods to fetch data regarding queue of videos.
    def __fetch_data(self):
        """A function to initialize the queue data."""
        try:
            with open(self.__data_path, "r") as data_file:
                self.__data = json.loads(data_file.readlines())
        except Exception as e:
            print("No queue data found.\n creating file for queue data")
            tmp = { "videos":[]}
            with open(self.__data_path, "w") as data_file:
                data_file.writelines(json.dumps(tmp))
    
    def save_data(self):
        try:
            with open(self.__data_path, "r") as data_file:
                data_file.writelines(json.dumps(self.__data))
        except Exception as e:
            print("Encountered an error while saving the data file:\t"+e)
    
    def get_queue(self):
        """A method to read from the queue"""
        return self.__data
    
    def write_queue(self,data=dict()):
        """A method to write to the queue"""
        self.__data = data

def main():
    Set =  settings()
    print(Set.get_queue())
    pass

if __name__ == "__main__":
    main()