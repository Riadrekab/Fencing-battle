
import os
import time
import Main

# def ReturnScene():
#     files =  os.listdir("./Scenes")
#     files = [item.replace('.ffscene','') for item in files if item.endswith('.ffscene')]
#     print(files)


def loadSceneFromFile(stdscr,scene,width):
    f = open(scene,'r')
    chars = f.read()
    if(('x' in chars or 'X' in chars)and ('1' in chars) and('2' in chars)):
        frames = chars.count('_')
        position1i = chars.find('1')
        position2i = chars.find('2')
        trapP = 0 
        position1 = position1i * int((width/frames))
        position2 = position2i * int((width/frames))
        f.close()
        if ('x' in chars or 'X' in chars):
            if('x' in chars):
                trapPi =  chars.find('x')
            else : 
                trapPi =  chars.find('X')
            trapP = trapPi * int((width/frames))
        return position1,position2,trapP
    else : 
        errorLoading(stdscr)

    

def errorLoading(stdscr):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(h//2,w//2 - int(len("Cannot load game because of Endomaged file")/2),"Cannot load game because of Endomaged file")
    stdscr.refresh() 
    time.sleep(3)
    Main.displayMainMenu(stdscr)