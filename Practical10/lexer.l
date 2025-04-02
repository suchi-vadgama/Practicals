%{
#include "parser.tab.h"  // Include Bison's header file
%}

DIGIT  [0-9]+(\.[0-9]+)?

%%

{DIGIT}      { yylval.fval = atof(yytext); return NUMBER; }
"("          { return LPAREN; }
")"          { return RPAREN; }
"+"          { return PLUS; }
"-"          { return MINUS; }
"*"          { return TIMES; }
"/"          { return DIVIDE; }
"^"          { return POWER; }
[ \t\n]+     { /* Ignore whitespace */ }
.            { printf("Invalid character: %s\n", yytext); return 0; }

%%

int yywrap() { return 1; }  // Required for Flex
