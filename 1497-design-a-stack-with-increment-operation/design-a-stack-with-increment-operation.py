class CustomStack:
    
    def __init__(self, maxSize: int):
        self.size=-1
        self.maxSize=maxSize
        self.stack=[]
    def push(self, x: int) -> None:
        if self.size+1>=self.maxSize:
            return
        else:
            
            self.stack.append(x)
            self.size+=1
       
            

    def pop(self) -> int:
        
        if self.size==-1:
          
            return -1
        else:
            self.size-=1
            
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        i=0
        
        while i<=self.size and i<k:
            self.stack[i]+=val
            i+=1
       


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)