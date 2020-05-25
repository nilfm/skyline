# Generated from Skyline.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4(\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\7\49\n\4\f\4\16\4<\13\4\3\5\3\5\3\5\5\5A\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7O\n")
        buf.write("\7\f\7\16\7R\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\2\3\6\13\2\4")
        buf.write("\6\b\n\f\16\20\22\2\2\2h\2\24\3\2\2\2\4\34\3\2\2\2\6\'")
        buf.write("\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\fJ\3\2\2\2\16U\3\2\2\2")
        buf.write("\20a\3\2\2\2\22c\3\2\2\2\24\25\5\4\3\2\25\26\7\2\2\3\26")
        buf.write("\3\3\2\2\2\27\30\5\20\t\2\30\31\7\6\2\2\31\32\5\6\4\2")
        buf.write("\32\35\3\2\2\2\33\35\5\6\4\2\34\27\3\2\2\2\34\33\3\2\2")
        buf.write("\2\35\5\3\2\2\2\36\37\b\4\1\2\37(\5\b\5\2 (\5\20\t\2!")
        buf.write("\"\7\13\2\2\"#\5\6\4\2#$\7\f\2\2$(\3\2\2\2%&\7\b\2\2&")
        buf.write("(\5\6\4\b\'\36\3\2\2\2\' \3\2\2\2\'!\3\2\2\2\'%\3\2\2")
        buf.write("\2(:\3\2\2\2)*\f\6\2\2*+\7\t\2\2+9\5\6\4\7,-\f\5\2\2-")
        buf.write(".\7\7\2\2.9\5\6\4\6/\60\f\7\2\2\60\61\7\t\2\2\619\5\22")
        buf.write("\n\2\62\63\f\4\2\2\63\64\7\7\2\2\649\5\22\n\2\65\66\f")
        buf.write("\3\2\2\66\67\7\b\2\2\679\5\22\n\28)\3\2\2\28,\3\2\2\2")
        buf.write("8/\3\2\2\28\62\3\2\2\28\65\3\2\2\29<\3\2\2\2:8\3\2\2\2")
        buf.write(":;\3\2\2\2;\7\3\2\2\2<:\3\2\2\2=A\5\n\6\2>A\5\f\7\2?A")
        buf.write("\5\16\b\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\t\3\2\2\2BC\7")
        buf.write("\13\2\2CD\5\22\n\2DE\7\n\2\2EF\5\22\n\2FG\7\n\2\2GH\5")
        buf.write("\22\n\2HI\7\f\2\2I\13\3\2\2\2JK\7\r\2\2KP\5\n\6\2LM\7")
        buf.write("\n\2\2MO\5\n\6\2NL\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2")
        buf.write("\2QS\3\2\2\2RP\3\2\2\2ST\7\16\2\2T\r\3\2\2\2UV\7\13\2")
        buf.write("\2VW\5\22\n\2WX\7\n\2\2XY\5\22\n\2YZ\7\n\2\2Z[\5\22\n")
        buf.write("\2[\\\7\n\2\2\\]\5\22\n\2]^\7\n\2\2^_\5\22\n\2_`\7\f\2")
        buf.write("\2`\17\3\2\2\2ab\7\3\2\2b\21\3\2\2\2cd\7\4\2\2d\23\3\2")
        buf.write("\2\2\b\34\'8:@P")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':='", "'+'", "'-'", "'*'", "','", "'('", "')'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "VALID_ID", "VALID_NUM", "WS", "ASSIG", 
                      "PLUS", "MINUS", "PROD", "SEP", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE", "RIGHT_SQUARE", "DIGIT", "LETTER" ]

    RULE_root = 0
    RULE_base_expr = 1
    RULE_expr = 2
    RULE_constructor = 3
    RULE_single_building = 4
    RULE_multiple_buildings = 5
    RULE_random_buildings = 6
    RULE_identifier = 7
    RULE_num = 8

    ruleNames =  [ "root", "base_expr", "expr", "constructor", "single_building", 
                   "multiple_buildings", "random_buildings", "identifier", 
                   "num" ]

    EOF = Token.EOF
    VALID_ID=1
    VALID_NUM=2
    WS=3
    ASSIG=4
    PLUS=5
    MINUS=6
    PROD=7
    SEP=8
    LEFT_PAREN=9
    RIGHT_PAREN=10
    LEFT_SQUARE=11
    RIGHT_SQUARE=12
    DIGIT=13
    LETTER=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_expr(self):
            return self.getTypedRuleContext(SkylineParser.Base_exprContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.base_expr()
            self.state = 19
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Base_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SkylineParser.IdentifierContext,0)


        def ASSIG(self):
            return self.getToken(SkylineParser.ASSIG, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_base_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase_expr" ):
                return visitor.visitBase_expr(self)
            else:
                return visitor.visitChildren(self)




    def base_expr(self):

        localctx = SkylineParser.Base_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_base_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.identifier()
                self.state = 22
                self.match(SkylineParser.ASSIG)
                self.state = 23
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor(self):
            return self.getTypedRuleContext(SkylineParser.ConstructorContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SkylineParser.IdentifierContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SkylineParser.LEFT_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(SkylineParser.RIGHT_PAREN, 0)

        def MINUS(self):
            return self.getToken(SkylineParser.MINUS, 0)

        def PROD(self):
            return self.getToken(SkylineParser.PROD, 0)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)

        def num(self):
            return self.getTypedRuleContext(SkylineParser.NumContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 29
                self.constructor()
                pass

            elif la_ == 2:
                self.state = 30
                self.identifier()
                pass

            elif la_ == 3:
                self.state = 31
                self.match(SkylineParser.LEFT_PAREN)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(SkylineParser.RIGHT_PAREN)
                pass

            elif la_ == 4:
                self.state = 35
                self.match(SkylineParser.MINUS)
                self.state = 36
                self.expr(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(SkylineParser.PROD)
                        self.state = 41
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(SkylineParser.PLUS)
                        self.state = 44
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        self.match(SkylineParser.PROD)
                        self.state = 47
                        self.num()
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        self.match(SkylineParser.PLUS)
                        self.state = 50
                        self.num()
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 52
                        self.match(SkylineParser.MINUS)
                        self.state = 53
                        self.num()
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_building(self):
            return self.getTypedRuleContext(SkylineParser.Single_buildingContext,0)


        def multiple_buildings(self):
            return self.getTypedRuleContext(SkylineParser.Multiple_buildingsContext,0)


        def random_buildings(self):
            return self.getTypedRuleContext(SkylineParser.Random_buildingsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = SkylineParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constructor)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.single_building()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.multiple_buildings()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.random_buildings()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_buildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SkylineParser.LEFT_PAREN, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def RIGHT_PAREN(self):
            return self.getToken(SkylineParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_single_building

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_building" ):
                return visitor.visitSingle_building(self)
            else:
                return visitor.visitChildren(self)




    def single_building(self):

        localctx = SkylineParser.Single_buildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_single_building)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(SkylineParser.LEFT_PAREN)
            self.state = 65
            self.num()
            self.state = 66
            self.match(SkylineParser.SEP)
            self.state = 67
            self.num()
            self.state = 68
            self.match(SkylineParser.SEP)
            self.state = 69
            self.num()
            self.state = 70
            self.match(SkylineParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multiple_buildingsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE(self):
            return self.getToken(SkylineParser.LEFT_SQUARE, 0)

        def single_building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.Single_buildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.Single_buildingContext,i)


        def RIGHT_SQUARE(self):
            return self.getToken(SkylineParser.RIGHT_SQUARE, 0)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_multiple_buildings

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_buildings" ):
                return visitor.visitMultiple_buildings(self)
            else:
                return visitor.visitChildren(self)




    def multiple_buildings(self):

        localctx = SkylineParser.Multiple_buildingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiple_buildings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(SkylineParser.LEFT_SQUARE)
            self.state = 73
            self.single_building()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.SEP:
                self.state = 74
                self.match(SkylineParser.SEP)
                self.state = 75
                self.single_building()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(SkylineParser.RIGHT_SQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Random_buildingsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SkylineParser.LEFT_PAREN, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def RIGHT_PAREN(self):
            return self.getToken(SkylineParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_random_buildings

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom_buildings" ):
                return visitor.visitRandom_buildings(self)
            else:
                return visitor.visitChildren(self)




    def random_buildings(self):

        localctx = SkylineParser.Random_buildingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_random_buildings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SkylineParser.LEFT_PAREN)
            self.state = 84
            self.num()
            self.state = 85
            self.match(SkylineParser.SEP)
            self.state = 86
            self.num()
            self.state = 87
            self.match(SkylineParser.SEP)
            self.state = 88
            self.num()
            self.state = 89
            self.match(SkylineParser.SEP)
            self.state = 90
            self.num()
            self.state = 91
            self.match(SkylineParser.SEP)
            self.state = 92
            self.num()
            self.state = 93
            self.match(SkylineParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_ID(self):
            return self.getToken(SkylineParser.VALID_ID, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = SkylineParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SkylineParser.VALID_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALID_NUM(self):
            return self.getToken(SkylineParser.VALID_NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = SkylineParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(SkylineParser.VALID_NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




