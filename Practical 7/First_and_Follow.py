from collections import defaultdict

class CFG:
    def __init__(self, rules):
        self.rules = rules  # Grammar rules
        self.first_sets = defaultdict(set)
        self.follow_sets = defaultdict(set)
        self.non_terminals = set(rules.keys())
        self.compute_first_sets()
        self.compute_follow_sets()

    def compute_first_sets(self):
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.rules.items():
                for production in productions:
                    for symbol in production:
                        before = len(self.first_sets[non_terminal])
                        if symbol in self.non_terminals:
                            self.first_sets[non_terminal] |= (self.first_sets[symbol] - {'ε'})
                            if 'ε' not in self.first_sets[symbol]:
                                break
                        else:
                            self.first_sets[non_terminal].add(symbol)
                            break
                    else:
                        self.first_sets[non_terminal].add('ε')
                        
                    after = len(self.first_sets[non_terminal])
                    if before != after:
                        changed = True

    def compute_follow_sets(self):
        self.follow_sets['S'].add('$')  # Start symbol always has $
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.rules.items():
                for production in productions:
                    trailer = self.follow_sets[non_terminal].copy()
                    for symbol in reversed(production):
                        if symbol in self.non_terminals:
                            before = len(self.follow_sets[symbol])
                            self.follow_sets[symbol] |= trailer
                            if 'ε' in self.first_sets[symbol]:
                                trailer |= (self.first_sets[symbol] - {'ε'})
                            else:
                                trailer = self.first_sets[symbol]
                            after = len(self.follow_sets[symbol])
                            if before != after:
                                changed = True
                        else:
                            trailer = {symbol}

    def print_sets(self):
        for non_terminal in self.rules:
            print(f"First({non_terminal}) = {self.first_sets[non_terminal]}")
        print()
        for non_terminal in self.rules:
            print(f"Follow({non_terminal}) = {self.follow_sets[non_terminal]}")


# Define the grammar
rules = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

cfg = CFG(rules)
cfg.print_sets()