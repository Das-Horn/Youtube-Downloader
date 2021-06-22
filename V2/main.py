from os import link
from typing import ValuesView
from cef_ui import create_browser_instance
from YTDL_classes import *
import threading

def create_instance(js_callback=None ,linkin=str()):
    print(linkin)
    vid.change_link(link=linkin)
    data = vid.get_meta()
    if js_callback:
        js_callback.Call(data)
    else:
        return data

def on_progress(obj1,obj2,prog,stat=None):
    if stat == None:
        size = vid.get_file_size()
        current_progress = int((size-prog)/size * 60)
        print("current progress in %:\t"+str(current_progress))
        print("uodating ui")
        cef_ui.exec_func("downloadProgress",current_progress)
    else:
        if stat == "proc":
            cef_ui.exec_func("downloadProgress",65)
        else:
            cef_ui.exec_func("downloadProgress",100)

def download_video(js_callback=None,mp3=bool()):
    print("downloading video now")
    dl = threading.Thread(target=vid.download,daemon=True,args=[mp3])
    dl.start()
    return

def video_dl_prog(prog=int()):
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
    cef_ui.set_javascript_bindings()
    cef_ui.start()
    return

def main():
    init_ui()
    return

if __name__ == "__main__":
    js_prog_func = None
    cef_ui = create_browser_instance()
    vid = video("https://youtu.be/Fk6grF2gVbk",on_progress)
    main()