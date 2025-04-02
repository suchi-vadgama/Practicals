import ast
import re

def evaluate_constants(expression):
    # Regular expression to match arithmetic expressions with constants only
    pattern = re.compile(r'\b\d+[\s]*[+\-*/][\s]*\d+\b')
    
    while True:
        match = pattern.search(expression)
        if not match:
            break  # Stop if no more constant subexpressions are found
        
        # Evaluate the matched constant subexpression
        result = eval(match.group())
        
        # Replace the matched expression with its evaluated result
        expression = expression[:match.start()] + str(result) + expression[match.end():]
    
    return expression

def main():
    expr = input("Enter an arithmetic expression: ")
    optimized_expr = evaluate_constants(expr)
    print("Optimized Expression:", optimized_expr)

if __name__ == "__main__":
    main()