class Stack:
    
    def __init__(self):
        self.items = []
		# Initialise the stack's data attributes
	
    def push(self, item):
        self.items =  self.items+[item]
            
            
		# Push an item to the stack
	    

    def peek(self):
        
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
        if self.is_empty():
            return 'ERROR'
        else:
            return self.items[-1]

    def pop(self):
        self.items.pop()
        
		# Pop an item from the stack if non-empty
     	

    def is_empty(self):
        return self.items == []
		# Return True if stack is empty, False otherwise
	    

    def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
        s = ''
        for i in self.items:
            s+= ' ' + str(i)
        return s[1:]    

    def __len__(self):
		# Return current number of elements in the stack
        return len(self.items)
    
