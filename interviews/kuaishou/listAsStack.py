class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        """Pushes an element onto the stack."""
        self.stack.append(value)
    
    def pop(self):
        """Pops the top element from the stack and returns it."""
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        """Returns the top element of the stack without removing it."""
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)
