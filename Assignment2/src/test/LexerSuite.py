import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lexer1(self):
        self.assertTrue(TestLexer.test("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",101))

    def test_lexer2(self):
        self.assertTrue(TestLexer.test("-45.0E124459 -382.98989428 -3. -0.E99","-,45.0E124459,-,382.98989428,-,3.,-,0.E99,<EOF>",102))

    def test_lexer3(self):
        self.assertTrue(TestLexer.test("0.11e849 0.33e-12 0.E+0 0.E-00 10e+425 -0.E+991299","0.11e849,0.33e-12,0.E+0,0.E-00,10e+425,-,0.E+991299,<EOF>",103))
    
    def test_lexer4(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",104))

    def test_lexer5(self):
        self.assertTrue(TestLexer.test("xawffVVVawaar","xawffVVVawaar,<EOF>",105))

    def test_lexer6(self):
        self.assertTrue(TestLexer.test("uwqbuewqeANFWKNKF0_j12JKJNKJN1JFNdsnmKEFjdnfvjn","uwqbuewqeANFWKNKF0_j12JKJNKJN1JFNdsnmKEFjdnfvjn,<EOF>",106))

    def test_lexer7(self):
        self.assertTrue(TestLexer.test("uv 8 a9Aziw ko9jjjj axxzdwq bn0x0x009","uv,8,a9Aziw,ko9jjjj,axxzdwq,bn0x0x009,<EOF>",107))

    def test_lexer8(self):
        self.assertTrue(TestLexer.test("ajdjdjjjdj 9akk 12ksAVU 100jfnd [nNnNnNkNn12","ajdjdjjjdj,9,akk,12,ksAVU,100,jfnd,[,nNnNnNkNn12,<EOF>",108))

    def test_lexer9(self):
        self.assertTrue(TestLexer.test("hvbwe + - wn 0 9 ","hvbwe,+,-,wn,0,9,<EOF>",109))

    def test_lexer10(self):
        self.assertTrue(TestLexer.test("a88jdjij + a2x - 40 > 12","a88jdjij,+,a2x,-,40,>,12,<EOF>",110))

    def test_lexer11(self):
        self.assertTrue(TestLexer.test("as<.>iooi" ,"as,<,.,>,iooi,<EOF>",111))

    def test_lexer12(self):
        self.assertTrue(TestLexer.test("[;]12kkkasijiasdijANXNMXMM\t","[,;,],12,kkkasijiasdijANXNMXMM,<EOF>",112))

    def test_lexer13(self):
        self.assertTrue(TestLexer.test(":a:sxassa:,irejgioj0990hiju.",":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>",113))

    def test_lexer14(self):
        self.assertTrue(TestLexer.test("class a extends B {} new","class,a,extends,B,{,},new,<EOF>",114))
    
    def test_lexer15(self):
        self.assertTrue(TestLexer.test("""12.000e3""","""12.000e3,<EOF>""", 115))
    
    def test_lexer16(self):
        self.assertTrue(TestLexer.test(""" "Hello" """,""""Hello",<EOF>""",116))
    
    def test_lexer17(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,""""This is a string containing tab \\t",<EOF>""",117))
    
    def test_lexer18(self):
         self.assertTrue(TestLexer.test(""" "Hellooo" """,""""Hellooo",<EOF>""",118))

    def test_lexer19(self):
        input = """ "hjhk\n" """
        expect = """Unclosed String: "hjhk"""
        self.assertTrue(TestLexer.test(input,expect,119))
    
    def test_lexer20(self):
         self.assertTrue(TestLexer.test(""" "wet a** pu**y" """,""""wet a** pu**y",<EOF>""",120))
    
    def test_lexer21(self):
         self.assertTrue(TestLexer.test("","<EOF>",121))
    
    def test_lexer22(self):
        input = """ "
                 " """
        expect = """Unclosed String: \""""
        self.assertTrue(TestLexer.test(input,expect,122))

    def test_lexer23(self):
         self.assertTrue(TestLexer.test("+ - * /","+,-,*,/,<EOF>",123))
    
    def test_lexer24(self):
         self.assertTrue(TestLexer.test("downto static final","downto,static,final,<EOF>",124))
    
    def test_lexer25(self):
        self.assertTrue(TestLexer.test(""" 10E+9.23 aAKK -45e10 + 2-- 0.e34 +00 ;  ; } ""","""10E+9,.,23,aAKK,-,45e10,+,2,-,-,0.e34,+,00,;,;,},<EOF>""",125))
    
    def test_lexer26(self):
        self.assertTrue(TestLexer.test(""" csjkjjk \" sdiwkopslssal ""","""csjkjjk,Unclosed String: " sdiwkopslssal """,126))

    def test_lexer27(self):
         self.assertTrue(TestLexer.test(""" ksdcm akak % == lap al 10.94 ! @ ksmdk ""","""ksdcm,akak,%,==,lap,al,10.94,!,Error Token @""",127))
    
    def test_lexer28(self):
         self.assertTrue(TestLexer.test("!== != && * % $ ... ","!=,=,!=,&&,*,%,Error Token $",128))
    
    def test_lexer29(self):
        self.assertTrue(TestLexer.test(""" 12+3>9-3x \"**asndabc+\\^ def\" ""","""12,+,3,>,9,-,3,x,Illegal Escape In String: "**asndabc+\^""",129))
    
    def test_lexer30(self):
        self.assertTrue(TestLexer.test("""  \"\\!LScna\" ""","""Illegal Escape In String: "\!""",130))
    
    def test_lexer31(self):
        self.assertTrue(TestLexer.test("!a%5&&b||c+*", "!,a,%,5,&&,b,||,c,+,*,<EOF>", 131))

    def test_lexer32(self):
        self.assertTrue(TestLexer.test("a==b==01234!=43210<3>4", "a,==,b,==,01234,!=,43210,<,3,>,4,<EOF>", 132))

    def test_lexer33(self):
        self.assertTrue(TestLexer.test("*and<=>mod<\\<=", "*,and,<=,>,mod,<,\\,<=,<EOF>", 133))

    def test_lexer34(self):
        self.assertTrue(TestLexer.test("/*this is a cmt*/", "<EOF>", 134))

    def test_lexer35(self):
        self.assertTrue(TestLexer.test("#hjhjhuhu/*youare live */", "<EOF>", 135))

    def test_lexer36(self):
        self.assertTrue(TestLexer.test("#hello my friend \n asda", "asda,<EOF>", 136))

    def test_lexer37(self):
        self.assertTrue(TestLexer.test("/*hello my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 137))

    def test_lexer38(self):
        self.assertTrue(TestLexer.test("asf aso Dowoad ", "asf,aso,Dowoad,<EOF>", 138))

    def test_lexer39(self):
        self.assertTrue(TestLexer.test("tuoitre chuwa trai su doi", "tuoitre,chuwa,trai,su,doi,<EOF>", 139))

    def test_lexer40(self):
        self.assertTrue(TestLexer.test("imposter lol ", "imposter,lol,<EOF>", 140))

    def test_lexer41(self):
        self.assertTrue(TestLexer.test("01 10 001 100", "01,10,001,100,<EOF>", 141))

    def test_lexer42(self):
        self.assertTrue(TestLexer.test("01. 10.3e+9 0.3e5","01.,10.3e+9,0.3e5,<EOF>", 142))

    def test_lexer43(self):
        self.assertTrue(TestLexer.test("5.e5 6. 5.e-8","5.e5,6.,5.e-8,<EOF>", 143))

    def test_lexer44(self):
        self.assertTrue(TestLexer.test("anD then false", "anD,then,false,<EOF>", 144))

    def test_lexer45(self):
        self.assertTrue(TestLexer.test("sTRIng False", "sTRIng,False,<EOF>", 145))

    def test_lexer46(self):
        self.assertTrue(TestLexer.test(""" ",dls\\F12" """, """Illegal Escape In String: ",dls\\F""", 146))

    def test_lexer147(self):
        input = "a88jdjij + a2x - 40 > 12"
        expect = "a88jdjij,+,a2x,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_lexer148(self):
        input = "as<.>iooi"
        expect = "as,<,.,>,iooi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_lexer149(self):
        input = "[;]12kkkasijiasdijANXNMXMM\t"
        expect = "[,;,],12,kkkasijiasdijANXNMXMM,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_lexer150(self):
        input = ":a:sxassa:,irejgioj0990hiju."
        expect = ":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_lexer151(self):
        input = "class a extends B {}"
        expect = "class,a,extends,B,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_lexer152(self):
        input = "class ABC }"
        expect = "class,ABC,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_lexer153(self):
        input = "class ABC { }"
        expect = "class,ABC,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_lexer154(self):
        input = "class ABC extends { }"
        expect = "class,ABC,extends,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_lexer155(self):
        input = "class { }"
        expect = "class,{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_lexer156(self):
        input = "int main(){}"
        expect = "int,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_lexer157(self):
        input = "a.x() this.x.a().a"
        expect = "a,.,x,(,),this,.,x,.,a,(,),.,a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_lexer158(self):
        input = "static int getNumOfShape() {return numOfShape;}"
        expect = "static,int,getNumOfShape,(,),{,return,numOfShape,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_lexer159(self):
        input = """s := new A();
                    a.a().a := 12;
                    this.a := 12;
                    io.writeFloatLn(s.getArea());"""
        expect = "s,:=,new,A,(,),;,a,.,a,(,),.,a,:=,12,;,this,.,a,:=,12,;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_lexer160(self):
        input = "ox128 + 1258.e8"
        expect = "ox128,+,1258.e8,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_lexer161(self):
        input = "a := true, b = false"
        expect = "a,:=,true,,,b,=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_lexer162(self):
        input = """ "abc\\e def" """
        expect = """Illegal Escape In String: "abc\\e"""
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_lexer163(self):
        input = """ "ab'c\\n def" """
        expect = """"ab'c\\n def",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_lexer164(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 164))

    def test_lexer165(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 165))

    def test_lexer166(self):
        input = """a= "He said: " Im Super'Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,"He said: ",Im,Super,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_lexer167(self):
        input = """a= "He said: " Hello " \n ";"""
        expect = """a,=,"He said: ",Hello,Unclosed String: " """
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_lexer168(self):
        input = """a = "Hello \n world !";"""
        expect = """a,=,Unclosed String: "Hello """
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_lexer169(self):
        input = "{1,2,3}"
        expect = "{,1,,,2,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_lexer170(self):
        input = "{2.3, 4.2, 102e3}"
        expect = "{,2.3,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_lexer171(self):
        input = "a[4] = {1, 2,  3, 4}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_lexer172(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_lexer173(self):
        input = "int[5] a;"
        expect = "int,[,5,],a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_lexer174(self):
        input = "a[3 + x.foo(2)] := a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_lexer175(self):
        input = "s:=r*r*this.myPI;"
        expect = "s,:=,r,*,r,*,this,.,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_lexer176(self):
        input = "1/2"
        expect = "1,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_lexer177(self):
        input = """ " \\h " """
        expect = """Illegal Escape In String: " \h"""
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_lexer178(self):
        input = """ " \\naaa\\t" """
        expect = """" \\naaa\\t",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_lexer179(self):
        input = "{}"
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_lexer180(self):
        input = """{"}"""
        expect = """{,Unclosed String: "}"""
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_lexer181(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_lexer182(self):
        input = "#{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_lexer183(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_lexer184(self):
        input = "# this is a line comment /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_lexer185(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_lexer186(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """"\\"aadadddldld\\"",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_lexer187(self):
        input = """ "dshf"""
        expect = """Unclosed String: "dshf"""
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_lexer188(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: "}*/*"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_lexer189(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: "-a)"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_lexer190(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: "abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_lexer191(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: "\\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_lexer192(self):
        input = """ "        " """
        expect = """"        ",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_lexer193(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_lexer194(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_lexer195(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_lexer196(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_lexer197(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,"1",,,"2",,,"3",},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
    
    def test_lexer198(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))
    
    def test_lexer199(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
    
    def test_lexer200(self):
        input = "\"abc\\e def\""
        expect = """Illegal Escape In String: "abc\e"""
        self.assertTrue(TestLexer.test(input, expect, 200))
    