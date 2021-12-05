import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: class main {} """
#         input = """class main {}"""
#         expect = str(Program([ClassDecl(Id("main"),[],None)]))
#         self.assertTrue(TestAST.test(input,expect,300))

#     def test_class_with_one_decl_program(self):
#         """More complex program"""
#         input = """class main {
#             int a;
#         }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))],None)]))
#                      # Program([ClassDecl(Id(main), [AttributeDecl(Instance, VarDecl(Id(a), IntType))])])
#         self.assertTrue(TestAST.test(input,expect,301))

#     def test_class_with_two_decl_program(self):
#         """More complex program"""
#         input = """class main {
#             int a;
#             int b;
#         }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))],None)]))
#         self.assertTrue(TestAST.test(input,expect,302))

#     def test303(self):
#         input = """class main {

#             static final int numOfShape = 0;
#             final int immuAttribute = 0;
#             float length,width;
#             static int getNumOfShape() {
#             return numOfShape;
#             }
#                         }
#             class Rectangle extends Shape {
#             float getArea(){
#             return this.length*this.width;
#             }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Static(),ConstDecl(Id("numOfShape"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),ConstDecl(Id("immuAttribute"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Static(),Id("getNumOfShape"),[],IntType(),Block([],[Return(Id("numOfShape"))]))],None),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape"))]))
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test304(self):
#         input = """class main {

#                final int My1stCons = 1 + 5,My2ndCons = 2;
# static int x,y = 0;


#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),AttributeDecl(Static(),VarDecl(Id("x"),IntType())),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0)))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test305(self):
#         input = """class main {
#                                float getArea(){
#                 a[3+x.foo(2)] := a[b[2]] +3;
#                 return this.length*this.width;
#                 }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Assign(ArrayCell(Id("a"),BinaryOp("+",IntLiteral(3),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 305))

#     def test306(self):
#         input = """class main {
#                             float getArea(){
#                 x.b[2] := x.m()[3];
#                 a[3+x.foo(2)] := a[b[2]] +3;
#                 return this.length*this.width;
#                 }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Assign(ArrayCell(FieldAccess(Id("x"),Id("b")),IntLiteral(2)),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))),Assign(ArrayCell(Id("a"),BinaryOp("+",IntLiteral(3),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 306))

#     def test307(self):
#         input = """class main {
#                  float getArea(){
#                 x.b[2] := x.m()[3];
#                 #start of declaration part
#                 {
# float r,s;
# int[5] a,b;
# #list of statements
# r:=2.0;
# s:=r*r*this.myPI;
# a[0]:= s;
# }
#                 return this.length*this.width;
#                 }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Assign(ArrayCell(FieldAccess(Id("x"),Id("b")),IntLiteral(2)),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))),Block([VarDecl(Id("r"),FloatType()),VarDecl(Id("s"),FloatType()),VarDecl(Id("a"),ArrayType(5,IntType())),VarDecl(Id("b"),ArrayType(5,IntType()))],[Assign(Id("r"),FloatLiteral(2.0)),Assign(Id("s"),BinaryOp("*",BinaryOp("*",Id("r"),Id("r")),FieldAccess(SelfLiteral(),Id("myPI")))),Assign(ArrayCell(Id("a"),IntLiteral(0)),Id("s"))]),Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 307))

#     def test308(self):
#         input = """class main {
#                            int x(){

# #                 for i := 1 to 100 do {
# # io.writeIntLn(i);
# # Intarray[i] := i + 1;
# # }
# # for x := 5 downto 2 do
# io.writeIntLn(x);
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("x")])]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 308))

#     def test309(self):
#         input = """class main {
#                int x(){
# for i := 1 to 100 do {
# io.writeIntLn(i);
# Intarray[i] := i + 1;
# }
# for x := 5 downto 2 do
# io.writeIntLn(x);

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("i")]),Assign(ArrayCell(Id("Intarray"),Id("i")),BinaryOp("+",Id("i"),IntLiteral(1)))])),For(Id("x"),IntLiteral(5),IntLiteral(2),False,CallStmt(Id("io"),Id("writeIntLn"),[Id("x")]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 309))

