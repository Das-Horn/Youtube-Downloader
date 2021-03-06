from ctypes import *
from ctypes.wintypes import *
from os import path
import platform

LRESULT = c_int64 if platform.architecture()[0] == "64bit" else c_long

SendMessage = windll.user32.SendMessageW
SendMessage.restype = LRESULT
SendMessage.argtypes = [HWND, UINT, WPARAM, LPARAM]

GetModuleHandle = windll.kernel32.GetModuleHandleW
GetModuleHandle.restype = HMODULE
GetModuleHandle.argtypes = [LPCWSTR]

IMAGE_ICON = 1
LR_LOADFROMFILE = 0x00000010
LR_CREATEDIBSECTION = 0x00002000

LoadImage = windll.user32.LoadImageW
LoadImage.restype = HANDLE
LoadImage.argtypes = [HINSTANCE, LPCWSTR, UINT, c_int, c_int, UINT]

RelPath = lambda file : path.join(path.dirname(path.abspath(__file__)), file)


def AlterIcon(_hWnd, lpszIcon):

    WM_SETICON = 0x0080
    ICON_BIG = 1

    hModel = GetModuleHandle(None)
    hIcon = LoadImage(hModel,
                      RelPath(lpszIcon),
                      IMAGE_ICON,
                      0, 0,
                      LR_LOADFROMFILE | LR_CREATEDIBSECTION)


    SendMessage(_hWnd, WM_SETICON, ICON_BIG, hIcon)