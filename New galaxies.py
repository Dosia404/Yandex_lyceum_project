# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QPalette, QImage, QBrush
from PyQt5 import uic
import pygame
import random


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создадим виджет и сохраним ссылку на него
        self.dialog = Dialog()

        self.button_show = QPushButton('Играть')
        self.button_show.clicked.connect(self.show_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button_show)
        layout.addStretch()

        self.setLayout(layout)
        
        
    def show_dialog(self):
        self.dialog.show()

 
class Dialog(QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        p = uic.loadUi('first formm.ui',self)
        self.pushButton.clicked.connect(self.run)
        
        self.dialog2 = Dialog2()
        self.dialog3 = Dialog3()
        
        
    def run(self):
        pygame.init()
        WIN_WIDTH = 800
        WIN_HEIGHT = 600
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        screen = pygame.display.set_mode([800, 600])
        clock = pygame.time.Clock()
        
        background_position = [0, 0]
        #подгружаю все картинки, которые в дальнейшем буду использовать
        background_image = pygame.image.load("fon.jpg").convert()
        player_image = pygame.image.load("Rac.png").convert()
        player_image.set_colorkey(BLACK)
        
        Ast_im = pygame.image.load("m.gif").convert()
        Ast_im.set_colorkey(BLACK)
        
        portal = pygame.image.load("portal6.png").convert() 
        portal_x = 450 
        portal_y = 400 
        portal.set_colorkey(WHITE)        
        
        
        x_speed = 0
        y_speed = 0
        
        # Текущие координаты ракеты
        x_coord = random.randint(0, 750)
        y_coord = random.randint(0, 550)
        
        spisok = []
        n = 0
        k = 0
        chislo = random.randint(1, 6)
        i = chislo
        flag = True
     
        while i != 0: # Текущие координаты метеорита(одного)
            spisok.append(random.randint(0,800))
            spisok.append(random.random())
            spisok.append(random.random())
            i-= 1
         
        done = False
    
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True 
            screen.blit(background_image, background_position)
            screen.blit(portal, [portal_x, portal_y])
            rect4 = pygame.Rect(400, 650, 120, 120)

                # Если игрок нажал каку-нибудь кнопку -- начинаем движение
            if event.type == pygame.KEYDOWN:
                # Выясняем какая именно кнопка была нажата
                if event.key == pygame.K_LEFT:
                    x_speed =-3
                if event.key == pygame.K_RIGHT:
                    x_speed = 3
                if event.key == pygame.K_UP:
                    y_speed = -3
                if event.key == pygame.K_DOWN:
                    y_speed = 3
            
                # Если кнопка была отпущена, то и движение надо прекратить
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0  
                   
            x_coord += x_speed;
            y_coord += y_speed;
            
            
            rect1 = pygame.Rect(x_coord, y_coord, x_coord, y_coord)
            if rect1.colliderect(rect4): 
                self.dialog3.show()
                flag = False 
            #Если ракета добралась до портала
            
            for i in range(chislo):
                f = spisok[i * 3]
                n += random.random() + random.random() - spisok[i * 3 + 1] 
                f += random.random() - spisok[i * 3 + 2]
                
                rect2 = pygame.Rect(f, 0, 0, n)
                if rect1.colliderect(rect2) and flag: 
                    self.dialog2.show()
             
                screen.blit(Ast_im, [f, n])  
            for i in range(chislo):
                p = spisok[i * 3]
                k += spisok[i * 3 + 1]
                p += spisok[i * 3 + 2]
                
                rect3 = pygame.Rect(k, 0, 0, p)
                if rect1.colliderect(rect3) and flag: 
                    self.dialog2.show()
            #Два случая попадания в ракету метеорита
                screen.blit(Ast_im, [k, p])             
            screen.blit(Ast_im, [f, n])  
            screen.blit(player_image, [x_coord,y_coord])

            clock.tick(70)
            pygame.display.flip()
            
    
        pygame.quit()                
        
class Dialog2(QMainWindow): #Окно поражения
    def __init__(self):
        super(Dialog2, self).__init__()
        uic.loadUi('gameover.ui',self)
 
        
class Dialog3(QMainWindow): #Окно победы
    def __init__(self):
        super(Dialog3, self).__init__()
        uic.loadUi('win.ui',self)        
       
        
    
if __name__ == '__main__':
    app = QApplication([])
 
    w = MainWindow()
    w.resize(200, 100)
    w.show()
 
    app.exec()