#     def test310(self):
#         input = """class main {
#                int x(){

# Shape.getNumOfShape();
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[CallStmt(Id("Shape"),Id("getNumOfShape"),[])]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 310))

#     def test311(self):
#         input = """class hello {
#                           float length,width;
#                 int[3] a = {1,2,3};
#                 static int get() {
#                 return num;
#           }
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),MethodDecl(Static(),Id("get"),[],IntType(),Block([],[Return(Id("num"))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 311))

#     def test312(self):
#         input = """class main {

#           static final int numOfShape = 0;
# final int immuAttribute = 0;
# float length,width;
# static int getNumOfShape() {
# return numOfShape;
# }
#                 }
#                 class goobye {
#                 float getArea(){
# return this.length*this.width;
# }
#           }
#           class goobye {

#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Static(),ConstDecl(Id("numOfShape"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),ConstDecl(Id("immuAttribute"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Static(),Id("getNumOfShape"),[],IntType(),Block([],[Return(Id("numOfShape"))]))],None),ClassDecl(Id("goobye"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 312))

#     def test313(self):
#         input = """class main {
#                int x(){


#                }
#                final int My1stCons = 1 + 5,My2ndCons = 2;
# static int x,y = 0;
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[])),AttributeDecl(Instance(),ConstDecl(Id("My1stCons"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(5)))),AttributeDecl(Instance(),ConstDecl(Id("My2ndCons"),IntType(),IntLiteral(2))),AttributeDecl(Static(),VarDecl(Id("x"),IntType())),AttributeDecl(Static(),VarDecl(Id("y"),IntType(),IntLiteral(0)))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 313))

#     def test314(self):
#         input = """class hello {
#           a(){{if block then {}}}
#           }

#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Block([],[If(Id("block"),Block([],[]))])]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 314))

#     def test315(self):
#         input = """
#           class hello {
#           final static asdasdjwioj genshin = lumia;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Static(),ConstDecl(Id("genshin"),ClassType(Id("asdasdjwioj")),Id("lumia")))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 315))

#     def test316(self):
#         input = """class hello {
#           int note(){
#             return this.v;
#           }
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("note"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("v")))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 316))

#     def test317(self):
#         input = """class hello {
#             int a(){s:= a; b:=c; }
#           }
#           class goobye {
#           main(){int a =0; b:= a.s[1];}
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],IntType(),Block([],[Assign(Id("s"),Id("a")),Assign(Id("b"),Id("c"))]))],None),ClassDecl(Id("goobye"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("a"),IntType(),IntLiteral(0))],[Assign(Id("b"),ArrayCell(FieldAccess(Id("a"),Id("s")),IntLiteral(1)))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 317))

#     def test318(self):
#         input = """class hello {
#           a a(){
#           for i:=1 to end do a:=0;
#           }
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],ClassType(Id("a")),Block([],[For(Id("i"),IntLiteral(1),Id("end"),True,Assign(Id("a"),IntLiteral(0)))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 318))

#     def test319(self):
#         input = """class hello {
#           float a(){return 0;}
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],FloatType(),Block([],[Return(IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 319))

#     def test320(self):
#         input = """class hello {
#           }
#           class goobye {
#           a bb(){continue;xxx.xxx[2] := aaa.aaa(a)[aaa];}
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[],None),ClassDecl(Id("goobye"),[MethodDecl(Instance(),Id("bb"),[],ClassType(Id("a")),Block([],[Continue(),Assign(ArrayCell(FieldAccess(Id("xxx"),Id("xxx")),IntLiteral(2)),ArrayCell(CallExpr(Id("aaa"),Id("aaa"),[Id("a")]),Id("aaa")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 320))

#     def test321(self):
#         input = """class hello {
#           int a = a + b + c - a * a / w % r \ v ^ "" ;
#           }
#           class goobye {
#           a a = aaaaaaaaa ,a,w,e,qasdas ,dasdas ,ffdfsdf;
#           asdwq qw ,asdasdasd,asdasda;
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("-",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),BinaryOp("\\",BinaryOp("%",BinaryOp("/",BinaryOp("*",Id("a"),Id("a")),Id("w")),Id("r")),BinaryOp("^",Id("v"),StringLiteral("\"\""))))))],None),ClassDecl(Id("goobye"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),Id("aaaaaaaaa"))),AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("w"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("e"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("qasdas"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("dasdas"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("ffdfsdf"),ClassType(Id("a")))),AttributeDecl(Instance(),VarDecl(Id("qw"),ClassType(Id("asdwq")))),AttributeDecl(Instance(),VarDecl(Id("asdasdasd"),ClassType(Id("asdwq")))),AttributeDecl(Instance(),VarDecl(Id("asdasda"),ClassType(Id("asdwq"))))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 321))

