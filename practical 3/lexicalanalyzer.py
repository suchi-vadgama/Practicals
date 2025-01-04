import re

class LexicalAnalyzer:
    def __init__(self):
        self.keywords = {
            "int", "char", "return", "float", "double", "if", "else", "while", "for", "long", "auto", "const", "short",
            "struct", "unsigned", "break", "continue", "signed", "switch", "void", "case", "default", "enum", "goto",
            "register", "sizeof", "typedef", "volatile", "union", "static", "extern", "do", "char"
        }
        self.reserved_functions = {"main", "scanf", "printf"}  # Functions treated as identifiers but excluded from the symbol table
        self.operators = {
            "=", "+", "-", "*", "/", "%", "++", "--", "&&", "||", "!", "==", "!=", ">", "<", ">=", "<="
        }
        self.punctuations = {"(", ")", "{", "}", "[", "]", ",", ";", "'", '"', "&"}
        self.symbol_table = []  # List to store unique identifiers
        self.tokens = []  # List to store tokens
        self.lexical_errors = []  # List to store lexical errors
        self.modified_source = ""  # Cleaned source code without lexical errors

    def analyze(self, filepath):
        # Step 1: Read the C source code file
        with open(filepath, "r") as file:
            source_code = file.read()

        # Step 2: Remove comments
        source_code_no_comments = self.remove_comments(source_code)

        # Step 3: Normalize white spaces
        normalized_source_code = self.normalize_whitespace(source_code_no_comments)

        # Step 4: Tokenize, clean invalid tokens, and rebuild source code
        self.tokenize(normalized_source_code)

        # Step 5: Display results
        self.display_results()

    def remove_comments(self, source_code):
        # Removes both single-line and multi-line comments
        return re.sub(r"//.*?$|/\*.*?\*/", "", source_code, flags=re.DOTALL | re.MULTILINE)

    def normalize_whitespace(self, source_code):
        # Replace multiple spaces/newlines with a single space, keeping structure intact
        return re.sub(r"\s+", " ", source_code).strip()

    def tokenize(self, source_code):
        # Define regex for token types
        token_pattern = re.compile(
            r"\b(?:int|char|return|float|double|if|else|while|for)\b|"  # Keywords
            r"[a-zA-Z_]\w*|"  # Identifiers
            r"\d+[a-zA-Z_]\w*|"  # Invalid tokens like 7H
            r"\d+|"  # Constants
            r"'[^']'|\".*?\"|"  # Strings
            r"[=+\-*/%<>!&|]+|"  # Operators
            r"[(){}\[\],;']"  # Punctuations
        )

        tokens = re.finditer(token_pattern, source_code)
        cleaned_code = source_code  # For building modified source code

        for match in tokens:
            token = match.group()
            if token in self.keywords:
                self.tokens.append(f"keyword: {token}")
            elif token in self.punctuations:
                self.tokens.append(f"punctuation: {token}")
            elif token in self.operators:
                self.tokens.append(f"operator: {token}")
            elif re.match(r"^\d+$", token):  # Numeric constant
                self.tokens.append(f"constant: {token}")
            elif re.match(r"^\d+[a-zA-Z_]\w*$", token):  # Invalid lexeme (e.g., 7H)
                self.lexical_errors.append(f"{token} invalid lexeme")
                # Remove invalid lexemes from the modified source code
                cleaned_code = cleaned_code.replace(token, "", 1)
            elif re.match(r"^[a-zA-Z_]\w*$", token):  # Valid identifier
                self.tokens.append(f"identifier: {token}")
                if token not in self.symbol_table and token not in self.reserved_functions:
                    self.symbol_table.append(token)
            elif re.match(r"'[^']'|\".*?\"", token):  # Strings
                self.tokens.append(f"string: {token}")
            else:
                self.lexical_errors.append(f"{token} invalid lexeme")
                cleaned_code = cleaned_code.replace(token, "", 1)

        # Update the modified source code
        self.modified_source = self.normalize_whitespace(cleaned_code)

    def display_results(self):
        print("Tokens:")
        for token in self.tokens:
            print(token)

        print("\nLexical Errors:")
        if self.lexical_errors:
            for error in self.lexical_errors:
                print(error)
        else:
            print("None")

        print("\nSymbol Table Entries:")
        for i, identifier in enumerate(self.symbol_table, start=1):
            print(f"{i}.{identifier}")

        print("\nModified Source Code:")
        print(self.modified_source)


# Example usage
if __name__ == "__main__":
    # Replace "salary.c" with the path to your C source code file
    filepath = "function.c"
    analyzer = LexicalAnalyzer()
    analyzer.analyze(filepath)