from pynput.keyboard import Key, Listener,KeyCode
import threading
import sys
import pyautogui as pya
import pyperclip
import time


def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()    


def on_press(key):
    print(key)
    
def on_release(key):
    # print('{0} release'.format(key.char))
    
    # if key.format(key.char) == 'a':
    #     
    if key == KeyCode(vk = 0, char='1'):
        clippy = copy_clipboard()
        print(clippy)
        
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
def thread_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:listener.join()

heyListen = threading.Thread(target=thread_listen)

heyListen.start()