#     def test322(self):
#         input = """class hello {
#           a(){
#           a a = 0;
#           }
#           #helllo world ;
#           #shold i do some thing;
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("a"),ClassType(Id("a")),IntLiteral(0))],[]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 322))

#     def test323(self):
#         input = """class hello {
#           a(a a; b b;a a){
#           a a = new a();

#           }
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),ClassType(Id("a"))),VarDecl(Id("b"),ClassType(Id("b"))),VarDecl(Id("a"),ClassType(Id("a")))],None,Block([VarDecl(Id("a"),ClassType(Id("a")),NewExpr(Id("a"),[]))],[]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 323))

#     def test324(self):
#         input = """class hello {
#           a(){boolean a;
#           boolean[100] a = a;
#           a := true;
#           }

#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("a"),BoolType()),VarDecl(Id("a"),ArrayType(100,BoolType()),Id("a"))],[Assign(Id("a"),BooleanLiteral(True))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 324))

#     def test325(self):
#         input = """class hello {
#           a(){a a = new a() + new b();}
#           }
#           class goobye {
#           }"""
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("a"),ClassType(Id("a")),BinaryOp("+",NewExpr(Id("a"),[]),NewExpr(Id("b"),[])))],[]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 325))

#     def test326(self):
#         input = """
#           class hello {
#           a a(){a := "r  ,as'damsd ladaslfasmfmakmc asdalmqwr3 923jimwef ";}
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],ClassType(Id("a")),Block([],[Assign(Id("a"),StringLiteral("\"r  ,as'damsd ladaslfasmfmakmc asdalmqwr3 923jimwef \""))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 326))
# #
#     def test327(self):
#         input = """
#           class hello {
#           float asd = asd , asd ,asd ,asd =das, asd ,da;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("asd"),FloatType(),Id("asd"))),AttributeDecl(Instance(),VarDecl(Id("asd"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("asd"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("asd"),FloatType(),Id("das"))),AttributeDecl(Instance(),VarDecl(Id("asd"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("da"),FloatType()))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 327))

#     def test328(self):
#         input = """
#           class hello {
#           string a = asd ,a213, wwe;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),Id("asd"))),AttributeDecl(Instance(),VarDecl(Id("a213"),StringType())),AttributeDecl(Instance(),VarDecl(Id("wwe"),StringType()))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 328))

#     def test329(self):
#         input = """
#           class hello {
#           int a = 213,asd= asd,a = "";
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(213))),AttributeDecl(Instance(),VarDecl(Id("asd"),IntType(),Id("asd"))),AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),StringLiteral("\"\"")))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 329))

#     def test330(self):
#         input = """
#           class hello {
#           float[12] a = asdas ;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(12,FloatType()),Id("asdas")))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 330))

#     def test331(self):
#         input = """
#           class hello {
#           int fun(i v;tr a){if a == 0 then b :=k;}
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("fun"),[VarDecl(Id("v"),ClassType(Id("i"))),VarDecl(Id("a"),ClassType(Id("tr")))],IntType(),Block([],[If(BinaryOp("==",Id("a"),IntLiteral(0)),Assign(Id("b"),Id("k")))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 331))

