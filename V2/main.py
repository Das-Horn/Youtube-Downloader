from os import link, system
from typing import ValuesView
from cef_ui import create_browser_instance
from YTDL_classes import *
import threading
import subprocess

def create_instance(js_callback=None ,linkin=str()):
    print(linkin)
    vid.change_link(link=linkin)
    data = vid.get_meta()
    if js_callback:
        js_callback.Call(data)
    else:
        return data

def open_main_dir():
    dir = vid.get_main_dir()
    subprocess.run(f"explorer {dir}")

def on_progress(obj1,obj2,prog,stat=None):
    global second_download
    if stat == None and second_download == False:
        size = vid.get_file_size()
        current_progress = int((size-prog)/size * 60)
        print("current progress in %:\t"+str(current_progress))
        print("uodating ui")
        cef_ui.exec_func("downloadProgress",current_progress)
    else:
        if stat == "proc":
            cef_ui.exec_func("downloadProgress",65)
            second_download = True
        elif stat == "downVid":
            cef_ui.exec_func("downloadProgress",75)
        elif stat == "procVid":
            cef_ui.exec_func("downloadProgress",80)
        else:
            cef_ui.exec_func("downloadProgress",100)
            second_download = False

def download_video(js_callback=None,mp3=bool()):
    print("downloading video now")
    dl = threading.Thread(target=vid.download,daemon=True,args=[mp3])
    dl.start()
    return

def set_status():
    return

def set_prog(js_callback=None):
    print("Setting UI progression function\t\t"+str(js_callback))
    js_prog_func = js_callback

def init_ui():
    cef_ui.init_javascript_bindings()
    cef_ui.add_javascript_bindings("getVidData",create_instance)
    cef_ui.add_javascript_bindings("downloadVideo",download_video)
    cef_ui.add_javascript_bindings("setProg",set_prog)
    cef_ui.add_javascript_bindings("openFolder",open_main_dir)
    cef_ui.set_javascript_bindings()
    cef_ui.start()
    return

def main():
    init_ui()
    return

if __name__ == "__main__":
    second_download = False
    js_prog_func = None
    cef_ui = create_browser_instance()
    vid = video("https://youtu.be/Fk6grF2gVbk",on_progress)
    main()