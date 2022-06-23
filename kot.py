from random import randint

class kot:
    mx=[]
    my=[]
    def __init__(self,x,y):
        self.mx.append(x)
        self.my.append(y)
        self.x=x
        self.y=y
    def kotruch(self):
        rx=randint(-10,10)    
        if rx+self.x<=1000 and rx+self.x>=0:
            self.x+=rx
        else: None
        ry=randint(-10,10)    
        if ry+self.y<=1000 and ry+self.y>=0:
            self.y+=ry
        else: None
        # self.x+=rx
        # self.y+=ry
        self.mx.append(self.x)
        self.my.append(self.y)
   

    
    
    
