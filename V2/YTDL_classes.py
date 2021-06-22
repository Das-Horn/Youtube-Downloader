import pytube
import ffmpeg
import json
import os
import tempfile
from pathlib import Path


class video:
    def __init__(self, link=str(), prog_fun=object()) -> None:
        self.__link = link
        self.__current_file_size = int()
        self.__tmp_path = tempfile.TemporaryDirectory().name
        self.__main_path = os.path.join(str(Path.home()), "Videos", "YTDL")
        self.__Title = str()
        self.__thumbnail = str()
        self.__yt = pytube.YouTube(self.__link,on_progress_callback=prog_fun)

        self.__init_file_sys()
    # Init Methods

    def __init_file_sys(self):
        folders = [
            self.__main_path,
            os.path.join(self.__main_path, "Video"),
            os.path.join(self.__main_path, "Audio")
        ]
        for x in folders:
            if os.path.isdir(x):
                print("Found directory:\t"+x)
            else:
                try:
                    os.mkdir(x)
                except Exception as e:
                    print("Encountered an exception while creating file system:\t"+e)
        return

    def change_link(self, link):
        print("changing link of the video.")
        self.__link = link
        self.__yt = pytube.YouTube(link)
        print("finished updating variables:\nlink:\t" +
              self.__link+"\nupdating meta data now.")
        self.__set_meta(self.__yt)
        return

    # MetaData methods
    def __set_meta(self, yt):
        stream = yt.streams
        self.__thumbnail = yt.thumbnail_url
        stream = stream.filter(adaptive=True).first()
        self.__Title = stream.title
        print("new meta set:\nthumb:\t" +
              self.__thumbnail+"\nname:\t"+self.__Title)
        return

    def get_meta(self):
        """Method to get the video title and thumbnail./,
        Returns an array
        """
        self.__set_meta(self.__yt)
        return [self.__Title, self.__thumbnail]

    # Downloading methods
    def download(self, Aud=bool()):
        print("Downloading Video")
        try:
            yt_streams = self.__yt.streams
            yt_title = yt_streams.get_audio_only().default_filename
            self.__current_file_size = yt_streams.get_audio_only().filesize
            yt_title = yt_title[:-4]
            self.__audio_dl(yt_title, yt_streams)
            self.__convert_audio(yt_title)
            if Aud == False:
                self.__video_dl(yt_title, yt_streams)
            self.__video_post(yt_title, Aud)
            print("Finished Downloading video")
        except Exception as e:
            print("Video download has failed:\t"+str(e))
        return

    def __audio_dl(self, title, streams):
        streams.get_audio_only().download(self.__tmp_path)
        return

    def __video_dl(self, title, streams):
        vid_stream = streams.filter(adaptive=True).first()
        vid_stream.download(self.__tmp_path)
        return

    def __video_post(self, title, Aud):
        if Aud:
            os.system(
                'copy "'+os.path.join(self.__tmp_path, title+".mp3")+'" "' +
                os.path.join(self.__main_path, "Audio", title+".mp3")+'"'
            )
            return
        else:
            ffmpeg.concat(
                ffmpeg.input(os.path.join(self.__tmp_path, title+".mp4")),
                ffmpeg.input(os.path.join(self.__tmp_path, title+".mp3")),
                v=1,
                a=1
            ).output(
                os.path.join(self.__main_path, "Video", title+".mp4")
            ).run()
            os.system(
                'copy "'+os.path.join(self.__tmp_path, title+".mp4")+'" "' +
                os.path.join(self.__main_path, "Audio", title+".mp3")+'"'
            )
            pass
        return

    def __convert_audio(self, title):
        ffmpeg.input(
            os.path.join(self.__tmp_path, title+".mp4")).output(
                os.path.join(self.__tmp_path, title+".mp3")).run()

    # IO Methods
    def get_link(self):
        return self.__link

    # def change_link(self, link=str()):
    #     self.__link = link

    def get_temp_dir(self):
        return self.__tmp_path

    def get_main_dir(self):
        return self.__main_path
    
    def get_file_size(self):
        return self.__current_file_size


class settings:
    def __init__(self) -> None:
        # init vars
        self.__data_path = "Data.json"
        self.__data = dict()

        # init methods
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
            tmp = {"videos": []}
            with open(self.__data_path, "w") as data_file:
                data_file.writelines(json.dumps(tmp))

    def save_data(self):
        try:
            with open(self.__data_path, "r") as data_file:
                data_file.writelines(json.dumps(self.__data))
        except Exception as e:
            print("Encountered an error while saving the data file:\t"+str(e))

    def get_queue(self):
        """A method to read from the queue"""
        return self.__data

    def write_queue(self, data=dict()):
        """A method to write to the queue"""
        self.__data = data


class queue:
    def __init__(self) -> None:
        self.__queue = []
        self.__running = False

    def set_queue(self, data=list()):
        self.__queue = data

    def get_queue(self):
        return self.__queue


def main():
    Set = settings()
    print(Set.get_queue())
    Vid = video("https://youtu.be/l0CbhG-P1UA")
    Vid.download(False)
    pass


if __name__ == "__main__":
    main()
