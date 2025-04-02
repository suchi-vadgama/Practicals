import re

class QuadrupleGenerator:
    def __init__(self):
        self.temp_count = 1
        self.quadruples = []

    def new_temp(self):
        temp_var = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_var

    def generate_quadruples(self, expression):
        postfix = self.infix_to_postfix(expression)
        stack = []

        for token in postfix:
            if token.isnumeric():
                stack.append(token)
            elif token in {"+", "-", "*", "/"}:
                op2 = stack.pop()
                op1 = stack.pop()
                temp_var = self.new_temp()
                self.quadruples.append((token, op1, op2, temp_var))
                stack.append(temp_var)

        return self.quadruples

    def infix_to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []
        
        tokens = re.findall(r'\d+|[+*/()-]', expression)

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token in precedence:
                while (stack and stack[-1] != '(' and 
                       precedence.get(stack[-1], 0) >= precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('

        while stack:
            output.append(stack.pop())

        return output

    def print_quadruples(self):
        print("\nQuadruple Table:")
        print(f"{'Operator':<10} {'Operand1':<10} {'Operand2':<10} {'Result':<10}")
        print("-" * 40)
        for quad in self.quadruples:
            print(f"{quad[0]:<10} {quad[1]:<10} {quad[2]:<10} {quad[3]:<10}")

# Get user input
expression = input("Enter an arithmetic expression: ")

quad_gen = QuadrupleGenerator()
quad_gen.generate_quadruples(expression)
quad_gen.print_quadruples()