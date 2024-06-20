import WebEngine

class Main():
    def __init__(self):
        self.x = WebEngine.GUI()
        
    def run(self):
        self.x.m.mainloop()

if __name__ == "__main__":
    k = Main()
    k.run()