#     def test332(self):
#         input = """
#           class hello {
#           static int a;
#           foo(){return a;}
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Return(Id("a"))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 332))

#     def test333(self):
#         input = """
#           class hello {
#           a(int d){int[4] b;
#           for i := 0 to z do
#           this.delete(g);
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("d"),IntType())],None,Block([VarDecl(Id("b"),ArrayType(4,IntType()))],[For(Id("i"),IntLiteral(0),Id("z"),True,CallStmt(SelfLiteral(),Id("delete"),[Id("g")]))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 333))

#     def test334(self):
#         input = """
#           class hello {
#           a(int a; int b ; int c){
#           this.visit(a);
#           this.visit(b);
#           if a == b then return c; else this.kill(c);
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],None,Block([],[CallStmt(SelfLiteral(),Id("visit"),[Id("a")]),CallStmt(SelfLiteral(),Id("visit"),[Id("b")]),If(BinaryOp("==",Id("a"),Id("b")),Return(Id("c")),CallStmt(SelfLiteral(),Id("kill"),[Id("c")]))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 334))

#     def test335(self):
#         input = """
#           class hello {
#           final static idk adki;
#           foo(){lololo lololo = asd ;
#           if thi then return "";
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Static(),ConstDecl(Id("adki"),ClassType(Id("idk")),None)),MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("lololo"),ClassType(Id("lololo")),Id("asd"))],[If(Id("thi"),Return(StringLiteral("\"\"")))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 335))


# ###############################################################################################




#     def test336(self):
#         input = """
#           class hello {
#           a(){a[asd[asdasa[asdasda]- asdas] - asdas] := 2;}
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(ArrayCell(Id("a"),BinaryOp("-",ArrayCell(Id("asd"),BinaryOp("-",ArrayCell(Id("asdasa"),Id("asdasda")),Id("asdas"))),Id("asdas"))),IntLiteral(2))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 336))

#     def test337(self):
#         input = """
#           class hello {
#           a a = a[asd + 23 ];
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),ArrayCell(Id("a"),BinaryOp("+",Id("asd"),IntLiteral(23)))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 337))

#     def test338(self):
#         input = """
#           class hello {
#           int buongnuqua(){int khocdi = 00; str sad;
#           tram cam = khoc + sad;
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("buongnuqua"),[],IntType(),Block([VarDecl(Id("khocdi"),IntType(),IntLiteral(0)),VarDecl(Id("sad"),ClassType(Id("str"))),VarDecl(Id("cam"),ClassType(Id("tram")),BinaryOp("+",Id("khoc"),Id("sad")))],[]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 338))

#     def test339(self):
#         input = """
#           class hello {
#           int zalo, facbook, nikola;
#           a(){
#           if notthing then statement := 0;
#           }
#           aloalo aloalo;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("zalo"),IntType())),AttributeDecl(Instance(),VarDecl(Id("facbook"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nikola"),IntType())),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(Id("notthing"),Assign(Id("statement"),IntLiteral(0)))])),AttributeDecl(Instance(),VarDecl(Id("aloalo"),ClassType(Id("aloalo"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 339))

#     def test340(self):
#         input = """
#           class hello {
#           lam trinh(){a.while();}
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("trinh"),[],ClassType(Id("lam")),Block([],[CallStmt(Id("a"),Id("while"),[])]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 340))

#     def test341(self):
#         input = """
#           class hello {
#           int fun(a a ; b b; c c){
#           final f f;
#           a a ;
#           a:= a + a;
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("fun"),[VarDecl(Id("a"),ClassType(Id("a"))),VarDecl(Id("b"),ClassType(Id("b"))),VarDecl(Id("c"),ClassType(Id("c")))],IntType(),Block([ConstDecl(Id("f"),ClassType(Id("f")),None),VarDecl(Id("a"),ClassType(Id("a")))],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("a")))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 341))

#     def test342(self):
#         input = """
#           class hello {
#           string a(){
#           a[2] := 0;
#           }
#           }

#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 342))

