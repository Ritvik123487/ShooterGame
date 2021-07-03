#Author: Ritvik Jayanthi
#Purpose: Game for Culminating
#Decription: This is a shooter gamer

import turtle #To create players and objects
import math #For collision checks
import random #To set positions for the objects
import os #To connect with Mac for soundfile
import platform #To connect with Windows for soundfile
import time #To pause the program

lolly = 1
pausestatus = 'ready'
pause = 5
easterstatus = 0
finalshoot = 0
herty = 0
r = []
wer = []
yeet = 0
redo = 0
score = 0
shootsp = 20
health = 3
yeety = 0
speed = 2
speedt = 2
sizeb = 10
sizeb2 = 6
sizeb3 = 6
speedb = 10
p1status = 'Ready'
b1status = 'Ready'
b2status = 'Ready'
b3status = 'Ready'

#Screen set up
wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Game Time')

#Instructions
i_pen = turtle.Turtle()
i_pen.hideturtle()
i_pen.speed(0)
i_pen.color('red')
i_pen.penup()
i_pen.setposition(-20, 0)
i_pen.write('Game Start', False, align='left', font=('Arial', 18, 'normal'))
dqdwqdwd = str(input('Please Press Enter'))
i_pen.clear()
i_pen.hideturtle()

#sound for windows
if platform.system() == 'Windows':
    try:
        import winsound
    except:
        print('Windsound is not downloaded, please do so')

#score
s_pen = turtle.Turtle()
s_pen.speed(0)
s_pen.color('orange')
s_pen.penup()
s_pen.setposition(-780, 400)

#This makes it a live score using your variable
s_string = 'Score: %s' %score
s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
s_pen.hideturtle()

#health
h_pen = turtle.Turtle()
h_pen.speed(0)
h_pen.color('orange')
h_pen.penup()
h_pen.setposition(-780, 370)
h_string = 'Lives: %s' %health
h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
h_pen.hideturtle()

#Making a player(p1)
wn.register_shape('p1i.gif')
p1 = turtle.Turtle()
p1.color('lightgreen')
p1.shape('p1i.gif')
p1.penup() #Makes it so there is no trail
p1.speed(0) #Makes the animation speed fast
p1.turtlesize(1.25, 1.25, 1)

#Boundaries for the screen (Border)
bb = turtle.Turtle()
bb.penup()
bb.speed(0)

#shooter
wn.register_shape('ball.gif')
shoot = turtle.Turtle()
shoot.color('yellow')
shoot.shape('ball.gif')
shoot.penup()
shoot.speed(0)
shoot.hideturtle()

#shootspeed = shoot.forward(15)
shooting = 'ready'

#Draws the rectangle for the boundry
bb.setposition(-800,-430)
bb.pendown()
bb.pensize(2)
bb.forward(1600)
bb.left(90)
bb.forward(860)
bb.left(90)
bb.forward(1600)
bb.left(90)
bb.forward(860)
bb.hideturtle()

#Making the Target
wn.register_shape('as.gif')
wn.register_shape('sat.gif')
t1 = turtle.Turtle()
t1.color('red')
t1.shape('as.gif')
t1.penup()
t1.speed(0)
t1.setposition(random.randint(-780,780), random.randint(-410,410))

#Defining functions

def play_sound(sound_file, time = 0):
    #for Winmdows
    if platform.system() == 'Windows':
        winsound.Playsound(sound_file, windsound.SND_ASYNC)       
    #Linux
    elif platform.system() == 'Linux':
        os.system('aplay -q{}&'.format(sound_file))
    #mac
    else:
        os.system('afplay {}&'.format(sound_file))
        
    #for Background music
    if time > 0:     
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))

play_sound('back.wav', 150)

def reload():
    global shooting
    global redo
    
    if redo < 4:
        redo += 1
        shooting = 'ready'

def turnleft():
    p1.left(90)
    
def turnright():
    p1.right(90)

def speedin():
    global speed
    global shootsp
    
    speed += 1
    shootsp += 2

def speedde():
    global speed
    global shootsp

    if speed >= 2:
        speed -= 1
    if shootsp >= 20:
        shootsp -= 2

def pause():

    global pausestatus

    if pausestatus == 'ready':
        pausestatus = 'not ready'
        p_pen = turtle.Turtle()
        p_pen.speed(0)
        p_pen.color('red')
        p_pen.penup()
        p_pen.setposition(-75, 0)
        p_pen.write('Pause Time: 5', False, align='left', font=('Arial', 18, 'normal'))
        p_pen.hideturtle()
        play_sound('5.wav')
        time.sleep(1)
        p_pen.clear()
        p_pen.write('Pause Time: 4', False, align='left', font=('Arial', 18, 'normal'))
        play_sound('4.wav')
        time.sleep(1)
        p_pen.clear()
        p_pen.write('Pause Time: 3', False, align='left', font=('Arial', 18, 'normal'))
        play_sound('3.wav')
        time.sleep(1)
        p_pen.clear()
        p_pen.write('Pause Time: 2', False, align='left', font=('Arial', 18, 'normal'))
        play_sound('2.wav')
        time.sleep(1)
        p_pen.clear()
        p_pen.write('Pause Time: 1', False, align='left', font=('Arial', 18, 'normal'))
        play_sound('1.wav')
        time.sleep(1)
        p_pen.clear()
        p_pen.setposition(-55, 0)
        p_pen.write('Resuming', False, align='left', font=('Arial', 18, 'normal'))
        play_sound('0.wav')
        time.sleep(1)
        p_pen.clear()
        pausestatus = 'ready'

