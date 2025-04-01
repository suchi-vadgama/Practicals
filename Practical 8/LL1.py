from collections import defaultdict
import pandas as pd

class PredictiveParsing:
    def __init__(self, grammar, first, follow):
        self.grammar = grammar
        self.first = first
        self.follow = follow
        self.table = defaultdict(dict)
        self.construct_parsing_table()

    def construct_parsing_table(self):
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                first_set = self.compute_first_for_production(production)
                for terminal in first_set - {'ε'}:
                    if terminal in self.table[non_terminal]:
                        print("Grammar is not LL(1) due to conflict in", non_terminal)
                        return False
                    self.table[non_terminal][terminal] = production
                
                if 'ε' in first_set:
                    for terminal in self.follow[non_terminal]:
                        if terminal in self.table[non_terminal]:
                            print("Grammar is not LL(1) due to conflict in", non_terminal)
                            return False
                        self.table[non_terminal][terminal] = production
        return True

    def compute_first_for_production(self, production):
        first_set = set()
        for symbol in production:
            if symbol in self.first:
                first_set |= (self.first[symbol] - {'ε'})
                if 'ε' not in self.first[symbol]:
                    break
            else:
                first_set.add(symbol)
                break
        else:
            first_set.add('ε')
        return first_set

    def print_table(self):
        df = pd.DataFrame(self.table).fillna('-')
        print("Predictive Parsing Table:")
        print(df.transpose())

    def validate_string(self, input_string):
        stack = ['$', 'S']  # Assuming 'S' is the start symbol
        input_string += '$'
        index = 0
        
        while stack:
            top = stack.pop()
            if top == input_string[index]:
                index += 1
            elif top in self.table and input_string[index] in self.table[top]:
                stack.extend(reversed(self.table[top][input_string[index]]))
            else:
                print("Invalid string")
                return
        print("Valid string")


# Define grammar, first, and follow sets
grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

first = {
    'S': {'a', 'b', '(', 'c'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'},
    'C': {'(', 'c'},
    'D': {'a', '('}
}

follow = {
    'S': {')', '$'},
    'A': {'b', '(', ')', '$'},
    'B': {'c', ')', '$'},
    'C': {')', '$'},
    'D': {')', '$'}
}

parser = PredictiveParsing(grammar, first, follow)
parser.print_table()

# Validate test cases
test_cases = ["abc", "ac", "(abc)", "c", "(ac)", "a", "()", "(ab)", "abcabc", "b"]
for test in test_cases:
    print(f"Input: {test}")
    parser.validate_string(test)