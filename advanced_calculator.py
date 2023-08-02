from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		self.history=[]
		

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		
		if self.check_brackets(input_expression):
			try:
				self.history.append((input_expression,self.evaluate_list_tokens(self.tokenize(input_expression))[0]))
				return self.evaluate_list_tokens(self.tokenize(input_expression))[0]
			except:
				
				self.history.append((input_expression,'ERROR'))
				return('ERROR')
		self.history.append((input_expression,'ERROR'))
		return 'ERROR'
		

	def tokenize(self, input_expression):
		"""
		convert the input string expression to tokens, and return this list
		Each token is either an integer operand or a character operator or bracket
		"""
		list_token=[]
		t=''
		for i in input_expression:
			
			if i in ['{','}','(',')','+','-','*','/']:
				if t!='':
					list_token.append(int(t))
					list_token.append(i)
					t=''
				elif i=='-' :
					if list_token[-1] in ('(',')','{','}'):
						t+=i
					else:
						list_token.append(i)
				else:
					list_token.append(i)

			elif i==' ':
				if t!='':
					list_token.append(int(t))
					t=''
			
			else:
				t+=i
		if input_expression[-1] not in ['{','}','(',')','+','-','*','/',' ']:
			list_token.append(int(t))
		return(list_token)		
		
			

	def check_brackets(self, list_tokens):
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		count_of_open_round,count_of_close_round,count_of_open_curly,count_of_close_curly=0,0,0,0
		for i in list_tokens:
			if i=='(':
				count_of_open_round+=1
				
			elif i==')':
				count_of_close_round+=1
				if count_of_close_round>count_of_open_round:
					return False
			elif i=='{':
				count_of_open_curly+=1
				if count_of_open_round!=count_of_close_round:
					return False
			elif i=='}':
				count_of_close_curly+=1
				if count_of_close_curly>count_of_open_curly:
					return False
		if count_of_open_curly!=count_of_close_curly or count_of_close_round!=count_of_open_round:
			return False
		return True

	def evaluate_list_tokens(self, list_tokens):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""

		def dmas(lst_tok):
			i=0
			while i<len(lst_tok):
				if lst_tok[i]=='/':
					lst_tok=lst_tok[:i-1]+[lst_tok[i-1]/lst_tok[i+1]]+lst_tok[i+2:]
				i+=1
			i=0
			while i<len(lst_tok):
				if lst_tok[i]=='*':
					lst_tok=lst_tok[:i-1]+[lst_tok[i-1]*lst_tok[i+1]]+lst_tok[i+2:]
				i+=1
			i=0
			while i<len(lst_tok):
				if lst_tok[i]=='-':
					lst_tok=lst_tok[:i-1]+[lst_tok[i-1]-lst_tok[i+1]]+lst_tok[i+2:]
				i+=1
			i=0
			while i<len(lst_tok):
				if lst_tok[i]=='+':
					lst_tok=lst_tok[:i-1]+[lst_tok[i-1]+lst_tok[i+1]]+lst_tok[i+2:]
				i+=1
			return lst_tok
		
		while len(list_tokens)>1:
			if list_tokens[0] not in ['{','(']:
				list_tokens=['{']+list_tokens+['}']
			i=0
			j=0
			while i<len(list_tokens):
				if list_tokens[i] in ['{','(']:
					j=i
					i+=1
				elif list_tokens[i] not in ['}',')']:
					i+=1
				else:
					o=dmas(list_tokens[j+1:i])
					list_tokens=list_tokens[:j]+o+list_tokens[i+1:]
					return self.evaluate_list_tokens(list_tokens)
		return list_tokens		

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.history.reverse()

