from pynput.keyboard import Key, Listener
import threading


def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
def thread_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:listener.join()

heyListen = threading.Thread(target=thread_listen)

heyListen.start()