def shootit():
    
    global shooting

    if finalshoot == 0:


        if shooting == 'ready':
            shooting = 'not ready'
        
            #place shoot
        
            x = p1.xcor()
            y = p1.ycor() + 10
            shoot.setposition(x,y)
            shoot.setheading(p1.heading())
            shoot.showturtle()
            play_sound('shot.wav')

#Checks collsion with b1
def boss_collide(x, y):
    d1 = math.sqrt(math.pow(x.xcor()-y.xcor(),2)+math.pow(x.ycor()-y.ycor(),2))

    if d1 < sizeb*10:
        play_sound('explosion+1.wav')
        #The & makes it so that the sound plays with the game
        return True

    else:
        return False

#Checks collsion with b2

def boss2_collide(x, y):
    d1 = math.sqrt(math.pow(x.xcor()-y.xcor(),2)+math.pow(x.ycor()-y.ycor(),2))
    
    if d1 < sizeb2*10:
        play_sound('explosion+1.wav')
        #The & makes it so that the sound plays with the game
        return True

    else:
        return False

#Checks collsion with b3

def boss3_collide(x, y):

    d1 = math.sqrt(math.pow(x.xcor()-y.xcor(),2)+math.pow(x.ycor()-y.ycor(),2))
    
    if d1 < sizeb3*10:
        play_sound('explosion+1.wav')
        #The & makes it so that the sound plays with the game
        return True

    else:
        return False

def collision(x, y):
    
    d1 = math.sqrt(math.pow(x.xcor()-y.xcor(),2)+math.pow(x.ycor()-y.ycor(),2))
    
    if d1 < 20:
        play_sound('explosion+1.wav')
        #The & makes it so that the sound plays with the game
        return True
    
    else:      
        return False

def rec1_collide(x, y):

    if (x.xcor() > 130 and x.xcor() < 150) and (y.ycor() < re1.ycor() + 50 and y.cor() > re1.ycor() - 50):

        play_sound('explosion+1.wav')
        
        return True
    
    else:
        
        return False

#Making the keyboard for bindings

turtle.listen() #Makes the program listen to the keybaord input
wn.onkeypress(turnleft, 'a')
wn.onkeypress(turnright, 'd')
wn.onkeypress(speedin, 'w')
wn.onkeypress(speedde, 's')
wn.onkeypress(shootit, 'space')
wn.onkeypress(reload, 'r')
wn.onkeypress(pause, 'p')

#Making the Easter Egg
e1 = turtle.Turtle()
e1.color('lightblue')
e1.shape('square')
e1.penup() #Makes it so there is no trail
e1.speed(0) #Makes the animation speed fast
e1.setposition(-785, -415)

