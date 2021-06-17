from os import link
from typing import ValuesView
from cef_ui import create_browser_instance
from YTDL_classes import *

def create_instance(js_callback=None ,link=str()):
    vid.change_link(link)
    data = vid.get_meta()
    if js_callback:
        js_callback.Call(data)
    else:
        return data

def init_ui():
    cef_ui = create_browser_instance()
    cef_ui.init_javascript_bindings()
    cef_ui.add_javascript_bindings("getVidData",create_instance)
    cef_ui.set_javascript_bindings()
    cef_ui.start()
    return

def main():
    init_ui()
    return

if __name__ == "__main__":
    vid = video("https://youtu.be/Fk6grF2gVbk")
    main()