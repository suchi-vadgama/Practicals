%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(const char *s);
int yylex();
%}

/* Tokens from lexer */
%union {
    double fval;
}

%token <fval> NUMBER
%token PLUS MINUS TIMES DIVIDE POWER LPAREN RPAREN

/* Operator precedence */
%left PLUS MINUS
%left TIMES DIVIDE
%right POWER  /* Right-associative for exponentiation */
%nonassoc UMINUS /* Unary minus */

%type <fval> E T F G

%%

L  : E { printf("Result: %lf\n", $1); }
   ;

E  : E PLUS T   { $$ = $1 + $3; }
   | E MINUS T  { $$ = $1 - $3; }
   | T          { $$ = $1; }
   ;

T  : T TIMES F  { $$ = $1 * $3; }
   | T DIVIDE F { 
        if ($3 == 0) {
            printf("Error: Division by zero\n");
            exit(1);
        } 
        $$ = $1 / $3; 
   }
   | F          { $$ = $1; }
   ;

F  : G POWER F  { $$ = pow($1, $3); }
   | G          { $$ = $1; }
   ;

G  : LPAREN E RPAREN { $$ = $2; }
   | NUMBER          { $$ = $1; }
   ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter an arithmetic expression: ");
    yyparse();
    return 0;
}
