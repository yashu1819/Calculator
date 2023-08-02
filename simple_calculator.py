from stack import Stack

class SimpleCalculator:
    def __init__(self):
        """
		Instantiate any data attributes
		"""
        self.history = []

    def evaluate_expression(self, input_expression):
        """
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
        for i in range(len(input_expression)):
            if input_expression[i] in ['+','-','*','/']:
                pos = i
                
        if input_expression[pos] == '+':
            try:
                self.history.append((input_expression,float(input_expression[:pos]) + float(input_expression[pos+1:])))
                return str(float(input_expression[:pos]) + float(input_expression[pos+1:]))
            
            except:
                self.history.append((input_expression,'ERROR'))
                return 'ERROR'
        elif input_expression[pos] == '-':
            try:
                self.history.append((input_expression,float(input_expression[:pos]) - float(input_expression[pos+1:])))
                return str(float(input_expression[:pos]) - float(input_expression[pos+1:]))
            except:
                self.history.append((input_expression,'ERROR'))
                return 'ERROR'
        elif input_expression[pos] == '*':
            try:
                self.history.append((input_expression,float(input_expression[:pos]) * float(input_expression[pos+1:])))
                return str(float(input_expression[:pos]) * float(input_expression[pos+1:]))
            except:
                self.history.append((input_expression,'ERROR'))
                return 'ERROR'
        elif input_expression[pos] == '/':
            try:
                self.history.append((input_expression,float(input_expression[:pos]) / float(input_expression[pos+1:])))
                return str(float(input_expression[:pos]) / float(input_expression[pos+1:]))
            except:
                self.history.append((input_expression,'ERROR'))
                return 'ERROR'
                
                
    def get_history(self): 
        """
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
        return self.history.reverse()


    