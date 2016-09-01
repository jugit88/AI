import sys

class Stack:

    def __init__(self):
        self.stack = []

    def push(self,integer):
        lst = self.stack
        lst.append(integer)
        
    def pop(self):
        lst = self.stack
        if (len(lst) == 0):
            return "Stack empty."
        else:    
            return lst.pop()
    def checkSize(self):
        return len(self.stack)
    
