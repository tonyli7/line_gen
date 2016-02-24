from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if x1<x0:#handles left side
        tempx=x0
        tempy=y0
        x0=x1
        y0=y1
        x1=tempx
        y1=tempy

    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
   
    if (B==0 and A>=0) or A>=-B:
        d=A+2*B
        while y<=y1:
            plot(screen, color, x,y)
            if d<0:
                x+=1
                d+=2*A
            y+=1
            d+=2*B

    elif B==0 or A<=B:
        d=A-2*B
        while y>=y1:
            plot(screen,color,x,y)
            if d>0:
                x+=1
                d+=2*A
            y-=1
            d-=2*B

    elif A>=0 and A<-B: 
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x,y)
            if d>0:
                y+=1
                d+=2*B
            x+=1 
            d+=2*A
    else:
        d=2*A-B
        while x<=x1:
            plot(screen,color,x,y)
            if d<0:
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    
    
    pass
