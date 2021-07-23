import ply.yacc as yacc
from lex_map import tokens

# S -> L = R
# S -> R
# L -> * R
# L -> id
# R -> L

def p_P0(p):
    'S : L EQUALS R'

def p_P1(p):
    'S : R'

def p_P2(p):
    'L : TIMES R'

def p_P3(p):
    'L : ID'

def p_P4(p):
    'R : L'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
yacc.yacc()
