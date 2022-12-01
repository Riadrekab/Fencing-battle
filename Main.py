import curses
import multiprocessing
import os
import time
import threading
import os
from playsound import playsound
from Mouvements import *
from Player import Player 
from Game import Game
from display import *
from Menus import *
from filesManagements import *
from ScenesManagement import *


fileName = ''
saved = False
shape1 = ['O','_|_/','|','/|']
space = [0,1,0,1]
shape2= ['O','\_|_','|','|\x5c']
space2 = [0,2,0,0]
statesP1 = []
statesP2 = []

def CheckNewMouve(p1,p2,stdscr,frames=40,TrapP=0) :  
    global shape1
    global shape2
    global space2
    if(len(statesP1)): 
        if(statesP1[0]=='move'):
            p1.hauteur = 0
            statesP1.pop(0)

        elif(statesP1[0]=='jump' or (statesP1[0]=='jumpB')):
            statesP1.append('move')
            p1.hauteur = p1.mouvementRange
            
            if(statesP1[0]=='jump'):
                jumpPlayer1(p1,p2,TrapP)
            else : 
                jumpBackP1(p1,TrapP)
            statesP1.pop(0)
        elif(len(statesP1) and (statesP1[0]=='rest')):
                shape1 = ['O','_|_/','|','/|']
                statesP1.pop(0)
                if(p1.attack):
                    p1.position -=1

                    if(p2.attack):
                        shape2= ['O','\_|_','|','|\x5c']
                        p2.attack = False
                        p1.attack = False
                        p1.position = p1.initPosition
                        p2.position = p2.initPosition
                        statesP1.clear()
                        statesP2.clear()
                    elif((not p2.defense) and (p2.touched) ):
                        p1.score += 1
                        p1.position = p1.initPosition
                        p2.position = p2.initPosition
                        p2.touched = False
                        p1.attack = False   

                elif(p1.defense):
                    p1.defense = False



        elif(len(statesP1) and (statesP1[0]=='attack')):
                if(p1.position>TrapP):
                    if(p2.position-p1.position==5):
                        p1.position+=1
                        p2.touched = True
                    
                    elif(p2.position - p1.position -p1.attackRange >=6):
                        p1.position +=p1.attackRange
                    else : 
                        p1.position = p2.position - 4
                        p2.touched = True
                elif(p1.position<TrapP): 
                    if(p2.position-TrapP>=4):
                        if(p1.position +p1.attackRange >=TrapP):
                            p1.position = TrapP - 1
                        else : 
                            p1.position +=p1.attackRange 
                    else : 
                        p1.position = p2.position - 4
                        p2.touched = True



                shape1 = ['O','_|__','|','/|']
                # displayPlayers(p1,p2,stdscr,frames=frames,trapPos=TrapP)
                statesP1.pop(0)
                statesP1.append('rest')
        elif(len(statesP1) and (statesP1[0]=='block')):
                shape1 = ['O','_|_','| \x5c ','/|']
                p1.defense = True
                statesP1.pop(0)

    if(len(statesP2)) : 
        if(statesP2[0]=='move'):
            p2.hauteur = 0

            statesP2.pop(0)


        elif((statesP2[0]=='jump' or (statesP2[0]=='jumpB'))):
            statesP2.append('move')
            p2.hauteur = p2.mouvementRange
            
            if(statesP2[0]=='jump'):
                if(p2.position-p2.mouvementRange - (p1.position)>=6):
                    p2.position -= p2.mouvementRange
                else : 
                    p2.position = p1.position + 5
            else : 
                if(p2.position < frames -3):
                    p2.position += p2.mouvementRange
                else : 
                    p2.position = frames - 1
            statesP2.pop(0)
        elif( (statesP2[0]=='rest')):
            shape2= ['O','\_|_','|','|\x5c']
            if(p2.attack):
                p2.position +=1
                p2.attack = False
                if( not p1.defense and not p1.attack and p1.touched):
                    p2.score += 1
                    p1.position = p1.initPosition
                    p2.position = p2.initPosition
                    p1.touched = False
                    
            elif(p2.defense):
                p2.defense = False
            statesP2.pop(0)






        elif( (statesP2[0]=='attack')):
            p2.attack = True
            
            if(p2.position<TrapP):
                if(p2.position-p2.attackRange - p1.position > 5):
                    p2.position -=p2.attackRange
                elif(p2.position-p2.attackRange - p1.position  <=5):
                    p2.position = p1.position + 4
                    p1.touched = True
            elif(p2.position>TrapP): 
                if(TrapP-p1.position>=4):
                    if(p2.position -p2.attackRange <=TrapP):
                        p2.position = TrapP + 1
                    else : 
                        p2.position -=p2.attackRange 
                else : 
                    p2.position = p1.position + 4
                    p1.touched = True
            

            shape2= ['O','__|_','|','|\x5c']
            statesP2.pop(0)
            statesP2.append('rest')
            # displayPlayersForP2(p1,p2,stdscr,frames=frames,trapPos=TrapP)
        elif( (statesP2[0]=='block')):
            shape2= ['O','_|_','/ |','|\x5c']
            space2 =[0,1,2,0]
            p2.defense = True
            statesP2.pop(0)
    if(p2.attack and p1.touched):
        displayPlayersForP2(p1,p2,stdscr,frames=frames,trapPos=TrapP)
    else : 
        displayPlayers(p1,p2,stdscr,frames=frames,trapPos=TrapP)


            