while True:

    if lolly == 0:
        e1.hideturtle
    
    p1.forward(speed)

    #Easter Egg

    if p1status == 'Ready':
        if lolly == 1:
            if collision (p1, e1):
                #Instructions
                ei_pen = turtle.Turtle()
                ei_pen.hideturtle()
                ei_pen.speed(0)
                ei_pen.color('red')
                ei_pen.penup()
                ei_pen.setposition(-100, 0)
                ei_pen.write('You Have Found the Easter Egg', False, align='left', font=('Arial', 18, 'normal'))
                time.sleep(1.5)
                ei_pen.clear()
                ei_pen.hideturtle()
                easterstatus = 1
                break

    #For player boundries
    
    if p1.xcor() > (800-14.9) or p1.xcor() < (-800+14.9):
        p1.right(180)

    elif p1.ycor() > (430-14.9) or p1.ycor() < (-430+14.9):
        p1.left(180)
    
    #This does a collision check with t1 

    if p1status == 'Ready':
        if collision (p1, t1):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))
            if health >=1:
                health -= 1
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            p1status = 'Not ready'
            p1.setposition(0,0)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'
            

    if shooting == 'not ready':
        if collision (shoot, t1):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))
            shooting = 'ready'
            shoot.hideturtle()
            speedt += 1
            lolly = 0
        
            score += 1
        
            #This makes it a live score using your variable

            s_string = 'Score: %s' %score
            s_pen.clear()
            s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

            #Make more targets

            yeet += 1

            if yeet == 1:

                lll = random.randint(1, 2)
                r.append(turtle.Turtle())
                r[0].color('red')
                if lll == 1:
                    r[0].shape('as.gif')
                else:
                    r[0].shape('sat.gif')
                r[0].penup()
                r[0].speed(0)
                r[0].setposition(random.randint(-780,780), random.randint(-410,410))

            else:

                lll = random.randint(1, 2)
                r.append(turtle.Turtle())
                r[yeet - 1].color('red')
                if lll == 1:
                    r[yeet - 1].shape('as.gif')
                else:
                    r[yeet - 1].shape('sat.gif')
                r[yeet - 1].penup()
                r[yeet - 1].speed(0)
                r[yeet - 1].setposition(random.randint(-780,780), random.randint(-410,410))

    #boundaries for t1

    if t1.xcor() > 800 or t1.xcor() < -800:
        t1.right(180)

    elif t1.ycor() > 430 or t1.ycor() < -430:
        t1.left(180)

    #Boundaries for shoot

    if shoot.xcor() > 800 or shoot.xcor() < -800:
        shoot.right(180)
        shooting = 'ready'
        shoot.hideturtle()
        

    elif shoot.ycor() > 430 or shoot.ycor() < -430:
        shoot.left(180)
        shooting = 'ready'
        shoot.hideturtle()
        
    
    #move t1
    t1.forward(speedt)

    #move shoot

    shoot.forward(shootsp)


    #Makes more Targets

    for x in range(0, len(r)):
        r[x].forward(speedt)

        if r[x].xcor() > 800 or r[x].xcor() < -800:
            r[x].right(180)

        elif r[x].ycor() > 430 or r[x].ycor() < -430:
            r[x].left(180)

        if p1status == 'Ready':
            if collision (p1, r[x]):
                r[x].setposition(random.randint(-780,780), random.randint(-410,410))
                r[x].left(random.randint(0,360))
                if health >=1:
                    health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                p1status = 'Not ready'
                p1.setposition(0,0)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'

        if shooting == 'not ready':
            if collision (shoot, r[x]):
                r[x].setposition(random.randint(-780,780), random.randint(-410,410))
                r[x].left(random.randint(0,360))
                shooting = 'ready'
                shoot.hideturtle()
            
                speedt += 1

                score += 1
            
                #This makes it a live score using your variable. If I dont do this (and thus instaed place this part in the while statement, the score text piles o top of each other)

                s_string = 'Score: %s' %score
                s_pen.clear()
                s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

                yeet = yeet + 1

                if yeet == 1:

                    r.append(turtle.Turtle())
                    r[0].color('red')
                    r[0].shape('as.gif')
                    r[0].penup()
                    r[0].speed(0)
                    r[0].setposition(random.randint(-780,780), random.randint(-410,410))
                        

                else:
                        
                    r.append(turtle.Turtle())
                    r[yeet - 1].color('red')
                    r[yeet - 1].shape('as.gif')
                    r[yeet - 1].penup()
                    r[yeet - 1].speed(0)
                    r[yeet - 1].setposition(random.randint(-780,780), random.randint(-410,410))

    #Getting to Level 2
    if score == 5:
        p1.hideturtle()
        t1.hideturtle()
        t1.ht()
        score = 0
        speedt = 2
        health = 3
        shootsp = 20
        speed = 2
        finalshoot = 1
        for x in range(0, len(r)):
            r[x].hideturtle()
        h_string = 'Lives: %s' %health
        h_pen.clear()
        h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
        h_pen.hideturtle()
        s_string = 'Score: %s' %score
        s_pen.clear()
        s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
        break

    #Ending the game
    if health <=0:
        p1.hideturtle()
        t1.hideturtle()
        t1.ht()
        for x in range(0, len(r)):
            r[x].hideturtle()
            r[x].ht()
        end_pen = turtle.Turtle()
        end_pen.hideturtle()
        end_pen.speed(0)
        end_pen.color('red')
        end_pen.penup()
        end_pen.setposition(0, 0)
        end_pen.write('GAME OVER', False, align='left', font=('Arial', 18, 'normal'))
        time.sleep(100000000000000000000000000000000000)
        end_pen.clear()
        end_pen.hideturtle()

