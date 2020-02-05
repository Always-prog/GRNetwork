import numpy as np
from tkinter import *







def fullsXY(N,y_index):
    y_cord = np.full((len(N),2),0.0)
    x_cord = []
    y_index = y_index
    for i in range(len(N)):
        y_cord[i][0] = y_index
        y_cord[i][1] = N[i][0]
        y_index += 10 
    return y_cord
    
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
    
def DrawNeurons(Win,N,X):
    for elem in range(len(N)):
        try:
            Win.create_oval([int(X),int(N[elem][0])],[int(X+8),int(N[elem][0]+8)],fill=from_rgb((int(N[elem][1] * 255),0,0)))  
        except(BaseException):
            pass
        
def DrawWeights(Win,W1,DrawN1,DrawN2,X1,X2):
    for elem in range(len(W1)):
        for elem2 in range(len(W1[elem])):
            try:
                Win.create_line(X1,DrawN1[elem][0],X2,DrawN2[elem2][0],width=1/3,fill=from_rgb((0,int(W1[elem][elem2] * 255),0)))
            except(BaseException):
                pass
            
class DrawNetwork():
    def __init__(self,WinH, WinW,):
        self.root = Tk()
        self.WinW = WinW
        self.WinH = WinH
        self.canvas = Canvas(self.root,width=self.WinW,height=self.WinH,bg="black")
        self.canvas.pack()  
        self.root.update()


           
    def Start(self,N1,N2,N3,N4,N5,W1,W2,W3,W4):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3 
        self.N4 = N4
        self.N5 = N5
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.W4 = W4
        self.DrawN1 = fullsXY(self.N1,10)
        self.DrawN2 = fullsXY(self.N2,10)
        self.DrawN3 = fullsXY(self.N3,10)
        self.DrawN4 = fullsXY(self.N4,10)
        self.DrawN5 = fullsXY(self.N5,10)
           
           
        DrawWeights(self.canvas,self.W1,self.DrawN1,self.DrawN2,100,200)        
        DrawWeights(self.canvas,self.W2,self.DrawN2,self.DrawN3,200,300)        
        DrawWeights(self.canvas,self.W3,self.DrawN3,self.DrawN4,300,400)        
        DrawWeights(self.canvas,self.W4,self.DrawN4,self.DrawN5,400,500) 
        DrawNeurons(self.canvas,self.DrawN1,100)     
        DrawNeurons(self.canvas,self.DrawN2,200) 
        DrawNeurons(self.canvas,self.DrawN3,300)     
        DrawNeurons(self.canvas,self.DrawN4,400) 
        DrawNeurons(self.canvas,self.DrawN5,500)         
        try:
            self.root.update()
        except(BaseException):
            pass
    def KillWin(self):
        self.root.destroy()


            

        
        
        
        