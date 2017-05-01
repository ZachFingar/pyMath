import random
import turtle
t = turtle
t.shape("turtle")

def main():
    n = 8 #Disk Control
    p1x, p1y = -200, 0 #Peg 1 distance (need to set height to start turtle stack)
    p2x = 0 #Peg 2 X (y depends on current turtles stacked)
    p3x = 200 #Peg 3 X (y depends on current turtles stacked)
    disk = []
    color = []
    global actions
    actions = []
    length = 20*n
    pegs(p1x,p1y,length,3)

    t.penup()
    t.goto(p1x , p1y)
    
    for i in range(0, n):
        t.pendown()
        t.st()
        
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        t.fillcolor(r1, r2, r3)
        color.append((r1, r2, r3))
        
        ID = t.stamp()
        disk.append(ID)
        
        t.penup()
        t.ht()
        t.sety(16 * (i + 1))

    t.goto(-300,0)
    for i in range(0,n):
        t.pendown()
        t.st()
        t.fillcolor(color[i])
        t.stamp()
        t.ht()
        t.penup()
        t.sety(16 * (i + 1))
        
    move(p1x,p2x,p3x,n)
    f1 = n
    t2 = 0
    a3 = 0
    t.speed(0)
    disk.reverse()
    color.reverse()


    for i in range(0,len(actions),3):
        for j in range(1,n + 1): #list is reversed, to go to next highest, must subtract
            if actions[i] == (j): #IF DISK = 1-10, converter - disk 8 breaks it, dont know why
                print("Move Disk:",j)
                actions[i] = disk[j - 1]
                x = j-1
                t.fillcolor(color[j-1])
                
            
        fromPeg = actions[i + 1]
        if fromPeg == p1x: #Goto the frompeg to smooth out graphics
            #without it, it feels laggy and has random pauses / surges
            t.goto(fromPeg, f1*16)             
            f1 -= 1
        elif fromPeg == p2x:
            t.goto(fromPeg, t2*16)
            t2 -= 1
        else:
            t.goto(fromPeg, a3*16)
            a3 -= 1
    
        t.clearstamp(actions[i])
        
        toPeg = actions[i + 2]
        if toPeg == p1x:
            t.goto(toPeg, f1*16)
            f1 += 1
        elif toPeg == p2x:
            t.goto(toPeg, t2*16)
            t2 += 1
        elif toPeg == p3x:
            t.goto(toPeg, a3*16)
            a3 += 1

        t.st()
        disk[x] = t.stamp()
        t.ht()
        
    t.done()
    
def pegs(x1,y1,l,n):
    if n == 0:
        return
    else:
        t.penup()
        t.goto(x1 , y1)
        t.pendown()
        t.setheading(90)
        t.forward(l)
        t.setheading(0)
        pegs(x1 + 200, y1, l, n-1)

def move(x,y,z,n):
    if n == 1:
        actions.append(n)
        actions.append(x)
        actions.append(y)
    else:
        move(x,z,y,n-1)
        actions.append(n)
        actions.append(x)
        actions.append(y)
        move(z,y,x,n-1)


main()
#p,lg,g,dg,

            