#------------------------------------------------------------------------------------------------------Level 2 Easter Egg Version------------------------------------------------------------------------------------------------------------------------------
if easterstatus == 1:
    
    finalshoot = 0
    
    #Level 2 screen
    l2_pen = turtle.Turtle()
    l2_pen.hideturtle()
    l2_pen.speed(0)
    l2_pen.color('red')
    l2_pen.penup()
    l2_pen.setposition(-100, 0)
    l2_pen.write('Level 2 - Easter Eggs Version', False, align='left', font=('Arial', 18, 'normal'))
    time.sleep(1.5)
    l2_pen.clear()
    l2_pen.hideturtle()

    #Bring back p1
    p1.setposition(0,0)
    p1.showturtle()

    #Making the rectangle walls
    re1 = turtle.Turtle()
    re1.penup()
    re1.shape('square')
    re1.color('black')
    re1.setposition(150,150) 
    re1.speed(0) #Makes the animation speed fast
    re1.turtlesize(20, 1, 1)

    re2 = turtle.Turtle()
    re2.penup() #Makes it so there is no trail
    re2.shape('square')
    re2.color('black')
    re2.setposition(-250,-150)
    re2.speed(0) #Makes the animation speed fast
    re2.turtlesize(15, 1, 1)

    #Bring back t1
    wn.register_shape('egg.gif')
    t1.shape('egg.gif')
    t1.setposition(random.randint(-780,780), random.randint(-410,410))
    t1.showturtle()


    while True:
        
        p1.forward(speed)

        #For player boundries
    
        if p1.xcor() > (800-14.9) or p1.xcor() < (-800+14.9):
            p1.right(180)

        elif p1.ycor() > (430-14.9) or p1.ycor() < (-430+14.9):
            p1.left(180)
        
        #This does a collision check with t1 

        if p1status == 'Ready':
            
            if collision (p1, t1):
                t1.setposition(random.randint(-780,780), random.randint(-410,410))
                t1.left(random.randint(0,360))
                if health >=1:
                    health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                p1status = 'Not ready'
                p1.setposition(0,0)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'

        if shooting == 'not ready':
            if collision (shoot, t1):
                t1.setposition(random.randint(-780,780), random.randint(-410,410))
                t1.left(random.randint(0,360))
                shooting = 'ready'
                shoot.hideturtle()
                speedt += 1
            
                score += 1
            
                #This makes it a live score using your variable

                s_string = 'Score: %s' %score
                s_pen.clear()
                s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
            
                #Make more targets

                yeety += 1

                if yeety == 1:

                    wer.append(turtle.Turtle())
                    wer[0].color('red')
                    wer[0].shape('egg.gif')
                    wer[0].penup()
                    wer[0].speed(0)
                    wer[0].setposition(random.randint(-780,780), random.randint(-410,410))

                else:
            
                    wer.append(turtle.Turtle())
                    wer[yeety - 1].color('red')
                    wer[yeety - 1].shape('egg.gif')
                    wer[yeety - 1].penup()
                    wer[yeety - 1].speed(0)
                    wer[yeety - 1].setposition(random.randint(-780,780), random.randint(-410,410))


        #boundaries for t1

        if t1.xcor() > 800 or t1.xcor() < -800:
            t1.right(180)

        elif t1.ycor() > 430 or t1.ycor() < -430:
            t1.left(180)

        #Boundaries for shoot

        if shoot.xcor() > 800 or shoot.xcor() < -800:
            shoot.right(180)
            shooting = 'ready'
            shoot.hideturtle()

        elif shoot.ycor() > 430 or shoot.ycor() < -430:
            shoot.left(180)
            shooting = 'ready'
            shoot.hideturtle()
        
        #move t1
        t1.forward(speedt)

        #move shoot

        shoot.forward(shootsp)


        #Makes more Targets

        for x in range(0, len(wer)):
            wer[x].forward(speedt)

            if wer[x].xcor() > 800 or wer[x].xcor() < -800:
                wer[x].right(180)

            elif wer[x].ycor() > 430 or wer[x].ycor() < -430:
                wer[x].left(180)

            if p1status == 'Ready':
                
                if collision (p1, wer[x]):
                    wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                    wer[x].left(random.randint(0,360))
                    if health >=1:
                        health -= 1 
                    h_string = 'Lives: %s' %health
                    h_pen.clear()
                    h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                    h_pen.hideturtle()
                    p1status = 'Not ready'
                    p1.setposition(0,0)
                    p1.hideturtle()
                    time.sleep(0.3)
                    p1.showturtle()
                    time.sleep(0.3)
                    p1.hideturtle()
                    time.sleep(0.3)
                    p1.showturtle()
                    p1status = 'Ready'

            if shooting == 'not ready':
                if collision (shoot, wer[x]):
                    wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                    wer[x].left(random.randint(0,360))
                    shooting = 'ready'
                    shoot.hideturtle()
                
                    speedt += 1

                    score += 1
                    s_string = 'Score: %s' %score
                    s_pen.clear()
                    s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

                    yeety = yeety + 1

                    if yeety == 1:

                        wer.append(turtle.Turtle())
                        wer[0].color('red')
                        wer[0].shape('egg.gif')
                        wer[0].penup()
                        wer[0].speed(0)
                        wer[0].setposition(random.randint(-780,780), random.randint(-410,410))
                            
                    else:
                            
                        wer.append(turtle.Turtle())
                        wer[yeety - 1].color('red')
                        wer[yeety - 1].shape('egg.gif')
                        wer[yeety - 1].penup()
                        wer[yeety - 1].speed(0)
                        wer[yeety - 1].setposition(random.randint(-780,780), random.randint(-410,410))

        #collision between shoot and p1

        if shoot == 'not ready' and p1status == 'Ready':
            if collision (shoot, p1):
                shooting = 'ready'
                shoot.hideturtle()
                if health >=1:
                        health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                p1status = 'Not ready'
                p1.setposition(0,0)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'
                
        #Rectangle Collisions

        if shoot == 'not ready':
            if (shoot.xcor() > 130 and shoot.xcor() < 150) and (shoot.ycor() < re1.ycor() + 200 and shoot.ycor() > re1.ycor() - 200):
                shoot.right(180)

        if shoot == 'not ready':
            if (shoot.xcor() < -235 and shoot.xcor() > -250) and (shoot.ycor() < re2.ycor() + 150 and shoot.ycor() > re2.ycor() - 150):
                shoot.left(180)

        if (p1.xcor() > 130 and p1.xcor() < 150) and (p1.ycor() < re1.ycor() + 200 and p1.ycor() > re1.ycor() - 200):
            if health >=1:
                    health -= 1
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            play_sound('Explosion+1.wav')
            p1status = 'Not ready'
            p1.setposition(0,0)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'

        if (p1.xcor() < -235 and p1.xcor() > -250) and (p1.ycor() < re2.ycor() + 150 and p1.ycor() > re2.ycor() - 150):
            if health >=1:
                    health -= 1
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            play_sound('Explosion+1.wav')
            p1status = 'Not ready'
            p1.setposition(0,0)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'
                        
        if (t1.xcor() > 130 and t1.xcor() < 150) and (t1.ycor() < re1.ycor() + 200 and t1.ycor() > re1.ycor() - 200):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))

        elif (t1.xcor() < -235 and t1.xcor() > -250) and (t1.ycor() < re2.ycor() + 150 and t1.ycor() > re2.ycor() - 150):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))

        for x in range(0, len(wer)):

            if (wer[x].xcor() > 130 and wer[x].xcor() < 150) and (wer[x].ycor() < re1.ycor() + 200 and wer[x].ycor() > re1.ycor() - 200):
                wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                wer[x].left(random.randint(0,360))

            elif (wer[x].xcor() < -235 and wer[x].xcor() > -250) and (wer[x].ycor() < re2.ycor() + 150 and wer[x].ycor() > re2.ycor() - 150):
                wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                wer[x].left(random.randint(0,360))

        #Ending the game
        if health <=0:
            p1.hideturtle()
            t1.hideturtle()
            t1.ht()
            for x in range(0, len(r)):
                r[x].hideturtle()
                r[x].ht()
            end_pen = turtle.Turtle()
            end_pen.hideturtle()
            end_pen.speed(0)
            end_pen.color('red')
            end_pen.penup()
            end_pen.setposition(0, 0)
            end_pen.write('GAME OVER', False, align='left', font=('Arial', 18, 'normal'))
            time.sleep(100000000000000000000000000000000000)
            end_pen.clear()
            end_pen.hideturtle()

        #For level 3

        if score >= 5:
            p1.hideturtle()
            t1.hideturtle()
            re1.hideturtle()
            re2.hideturtle()
            finalshoot = 1
            t1.ht()
            score = 0
            speedt = 2
            health = 3
            shootsp = 20
            speed = 2
            for x in range(0, len(wer)):
                wer[x].hideturtle()
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            s_string = 'Score: %s' %score
            s_pen.clear()
            s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
            break
        