#     def test343(self):
#         input = """
#           class hello {
#             string sting(){
#           a[2] := 0;
#           }

#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("sting"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 343))

#     def test344(self):
#         input = """
#           class hello {
#             string a(){
#           a := 0;
#           }

#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],StringType(),Block([],[Assign(Id("a"),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 344))

#     def test345(self):
#         input = """
#           class hello {
#             string strin(){
#           a[897] := 0;

#           }

#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("strin"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(897)),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 345))

#     def test346(self):
#         input = """
#           class hello {
#           a(){
#           for baukhiquyen := 0 to mattroi do {}
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[For(Id("baukhiquyen"),IntLiteral(0),Id("mattroi"),True,Block([],[]))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 346))

#     def test347(self):
#         input = """
#           class hello {
#           a(){
#           {}{}{}{}
#           {}{}{}{}{}{}
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[])]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 347))

#     def test348(self):
#         input = """
#           class hello {
#           int main () {
#           a := 6;
#           b:= 8;
#           if b >= a then return a;
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),IntLiteral(6)),Assign(Id("b"),IntLiteral(8)),If(BinaryOp(">=",Id("b"),Id("a")),Return(Id("a")))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 348))

#     def test349(self):
#         input = """
#           class hello {
#           a(){}
#           b(){}
#           c c ;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),AttributeDecl(Instance(),VarDecl(Id("c"),ClassType(Id("c"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 349))

#     def test350(self):
#         input = """
#           class hello {
#           a a = a[a] + (a + this);
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),BinaryOp("+",ArrayCell(Id("a"),Id("a")),BinaryOp("+",Id("a"),SelfLiteral()))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 350))






# ######################################################





#     def test351(self):
#         input = """
#           class hello {
#           a a = a + a - a ;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),BinaryOp("-",BinaryOp("+",Id("a"),Id("a")),Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 351))

#     def test352(self):
#         input = """
#           class hello {
#           a a = - a;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("-",Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 352))

#     def test353(self):
#         input = """
#           class hello {
#           a a = + a;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("+",Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 353))

#     def test354(self):
#         input = """
#           class hello {
#           /* asdasdkjdnlqw masd amdw */
#           no(){pls stop;
#           continue; break; return turn;
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("stop"),ClassType(Id("pls")))],[Continue(),Break(),Return(Id("turn"))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 354))

#     def test355(self):
#         input = """
#           class hello {
#           aaasd asdasd ,asdasda ;

#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("asdasd"),ClassType(Id("aaasd")))),AttributeDecl(Instance(),VarDecl(Id("asdasda"),ClassType(Id("aaasd"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 355))

#     def test356(self):
#         input = """
#           class hello {
#           a a = 12312,asdasd = 1232,sadasd;

#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),IntLiteral(12312))),AttributeDecl(Instance(),VarDecl(Id("asdasd"),ClassType(Id("a")),IntLiteral(1232))),AttributeDecl(Instance(),VarDecl(Id("sadasd"),ClassType(Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 356))

#     def test357(self):
#         input = """
#           class hello {
#           a a = !!!!!!!!!!!!!!!!!a;
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a"))))))))))))))))))))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 357))

#     def test358(self):
#         input = """
#           class hello {
#           a(){
#           if thisworld then {} if iff then {}
#           }
#           }
#           class goobye {
#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(Id("thisworld"),Block([],[])),If(Id("iff"),Block([],[]))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 358))

#     def test359(self):
#         input = """class main {

#             int x(){

#                 for i := 1 to 100 do {
# io.writeIntLn(i);
# Intarray[i] := i + 1;
# }
# for x := 5 downto 2 do
# io.writeIntLn(x);
#                }

#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("i")]),Assign(ArrayCell(Id("Intarray"),Id("i")),BinaryOp("+",Id("i"),IntLiteral(1)))])),For(Id("x"),IntLiteral(5),IntLiteral(2),False,CallStmt(Id("io"),Id("writeIntLn"),[Id("x")]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 359))

#     def test360(self):
#         input = """class main {
#                int x(){
#                 a := a + b;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 360))

