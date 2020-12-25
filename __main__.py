import ini.keez
import ini.tkgui
import threading

keez = threading.Thread(target=ini.keez)
tkgui = threading.Thread(target=ini.tkgui)

def ini():
    print('The main function')

initi = threading.Thread(target=ini)

def main():
    initi.start()
    tkgui.start()
    keez.start()
    
 
if __name__ == '__main__':
    main()