#------------------------------------------------------------------------------------------------------Level 2------------------------------------------------------------------------------------------------------------------------------
if easterstatus == 0:
    
    finalshoot = 0
    #Level 2 screen
    l2_pen = turtle.Turtle()
    l2_pen.hideturtle()
    l2_pen.speed(0)
    l2_pen.color('red')
    l2_pen.penup()
    l2_pen.setposition(0, 0)
    l2_pen.write('Level 2', False, align='left', font=('Arial', 18, 'normal'))
    time.sleep(1)
    l2_pen.clear()
    l2_pen.hideturtle()

    #Bring back p1
    p1.setposition(0,0)
    p1.showturtle()

    #Making the rectangle walls
    re1 = turtle.Turtle()
    re1.penup()
    re1.shape('square')
    re1.color('black')
    re1.setposition(150,150) 
    re1.speed(0) #Makes the animation speed fast
    re1.turtlesize(20, 1, 1)

    re2 = turtle.Turtle()
    re2.penup() #Makes it so there is no trail
    re2.shape('square')
    re2.color('black')
    re2.setposition(-250,-150)
    re2.speed(0) #Makes the animation speed fast
    re2.turtlesize(15, 1, 1)

    #Bring back t1
    t1.setposition(random.randint(-780,780), random.randint(-410,410))
    t1.showturtle()

    while True:
        
        p1.forward(speed)

        #For player boundries
    
        if p1.xcor() > (800-14.9) or p1.xcor() < (-800+14.9):
            p1.right(180)

        elif p1.ycor() > (430-14.9) or p1.ycor() < (-430+14.9):
            p1.left(180)
        
        #This does a collision check with t1 

        if p1status == 'Ready':
            
            if collision (p1, t1):
                t1.setposition(random.randint(-780,780), random.randint(-410,410))
                t1.left(random.randint(0,360))
                if health >=1:
                    health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                p1status = 'Not ready'
                p1.setposition(0,0)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'

        if shooting == 'not ready':
            if collision (shoot, t1):
                t1.setposition(random.randint(-780,780), random.randint(-410,410))
                t1.left(random.randint(0,360))
                shooting = 'ready'
                shoot.hideturtle()
                speedt += 1
            
                score += 1
            
                #This makes it a live score using your variable

                s_string = 'Score: %s' %score
                s_pen.clear()
                s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
            
                #Make more targets

                yeety += 1

                if yeety == 1:

                    lll = random.randint(1, 2)
                    wer.append(turtle.Turtle())
                    wer[0].color('red')
                    if lll == 1:
                        wer[0].shape('as.gif')
                    else:
                        wer[0].shape('sat.gif')
                    wer[0].penup()
                    wer[0].speed(0)
                    wer[0].setposition(random.randint(-780,780), random.randint(-410,410))

                else:

                    lll = random.randint(1, 2)
                    wer.append(turtle.Turtle())
                    wer[yeety - 1].color('red')
                    if lll == 1:
                        wer[yeety - 1].shape('as.gif')
                    else:
                        wer[yeety - 1].shape('sat.gif')
                    wer[yeety - 1].penup()
                    wer[yeety - 1].speed(0)
                    wer[yeety - 1].setposition(random.randint(-780,780), random.randint(-410,410))

        #boundaries for t1

        if t1.xcor() > 800 or t1.xcor() < -800:
            t1.right(180)

        elif t1.ycor() > 430 or t1.ycor() < -430:
            t1.left(180)

        #Boundaries for shoot

        if shoot.xcor() > 800 or shoot.xcor() < -800:
            shoot.right(180)
            shooting = 'ready'
            shoot.hideturtle()

        elif shoot.ycor() > 430 or shoot.ycor() < -430:
            shoot.left(180)
            shooting = 'ready'
            shoot.hideturtle()
        
        #move t1
        t1.forward(speedt)

        #move shoot

        shoot.forward(shootsp)

        #Makes more Targets

        for x in range(0, len(wer)):
            wer[x].forward(speedt)

            if wer[x].xcor() > 800 or wer[x].xcor() < -800:
                wer[x].right(180)

            elif wer[x].ycor() > 430 or wer[x].ycor() < -430:
                wer[x].left(180)

            if p1status == 'Ready':
                
                if collision (p1, wer[x]):
                    wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                    wer[x].left(random.randint(0,360))
                    if health >=1:
                        health -= 1 
                    h_string = 'Lives: %s' %health
                    h_pen.clear()
                    h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                    h_pen.hideturtle()
                    p1status = 'Not ready'
                    p1.setposition(0,0)
                    p1.hideturtle()
                    time.sleep(0.3)
                    p1.showturtle()
                    time.sleep(0.3)
                    p1.hideturtle()
                    time.sleep(0.3)
                    p1.showturtle()
                    p1status = 'Ready'

            if shooting == 'not ready':
                if collision (shoot, wer[x]):
                    wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                    wer[x].left(random.randint(0,360))
                    shooting = 'ready'
                    shoot.hideturtle()
                
                    speedt += 1

                    score += 1
                    s_string = 'Score: %s' %score
                    s_pen.clear()
                    s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

                    yeety = yeety + 1

                    if yeety == 1:

                        lll = random.randint(1, 2)
                        wer.append(turtle.Turtle())
                        wer[0].color('red')
                        if lll == 1:
                            wer[0].shape('as.gif')
                        else:
                            wer[0].shape('sat.gif')
                        wer[0].penup()
                        wer[0].speed(0)
                        wer[0].setposition(random.randint(-780,780), random.randint(-410,410))
                            
                    else:

                        lll = random.randint(1, 2)
                        wer.append(turtle.Turtle())
                        wer[yeety - 1].color('red')
                        if lll == 1:
                            wer[yeety - 1].shape('as.gif')
                        else:
                            wer[yeety - 1].shape('sat.gif')
                        wer[yeety - 1].penup()
                        wer[yeety - 1].speed(0)
                        wer[yeety - 1].setposition(random.randint(-780,780), random.randint(-410,410))

        #collision between shoot and p1

        if shoot == 'not ready' and p1status == 'Ready':
            if collision (shoot, p1):
                shooting = 'ready'
                shoot.hideturtle()
                if health >=1:
                        health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                p1status = 'Not ready'
                p1.setposition(0,0)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'

        #Rectangle Collisions

        if shoot == 'not ready':
            if (shoot.xcor() > 130 and shoot.xcor() < 150) and (shoot.ycor() < re1.ycor() + 200 and shoot.ycor() > re1.ycor() - 200):
                shoot.right(180)

        if shoot == 'not ready':
            if (shoot.xcor() < -235 and shoot.xcor() > -250) and (shoot.ycor() < re2.ycor() + 150 and shoot.ycor() > re2.ycor() - 150):
                shoot.left(180)

        if (p1.xcor() > 130 and p1.xcor() < 150) and (p1.ycor() < re1.ycor() + 200 and p1.ycor() > re1.ycor() - 200):
            if health >=1:
                    health -= 1
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            play_sound('Explosion+1.wav')
            p1status = 'Not ready'
            p1.setposition(0,0)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'

        if (p1.xcor() < -235 and p1.xcor() > -250) and (p1.ycor() < re2.ycor() + 150 and p1.ycor() > re2.ycor() - 150):
            if health >=1:
                    health -= 1
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            play_sound('Explosion+1.wav')
            p1status = 'Not ready'
            p1.setposition(0,0)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'
                        
        if (t1.xcor() > 130 and t1.xcor() < 150) and (t1.ycor() < re1.ycor() + 200 and t1.ycor() > re1.ycor() - 200):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))

        elif (t1.xcor() < -235 and t1.xcor() > -250) and (t1.ycor() < re2.ycor() + 150 and t1.ycor() > re2.ycor() - 150):
            t1.setposition(random.randint(-780,780), random.randint(-410,410))
            t1.left(random.randint(0,360))

        for x in range(0, len(wer)):

            if (wer[x].xcor() > 130 and wer[x].xcor() < 150) and (wer[x].ycor() < re1.ycor() + 200 and wer[x].ycor() > re1.ycor() - 200):
                wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                wer[x].left(random.randint(0,360))

            elif (wer[x].xcor() < -235 and wer[x].xcor() > -250) and (wer[x].ycor() < re2.ycor() + 150 and wer[x].ycor() > re2.ycor() - 150):
                wer[x].setposition(random.randint(-780,780), random.randint(-410,410))
                wer[x].left(random.randint(0,360))

        #Ending the game
        if health <=0:
            p1.hideturtle()
            t1.hideturtle()
            t1.ht()
            for x in range(0, len(r)):
                r[x].hideturtle()
                r[x].ht()
            end_pen = turtle.Turtle()
            end_pen.hideturtle()
            end_pen.speed(0)
            end_pen.color('red')
            end_pen.penup()
            end_pen.setposition(0, 0)
            end_pen.write('GAME OVER', False, align='left', font=('Arial', 18, 'normal'))
            time.sleep(100000000000000000000000000000000000)
            end_pen.clear()
            end_pen.hideturtle()

        #For level 3

        if score >= 5:
            p1.hideturtle()
            t1.hideturtle()
            re1.hideturtle()
            re2.hideturtle()
            finalshoot = 1
            t1.ht()
            score = 0
            speedt = 2
            health = 3
            shootsp = 20
            speed = 2
            for x in range(0, len(wer)):
                wer[x].hideturtle()
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            s_string = 'Score: %s' %score
            s_pen.clear()
            s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
            break
