import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from stockfish import Stockfish
from AutoClick import *
import chess
import time

class GUI():
    def __init__(self,path):
        self.m = tk.Tk()
        self.m.title("Chess AI")        
        self.button = tk.Button(self.m,text="Start",command=self.Start)
        self.button.pack(padx=20,pady=10)
        self.button1 = tk.Button(self.m,text="Run White",command=self.run_bot_white)
        self.button1.pack(padx=20,pady=10)     
        self.button2 = tk.Button(self.m,text="Run Black",command=self.run_bot_black)
        self.button2.pack(padx=20,pady=10)
        self.m.geometry("300x150")
        self.AutoMouse = AutoDragger()
        self.m.resizable(False,False)
        self.path = path

    def Start(self):
        self.browser = webdriver.Chrome()
        self.browser.get(r"https://www.chess.com/play")
        
    def run_bot_white(self):
        self.setup()
        best_move = self.engine.get_best_move()
        self.AutoMouse.Drag((self.AutoMouse.convertStrToPositionWhite(best_move[:2])),self.AutoMouse.convertStrToPositionWhite(best_move[2:5]))
        self.bot_logic(self.AutoMouse.convertStrToPositionWhite,True)

                

    def run_bot_black(self):
        self.setup()
        self.bot_logic(self.AutoMouse.convertStrToPositionBlack,False)

    def setup(self):
        self.engine = Stockfish(path=self.path)
        self.board = chess.Board()
        self.moves = []

    def bot_logic(self,function,condition):

        while(True):
            elements = self.browser.find_elements(By.CSS_SELECTOR, '[class*="node-highlight-content"][class*="offset-for-annotation-icon"]')
            if(len(elements) != len(self.moves)):
                try:
                    self.moves.append(elements[-1].find_element(By.CSS_SELECTOR,"[class*=icon-font-chess]").get_attribute("data-figurine")+elements[-1].text)
                except:
                    self.moves.append(elements[-1].text)
                self.board.push_xboard(self.moves[-1])
                if(self.board.is_checkmate()):
                    print("Congrates!! CHECKMATE!!")
                    break
                try:
                    if(elements[-1].find_element(By.CSS_SELECTOR,"game-over-message-component").text.lower() == "game over"):
                        print("The Game Ended.")
                        break
                except:
                    pass
                self.engine.make_moves_from_current_position([self.board.peek()])
                if(condition == False):
                    if(len(self.moves)%2 == 1):
                        best_move = self.engine.get_best_move()
                        self.AutoMouse.Drag(function((best_move[:2])),function(best_move[2:]))
                else:
                    if(len(self.moves)%2 == 0 and len(self.moves) != 1):
                        best_move = self.engine.get_best_move()      
                        self.AutoMouse.Drag(function((best_move[:2])),function(best_move[2:]))