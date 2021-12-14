# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write(")\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\'\n\5\3\5\2")
        buf.write("\2\6\2\4\6\b\2\2\2%\2\n\3\2\2\2\4\21\3\2\2\2\6\32\3\2")
        buf.write("\2\2\b&\3\2\2\2\n\13\7\3\2\2\13\f\7\b\2\2\f\r\7\f\2\2")
        buf.write("\r\16\5\4\3\2\16\17\7\r\2\2\17\20\7\2\2\3\20\3\3\2\2\2")
        buf.write("\21\22\7\4\2\2\22\23\7\5\2\2\23\24\7\b\2\2\24\25\7\n\2")
        buf.write("\2\25\26\7\13\2\2\26\27\7\f\2\2\27\30\5\6\4\2\30\31\7")
        buf.write("\r\2\2\31\5\3\2\2\2\32\33\7\b\2\2\33\34\7\6\2\2\34\35")
        buf.write("\7\b\2\2\35\36\7\n\2\2\36\37\5\b\5\2\37 \7\13\2\2 !\7")
        buf.write("\16\2\2!\7\3\2\2\2\"#\7\t\2\2#$\7\7\2\2$\'\7\t\2\2%\'")
        buf.write("\7\t\2\2&\"\3\2\2\2&%\3\2\2\2\'\t\3\2\2\2\3&")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'static'", "'void'", "'.'", 
                     "'+'", "<INVALID>", "<INVALID>", "'('", "')'", "'{'", 
                     "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INTLIT", "LB", "RB", 
                      "LP", "RP", "SEMI", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_member = 1
    RULE_body = 2
    RULE_exp = 3

    ruleNames =  [ "program", "member", "body", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    INTLIT=7
    LB=8
    RB=9
    LP=10
    RP=11
    SEMI=12
    WS=13
    ERROR_CHAR=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(BKOOLParser.T__0)
            self.state = 9
            self.match(BKOOLParser.ID)
            self.state = 10
            self.match(BKOOLParser.LP)
            self.state = 11
            self.member()
            self.state = 12
            self.match(BKOOLParser.RP)
            self.state = 13
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(BKOOLParser.T__1)
            self.state = 16
            self.match(BKOOLParser.T__2)
            self.state = 17
            self.match(BKOOLParser.ID)
            self.state = 18
            self.match(BKOOLParser.LB)
            self.state = 19
            self.match(BKOOLParser.RB)
            self.state = 20
            self.match(BKOOLParser.LP)
            self.state = 21
            self.body()
            self.state = 22
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(BKOOLParser.ID)
            self.state = 25
            self.match(BKOOLParser.T__3)
            self.state = 26
            self.match(BKOOLParser.ID)
            self.state = 27
            self.match(BKOOLParser.LB)
            self.state = 28
            self.exp()
            self.state = 29
            self.match(BKOOLParser.RB)
            self.state = 30
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.INTLIT)
            else:
                return self.getToken(BKOOLParser.INTLIT, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(BKOOLParser.INTLIT)
                self.state = 33
                self.match(BKOOLParser.T__4)
                self.state = 34
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(BKOOLParser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