#------------------------------------------------------------------------------------------------------Boss Fight------------------------------------------------------------------------------------------------------------------------------
#Level Boss screen
l3_pen = turtle.Turtle()
l3_pen.hideturtle()
l3_pen.speed(0)
l3_pen.color('red')
l3_pen.penup()
l3_pen.setposition(0, 0)
l3_pen.write('Boss Fight', False, align='left', font=('Arial', 18, 'normal'))
time.sleep(1)
l3_pen.clear()
l3_pen.hideturtle()

#Bring back p1
p1.setposition(0,-100)
p1.showturtle()

#Making the boss1
b1 = turtle.Turtle()
b1.color('lightgreen')
b1.shape('circle')
b1.penup() #Makes it so there is no trail
b1.setposition(0,100) 
b1.speed(0) #Makes the animation speed fast
b1.turtlesize(sizeb, sizeb, 1)

finalshoot = 0

while True:

    if sizeb == 16:

        if herty == 0:
        
            #Turns of the boss1
            b1status = 'not ready'
            b1.hideturtle()
        
            #Making the boss2
            b2 = turtle.Turtle()
            b2.color('lightgreen')
            b2.shape('circle')
            b2.penup() #Makes it so there is no trail
            b2.setposition(0,-200) 
            b2.speed(0) #Makes the animation speed fast
            b2.turtlesize(sizeb2, sizeb2, 1)


            #Making the boss3
            b3 = turtle.Turtle()
            b3.color('lightgreen')
            b3.shape('circle')
            b3.penup() #Makes it so there is no trail
            b3.setposition(0,200) 
            b3.speed(0) #Makes the animation speed fast
            b3.turtlesize(sizeb3, sizeb3, 1)

            herty += 1


    #Moving the Boss's
    b1.forward(speedb)

    if b1status == 'not ready':
        
        b2.backward(speedb)
        
        b3.forward(speedb)
        

    #Moving shoot

    shoot.forward(shootsp)

    #Moving Player
        
    p1.forward(speed)

   

    #For boss3 boundries

    if b1status == 'not ready':
    
        if b3.xcor() > (800 - sizeb3) or b3.xcor() < (-800 + sizeb3):
            b3.right(120)

        elif b3.ycor() > (430 - sizeb3) or b3.ycor() < (-430 + sizeb3):
            b3.left(120)

   

    #For boss2 boundries

    if b1status == 'not ready':
    
        if b2.xcor() > (800 - sizeb2) or b2.xcor() < (-800 + sizeb2):
            b2.right(120)

        elif b2.ycor() > (430 - sizeb2) or b2.ycor() < (-430 + sizeb2):
            b2.left(120)

    #For boss1 boundries
    
    if b1.xcor() > (800 - sizeb) or b1.xcor() < (-800 + sizeb):
        b1.right(120)

    elif b1.ycor() > (430 - sizeb) or b1.ycor() < (-430 + sizeb):
        b1.left(120)

    #For player boundries
    
    if p1.xcor() > (800-14.9) or p1.xcor() < (-800+14.9):
        p1.right(180)

    elif p1.ycor() > (430-14.9) or p1.ycor() < (-430+14.9):
        p1.left(180)

    #Boundaries for shoot

    if shoot.xcor() > 800 or shoot.xcor() < -800:
        shoot.right(180)
        shooting = 'ready'
        shoot.hideturtle()

    elif shoot.ycor() > 430 or shoot.ycor() < -430:
        shoot.left(180)
        shooting = 'ready'
        shoot.hideturtle()

    #Boss1 collision with shoot

    if b1status == 'Ready':

        if shooting == 'not ready':
            if boss_collide(shoot,b1):
                sizeb += 2
                b1.turtlesize(sizeb, sizeb, 1)
                shooting = 'ready'
                shoot.hideturtle()
        
                score += 1
            
                s_string = 'Score: %s' %score
                s_pen.clear()
                s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
                

    #Boss3 collision with shoot

    if b1status == 'not ready':

        if b3status == 'Ready':

            if shooting == 'not ready':
                if boss3_collide(shoot,b3):
                    sizeb3 += 2
                    b3.turtlesize(sizeb3, sizeb3, 1)
                    shooting = 'ready'
                    shoot.hideturtle()
        
                    score += 1
            
                    s_string = 'Score: %s' %score
                    s_pen.clear()
                    s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

                

    #Boss2 collision with shoot

    if b1status == 'not ready':

        if b2status == 'Ready':

            if shooting == 'not ready':
                if boss2_collide(shoot,b2):
                    sizeb2 += 2
                    b2.turtlesize(sizeb2, sizeb2, 1)
                    shooting = 'ready'
                    shoot.hideturtle()
        
                    score += 1
            
                    s_string = 'Score: %s' %score
                    s_pen.clear()
                    s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))
                    s_pen.write(s_string, False, align='left', font=('Arial', 18, 'normal'))

    #Boss2 collision with p1
    if b1status == 'not ready' and p1status == 'Ready':

        if b2status == 'Ready':
        
            if boss2_collide(p1,b2):
                if health >=1:
                    health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                sizeb2 += 2
                b2.turtlesize(sizeb2, sizeb2, 1)
                p1status = 'Not ready'
                p1.setposition(0,-100)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'
                

    #Boss3 collision with p1
    if b1status == 'not ready' and p1status == 'Ready':

        if b3status == 'Ready':
        
            if boss3_collide(p1,b3):
                if health >=1:
                    health -= 1 
                h_string = 'Lives: %s' %health
                h_pen.clear()
                h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
                h_pen.hideturtle()
                sizeb3 += 2
                b3.turtlesize(sizeb3, sizeb3, 1)
                p1status = 'Not ready'
                p1.setposition(0,-100)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                time.sleep(0.3)
                p1.hideturtle()
                time.sleep(0.3)
                p1.showturtle()
                p1status = 'Ready'
                


    #Boss1 collision with p1
    if b1status == 'Ready' and p1status == 'Ready':
        
        if boss_collide(p1,b1):
            if health >=1:
                health -= 1 
            h_string = 'Lives: %s' %health
            h_pen.clear()
            h_pen.write(h_string, False, align='left', font=('Arial', 18, 'normal'))
            h_pen.hideturtle()
            sizeb += 2
            b1.turtlesize(sizeb, sizeb, 1)
            p1status = 'Not ready'
            p1.setposition(0,-100)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            time.sleep(0.3)
            p1.hideturtle()
            time.sleep(0.3)
            p1.showturtle()
            p1status = 'Ready'

    #Ends the game

    if health <= 0:
        p1.hideturtle()
        b1.hideturtle()
        shoot.hideturtle()
        end3_pen = turtle.Turtle()
        end3_pen.hideturtle()
        end3_pen.speed(0)
        end3_pen.color('red')
        end3_pen.penup()
        end3_pen.setposition(0, 0)
        end3_pen.write('GAME OVER', False, align='left', font=('Arial', 18, 'normal'))
        time.sleep(100000000000000000000000000000000000)
        end3_pen.clear()
        end3_pen.hideturtle()

    if sizeb2 == 20:
        b2status = 'Not ready'
        b2.hideturtle()

    if sizeb3 == 20:
        b3status = 'Not ready'
        b3.hideturtle()

    if b2status == 'Not ready' and b3status == 'Not ready':
        
        p1.hideturtle()
    
        l4_pen = turtle.Turtle()
        l4_pen.hideturtle()
        l4_pen.speed(0)
        l4_pen.color('red')
        l4_pen.penup()
        l4_pen.setposition(-100,0)
        l4_pen.write('You Have Finished the Game !!!', False, align='left', font=('Arial', 18, 'normal'))
        time.sleep(100000000000)
        l4_pen.clear()
        l4_pen.hideturtle()
        
        finalshoot = 1
        
        break
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





    


    
 


   
    





    


    









    
