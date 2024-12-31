class FiniteAutomaton:
    def __init__(self, states, symbols, transitions, initial_state, final_states):
        self.states = states
        self.symbols = symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def is_valid_string(self, input_string):
        current_state = self.initial_state

        for symbol in input_string:
            if symbol not in self.symbols:
                return False  

            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False  

            current_state = self.transitions[current_state][symbol]

        return current_state in self.final_states

# Function to read the automaton details and process the input string
def main():
    num_symbols = int(input("Number of input symbols: "))
    symbols = input("Input symbols: ").split()

    num_states = int(input("Enter number of states: "))
    states = [str(i) for i in range(1, num_states + 1)]

    initial_state = input("Initial state: ")

    num_final_states = int(input("Number of accepting states: "))
    final_states = input("Final state(s): ").split()

    print("Enter transitions (e.g., '1 (symbol) 2' means from state 1 on symbol like 'a' go to state 2):")
    transitions = {}
    while True:
        transition_input = input()
        if not transition_input.strip():
            break

        from_state, symbol, to_state = transition_input.split()
        if from_state not in transitions:
            transitions[from_state] = {}
        transitions[from_state][symbol] = to_state

    fa = FiniteAutomaton(states, symbols, transitions, initial_state, final_states)

    input_string = input("Input string: ")

    if fa.is_valid_string(input_string):
        print("Valid string")
    else:
        print("Invalid string")

if __name__ == "__main__":
    main()