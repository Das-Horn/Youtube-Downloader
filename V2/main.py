from cef_ui import create_browser_instance
from YTDL_classes import *

def init_ui():
    cef_ui = create_browser_instance()
    cef_ui.init_javascript_bindings()
    cef_ui.set_javascript_bindings()
    cef_ui.start()
    return

def main():
    init_ui()
    return

if __name__ == "__main__":
    main()