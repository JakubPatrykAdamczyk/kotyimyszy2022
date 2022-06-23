from random import randint

class kotek:
    mx=[]
    my=[]
    def __init__(self,x,y):
        self.mx.append(x)
        self.my.append(y)
        self.x=x
        self.y=y
    def kotruch(self):
        rx=randint(-5,5)    
        if rx+self.x<=100 and rx+self.x>=0:
            self.x+=rx
        else: None
        ry=randint(-5,5)    
        if ry+self.y<=100 and ry+self.y>=0:
            self.y+=ry
        else: None
    def zapisz(self):
        self.mx.append(self.x)
        self.my.append(self.y)
    def meat(self,x,y):
        self.x=x
        self.y=y
        self.zapisz()