#     def test361(self):
#         input = """class main {
#                int x(){
#                 a := a * b;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("*",Id("a"),Id("b")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 361))

#     def test362(self):
#         input = """class main {
#                int x(){
# a := a * b;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("*",Id("a"),Id("b")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 362))

#     def test363(self):
#         input = """class main {
#                int x(){

# a := a + b + c + d;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("d")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 363))

#     def test364(self):
#         input = """class main {
#                int x(){
# a := a + b + c * d;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 364))

#     def test365(self):
#         input = """class main {
#                int x(){

# a := a * b * c + d;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 365))

#     def test366(self):
#         input = """class main {
#                int x(){

# if a  then b :=a;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 366))

#     def test367(self):
#         input = """class main {
#                int x(){

# if a  then b :=a;else c:=c;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),Assign(Id("c"),Id("c")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 367))

#     def test368(self):
#         input = """class main {
#                int x(){

# if a  then b :=a; else if a then c:=c;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 368))

#     def test369(self):
#         input = """class main {
#                int x(){

# if a  then b :=a; else if a then c:=c ;else c := qweqw;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 369))

#     def test370(self):
#         input = """class main {
#                            int x(){

#                 for i := 1 to 100 do {
# io.writeIntLn(i);
# Intarray[i] := i + 1;
# }
# for x := 5 downto 2 do
# io.writeIntLn(x);
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("i")]),Assign(ArrayCell(Id("Intarray"),Id("i")),BinaryOp("+",Id("i"),IntLiteral(1)))])),For(Id("x"),IntLiteral(5),IntLiteral(2),False,CallStmt(Id("io"),Id("writeIntLn"),[Id("x")]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 370))

#     def test371(self):
#         input = """class main {
#                            int x(){

#                 for i := 1 to 100 do {
#                 {
#                 }{ }{ }{ }{ }{ }{
#                 }
# }
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 371))

#     def test372(self):
#         input = """class main {
#                            int x(){

#                 for i := 1 to 100 do {
#                 {
#                 }{ }{ }{
# if a  then b :=a; else if a then c:=c ;else c := qweqw; }{ }{ }{
#                 }
# }
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 372))

#     def test373(self):
#         input = """class main {
#                            int x(){

#                 for i := 1 to 100 do {
#                 {a := a + b + c * d;
#                 }{ }{ }{
# if a  then b :=a; else if a then c:=c ;else c := qweqw; }{ }{ }{
#                 }
# }
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))))]),Block([],[]),Block([],[]),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 373))

#     def test374(self):
#         input = """
#           class hello {
#             string sting(){
#           a[2] := 0;for i:=1 to end do a:=0;
#           }

#           }
#           class goobye {

#           }
#           """
#         expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("sting"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0)),For(Id("i"),IntLiteral(1),Id("end"),True,Assign(Id("a"),IntLiteral(0)))]))],None),ClassDecl(Id("goobye"),[],None)]))
#         self.assertTrue(TestAST.test(input, expect, 374))

#     def test375(self):
#         input = """class main {
#                int x(){
# a:=9;b:=c;a:=21123+qweqwe+203123;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),IntLiteral(9)),Assign(Id("b"),Id("c")),Assign(Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(21123),Id("qweqwe")),IntLiteral(203123)))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 375))





# #########################################################################






#     def test376(self):
#         input = """class main {
#                int x(){
# break;break;break;break;break;break;break;break;break;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Break(),Break(),Break(),Break(),Break(),Break(),Break(),Break(),Break()]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 376))

#     def test377(self):
#         input = """class main {
#                int x(){

# continue;continue;continue;continue;continue;continue;continue;continue;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Continue(),Continue(),Continue(),Continue(),Continue(),Continue(),Continue(),Continue()]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 377))

#     def test378(self):
#         input = """class main {
#                int x(){
# return 0;
# return 0; return 0; return 0; return 0; return 0; return 0;
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 378))

