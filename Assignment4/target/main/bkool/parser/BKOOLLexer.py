# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\6\7\67\n\7\r\7\16\78\3\b\6\b<\n\b\r\b\16\b=\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16K\n\16\r\16")
        buf.write("\16\16L\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2")
        buf.write("\5\4\2C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2T\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\3\37\3\2\2\2\5%\3\2\2\2\7,\3\2\2\2\t\61\3\2\2\2\13")
        buf.write("\63\3\2\2\2\r\66\3\2\2\2\17;\3\2\2\2\21?\3\2\2\2\23A\3")
        buf.write("\2\2\2\25C\3\2\2\2\27E\3\2\2\2\31G\3\2\2\2\33J\3\2\2\2")
        buf.write("\35P\3\2\2\2\37 \7e\2\2 !\7n\2\2!\"\7c\2\2\"#\7u\2\2#")
        buf.write("$\7u\2\2$\4\3\2\2\2%&\7u\2\2&\'\7v\2\2\'(\7c\2\2()\7v")
        buf.write("\2\2)*\7k\2\2*+\7e\2\2+\6\3\2\2\2,-\7x\2\2-.\7q\2\2./")
        buf.write("\7k\2\2/\60\7f\2\2\60\b\3\2\2\2\61\62\7\60\2\2\62\n\3")
        buf.write("\2\2\2\63\64\7-\2\2\64\f\3\2\2\2\65\67\t\2\2\2\66\65\3")
        buf.write("\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\16\3\2\2\2:")
        buf.write("<\t\3\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\20")
        buf.write("\3\2\2\2?@\7*\2\2@\22\3\2\2\2AB\7+\2\2B\24\3\2\2\2CD\7")
        buf.write("}\2\2D\26\3\2\2\2EF\7\177\2\2F\30\3\2\2\2GH\7=\2\2H\32")
        buf.write("\3\2\2\2IK\t\4\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2")
        buf.write("\2\2MN\3\2\2\2NO\b\16\2\2O\34\3\2\2\2PQ\13\2\2\2Q\36\3")
        buf.write("\2\2\2\6\28=L\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ID = 6
    INTLIT = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    WS = 13
    ERROR_CHAR = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'static'", "'void'", "'.'", "'+'", "'('", "')'", 
            "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "ID", "INTLIT", 
                  "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


