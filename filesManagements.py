import curses
import time
import os
from Player import Player
import Menus 
import pickle 
import datetime
import Main

def CreateNewFile(stdscr):
    current_dir = os.getcwd()
    # notOklen= True
    current_time = datetime.datetime.now()
    extension = getNewNameForFile()
    name ='/Saves/save'+'-'+str(extension)+'.save'
    

    # while(notOklen):
    #     # stdscr.clear()
    #     # stdscr.addstr(h//2,w//2,'Enter the name of file :')
    #     # stdscr.refresh()
    #     # h, w = stdscr.getmaxyx()
    #     # stdscr.addstr(0,0,'test')
    #     # name = stdscr.getstr(h//2 +3 ,w//2, 15)     
    #     # stdscr.addstr(0,0,name)
    #     # stdscr.refresh()


    #     if (len(name)<=0):
    #         # stdscr.clear()
    #         stdscr.addstr(h//2,w//2,'TEST')
    #         stdscr.addstr(0,0,name)
    #         stdscr.refresh()
    #         time.sleep(2)


    #     else :
            
    fileName = current_dir + name


    if(os.path.exists(fileName)):
        stdscr.clear()
        stdscr.addstr(0,0,'File already exists.')
        stdscr.refresh()
        time.sleep(2)
    else :
        stdscr.addstr(0,0,'File already exists.')
        stdscr.refresh()

        file = open(fileName, "wb+")
        file.close()
        return fileName


def SaveGame(fileName,p1,p2,game) :
    try :
        file = open(fileName,'wb')
        pickle.dump(p1, file, pickle.HIGHEST_PROTOCOL)
        pickle.dump(p2, file, pickle.HIGHEST_PROTOCOL)
        pickle.dump(game, file, pickle.HIGHEST_PROTOCOL)
        file.close()
        return True
    except Exception as e: 
        print(e)
        return False

    


# def checkForAvailableFiles(): 
#     files = os.listdir("./Saves")
#     files = [item.replace('.save','') for item in files if item.endswith('.save')]
#     if (len(files)):
#         print(len(files))
#         print('ok')
#         return True
#     return False

def getNewNameForFile(): 
    files =  os.listdir("./Saves")
    files = [item.replace('.save','') for item in files if item.endswith('.save')]
    return  len(files) + 1
        

def checkForAvailableFiles(): 
    files =  os.listdir("./Saves")
    files = [item.replace('.save','') for item in files if item.endswith('.save')]
    if (len(files)):
        return True
    return False




# def loadGame(stdscr):  
#     stdscr.clear()
#     h, w = stdscr.getmaxyx()
#     files = os.listdir()
#     files = [item.replace('.txt','') for item in files if item.endswith('.txt')]
#     stdscr.addstr(h//2 - 5, w//2,'Select your save to load :')
#     curses.curs_set(0) # turn off cursor blinking
#     curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
#     current_row = 0  # specify the current selected row 
#     Menus.menuWithCursos(stdscr, current_row,files)    # print the menu
#     val = 0
#     while 1:
#         key = stdscr.getch()
#         if key == curses.KEY_UP and current_row > 0:
#             current_row -= 1
#         elif key == curses.KEY_DOWN and current_row < len(files)-1:
#             current_row += 1

#         elif key == curses.KEY_ENTER :
#             current_dir = os.getcwd()
#             f = files[current_row] + '.txt'
#             fileName = current_dir + '/'+ f
#             stdscr.addstr(0,0,fileName)
#             stdscr.refresh()
#             time.sleep(6)
#             return fileName
#             # if user selected last row, exit the program
#         if current_row == len(files)-1:
#             break
#         Menus.menuWithCursos(stdscr, current_row,files)
        
def fileToGame(file):
    try : 
        f = open(file,'r')
        print(file)
        values = f.read().split('/')
    except: 
        pass




def readAndLaunchGame(stdscr,fileName):
    try :
        with open(fileName, 'rb') as gameToLoad:
            p1 = pickle.load(gameToLoad)
            p2= pickle.load(gameToLoad)
            game = pickle.load(gameToLoad)
            return p1,p2,game
    except  : 
        errorLoading(stdscr)


def errorLoading(stdscr):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(h//2,w//2 - int(len("Cannot load game because of Endomaged file")/2),"Cannot load game because of Endomaged file")
    stdscr.refresh() 
    time.sleep(3)
    Main.displayMainMenu(stdscr)






# current_dir = os.getcwd()
# fileName = current_dir + '/'+ 'ok123.txt'
# readAndLaunchGame(fileName)

# v = checkForAvailableFiles()
# print(v)

