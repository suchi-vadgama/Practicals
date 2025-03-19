%{
    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>
    
    int has_lower = 0; 
    int has_upper = 0;
    int has_digit = 0;
    int has_symbol = 0;
    int length = 0;
%}

%%

[a-z]     { has_lower++; length++; }
[A-Z]     { has_upper++; length++; }
[0-9]     { has_digit++; length++; }
[*;#$@]   { has_symbol++; length++; }
.         { length++; }
\n {
    if (length >= 9 && length <= 15 && has_lower && has_upper && has_digit && has_symbol) {
        printf("Valid Password\n");
    } else {
        printf("Invalid Password\n");
    }
    has_lower = has_upper = has_digit = has_symbol = length = 0;  // Removed 'input'
}
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
