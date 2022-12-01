
import pygame
from pygame import display,init


screen_w=1000
screen_h=700



def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen


class Button:
    def __init__(self, txt, pos,w,h):
        self.text = txt
        self.pos = pos
        self.width=w
        self.height=h
        self.button = pygame.rect.Rect((self.pos[0]-(w/2), self.pos[1]-(h/2)), (w, h))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0]- (self.width/2), self.pos[1]-(self.height/2), self.width, self.height], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0]-(self.width/2)+ 60, self.pos[1]-(self.height/2)+ 5 ))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False




def draw_game(h,w) :
    button = Button ('Main Menu', ((w//2), (h//2) + 60),260,40)
    button.draw()
    return button.check_clicked()
def draw_menu(h,w):

    # btn1 = Button ('Button 1', ((w//2), (h//2)),260,30)
    # btn2 = Button( 'Button 21' ,((w//2), (h//2)),260,30)
    # btn3 = Button ('Button 3', ((w//2), (h//2)),260,30)
    menu_btn = Button ('Exit Menu', ((w//2), (h//2)), 300,40)

    menu_btn.draw() 
    # btn1.draw()
    # btn2.draw()
    # btn3.draw()
    return not menu_btn.check_clicked ()


init()

screen = display.set_mode((screen_w, screen_h))
display.set_caption('Fencing Simulator 2022')
font = pygame.font.SysFont("arialblack",20)
main_menu = False


running = True

while running:
    screen.fill('light blue')
    if(main_menu ):
        main_menu =draw_menu(screen_h,screen_w)
    else : 
        main_menu=draw_game(screen_h,screen_w)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False            
    display.flip()

pygame.quit()


