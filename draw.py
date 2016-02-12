from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = 2*A + B

    if A>=0 or B/A > 1: 
        while (x <= x1):
            plot(screen, color, x,y)
            if (d>0):
                y+=1
                d+=2*B
            x+=1 
            d+=2*A
    
    elif -B/A > 0 and B/A < 1:
        while (y <= y1):
            plot(screen, color, x,y)
            if (d>0):
                x+=1
                d+=2*B
            y+=1 
            d+=2*A
    pass
