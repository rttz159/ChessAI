import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from stockfish import Stockfish
import chess
import time

class GUI():
    def __init__(self):
        self.m = tk.Tk()
        self.m.title("Chess AI")        
        self.button = tk.Button(self.m,text="Start",command=self.Start)
        self.button.pack()
        self.button1 = tk.Button(self.m,text="Run White",command=self.run_bot_white)
        self.button1.pack()     
        self.button1 = tk.Button(self.m,text="Run Black",command=self.run_bot_black)
        self.button1.pack()
        self.m.geometry("200x200")

    def Start(self):
        self.browser = webdriver.Chrome()
        self.browser.get(r"https://www.chess.com/play")
        
    def run_bot_white(self):
        self.engine = Stockfish(path=r"D:/Study/ProgramFiles/stockfish/stockfish-windows-x86-64-avx2")
        board = chess.Board()
        moves = []
        print("the best move is " + self.engine.get_best_move())
        while(True):

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
                self.engine.make_moves_from_current_position([board.peek()])
                if(len(moves)%2 == 0 and len(moves) != 1):
                    print("the best move is " + self.engine.get_best_move())
            time.sleep(1)

    def run_bot_black(self):
        self.engine = Stockfish(path=r"D:/Study/ProgramFiles/stockfish/stockfish-windows-x86-64-avx2")
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
                    print("congrates!! CHECKMATE!!")
                    break
                self.engine.make_moves_from_current_position([board.peek()])
                if(len(moves)%2 == 1):
                    print("the best move is " + self.engine.get_best_move())
            time.sleep(1)