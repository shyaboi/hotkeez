from pynput.keyboard import Key, Listener,KeyCode
import threading
import sys
import pyautogui as pya
import pyperclip
import time

hotKeez = []

def get_capslock_state():
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)

def get_scrolllock_state():
    import ctypes
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_SCROLL = 0x91
    return hllDll.GetKeyState(VK_SCROLL)

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()    

def paste_clipboard():
    pya.press('backspace')
    pya.hotkey('ctrl', 'v')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster

def on_press(key):
    print(key)
    
def on_release(key):
    # print('{0} release'.format(key.char))
    
    # if key.format(key.char) == 'a':
    #     

    if key == KeyCode(vk = 0, char='1'):
        copy_clipboard()
        print(get_scrolllock_state())
    if key == KeyCode(vk = 0, char='2'):
        paste_clipboard()
   
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
def thread_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:listener.join()

heyListen = threading.Thread(target=thread_listen)

heyListen.start()
