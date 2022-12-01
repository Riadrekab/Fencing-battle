
# def displayPlayers(p1,p2,stdscr=0,frames=40,trapPos=0,shape1):
#     h, w = stdscr.getmaxyx()
#     stdscr.clear()
#     i = 0
#     j=int(h/2)-3
#     stdscr.addstr(2,10,str(p1.score))
#     stdscr.addstr(2,frames-10,str(p2.score))


#     stdscr.addstr(j-p1.hauteur-2,p1.position,'P1')
#     stdscr.addstr(j-p2.hauteur-2,p2.position,'P2')

#     for elem in shape1: 
#         val1 = j - p1.hauteur 
#         val2 = j - p2.hauteur
#         stdscr.addstr(val1,p1.position-space[i],shape1[i])
#         stdscr.addstr(val2,p2.position-space2[i],shape2[i])
#         i = i+1
#         j=j+1
#     for k in range(frames) : 
#         stdscr.addstr(j,k,'-')
    
#     if (trapPos):
#         stdscr.addstr(j,trapPos,'X')
#         stdscr.addstr(j-1,trapPos,'X')

        




# def displayPlayersForP2(p1,p2,stdscr,hauteurP1=0,hauteurP2=0,frames=40,trap=False,trapPos=0):
#     stdscr.clear()
#     h, w = stdscr.getmaxyx()
#     i = 0
#     j=int(h/2)-3
#     stdscr.addstr(0,0,str(p1.score))
#     stdscr.addstr(0,frames,str(p2.score))


#     stdscr.addstr(6-p1.hauteur,p1.position,'P1')
#     stdscr.addstr(6-p2.hauteur,p2.position,'P2')

#     for elem in shape1: 
#         val1 = j - p1.hauteur
#         val2 = j - p2.hauteur
#         stdscr.addstr(val2,p2.position-space2[i],shape2[i])
#         stdscr.addstr(val1,p1.position-space[i],shape1[i])
#         i = i+1
#         j=j+1
#     for k in range(frames) : 
#         stdscr.addstr(j,k,'-')
    
#     if (trapPos):
#         stdscr.addstr(j,trapPos,'X')
#         stdscr.addstr(j-1,trapPos,'X')

