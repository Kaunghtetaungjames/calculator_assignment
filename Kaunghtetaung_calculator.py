import math
import random

class Calculator:
    def __init__(self):
        self.calculator_version = "1.1"
    
    # Display options for the user
    def options(self):
        print("\nOptions")
        print("Enter 'calculate' to evaluate an expression")
        print("Enter 'prefix' to convert expression to prefix notation")
        print("Enter 'postfix' to convert expression to postfix notation")
        print("Enter 'info' for more information and help")
        print("Enter 'quit' to end the program")
        
    # Run the calculator
    def run(self):
        while True:
            self.options()
            user_input = input("\nPlease input your command: ")

            # Evaluate expression
            if user_input == "calculate":
                expression = input("Enter an arithmetic expression in infix notation: ")
                result = self.evaluate(expression)
                print("\nThe result is:", result)

            # Convert expression to prefix notation
            elif user_input == "prefix":
                expression = input("Enter an arithmetic expression in infix notation: ")
                prefix_expression = self.infix_to_prefix(expression)
                print("\nPrefix notation:", prefix_expression)

            # Convert expression to postfix notation
            elif user_input == "postfix":
                expression = input("Enter an arithmetic expression in infix notation: ")
                postfix_expression = self.infix_to_postfix(expression)
                print("\nPostfix notation:", postfix_expression)

            # Display more information
            elif user_input == "info":
                print("\nInformation")
                print("This calculator evaluates arithmetic expressions with + and * operators.")
                print("Operator + has higher priority than * operator.")
                print("You can also convert expressions to prefix and postfix notations.")
                print("Current version:", self.calculator_version)

            # Quit the program
            elif user_input == "quit":
                print("\nThank you for using this calculator!")
                break

            else:
                print("Unknown input")
    
    # Evaluate arithmetic expression
    def evaluate(self, expression):
        postfix_expression = self.infix_to_postfix(expression)
        return self.evaluate_postfix(postfix_expression)
    
    # Convert infix expression to postfix notation
    def infix_to_postfix(self, expression):
        precedence = {'+': 1, '*': 0}
        stack = []
        postfix = []

        for char in expression.split():
            if char.isdigit():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence.get(stack[-1], 0) <= precedence[char]:
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ' '.join(postfix)
    
    # Evaluate postfix expression
    def evaluate_postfix(self, expression):
        stack = []
        for char in expression.split():
            if char.isdigit():
                stack.append(int(char))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
        return stack.pop()

    # Convert infix expression to prefix notation
    def infix_to_prefix(self, expression):
        reversed_expression = ' '.join(expression.split()[::-1])
        reversed_postfix = self.infix_to_postfix(reversed_expression)
        return ' '.join(reversed_postfix.split()[::-1])

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
