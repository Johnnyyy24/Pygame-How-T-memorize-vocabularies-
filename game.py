import pygame
import math
import random
from pygame.sprite import Sprite
#調整圖片大小
from PIL import Image
import sys
pygame.init()
win = pygame.display.set_mode((960,720),pygame.SRCALPHA)
pygame.display.set_caption("Game") 

Run = [pygame.image.load('joan_run_1.png'), pygame.image.load('joan_run_2.png'), pygame.image.load('joan_run_3.png'), pygame.image.load('joan_run_4.png'), pygame.image.load('joan_run_5.png'), pygame.image.load('joan_run_6.png')]
Jump = [pygame.image.load('joan_jump_3.png'),pygame.image.load('joan_jump_4.png')]
weapon = pygame.image.load('sshotgun.png')
bg = pygame.image.load('bg.png')
blood_half=[pygame.image.load('missions_icon.png'),pygame.image.load('missions_icon_complete.png')] #增加骷顱頭的圖示
NUMBER = [pygame.image.load('bold_0.png'), pygame.image.load('bold_1.png'), pygame.image.load('bold_2.png'),
          pygame.image.load('bold_3.png'), pygame.image.load('bold_4.png'), pygame.image.load('bold_5.png'),
          pygame.image.load('bold_6.png'), pygame.image.load('bold_7.png'), pygame.image.load('bold_8.png'),
          pygame.image.load('bold_9.png'), pygame.image.load('bold_dot.png')]
trap = [pygame.image.load('saws_down_bloody_1.png'), pygame.image.load('saws_down_bloody_2.png'), pygame.image.load('saws_down_bloody_3.png')]
health_image = [pygame.image.load('item_health_1.png'), pygame.image.load('item_health_2.png'), pygame.image.load('item_health_3.png'),
                pygame.image.load('item_health_4.png'), pygame.image.load('item_health_5.png'), pygame.image.load('item_health_6.png')]
bullet_image = [pygame.image.load('grenade_bullet_1.png'),pygame.image.load('grenade_bullet_2.png')]
bullet_image2 = [pygame.image.load('agent_shot_fx_1.png'), pygame.image.load('agent_shot_fx_1.png')]
platfrom_image = pygame.image.load('platform_2.png')
enemy_image = [pygame.image.load('agent_attack_1.png'), pygame.image.load('agent_attack_2.png'),pygame.image.load('agent_attack_3.png'),
              pygame.image.load('agent_attack_4.png'),pygame.image.load('agent_attack_5.png'),pygame.image.load('agent_attack_6.png')]

letter_image = [pygame.image.load('A.png'),pygame.image.load('B.png'),pygame.image.load('C.png'),pygame.image.load('D.png'),
                pygame.image.load('E.png'),pygame.image.load('F.png'),pygame.image.load('G.png'),pygame.image.load('H.png'),
                pygame.image.load('I.png'),pygame.image.load('J.png'),pygame.image.load('K.png'),pygame.image.load('L.png'),
                pygame.image.load('M.png'),pygame.image.load('N.png'),pygame.image.load('O.png'),pygame.image.load('P.png'),
                pygame.image.load('Q.png'),pygame.image.load('R.png'),pygame.image.load('S.png'),pygame.image.load('T.png'),
                pygame.image.load('U.png'),pygame.image.load('V.png'),pygame.image.load('W.png'),pygame.image.load('X.png'),
                pygame.image.load('Y.png'),pygame.image.load('Z.png')]
blood_bg=pygame.image.load('boss_health_back.png')
blood_front=pygame.image.load('boss_health.png')
bg_intro=pygame.image.load('menu.png') #改
bg_help=pygame.image.load('john.jpg') #改
bg_about=pygame.image.load('meme.jpg')
main=pygame.image.load('missions_button.png')
pause_icon=[pygame.image.load('pause.png'),pygame.image.load('pause_tap.png')]#改

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
J = 9
K = 10
L = 11
M = 12
N = 13
O = 14
P = 15
Q = 16
R = 17
S = 18
T = 19
U = 20
V = 21
W = 22
X = 23
Y = 24
Z = 25
clock = pygame.time.Clock()


