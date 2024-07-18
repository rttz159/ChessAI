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
        self.path = path

    def Start(self):
        self.browser = webdriver.Chrome()
        self.browser.get(r"https://www.chess.com/play")
        
    def run_bot_white(self):
        self.engine = Stockfish(path=self.path)
        board = chess.Board()
        moves = []
        best_move = self.engine.get_best_move()
        print("the best move is " + best_move)
        self.AutoMouse.Drag((self.AutoMouse.convertStrToPositionWhite(best_move[:2])),self.AutoMouse.convertStrToPositionWhite(best_move[2:5]))
        while(True):
            game_over = self.browser.find_elements(By.CSS_SELECTOR, '[class*="game-over-arena-details-component"]')
            print(game_over[0].get_attribute("style") == '')
            elements = self.browser.find_elements(By.CSS_SELECTOR, '[class*="node-highlight-content"][class*="offset-for-annotation-icon"]')
            if(len(elements) != len(moves)):
                try:
                    moves.append(elements[-1].find_element(By.CSS_SELECTOR,"[class*=icon-font-chess]").get_attribute("data-figurine")+elements[-1].text)
                except:
                    moves.append(elements[-1].text)
                board.push_xboard(moves[-1])
                if(board.is_checkmate()):
                    print("Congrats!! CHECKMATE!!")
                    break
                try:
                    if(elements[-1].find_element(By.CSS_SELECTOR,"game-over-message-component").text.lower() == "game over"):
                        print("The Game Ended.")
                        break
                except:
                    pass
                self.engine.make_moves_from_current_position([board.peek()])
                if(len(moves)%2 == 0 and len(moves) != 1):
                    best_move = self.engine.get_best_move()
                    print("the best move is " + best_move)
                    self.AutoMouse.Drag((self.AutoMouse.convertStrToPositionWhite(best_move[:2])),self.AutoMouse.convertStrToPositionWhite(best_move[2:]))

    def run_bot_black(self):
        self.engine = Stockfish(path=self.path)
        board = chess.Board()
        moves = []
        while(True):
            elements = self.browser.find_elements(By.CSS_SELECTOR, '[class*="node-highlight-content"][class*="offset-for-annotation-icon"]')
            if(len(elements) != len(moves)):
                try:
                    moves.append(elements[-1].find_element(By.CSS_SELECTOR,"[class*=icon-font-chess]").get_attribute("data-figurine")+elements[-1].text)
                except:
                    moves.append(elements[-1].text)
                board.push_xboard(moves[-1])
                if(board.is_checkmate()):
                    print("Congrates!! CHECKMATE!!")
                    break
                try:
                    if(elements[-1].find_element(By.CSS_SELECTOR,"game-over-message-component").text.lower() == "game over"):
                        print("The Game Ended.")
                        break
                except:
                    pass
                self.engine.make_moves_from_current_position([board.peek()])
                if(len(moves)%2 == 1):
                    best_move = self.engine.get_best_move()
                    print("the best move is " + best_move)
                    self.AutoMouse.Drag((self.AutoMouse.convertStrToPositionBlack(best_move[:2])),self.AutoMouse.convertStrToPositionBlack(best_move[2:]))