import pyautogui


class AutoDragger():
    def __init__(self) -> None:
        self.mouse = pyautogui

    def convertStrToPositionWhite(self, x :str):
        return (275 + ((ord(x[0]) -97) * 100), 225 + ((800 - int(x[1]) * 100) ))
    
    def convertStrToPositionBlack(self, x :str):
        return (275 + ( (7 - (ord(x[0]) - 97)) * 100), 225 + ((int(x[1]) - 1) * 100) )

    def Drag(self,x,y):
        self.mouse.moveTo(x[0],x[1])
        self.mouse.dragTo(y[0],y[1])