class player(object): #人物
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.temp_y = self.y
        self.width = width
        self.height = height
        self.isJump = False
        self.runCount = 0
        self.jumpCount = 0
        self.jump_point = self.y
        self.isFall = False
        self.fallCount = 0
        self.hitbox1 = (self.x + 5, self.y + 5, 50, 50)
        self.hitbox2 = (self.x + 5, self.y + 50, 50, 5)
        self.goal = False
        self.goal_count = 0
        self.letter_count = 0
        self.letter_array = []
        self.voc_count = 0
        self.voc_size = [6,7,10,5,6,11,9,13,8,8,10,6,6,9,7,9,7,12,8,6,5,13,12,9,8,8,9,11,12,10]
        self.voc = [
    [L,E,D,G,E,R],
    [P,R,O,V,I,S,O],
    [A,S,S,E,S,S,M,E,N,T],
    [R,E,M,I,T],
    [M,A,R,G,I,N],
    [S,T,O,C,K,H,O,L,D,E,R],
    [A,R,B,I,T,R,A,G,E],
    [S,U,B,C,O,N,T,R,A,C,T,E,R],
    [D,I,V,I,D,E,N,D],
    [S,T,A,G,N,A,N,T],
    
    [P,A,R,A,S,I,T,I,S,M],
    [L,I,C,H,E,N],
    [P,O,R,O,U,S],
    [H,E,R,B,I,C,I,D,E],
    [N,E,P,T,U,N,E],
    [D,E,P,L,E,T,I,O,N],
    [P,O,L,A,R,I,S],
    [C,H,R,O,M,O,S,P,H,E,R,E],
    [N,E,U,T,R,I,N,O],
    [P,L,A,S,M,A],

    [A,P,P,L,E],
    [C,O,N,F,I,G,U,R,A,T,I,O,N],
    [I,N,C,O,M,P,A,T,I,B,L,E],
    [B,A,N,D,W,I,D,T,H],
    [P,R,O,T,O,C,O,L],
    [R,E,T,R,I,E,V,E],
    [H,E,U,R,I,S,T,I,C],
    [C,Y,B,E,R,N,E,T,I,C,S],
    [A,U,T,H,E,N,T,I,C,A,T,E],
    [R,E,S,O,L,U,T,I,O,N]]
        self.voc_text = [
    "LEDGER 總帳",
        "PROVISO 但書",
        "ASSESSMENT 評估",
        "REMIT 匯款",
        "MARGIN 保證金",
        "STOCKHOLDER 股東",
        "ARBITRAGE 套利",
        "SUBCONTRACTER 轉包商",
        "DIVIDEND 股息",
        "STAGNANT 不景氣",
        "PARASITISM 寄生",
        "LICHEN 地衣",
        "POROUS 多孔隙的",
        "HERBICIDE 除草劑",
        "NEPTUNE 海王星",
        "DEPLETION 枯竭",
        "POLARIS 北極星",
        "CHROMOSPHERE 色球層",
        "NEUTRINO 微中子",
        "PLASMA 電漿",
        "APPLE 蘋果",
        "CONFIGURATION 系統設定",
        "INCOMPATIBLE 不相容",
        "BANDWIDTH 頻寬",
        "PROTOCOL 通訊協定",
        "RETRIEVE 檢索",
        "HEURISTIC 啟發式的方法",
        "CYBERNETICS 模控學",
        "AUTHENTICATE 認證",
        "RESOLUTION 解析度"
    ]

    def Run_or_Jump_or_Fall(self, win, keys): #跳躍、跑步動畫
        if self.runCount // 2 >= 6:
            self.runCount = 0
        if not self.isJump:
            stand_on_platform(win)
        if not self.isFall:
            if not self.isJump:
                if keys[pygame.K_w]:
                    self.isJump = True
                    #self.isPause = False
                    #self.isFall = False
                    self.jump_point = self.y
                    self.runCount = 0
                    self.temp_y = self.y
                    self.jumpCount += 1
                    self.y -= 1
                    win.blit(Jump[0],(self.x,self.y))
                else:
                    win.blit(Run[self.runCount // 2],(self.x,self.y))
                    self.runCount += 1;
            if self.isJump:
                if self.jumpCount <= 40 / 4:
                    index = 0
                else:
                    index = 1
                if(self.jumpCount > 10):
                    if(stand_on_platform(win)):
                        self.isJump = False
                        self.isFall = False
                        win.blit(Run[self.runCount // 2],(self.x,self.y))
                        self.runCount += 1;
                    else:
                        self.isFall = False
                        if (self.jumpCount > 12):
                            self.y += 10
                        else:
                            self.y = self.jump_point - 40 * self.jumpCount + (self.jumpCount ** 2) * 2
                        
                        print(self.jumpCount, self.y)
                        win.blit(Jump[index],(self.x,self.y))
                        self.jumpCount += 1
                else:
                    self.y = self.jump_point - 40 * self.jumpCount + (self.jumpCount ** 2) * 2
                    print(self.jumpCount, self.y)
                    win.blit(Jump[index],(self.x,self.y))
                    self.jumpCount += 1
                if (self.y > 520):
                    self.y = 520
                    self.isJump = False
        else:
            self.isFall = True
            self.y += 10
            win.blit(Jump[1],(self.x,self.y))
            self.fallCount += 1    
        self.hitbox1 = (self.x + 5, self.y + 5, 50, 50)
        self.hitbox2 = (self.x + 5, self.y + 50, 50, 7)
        #pygame.draw.rect(win, (255,0,0),self.hitbox1, 2)
        #pygame.draw.rect(win, (255,255,0),self.hitbox2, 2)


class player_health(object): #人物血條
    def __init__(self, x, y, health):
        self.rect = blood_front.get_rect()
        self.rect.x = x + 7
        self.rect.y = y + 5
        self.x = x
        self.y = y
        self.health = health

    def draw(self,win):
        if self.health<73:
            win.blit(blood_half[1],(-5,85))
        else:
            win.blit(blood_half[0],(-5,85))
        self.health -= 0.04
        #if self.health <= 0:
            #self.health = 155
        #### byHenry
        if hit_by_bullet(win) == True:
            self.health -= 1
        if hit_by_heart(win) == True:
            self.health += 3
        if hit_by_trap(win) == True:
            self.health -= 0.5
        #########################
        win.blit(blood_bg,(self.x,self.y))
        win.blit(blood_front,self.rect,(0,0,self.health,self.rect.width))
class Text(): #字體的calss
    def __init__(self, text, color, y_displace = 0,x=0,y=0,size = 'small'): #新增x,y來表示文字出現的座標
        self.text = text
        self.color = color
        self.y_displace = y_displace
        self.size = size
        self.x=x
        self.y=y

    def choosing_font(self, size): #選出現在清單上的字體
        petitfont=pygame.font.Font("game_font3.ttf",15)
        smallfont = pygame.font.Font("game_font3.ttf",25)
        medfont = pygame.font.Font("game_font3.ttf",50)
        largefont = pygame.font.Font("game_font3.ttf",75)
        if(size == "small"):
            return smallfont
        elif(size=="petit"):
            return petitfont
        elif(size == "med"):
            return medfont
        elif(size == "large"):
            return largefont
        
    def text_objects(self, text, color, size):
        textSurface = (self.choosing_font(size)).render(text,True,color)
        return textSurface, textSurface.get_rect()
    
    def message_to_screen(self, screen):
        textSurf, textRect = self.text_objects(self.text, self.color, self.size)
        textRect.center = (self.x, self.y + self.y_displace)
        screen.blit(textSurf,textRect)
    
    def text_to_button(self,button_x,button_y,button_width,button_height,screen):
        textSurf, textRect = self.text_objects(self.text, self.color , self.size)
        textRect.center=((button_x+(button_width/2)),(button_y+(button_height/2)))
        screen.blit(textSurf,textRect)
    
    def button(self,x,y,width,height,inactive_color,active_color,screen):
        cur=pygame.mouse.get_pos()
        if x+width>cur[0]>x and y+height>cur[1]>y:
            pygame.draw.rect(screen,active_color,(x,y,width,height))
        else:   
            pygame.draw.rect(screen,inactive_color,(x,y,width,height))
        self.text_to_button(x,y,width,height,screen)    
        
def Paused(screen, isPause): #暫停函式
    #global pause #宣告成全域變數
    #pause = True
    Pause_text = Text("Paused", (255,255,255), -100,480,360,size = "large" )
    c_q_text = Text("Press 'c' to continue and press 'q' if you wanna quit", (255,255,255), 0, 480,360,size = 'small')
    btmenu_text=Text("Back to menu",(255,255,255), 0 ,910,50,size='petit') #改
    while isPause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    isPause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.set_alpha(255)
        screen.blit(pause_icon[1],(430,300))
        screen.blit(main,(900,0))
        btmenu_text.message_to_screen(win)
        cur=pygame.mouse.get_pos()
        if(960>cur[0]>900 and 50>cur[1]>0 and pygame.mouse.get_pressed()[0]):
            isPause=False
            global restart
            restart=True #只有Paused裡面可以把restart改成True
        pygame.display.update()

class Timer: #計時器
    def __init__(self):
        self.pausetime = 0
        self.time_since_enter = 0
        self.temp = 0
        self.time_since_pause = 0
        self.start_time = 0
        self.count = 0
        self.countdown_time= 0 #new
        self.LessenCount= 0 #new

    def GetStart_time(self,start_time): #取得開始遊戲的時間
        self.start_time = start_time
        
    def GameTime(self, screen, isPause, isTiming): #計算時經過的多久，並blit到螢幕上
        FONT = pygame.font.SysFont("Sans", 20) 
        TEXT_COLOR = (0, 0, 0) 
        #BG_COLOR = (255, 255, 255)
        #p = False #GameTime裡的暫停判斷變數 
        if isTiming: 
            if not isPause: #沒暫停的話時間才繼續算，否則就會是原本的數字
                self.time_since_pause = pygame.time.get_ticks() - self.pausetime
                if self.count == 1:
                    self.start_time += self.time_since_pause
                    self.count = 0
                self.time_since_enter = pygame.time.get_ticks() - self.start_time
                self.temp = self.time_since_enter
                print("Runnning")
            else:
                self.time_since_enter = self.temp
                self.pausetime = pygame.time.get_ticks()
                self.count += 1
                print("Pausing")

            self.time_since_enter = round(self.time_since_enter/1000,1)
            int = math.floor(self.time_since_enter) #取整數部分
            float = math.floor(10*(self.time_since_enter-int))#小數部分
            int_h = math.floor(int/100) #若小於一百就會為0 #舉例 145,int_h=1,int_t=4,int_s=5
            int_t = math.floor((int-int_h*100)/10)
            int_s = ((int-int_h*100-int_t*10))
            if int_h:#如果有大於100秒的話
                for i in range(10):
                    if(i == int_h):
                        screen.blit(NUMBER[i],(390,50))
                    if(i == int_t):
                        screen.blit(NUMBER[i],(420,50))
                    if(i == int_s):
                        screen.blit(NUMBER[i],(450,50))
                    if(i == float):
                        screen.blit(NUMBER[i],(480,50))
            else:
                if int_t:   
                    for i in range(10):
                        if(i == int_t):
                            screen.blit(NUMBER[i],(420,50))
                        if(i == int_s):
                            screen.blit(NUMBER[i],(450,50))
                        if(i == float):
                            screen.blit(NUMBER[i],(480,50))
                else:
                    for i in range(10):
                        if(i == int_s):
                            screen.blit(NUMBER[i],(450,50))
                        if(i == float):
                            screen.blit(NUMBER[i],(480,50))
            screen.blit(NUMBER[10],(465,50))
            pygame.display.update()
def help_surface(): #NEW
    help=True
    win.blit(bg_help,(0,0))
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    light_blue=(128,128,255)
    back_text=Text("BACK",red,-100,100,600,size="small")
    
    while(help):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        back_text.button(0,0,100,50,blue,light_blue,win)
        cur=pygame.mouse.get_pos()
        if (100>cur[0]>0) and (50>cur[1]>0) and (pygame.mouse.get_pressed()[0]): #按下Play鍵之後
            help=False
            game_intro()
        pygame.display.update()
        clock.tick(15)
    
def game_intro(): #NEW
    intro=True
    win.blit(bg_intro,(0,0))
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    light_blue=(128,128,255)
    play_text=Text("PlAY",red,-100,100,600,size="small")
    help_text=Text("HELP",red,-100,100,600,size="small")
    about_text=Text("ABOUT",red,-100,100,600,size="small")
    quit_text=Text("QUIT",red,-100,100,600,size="small")
    #pygame.display.update()
    while(intro):   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        play_text.button(430,300,100,50,blue,light_blue,win)
        help_text.button(430,400,100,50,blue,light_blue,win)
        about_text.button(430,500,100,50,blue,light_blue,win)
        quit_text.button(430,600,100,50,blue,light_blue,win)
        
        cur=pygame.mouse.get_pos()
        if (530>cur[0]>430) and (350>cur[1]>300) and (pygame.mouse.get_pressed()[0]) : #按下Play鍵之後
            intro=False
        elif (530>cur[0]>430) and (450>cur[1]>400) and (pygame.mouse.get_pressed()[0]):#按下Help鍵之後
            #日後再修改
            intro=False
            help_surface()
        elif (530>cur[0]>430) and (550>cur[1]>500) and (pygame.mouse.get_pressed()[0]): #按下About鍵之後 
            pass
        elif (530>cur[0]>430) and (650>cur[1]>600) and (pygame.mouse.get_pressed()[0]) : #按下Quit鍵之後
            pygame.quit()
            quit()
        

        pygame.display.update() 
        clock.tick(15)

    isRun=False
    y_list = [100, 200, 300, 300, 400, 400, 500, 500]
    x_list = [960]
    man = player(200, 520, 64,64)
    blood_chart = player_health(40,110,155) #改5->30
    timer = Timer()
    isRun = True
    isTiming = False
    start_time = 0
    time_since_pause = 0
    temp = 0
    pausetime = 0
    bullets = []
    hearts = []
    platforms = []
    platform_count = 10
    platforms_with_traps = []
    platform_with_trap_count = 20
    platforms_with_enemys = []
    platforms_with_enemys_count = 30
    enemys_bullets = []
class projectile(object): #主角的子彈
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.count = 0
        self.hitbox = (self.x, self.y , 30, 8)

    def draw(self,win): 
        if self.count == 0:
            win.blit(bullet_image[0], (self.x, self.y))
            self.count = self.count + 1
        else:
            win.blit(bullet_image[1], (self.x, self.y))
        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)
class item_health(object): #補血的愛心
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.heart_count = 0
        self.hitbox = (self.x, self.y , 34, 32)

    def draw(self,win):
        #愛心動畫
        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)
        win.blit(health_image[self.heart_count // 6], (self.x,self.y))
        self.heart_count += 1
        if self.heart_count // 6 >= 6:
            self.heart_count = 0

class item_platform(object): #一般的平台
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.hitbox = (self.x + 5, self.y, 184, 10)
    def draw(self,win):
        #pygame.draw.rect(win, (0,255,0), self.hitbox, 2)
        win.blit(platfrom_image, (self.x,self.y))


class item_platform_with_track(object): #有陷阱的平台
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.trap_count = 0
        self.hitbox1 = (self.x + 5, self.y, 184, 10)
        self.hitbox2 = (self.x + 70, self.y - 20, 45, 25)
    def draw(self,win):
        #pygame.draw.rect(win, (0,255,0), self.hitbox1, 2)
        #pygame.draw.rect(win, (0,255,0), self.hitbox2, 2)
        win.blit(platfrom_image, (self.x,self.y))
        win.blit(trap[self.trap_count // 1],(self.x + 60,self.y - 30))
        self.trap_count += 1
        if self.trap_count // 1 >= 3:
            self.trap_count = 0

class item_platform_with_enemy(object): #有敵人的平台
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 12
        self.enemy_count = 0
        self.key = True
        self.hitbox1 = (self.x + 5, self.y, 184, 10)
        self.hitbox2 = (self.x + 90, self.y - 50, 30, 60)
        self.letter_index = random.randint(0,25)
    def draw(self,win):
        #pygame.draw.rect(win, (0,255,0), self.hitbox1, 2)
        #pygame.draw.rect(win, (0,255,0), self.hitbox2, 2)
        win.blit(platfrom_image, (self.x,self.y))
        hit_the_enemy(win)
        if self.key == True:
            win.blit(letter_image[self.letter_index],(self.x + 70 ,self.y - 63))
            win.blit(enemy_image[self.enemy_count // 6],(self.x + 63 ,self.y - 53))
            self.enemy_count += 1
            if self.enemy_count // 6 >= 6:
                self.enemy_count = 0 
            if self.enemy_count == 29:
                enemys_bullets.append(projectile2(self.x + 30, self.y - 50))
       
            

class projectile2(object): #敵人的子彈
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 30
        self.count = 0
        self.hitbox = (self.x + 20, self.y + 20, 25, 8)
    def draw(self,win):
        #pygame.draw.rect(win, (0,255,0), self.hitbox, 2)
        if self.count == 0:
            win.blit(bullet_image2[0], (self.x, self.y))
            self.count = self.count + 1
        else:
            win.blit(bullet_image2[1], (self.x, self.y))
       
def redrawGameWindow(): #執行主要blit的部分
    win.blit(bg, (0,0))
    for i in range(man.letter_count):
        win.blit(letter_image[man.letter_array[i]], (160 + 60 * i, 100))
    voc_text = Text((man.voc_text[man.voc_count]), (255,255,255), -320,480,360, size = "large" )
    voc_text.message_to_screen(win)
    if(man.letter_count == man.voc_size[man.voc_count]):
        man.voc_count += 1
        man.letter_count = 0
        man.letter_array = []
        man.goal = True
        blood_chart.health = 155
    if (man.goal):
        goal_text = Text("GOAL", (255,255,255), -220,480,360, size = "large" )
        goal_text.message_to_screen(win)
        man.goal_count += 1
        if man.goal_count == 30:
            man.goal_count = 0
            man.goal = False
    if (blood_chart.health < 0):
        over_text = Text("GAME OVER", (255,255,255), -120,480,360, size = "large" )
        over_text.message_to_screen(win)
        Paused(win, True)
                            
    man.Run_or_Jump_or_Fall(win,keys)
    win.blit(weapon,(man.x, man.y - 1))
    for platform in platforms:
        platform.draw(win)
    for platform_with_trap in platforms_with_traps:
        platform_with_trap.draw(win)
    for platform_with_enemy in platforms_with_enemys:
        platform_with_enemy.draw(win)
    for heart in hearts:
        heart.draw(win) 
    for enemy_bullet in enemys_bullets:
        enemy_bullet.draw(win)
    for bullet in bullets: #將還存在list中的所有子彈物件都blit
        bullet.draw(win)
    blood_chart.draw(win)
    pygame.display.update()

def check_collision(a, b):
    #Calculate the sides of rect A
    leftA = a[0]
    rightA = a[0] + a[2]
    topA = a[1]
    bottomA = a[1] + a[3]
    
    #Calculate the sides of rect B
    leftB = b[0]
    rightB = b[0] + b[2]
    topB = b[1]
    bottomB = b[1] + b[3]
    
    #If any of the sides from A are outside of B
    if bottomA <= topB:
        return False

    if topA >= bottomB:
        return False

    if rightA <= leftB:
        return False

    if leftA >= rightB:
        return False
    #If none of the sides from A are outside B
    return True;
##### byHenry
def hit_by_bullet(screen):
    for enemy_bullet in enemys_bullets:
        if check_collision(man.hitbox1, enemy_bullet.hitbox):
            enemys_bullets.pop(enemys_bullets.index(enemy_bullet)) #這裡改了
            return True
def hit_by_heart(screen):
    for heart in hearts:
        if check_collision(man.hitbox1, heart.hitbox):
            hearts.pop(hearts.index(heart)) #這裡改了
            return True
def hit_by_trap(screen):
    for platform_with_trap in platforms_with_traps:
        if check_collision(man.hitbox1, platform_with_trap.hitbox2):
            return True
        
def stand_on_platform(screen):
    for platform in platforms:
        if check_collision(man.hitbox2, platform.hitbox):
            man.isJump = False
            man.isFall = False
            man.fallCount = 0
            man.jumpCount = 0
            return True
    for platform_with_trap in platforms_with_traps:
        if check_collision(man.hitbox2, platform_with_trap.hitbox1):
            man.isJump = False
            man.isFall = False
            man.fallCount = 0
            man.jumpCount = 0
            return True 
    for platform_with_enemy in platforms_with_enemys:
        if check_collision(man.hitbox2, platform_with_enemy.hitbox1):
            man.isJump = False
            man.isFall = False
            man.fallCount = 0
            man.jumpCount = 0
            return True 
    if man.y >= 520:
        man.y = 520
        man.isJump = False
        man.isFall = False
        man.fallCount = 0
        man.jumpCount = 0
        return True
    man.isFall = True
    return False

def hit_the_enemy(screen):
    for bullet in bullets:
        for platform_with_enemy in platforms_with_enemys:
            if platform_with_enemy.key == True:
                if check_collision(bullet.hitbox, platform_with_enemy.hitbox2):
                    bullets.pop(bullets.index(bullet)) #這裡改了
                    platform_with_enemy.key = False
                    if (platform_with_enemy.letter_index == man.voc[man.voc_count][man.letter_count]):
                        man.letter_array.append(platform_with_enemy.letter_index)
                        man.letter_count += 1
                        break
                    else:
                        blood_chart.health -= 0.1
#################################################


#mainloop
restart=False #NEW
y_list = [100, 200, 200, 300, 300, 400, 400, 500, 500] #存放y值的清單，用來隨機給object一預設y座標
x_list = [960] #存放x值的清單，用來隨機給object一預x座標
man = player(200, 520, 64,64) #建立一個主角
blood_chart = player_health(40,110,155) #改5->30 #建立血條
timer = Timer() #建立計時器
isRun = True #判斷mainloop是否運行
isTiming = False #判斷計時器是否運行
bullets = [] #存放所有主角子彈物件的list
hearts = [] #存放所有補血愛心物件的list
platforms = [] #存放所有平台物件的list
platform_count = 10 #用來延遲平台生成
platforms_with_traps = [] #存放所有陷阱平台物件的list
platform_with_trap_count = 20 #用來延遲平台生成
platforms_with_enemys = [] #存放所有怪物平台物件的list
platforms_with_enemys_count = 0 #用來延遲平台生成
enemys_bullets = [] #存放所有敵人子彈物件的list
game_intro()
while isRun:
    if restart: #new，如果restart是True的話就重給初值一次
        restart=False #然後把restart設為False以免每次都重跑
        y_list = [100, 200, 300, 300, 400, 400, 500, 500]
        x_list = [960]
        man = player(200, 520, 64,64)
        blood_chart = player_health(40,110,155) #改5->30
        timer = Timer()
        isRun = True
        isTiming = False
        start_time = 0
        time_since_pause = 0
        temp = 0
        pausetime = 0
        bullets = []
        hearts = []
        platforms = []
        platform_count = 10
        platforms_with_traps = []
        platform_with_trap_count = 20
        platforms_with_enemys = []
        platforms_with_enemys_count = 0
        enemys_bullets = []
        game_intro()
    clock.tick(27)
    isPause = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                isPause = True
            if event.key == pygame.K_RETURN:
                isTiming = True
                start_time = pygame.time.get_ticks()
                timer.GetStart_time(start_time)
###############################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #按下空白鍵時，會在bullets這個list中，添加一個子彈物件
                if len(bullets) < 30:
                    bullets.append(projectile(man.x + 70, man.y + 30))

#################################################
    for bullet in bullets:
        if bullet.x < 960 and bullet.x > 0: #讓bullets這個list中，所以的子彈物件往左移
            bullet.x += bullet.vel
            bullet.hitbox = (bullet.x, bullet.y , 30, 8)
        else:
            bullets.pop(bullets.index(bullet)) #若超過螢幕範圍，則把它從list中拿掉，即刪除之意
   
################################################
    for heart in hearts:
        if heart.x < 4000 and heart.x > -100 :#and hit_by_heart(win)!=True:
            heart.x -= heart.vel
            heart.hitbox = (heart.x, heart.y , 34, 32)
        else:
            hearts.pop(hearts.index(heart))
    if len(hearts) < 10:
         hearts.append(item_health(random.randint(1000,3999), random.randint(200,500)))

###############################################
    for platform in platforms:
        if platform.x < 4000 and platform.x > -300:
            platform.x -= platform.vel
            platform.hitbox = (platform.x + 5, platform.y, 184, 10)
        else:
            platforms.pop(platforms.index(platform))
    if len(platforms) < 20:
        if platform_count == 40:
            x = int(random.choices(x_list)[0])
            y = int(random.choices(y_list)[0])
            platforms.append(item_platform(x, y))
            #print(x,y)
            platform_count = 0
        else:
            platform_count = platform_count + 1

###############################################
    for platform_with_trap in platforms_with_traps:
        if platform_with_trap.x < 4000 and platform_with_trap.x > -300:
            platform_with_trap.x -= platform_with_trap.vel
            platform_with_trap.hitbox1 = (platform_with_trap.x + 5, platform_with_trap.y, 184, 10)
            platform_with_trap.hitbox2 = (platform_with_trap.x + 70, platform_with_trap.y - 20, 45, 25)
        else:
            platforms_with_traps.pop(platforms_with_traps.index(platform_with_trap))
    if len(platforms_with_traps) < 5:
        if platform_with_trap_count == 80:
            x = int(random.choices(x_list)[0]) 
            y = int(random.choices(y_list)[0]) + 25
            platforms_with_traps.append(item_platform_with_track(x, y))
            #print(x,y)
            platform_with_trap_count = 0
        else:
            platform_with_trap_count = platform_with_trap_count + 1

###############################################
    for platform_with_enemy in platforms_with_enemys:
        if platform_with_enemy.x < 4000 and platform_with_enemy.x > -300:
            platform_with_enemy.x -= platform_with_enemy.vel
            platform_with_enemy.hitbox1 = (platform_with_enemy.x + 5, platform_with_enemy.y, 184, 10)
            platform_with_enemy.hitbox2 = (platform_with_enemy.x + 90, platform_with_enemy.y - 50, 30, 60)
        else:
            platforms_with_enemys.pop(platforms_with_enemys.index(platform_with_enemy))
    if len(platforms_with_enemys) < 25:
        if  platforms_with_enemys_count == 10:
            x = int(random.choices(x_list)[0]) 
            y = int(random.choices(y_list)[0]) + 50
            platforms_with_enemys.append(item_platform_with_enemy(x, y))
            #print(x,y)
            platforms_with_enemys_count = 0
        else:
            platforms_with_enemys_count = platforms_with_enemys_count + 1

###############################################
    for enemy_bullet in enemys_bullets:
        if enemy_bullet.x < 960 and enemy_bullet.x > -100:
            enemy_bullet.x -= enemy_bullet.vel
            enemy_bullet.hitbox = (enemy_bullet.x + 20, enemy_bullet.y + 20, 25, 8)
        else:
            enemys_bullets.pop(enemys_bullets.index(enemy_bullet))

################################################


    keys = pygame.key.get_pressed()
    redrawGameWindow()
    timer.GameTime(win, isPause, isTiming)
    Paused(win, isPause)
    

pygame.quit()
