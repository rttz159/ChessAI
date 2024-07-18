import WebEngine

class Main():
    def __init__(self):
        self.x = WebEngine.GUI(r"D:\Study\ProgramFiles\stockfish\stockfish-windows-x86-64-avx2")
        
    def run(self):
        self.x.m.mainloop()

if __name__ == "__main__":
    k = Main()
    k.run()