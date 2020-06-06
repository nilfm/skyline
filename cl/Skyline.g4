grammar Skyline;

root : base_expr EOF ;

base_expr : identifier ASSIG expr 
    | expr;

expr :
    | LEFT_PAREN expr RIGHT_PAREN 
    | constructor
    | identifier
    | MINUS expr
    | expr PROD num
    | expr PROD expr
    | expr PLUS expr
    | expr PLUS num
    | expr MINUS num ;


constructor : single_building | multiple_buildings | random_buildings ;

single_building : LEFT_PAREN num SEP num SEP num RIGHT_PAREN ;

multiple_buildings : LEFT_SQUARE single_building (SEP single_building)* RIGHT_SQUARE ;

random_buildings : LEFT_BRACE num SEP num SEP num SEP num SEP num RIGHT_BRACE ;

identifier : VALID_ID;

num : VALID_NUM ;

VALID_ID : LETTER (DIGIT|LETTER)* ;
VALID_NUM : MINUS? [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
ASSIG : ':=' ;
PLUS : '+' ;
MINUS : '-' ;
PROD : '*' ;
SEP : ',' ;
LEFT_PAREN : '(' ;
RIGHT_PAREN : ')' ;
LEFT_SQUARE : '[' ;
RIGHT_SQUARE : ']' ;
LEFT_BRACE : '{' ;
RIGHT_BRACE : '}' ;
DIGIT : [0-9] ;
LETTER : [a-z|A-Z] ;
