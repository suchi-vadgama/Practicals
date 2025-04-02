%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
void yyerror(const char *s);
%}

%token I B T A e

%%

S0  : S { printf("Valid string\n"); } ;

S   : I F T S e S { printf("Valid string\n"); }
    | A           { printf("Valid string\n"); }
    ;

F   : B ;

%%

int main() {
    if (yyparse() == 0)
        printf("Valid string\n");
    else
        printf("Invalid string\n");
    return 0;
}

void yyerror(const char *s) {
    printf("Invalid string\n");
}
