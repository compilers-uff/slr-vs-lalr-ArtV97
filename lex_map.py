import ply.lex as lex

# S -> L = R | R
# L -> * R | id
# R -> L

tokens = ['EQUALS', 'TIMES', 'ID']

t_ignore  = ' \t\n' # espaco em branco
t_EQUALS = r'='
t_TIMES = r'\*'
t_ID = r'id'

lex.lex()
if __name__ == '__main__':

    lex.input("id*id")
    while True:
        tok = lex.token()
        if not tok: break

        print(tok)