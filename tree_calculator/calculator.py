from inspect import stack
import re


class Tree_calculator:
    def __init__(self):
        self.input = None
        self.output = []

    def get_operator_priority(self, operator: str) -> int:
        if operator in ['*', '/']:
            return 1
        elif operator in ['+', '-']:
            return 0
        elif operator == '(':
            return -1
    
    def convert_experssion(self, expression: str) -> list:
        return re.findall(r'[-+]|[0-9]*\.?[0-9]+|[*+-/()]', expression)
    
    def isOperand(self, ch):
        return ch.isdigit()
    
    def infixToPosfix(self, expression):
        stack = []
        for e in expression:
            if self.isOperand(e):
                self.output.append(e)

            elif e == '(':
                stack.append(e)
            
            elif e == ')':
                while stack:
                    if stack[-1] == '(': 
                        stack.pop()
                        break
                    self.output.append(stack.pop())
            
            elif not stack:
                stack.append(e)
            else:
                while stack:
                    if self.get_operator_priority(e) < self.get_operator_priority(stack[-1]):
                        self.output.append(stack.pop())
                    else:
                        break
                stack.append(e)
        
        while stack:
            self.output.append(stack.pop())

        print(expression, " -> " , "".join(self.output))
        self.output = []

a = Tree_calculator()
a.infixToPosfix("3+4*5")
a.infixToPosfix("3*4*5")
a.infixToPosfix("3+4-5")
a.infixToPosfix("3*4+5")
a.infixToPosfix("3*4/5")