def displayPlayers(p1,p2,stdscr=0,frames=40,trapPos=0):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    i = 0
    j=int(h/2)-3
    try : 
        stdscr.addstr(2,10,str(p1.score))
        stdscr.addstr(2,frames-10,str(p2.score))
        stdscr.addstr(j-p1.hauteur-2,p1.position,'P1')
        stdscr.addstr(j-p2.hauteur-2,p2.position,'P2')
    except Exception as e: 
        stdscr.addstr(h//2, w//2,'Fichier endomagé.')
        time.sleep(2)
        displayMainMenu(stdscr)


    for elem in shape1: 
        val1 = j - p1.hauteur 
        val2 = j - p2.hauteur
        stdscr.addstr(val1,p1.position-space[i],shape1[i])
        stdscr.addstr(val2,p2.position-space2[i],shape2[i])
        i = i+1
        j=j+1
    try:
        for k in range(frames) : 
            stdscr.addstr(j,k,'-')
    except  : 
        stdscr.addstr(h//2, w//2,'Fichier endomagé.')
        time.sleep(2)
        displayMainMenu(stdscr)

    
    if (trapPos):
        stdscr.addstr(j,trapPos,'X')
        stdscr.addstr(j-1,trapPos,'X')

        




def displayPlayersForP2(p1,p2,stdscr,hauteurP1=0,hauteurP2=0,frames=40,trap=False,trapPos=0):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    i = 0
    j=int(h/2)-3
    stdscr.addstr(0,0,str(p1.score))
    stdscr.addstr(0,frames,str(p2.score))


    stdscr.addstr(6-p1.hauteur,p1.position,'P1')
    stdscr.addstr(6-p2.hauteur,p2.position,'P2')

    for elem in shape1: 
        val1 = j - p1.hauteur
        val2 = j - p2.hauteur
        stdscr.addstr(val2,p2.position-space2[i],shape2[i])
        stdscr.addstr(val1,p1.position-space[i],shape1[i])
        i = i+1
        j=j+1
    for k in range(frames) : 
        stdscr.addstr(j,k,'-')
    
    if (trapPos):
        stdscr.addstr(j,trapPos,'X')
        stdscr.addstr(j-1,trapPos,'X')




def musicPlayer():
    try : 
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        audio_file_path = os.path.join(BASE_DIR, 'music.mp3')
        while(1):
            playsound(audio_file_path)
            playsound()
    except Exception as e : 
        pass
        


def launchAttackP1(p1,stdscr): 
    try:
        global statesP1
        p1.attack = True
        statesP1.append('attack')
    except Exception as e:
        stdscr.addstr(0,0,str(e))
        stdscr.refresh()
        exit()

def launchAttackP2(p2,stdscr):
    try:
        global statesP2
        p2.attack = True



        statesP2.append('attack')
    except Exception as e:
        stdscr.addstr(0,0,str(e))
        stdscr.refresh()
        exit()





def disableBlockP1():
    global shape1
    global statesP1
    shape1 = ['O','_|_/','|','/|']
    statesP1.append('rest')

def disableBlockP2():
    global shape2
    global space2
    global statesP2
    space2 = [0,2,0,0]

    shape2= ['O','\_|_','|','|\x5c']
    statesP2.append('rest')
    
    
def printNotAvailable(stdscr):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(h//2,w//2, "No available files")
    stdscr.refresh()
    
    time.sleep(3)


def launchNewGame(stdscr,trap) :
    h, w = stdscr.getmaxyx()
    pos1,pos2,trapP=loadScene(stdscr)
    p1 = Player(pos1,4,3,2,2,200)
    p2 = Player(pos2,1,4,3,1,100)
    game = Game(0,20,w-1)
    stdscr.clear()
    if (trap):
        game.trapP = trapP

    main(stdscr,p1,p2,game)


def displayPause(stdscr,p1,p2,game): 
    global fileName
    global saved
    menu = ['Continue','Save Game', 'Controls','Exit']
    stdscr.clear()   
    curses.curs_set(0) # turn off cursor blinking
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    current_row = 0  # specify the current selected row 
    menuWithCursos(stdscr, current_row,menu)    # print the menu
    val = 0
    while 1:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if (current_row == 0): 
                main(stdscr,p1,p2,game)
            elif (current_row == 1): # LOAD GAME
                saved = SaveGame(fileName,p1,p2,game)
            elif (current_row == 2): # LOAD GAME
                displayControlsInGame(stdscr,p1,p2,game)
            elif(current_row==3):
                if(not saved):
                    os.remove(fileName)
                
                displayMainMenu(stdscr)
            stdscr.refresh()


            
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        menuWithCursos(stdscr, current_row,menu)

def loadGame(stdscr):  
    global fileName
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    files =  os.listdir("./Saves")
    files = [item.replace('.save','') for item in files if item.endswith('.save')]
    stdscr.addstr(h//2 - 5, w//2,'Select your save to load :')
    curses.curs_set(0) # turn off cursor blinking
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    current_row = 0  # specify the current selected row 
    Menus.menuWithCursos(stdscr, current_row,files)    # print the menu
    val = 0
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files)-1:
            current_row += 1

        elif key == 10 :
            current_dir = os.getcwd()
            f = files[current_row] + '.save'
            fileName = current_dir + '/Saves/'+ f
            p1,p2,game= readAndLaunchGame(stdscr,fileName)
            main(stdscr,p1,p2,game)
            # if user selected last row, exit the program
        
        Menus.menuWithCursos(stdscr, current_row,files)


def loadScene(stdscr):  
    global fileName
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    files =  os.listdir("./Scenes")
    files = [item.replace('.ffscene','') for item in files if item.endswith('.ffscene')]
    stdscr.addstr(h//2 - 5, w//2,'Select your save to load :')
    curses.curs_set(0) # turn off cursor blinking
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    current_row = 0  # specify the current selected row 
    Menus.menuWithCursos(stdscr, current_row,files)    # print the menu
    val = 0
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files)-1:
            current_row += 1

        elif key == 10 :
            current_dir = os.getcwd()
            f = files[current_row] + '.ffscene'
            fileScene = current_dir + '/Scenes/'+ f
            p1,p2,trap = loadSceneFromFile(stdscr,fileScene,w)
            return p1,p2,trap
            # if user selected last row, exit the program
        
        Menus.menuWithCursos(stdscr, current_row,files)


def main(stdscr,p1,p2,game):
    stdscr.refresh()
    curses.curs_set(0) 
    fps = game.fps
    frames = game.frames
    TrapP= game.trapP
    displayPlayers(p1,p2,stdscr,frames=frames,trapPos=TrapP)
    refreshDelay = time.time() + 1/fps
    i = 0
    while(True):
        stdscr.timeout(0)   # Pour ne pas bloquer le programme pendant qu'il attend des inputs
        v=stdscr.getch()
        if(time.time()>refreshDelay):
            CheckNewMouve(p1,p2,stdscr,frames,TrapP=TrapP)
            refreshDelay = time.time() + 1/fps
        # Deplacements  de droite et gauche
        if(v==27):
            stdscr.clear()
            displayPause(stdscr,p1,p2,game)

        if(v==ord('d')):
            moveForwardP1(p1,p2,TrapP)
            statesP1.append('move')
        if(v==ord('q')):
            moveBackP1(p1,TrapP)
            statesP1.append('move')

        if(v==curses.KEY_RIGHT):
            moveBackP2(p2,TrapP,frames)
            statesP2.append('move')

        if(v==curses.KEY_LEFT):
            moveForwardP2(p1,p2,TrapP,stdscr)
            statesP2.append('move')
        #Saut
        if(v==ord('e')):
            statesP1.append('jump')
        if(v==ord('a')):
            statesP1.append('jumpB')
        if(v==curses.KEY_UP):
            statesP2.append('jump')
        if(v==curses.KEY_DOWN):
            statesP2.append('jumpB')
        #ATTAQUE
        if(v==ord('z')):
            timer = threading.Timer(1/p1.attackSpeed, launchAttackP1,args=(p1,stdscr))
            timer.start()
        if(v==ord('o')):
            timer = threading.Timer(1/p2.attackSpeed, launchAttackP2,args=(p2,stdscr))
            timer.start()

        if(v== ord('s')):
            statesP1.append('block')
            timer = threading.Timer(p1.blockTime, disableBlockP1)
            timer.start()
        if(v== ord('p')):
            statesP2.append('block')
            timer = threading.Timer(p2.blockTime, disableBlockP2)
            timer.start()





def displayMainMenu(stdscr): 
    global fileName
    menu = ['New Game','New Game With Trap', 'Load Game', 'Controls', 'Exit']
    stdscr.clear()   
    curses.curs_set(0) # turn off cursor blinking
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    current_row = 0  # specify the current selected row 
    menuWithCursos(stdscr, current_row,menu)    # print the menu
    val = 0
    while 1:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if (current_row == 0): 
                fileName = CreateNewFile(stdscr)
                launchNewGame(stdscr,0)
            elif (current_row == 1): 
                fileName = CreateNewFile(stdscr)
                launchNewGame(stdscr,1)
            elif (current_row == 2):
                if(checkForAvailableFiles()): 
                    fileName = loadGame(stdscr)
                else : 
                    printNotAvailable(stdscr)
                    displayMainMenu(stdscr)
            elif (current_row == 3): 
                displayControls(stdscr)
            elif (current_row == 4): 
                exit()
            stdscr.refresh()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        menuWithCursos(stdscr, current_row,menu)
          

def displayControls(stdscr) :
    ControlsP1 = ['For player 1 :','','Move right : D','Move left : Q','Block Attack : S','Jump right : E','Jump left : A','Attack : Z','','','Click on "M" to show Controls for Player 2','','Click on "A" to show main menu']
    ControlsP2 = ['For player 2 :','','Move right : Right Arrow','Move left : Left Arrow','Block Attack : P','Jump right : Up Arrow','Jump left : Down Arrow','Attack : O','','','Click on "M" to show Controls for Player 1','','Click on "A" to show main menu']
    currentMenu = ControlsP1
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    menuWithoutCursor(stdscr, currentMenu)    # print the menu
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_BACKSPACE or key ==ord('a') or key ==ord('A') or key == 27:
            displayMainMenu(stdscr)

        if key == ord('m') :
            if(currentMenu == ControlsP1):
                currentMenu =ControlsP2
            else : 
                currentMenu = ControlsP1
            stdscr.clear()
            menuWithoutCursor(stdscr, currentMenu)    # print the menu
            stdscr.refresh()


    
def displayControlsInGame(stdscr,p1,p2,game) :
    ControlsP1 = ['For player 1 :','','Move right : D','Move left : Q','Block Attack : S','Jump right : E','Jump left : A','Attack : Z','','','Click on "M" to show Controls for Player 2','','Click on "A" to show menu']
    ControlsP2 = ['For player 2 :','','Move right : Right Arrow','Move left : Left Arrow','Block Attack : P','Jump right : Up Arrow','Jump left : Down Arrow','Attack : O','','','Click on "M" to show Controls for Player 1','','Click on "A" to show menu']
    currentMenu = ControlsP1
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # color scheme for selected row
    menuWithoutCursor(stdscr, currentMenu)    # print the menu
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_BACKSPACE or key ==ord('a') or key ==ord('A') or key ==27:
            displayPause(stdscr,p1,p2,game)

        if key == ord('m') :
            if(currentMenu == ControlsP1):
                currentMenu =ControlsP2
            else : 
                currentMenu = ControlsP1
            stdscr.clear()
            menuWithoutCursor(stdscr, currentMenu)    # print the menu
            stdscr.refresh()

                
# menu = ['New Game','New Game With Trap', 'Load Game', 'Controls', 'Exit']
# music = threading.Timer(0, musicPlayer)
# music.start()

if __name__ ==  '__main__':
    p = multiprocessing.Process(target=musicPlayer,)
    p.start()
    curses.wrapper(displayMainMenu)
    p.terminate()



