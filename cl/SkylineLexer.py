# Generated from Skyline.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\7\2\'")
        buf.write("\n\2\f\2\16\2*\13\2\3\3\5\3-\n\3\3\3\6\3\60\n\3\r\3\16")
        buf.write("\3\61\3\4\6\4\65\n\4\r\4\16\4\66\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\2\2")
        buf.write("\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22\3\2\5\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\5\2C\\c|~~\2Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\3#\3\2\2\2\5,\3\2\2\2\7\64\3\2\2\2\t:\3\2\2\2")
        buf.write("\13=\3\2\2\2\r?\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23E\3")
        buf.write("\2\2\2\25G\3\2\2\2\27I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2")
        buf.write("\35O\3\2\2\2\37Q\3\2\2\2!S\3\2\2\2#(\5!\21\2$\'\5\37\20")
        buf.write("\2%\'\5!\21\2&$\3\2\2\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2")
        buf.write("()\3\2\2\2)\4\3\2\2\2*(\3\2\2\2+-\5\r\7\2,+\3\2\2\2,-")
        buf.write("\3\2\2\2-/\3\2\2\2.\60\t\2\2\2/.\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61/\3\2\2\2\61\62\3\2\2\2\62\6\3\2\2\2\63\65\t\3\2\2")
        buf.write("\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2")
        buf.write("\2\678\3\2\2\289\b\4\2\29\b\3\2\2\2:;\7<\2\2;<\7?\2\2")
        buf.write("<\n\3\2\2\2=>\7-\2\2>\f\3\2\2\2?@\7/\2\2@\16\3\2\2\2A")
        buf.write("B\7,\2\2B\20\3\2\2\2CD\7.\2\2D\22\3\2\2\2EF\7*\2\2F\24")
        buf.write("\3\2\2\2GH\7+\2\2H\26\3\2\2\2IJ\7]\2\2J\30\3\2\2\2KL\7")
        buf.write("_\2\2L\32\3\2\2\2MN\7}\2\2N\34\3\2\2\2OP\7\177\2\2P\36")
        buf.write("\3\2\2\2QR\t\2\2\2R \3\2\2\2ST\t\4\2\2T\"\3\2\2\2\b\2")
        buf.write("&(,\61\66\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VALID_ID = 1
    VALID_NUM = 2
    WS = 3
    ASSIG = 4
    PLUS = 5
    MINUS = 6
    PROD = 7
    SEP = 8
    LEFT_PAREN = 9
    RIGHT_PAREN = 10
    LEFT_SQUARE = 11
    RIGHT_SQUARE = 12
    LEFT_BRACE = 13
    RIGHT_BRACE = 14
    DIGIT = 15
    LETTER = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "','", "'('", "')'", "'['", "']'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "VALID_ID", "VALID_NUM", "WS", "ASSIG", "PLUS", "MINUS", "PROD", 
            "SEP", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE", "RIGHT_SQUARE", 
            "LEFT_BRACE", "RIGHT_BRACE", "DIGIT", "LETTER" ]

    ruleNames = [ "VALID_ID", "VALID_NUM", "WS", "ASSIG", "PLUS", "MINUS", 
                  "PROD", "SEP", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE", 
                  "RIGHT_SQUARE", "LEFT_BRACE", "RIGHT_BRACE", "DIGIT", 
                  "LETTER" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


