%{
    #include <stdio.h>
%}

%%
[0-9]* {printf("Integer token: %s\n", yytext);}
[a-zA-z_][a-zA-z_]* {printf("Identifier: %s\n", yytext);}
[ \t\n] {/*Ignore white spaces*/}
. {printf("Unkown character: %s\n", yytext);}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
