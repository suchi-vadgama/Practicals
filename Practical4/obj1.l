%{
    #include <stdio.h>
%}

%%
[cC][hH][aA][rR][uU][sS][aA][tT] {printf("university");}
. {putchar(yytext[0]);}
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
