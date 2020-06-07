class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[]
        self.history.append(homepage)
        self.length=1
        self.current_pointer=0

    def visit(self, url: str) -> None:
        self.history=self.history[:self.current_pointer+1]
        self.history.append(url)
        self.length=len(self.history)
        self.current_pointer+=1

    def back(self, steps: int) -> str:
        self.current_pointer=max(0,self.current_pointer-steps)
        return self.history[self.current_pointer]

    def forward(self, steps: int) -> str:
        self.current_pointer=min(self.current_pointer+steps,self.length-1)    
        return self.history[self.current_pointer]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)