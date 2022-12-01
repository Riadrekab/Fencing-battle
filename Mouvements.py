def moveBackP1(p1,TrapP):
    if( not p1.position - p1.mouvementRange>2):
        p1.position =1
    elif((TrapP < p1.position and  p1.position - p1.mouvementRange <= TrapP+1)) : 

        p1.position = TrapP + 2
    else : 
        p1.position -= p1.mouvementRange


def moveBackP2(p2,TrapP,frames):

    if(p2.position+p2.mouvementRange > frames - 2) :
        p2.position = frames-2
    elif(p2.position<TrapP and p2.position +p2.mouvementRange>=TrapP-1):
        p2.position = TrapP - 2
    else : 
        p2.position += p2.mouvementRange




def moveForwardP1(p1,p2,TrapP):

    if(p2.position -p1.position-p1.mouvementRange - 4 >   TrapP - p1.position - p1.mouvementRange) :
        if( (TrapP > p1.position and p1.position + p1.mouvementRange>=TrapP)) :
            p1.position = TrapP - 1
        else : 
            if(not p2.position - p1.position-p1.mouvementRange >= 5) :
                p1.position =p2.position-5
            else : p1.position+=p1.mouvementRange
    else : 
        if(not p2.position - p1.position-p1.mouvementRange >= 5) :
            p1.position =p2.position-5
        else : p1.position+=p1.mouvementRange


def moveForwardP2(p1,p2,TrapP,stdstr):
    if(p2.position - p2.mouvementRange -p1.position - 4 <  p2.position - p2.mouvementRange - TrapP):
        if(not p2.position - p2.mouvementRange - p1.position >=6) :
            p2.position = p1.position+5
        else : 
            p2.position -= p2.mouvementRange
    else : 
        if(TrapP< p2.position and p2.position -p2.mouvementRange <= TrapP):
            p2.position = TrapP +1
        else : 
            if(not p2.position - p2.mouvementRange - p1.position >=6) :
                p2.position = p1.position+5
            else : 
                p2.position -= p2.mouvementRange


def jumpPlayer1(p1,p2,TrapP):
    if(not p2.position - p1.position-p1.mouvementRange >= 6) :
        p1.position =p2.position-5
    elif( (TrapP > p1.position and (p1.position + p1.mouvementRange==TrapP or p1.position + p1.mouvementRange==TrapP+1 ))) :
        p1.position = TrapP - 1
    else : p1.position+=p1.mouvementRange
    
def jumpBackP1(p1,TrapP):
    if( not p1.position - p1.mouvementRange>2):
        p1.position =1
    elif((TrapP < p1.position and (p1.position - p1.mouvementRange == TrapP+1  or  p1.position - p1.mouvementRange == TrapP))) : 
        p1.position = TrapP + 2
    else : 
        p1.position -= p1.mouvementRange

def jumpBackP2(p2,TrapP,frames):
    if(p2.position+p2.mouvementRange > frames - 2) :
        p2.position = frames-2
    elif(p2.position<TrapP and (p2.position +p2.mouvementRange==TrapP-1 or p2.position +p2.mouvementRange==TrapP)):
        p2.position = TrapP - 2
    else : 
        p2.position += p2.mouvementRange

def jumpPlayer2(p2,TrapP):
    if(not p2.position- p2.mouvementRange - p1.position >=6) :
        p2.position = p1.position+5
    elif(TrapP< p2.position and (p2.position -p2.mouvementRange == TrapP or  p2.position -p2.mouvementRange == TrapP -1) ):
        p2.position = TrapP +1
    else : 
        p2.position -= p2.mouvementRange


