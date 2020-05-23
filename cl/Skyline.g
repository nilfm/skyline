grammar Skyline;

root : base_expr EOF ;

base_expr : identifier ASSIG expr 
    | expr;

expr : constructor
    | identifier
    | LEFT_PAREN expr RIGHT_PAREN
    | MINUS expr
    | expr PROD num
    | num PROD expr
    | expr PROD expr
    | expr PLUS expr
    | expr PLUS num
    | num PLUS expr
    | expr MINUS num ;


constructor : single_building | multiple_buildings | random_buildings ;

single_building : LEFT_PAREN num SEP num SEP num RIGHT_PAREN ;

multiple_buildings : LEFT_SQUARE single_building (SEP single_building)* RIGHT_SQUARE ;

random_buildings : LEFT_PAREN num SEP num SEP num SEP num SEP num RIGHT_PAREN ;

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
DIGIT : [0-9] ;
LETTER : [a-z|A-Z] ;
