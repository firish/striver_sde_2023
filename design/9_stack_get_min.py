# Leetcode Mediums
# Link: https://leetcode.com/problems/min-stack/submissions/
# 13k upvotes+

# My solutions
class MinStack:
    
    # The base idea is to use two stacks
    # If the first stack holds elements
    # The second stacks holds the minimum value in stack upto the addition of corresponding element in stack 1
    def __init__(self):
        self.stack = []
        self.minimums = []
        self.curr_min = 10**12
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.curr_min:
            self.curr_min = val
        self.minimums.append(self.curr_min)

        

    def pop(self) -> None:
        val = self.stack.pop()
        min_pop = self.minimums.pop()
        if len(self.minimums) > 0:
            self.curr_min = self.minimums[-1]
        else:
            self.curr_min = 10**12
            
        
        
    def top(self) -> int:
        return self.stack[-1]
    

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
