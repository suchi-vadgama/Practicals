class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")
        self.index = 0

    def parse_S(self):
        if self.match('a'):
            return True
        elif self.match('('):
            if self.parse_L() and self.match(')'):
                return True
        return False

    def parse_L(self):
        if self.parse_S():
            return self.parse_L_prime()
        return False

    def parse_L_prime(self):
        if self.match(','):
            if self.parse_S():
                return self.parse_L_prime()
            return False
        return True

    def match(self, char):
        if self.index < len(self.input) and self.input[self.index] == char:
            self.index += 1
            return True
        return False

    def validate(self):
        return self.parse_S() and self.index == len(self.input)


# Test cases
test_cases = ["a", "(a)", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)", "a)", "(a", "a,a", "(a,a),a"]

for test in test_cases:
    parser = RecursiveDescentParser(test)
    result = "Valid string" if parser.validate() else "Invalid string"
    print(f"Input: {test} => {result}")