from cefpython3 import cefpython as cef
import platform
import sys

import cefpython3


class create_browser_instance:
    def __init__(self):
        self.bindings = ""
        settings = {
            "debug": True,
            "log_severity": cef.LOGSEVERITY_INFO,
            "log_file": "debug.log",
        }
        switches = {
            "disable-web-security": ""
            # "remote-debugging-port": "7654"
        }
        self.check_versions()
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize(settings=settings,switches=switches)
        self.browser = cef.CreateBrowserSync(url="file:///www/index.html",
                            window_title="Youtube Video Downloader")

    def start(self):
        cef.MessageLoop()
        cef.Shutdown()

    def check_versions(self):
        ver = cef.GetVersion()
        print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
        print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
        print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
        print("[hello_world.py] Python {ver} {arch}".format(
            ver=platform.python_version(),
            arch=platform.architecture()[0]))
        assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"
    
    def init_javascript_bindings(self):
        self.bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
    
    def add_javascript_bindings(self,JSname,PYfunc):
        self.bindings.SetFunction(JSname, PYfunc)
    
    def set_javascript_bindings(self):
        self.browser.SetJavascriptBindings(self.bindings)
    
    def exec_func(self,func=str(),*arg):
        self.browser.ExecuteFunction(func,arg)



if __name__ == "__main__":
    win = create_browser_instance()