#     def test379(self):
#         input = """class main {
#                int x(){
# a.a.a.a.a.a.a.a.a.a.a.a := b.b.b.b.b.bb.d.b.b.b.b.b.b.b.b.l;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("b"),Id("b")),Id("b")),Id("b")),Id("b")),Id("bb")),Id("d")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("l")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 379))

#     def test380(self):
#         input = """class main {
#                int x(){
# a[2] := a.sdasd[3];

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(FieldAccess(Id("a"),Id("sdasd")),IntLiteral(3)))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 380))

#     def test381(self):
#         input = """class main {
#                int x(){
# {}{}{}{}{}{{}}
# {{}}{}{}{{}}{}{}
# {}{{}}{{}}{}{}{}
# {}{}{{}}{}{}{}{}
#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[Block([],[])]),Block([],[Block([],[])]),Block([],[]),Block([],[]),Block([],[Block([],[])]),Block([],[]),Block([],[]),Block([],[]),Block([],[Block([],[])]),Block([],[Block([],[])]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[Block([],[])]),Block([],[]),Block([],[]),Block([],[]),Block([],[])]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 381))

#     def test382(self):
#         input = """class main {
#                int x(){


#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 382))

#     def test383(self):
#         input = """class main {
#                int x(){
# if a == b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("==",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 383))

#     def test384(self):
#         input = """class main {
#                int x(){
# if a > b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp(">",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 384))

#     def test385(self):
#         input = """class main {
#                int x(){
# if a >= b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp(">=",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 385))

#     def test386(self):
#         input = """class main {
#                int x(){
# if a < b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("<",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 386))

#     def test387(self):
#         input = """class main {
#                int x(){
# if a <= b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("<=",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 387))

#     def test388(self):
#         input = """class main {
#                int x(){
# if a && b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("&&",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 388))

#     def test389(self):
#         input = """class main {
#                int x(){
# if a || b then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("||",Id("a"),Id("b")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 389))

#     def test390(self):
#         input = """class main {
#                int x(){
# if !a then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(UnaryOp("!",Id("a")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 390))

#     def test391(self):
#         input = """class main {
#                int x(){
# if !!!!!!!!!a then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a")))))))))),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 391))

#     def test392(self):
#         input = """class main {
#                int x(){
# if !!!!!!!!!a && !!!!!!aWDADASD then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("&&",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a")))))))))),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("aWDADASD")))))))),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 392))

#     def test393(self):
#         input = """class main {
#                int x(){
# if !!!!!!!!!a && !!!!!!aWDADASD || asdasdasd then c :=a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(BinaryOp("||",BinaryOp("&&",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a")))))))))),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("aWDADASD")))))))),Id("asdasdasd")),Assign(Id("c"),Id("a")))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 393))

#     def test394(self):
#         input = """class main {
#                int x(){
# if a then c :=a + a + a+ a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("c"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("a")),Id("a")),Id("a"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 394))

#     def test395(self):
#         input = """class main {
#                int x(){
# if a then c :=a * a - a- a;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("c"),BinaryOp("-",BinaryOp("-",BinaryOp("*",Id("a"),Id("a")),Id("a")),Id("a"))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 395))

#     def test396(self):
#         input = """class main {
#                int x(){
# if a then c := !!!!!!!ASDASDASD ;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("c"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("ASDASDASD"))))))))))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 396))

#     def test397(self):
#         input = """class main {
#                int x(){
# if a then c := new sup() ;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("c"),NewExpr(Id("sup"),[])))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 397))

#     def test398(self):
#         input = """class main {
#                int x(){
# if a then c := this ;

#                }
#            }"""
#         expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("c"),SelfLiteral()))]))],None)]))
#         self.assertTrue(TestAST.test(input, expect, 398))

    def test399(self):
        input = """
            class BkoolClass{
                static float d;
                float bb;
                void static main(){
                    int d;
                    d := 5;
                    io.writeInt(d);
                }
            }
        """
        expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(d),Static,[param(Id(o),StringType)],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType)],[Break]))])])"""
        self.assertTrue(TestAST.test(input, expect, 399))















