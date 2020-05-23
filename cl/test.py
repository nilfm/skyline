import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser

#input_stream = InputStream(input('>>> '))
input_stream = InputStream('d2 := (-(1, 1, 1)*5 + (2, 2, 2)) * -[(4,4,  4), (3, 3, 3)]')

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
