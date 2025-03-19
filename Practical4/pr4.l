%{
    #include <stdio.h>
%}

%%
[0-9]* {printf("%s\n",yytext);}
[a-zA-z]* {/*Ignore the characters*/}
[*=:_>] {/*Ignore the character*/}
[ \t\n] {/*Ignore white spaces*/}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
