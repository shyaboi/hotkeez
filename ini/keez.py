from pynput.keyboard import Key, Listener, KeyCode, HotKey
import threading
import sys
import pyautogui as pya
import pyperclip
import time

hotKeez = []
##################################hotkey testing#########################################
# def on_activate():
#     print('Global hotkey activated!')

# def for_canonical(f):
#     return lambda k: f(l.canonical(k))

# hotkey = HotKey(
#     HotKey.parse('<ctrl>+<alt>+h'),
#     on_activate)
# with Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as l:
#     l.join()
##################################hotkey testing#########################################


def get_capslock_state():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def get_scrolllock_state():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_SCROLL = 0x91
    return hllDll.GetKeyState(VK_SCROLL)


def copy_clipboard(i):
    pya.hotkey('ctrl', 'c')
    # time.sleep(.01)#TRY w/o sleep
    hotKeez.insert(i, pyperclip.paste())
    ok = hotKeez[i]
    return ok


def paste_clipboard(i):
    pya.press('backspace')
    pasty = hotKeez[i]
    pyperclip.copy(pasty)
    pya.hotkey('ctrl', 'v')
    # time.sleep(.01)  #TRY w/o sleep


def on_press(key):
    print(f'on press: {key}')


def on_release(key):
    if key == KeyCode(vk=0, char='1'):
        if get_scrolllock_state()==0:
            copy_clipboard(0)
            print(f'SL state: {get_scrolllock_state()}')
    if key == KeyCode(vk=0, char='1'):
        if get_scrolllock_state():
            print(f'SL state: {get_scrolllock_state()}')
            paste_clipboard(0)
    else:
        print(f'else:{key}')
    # if key == KeyCode(vk = 0, char='3'):
    #     copy_clipboard(1)
    #     print(get_scrolllock_state())
    # if key == KeyCode(vk = 0, char='4'):
    #     paste_clipboard(1)
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released


def thread_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


heyListen = threading.Thread(target=thread_listen)

heyListen.start()
