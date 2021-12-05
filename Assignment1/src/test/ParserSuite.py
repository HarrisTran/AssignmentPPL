import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
#     def test_101(self):
#         input = """
#         class Geometry {
#             float length,width;
#             float getArea() {}
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#             float getArea(){
#             return this.length*this.width;
#             }
#         }
#         class Triangle extends Geometry {
#             float getArea(){
#             return this.length*this.width / 2;
#             }
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             (b.coo().d.ass()).o();
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,201))

#     def test_102(self):
#         input = """
#         class Geometry {
#             float length,width;
#             float getArea() {}
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#             float getArea(){
#             x.b[2] := x.m()[3];
#             }
#         }
#         class Triangle extends Geometry {
#             float getArea(){
#             return this.length*this.width / 2;
#             }
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             io.writeFloatLn(s.getArea());
#             s := new Triangle(3,4);
#             io.writeFloatLn(s.getArea());
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,202))

#     def test_103(self):
#         input = """
#         class Geometry {
#             float length,width;
#             float getArea() {}
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#             float getArea(){
#             return this.length*this.width;
#             }
#         }
#         class Triangle extends Geometry {
#             float getArea(){
#             return this.length*a.foo()[2];
#             }
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             io.writeFloatLn(s.getArea());
#             s := new Triangle(3,4);
#             io.writeFloatLn(s.getArea());
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,203))

#     def test_104(self):
#         input = """
#         class Geometry {
#             float length,width;
#             float getArea() {}
#             Geometry(float length,width){
#                 this.length := 1+2/3.0;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,204))

#     def test_105(self):
#         input = """
#         class Geometry {
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,205))

#     def test_106(self):
#         input = """
#         class 1Geometry {
#         }
#         """
#         expect = "Error on line 2 col 14: 1"
#         self.assertTrue(TestParser.test(input,expect,206))

#     def test_107(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#         };
#         """
#         expect = "Error on line 7 col 9: ;"
#         self.assertTrue(TestParser.test(input,expect,207))

#     def test_108(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             ID(string name = "empty"){
#                 this.name:=name;
#             }
#         }
#         """
#         expect = "Error on line 7 col 27: ="
#         self.assertTrue(TestParser.test(input,expect,208))

#     def test_109(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             ID(string name){
#                 this.name=name;
#             }
#         }
#         """
#         expect = "Error on line 8 col 25: ="
#         self.assertTrue(TestParser.test(input,expect,209))

#     def test_110(self):
#         input = """
#         class ID {
#             static int total=0;
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             ID(string name){
#                 this.name:=name;
#                 ID.total := ID.total +1;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,210))

#     def test_111(self):
#         input = """
#         void main(){
#             int[5] a,b;
#         }
#         """
#         expect = "Error on line 2 col 8: void"
#         self.assertTrue(TestParser.test(input,expect,211))

#     def test_112(self):
#         input = """
#         class Example1 {
#             void main(){
#             float a;
#             a:=3.0;
#             io.writeFloatLn(a);
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,212))

#     def test_113(self):
#         input = """
#         class Example1 {
#             void main(){
#             float a=3.0;
#             io.writeFloatLn(a);
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,213))

#     def test_114(self):
#         input = """
#         class Example1 {
#             void main(){
#             string a
#             a := "Hello world \\n";
#             }
#         }
#         """
#         expect = "Error on line 5 col 12: a"
#         self.assertTrue(TestParser.test(input,expect,214))

#     def test_115(self):
#         input = """
#         class Example1 extends {
#             void main(){
#             string a = "Hello world \\n";
#             }
#         }
#         """
#         expect = "Error on line 2 col 31: {"
#         self.assertTrue(TestParser.test(input,expect,215))

#     def test_116(self):
#         input = """
#         class Example1 /* extends */ {
#             void main(){
#             string a;
#             a := "Hello world \\n";
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,216))

#     def test_117(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             void not(){
#                string b;
#                b:="I dont know";
#                this.name:=this.name^b;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,217))

#     def test_118(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             void if(){
#                string b;
#                b:="I dont know";
#                this.name:=this.name^b;
#                return;
#             }
#         }
#         """
#         expect = "Error on line 7 col 17: if"
#         self.assertTrue(TestParser.test(input,expect,218))

#     def test_119(self):
#         input = """
#         class ID {
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             void not(){
#                string b;
#                b:="I dont know";
#                return this.name^b;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,219))

#     def test_120(self):
#         input = """
#         class ID {
#             static int[4] total={0,0,0,0};
#             string name;
#             ID(){
#                 this.name:=nil;
#             }
#             ID(string name){
#                 this.name:=name;
#                 ID.total[0] := ID.total[0] +1;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,220))

#     def test_121(self):
#         input = """
#         class Geometry {
#             static float length,width;
#             final float getArea() {}
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#             float getArea(){
#             return this.length*this.width;
#             }
#         }
#         class Triangle extends Geometry {
#             float getArea(){
#             return this.length*this.width / 2;
#             }
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             (b.coo().d.ass()).o();
#             }
#         }
#         """
#         expect = "Error on line 4 col 31: ("
#         self.assertTrue(TestParser.test(input,expect,221))

#     def test_122(self):
#         input = """
#         class Geometry {
#             final static float length,width;
#             static float getArea() {}
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#             float getArea(){
#             return this.length*this.width;
#             }
#         }
#         class Triangle extends Geometry {
#             float getArea(){
#             return this.length*this.width / 2;
#             }
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             (b.coo().d.ass()).o();
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,222))

#     def test_123(self):
#         input = """
#         class Geometry {
#             static float length,width;
#             final float getArea;
#             Geometry(float length,width){
#                 this.length := "length";
#                 this.width := width;
#             }
#         }
#         class Rectangle extends Geometry {
#         }
#         class Example2 {
#             void main(){
#             s := new Rectangle(3,4);
#             (b.coo().d.ass()).o();
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,223))

#     def test_124(self):
#         input = """
#         class printer {
#             static void print(int a,b,c; float b){
#                 io.print(a+b+c+b);
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,224))

#     def test_125(self):
#         input = """class Example2 extends ABC {
# 	float length,width;
# 	float getArea() {}
# 	Geometry(float length,width; int alo; string re){

# 	}
# 	void main(){

# 	}
# }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,225))

#     def test_126(self):
#         input = """class a extends ABD{
#             static int a=4,b=7;
#             float[0] area(int a,b; boolean r){

#             }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,226))

#     def test_127(self):
#         input = """class a extends ABD{
#             static int a=4,b=7;
#             float[4] area(int a,b; boolean r){  #comment
#                 int z,y;
#                 float[10] array;
#             }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,227))

#     def test_128(self):
#         input = """class Example2 extends ABC {
#                     float length,width;
#                     float getArea() {}
#                     Geometry(float length,width){
#                         this.length := length;
#                         this.width := width;
#                     }
#                     void main(){
#                         a[x+b.foo(2)+3] := a[b[2]+6]+3;
#                         t.y[0] := r.len()[10];
#                     }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,228))

#     def test_129(self):
#         input = """class Example2 extends ABC {
#                     static final string[4] t=5;
#                     final float[4] c={1,2,3,5,2.5e-1,"khoa"};
#                     int[2] a;
#                     Geometry(float length,width){
#                         s := new A();
#                         a.a().a := 12;
#                         this.a := 12;
#                         io.writeFloatLn(s.getArea());
#                         s := new Triangle(3,4);
#                         io.writeFloatLn(s.getArea());
#                         (a.b[t0]).yt := 1;
#                         return a*this.abc(n-1);
#                     }
#                     void main(){
#                         a := 5+6-97*74;
#                     }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,229))

#     def test_130(self):
#         input = """class Example2 extends ABC {
#                     static int a=555;
#                     Geometry(float length,width){
#                         return a*this.abc(n-1);
#                     }
#                     void main(){
#                         a.x[k] := 5;
#                         for x:=8 to 100 do{
#                             i := i+1;
#                             a[f.x()] := "nam";
#                         }
#                     }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,230))

#     def test_131(self):
#         input = """class Example2 extends ABC {
#                     static int a=555;
#                     Geometry(float length,width){
#                         return a*this.abc(n-1);
#                     }
#                     void main(){
#                         system.out.println("hello");
#                         system.out(println,22,5.2,"tr",true);
#                     }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,231))

#     def test_132(self):
#         input = """class z extends a {
#                     static int a=555;
#                     static string b="aaaaaaa";
#                     # aa /* cccc */a
#                     void main(){
#                         system.out(s.x(cc));
#                     }
#         }"""
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,232))
#     def test_133(self):
#         input = """class z {
#                     }
#         """
#         expect="successful"
#         self.assertTrue(TestParser.test(input,expect,233))
#     def test_134(self):
#         input = """class ABC { }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,234))
#     def test_135(self):
#         input = """class ABC extends { }"""
#         expect = "Error on line 1 col 18: {"
#         self.assertTrue(TestParser.test(input,expect,235))
#     def test_136(self):
#         input = """class { }"""
#         expect = "Error on line 1 col 6: {"
#         self.assertTrue(TestParser.test(input,expect,236))
#     def test_137(self):
#         input = """class ABC }"""
#         expect = "Error on line 1 col 10: }"
#         self.assertTrue(TestParser.test(input,expect,237))

#     def test_138(self):
#         input = """class Geometry {
#                         static final int numOfGeometry = 0;
#                         final int immuAttribute = 0;
#                         float length,width;
#                         static int getNumOfGeometry() {
#                             return numOfGeometry;
#                         }
#                     }
#                     class Rectangle extends Geometry {
#                         float getArea(){
#                             return this.length*this.width;
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,238))

#     def test_139(self):
#         input = """class Geometry {
#                         static final int numOfGeometry = 0;
#                         final int immuAttribute = 0;
#                         float length,width;
#                         static int getNumOfGeometry() {
#                             return numOfGeometry;
#                         }
#                     }
#                     class Rectangle extends Geometry {
#                         float getArea(){
#                             return this.length*this.width;
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,239))

#     def test_140(self):
#         input = """class Example2 extends ABC {
#                         int length,width;
#                         float getArea() {}
#                         Geometry(float length,width){
#                             this.length := length;
#                             this.width := width;
#                         }
#                         void main(){
#                             s := new A();
#                             a.a().a := 12;
#                             this.a := 12;
#                             io.writeFloatLn(s.getArea());
#                             s := new Triangle(3,4);
#                             io.writeFloatLn(s.getArea());
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,240))

#     def test_141(self):
#         input = """class Example1 {
#                         int factorial(int n){
#                             if n == 0 then
#                                 return 1;
#                             else
#                                 return n * this.factorial(n - 1);
#                         }
#                         void main(){
#                             int x;
#                             l[3] := 2*value*2/2-c;
#                             x := io.readInt();
#                             io.writeIntLn(this.factorial(x));
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,241))

#     def test_142(self):
#         input = """class Geometry {
#                         float length,width;
#                         float getArea() {}
#                         Geometry(float length,width){
#                             this.length := length;
#                             this.width := width;
#                         }
#                     }
#                     class Example2 {
#                         void main(){
#                             Exam[2] x = {1.2, 3.4, 5};
#                             Geometry s = new Rectangle(3,4);
#                             io.writeFloatLn(s.getArea());
#                             s := 2+3-95*74;
#                             io.writeFloatLn(s.getArea());
#                             y := {1.2 ,2, 3};
#                             return a;
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,242))

#     def test_143(self):
#         input = """class QuotientRemainder {
#                         static void main(string[2] args) {
#                             int dividend = 25, divisor = 4;

#                             int quotient = dividend / divisor;
#                             int remainder = dividend % divisor;

#                             System.out.println("Quotient = " + quotient);
#                             System.out.println("Remainder = " + remainder);
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,243))
#     def test_144(self):
#         input = """class QuotientRemainder {
#                         static final int numOfGeometry = 0;
#                         final int b=0;
#                         float a,b=5,r=3.14;
#                         final static string hcmut= "hello";
#                         static int get(){
#                             a := b[3+m.foo(1)];
#                             return 22;
#                         }
#                     }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,244))
#     def test_145(self):
#         input = """class foo {
#             Ab[5] n = this.Geometry(x.foo(5)[4]*(!m) + (s >= m || m+-n));
#             H function(A a,b,c; H n){
#                 final int m = h;
#                 int b, h = 40, k, d = {3,true,false,5.e5,5.8e+12};
#                 a := 4;
#                 s[0] := 2 ;
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,245))
#     def test_146(self):
#         input = """class WAP {
#             int b = 2;
#             int[5] a = {1, 2, 3, 4, 5};
#             int c = b*a[0;
#         }"""
#         expect = "Error on line 4 col 25: ;"
#         self.assertTrue(TestParser.test(input,expect,246))
#     def test_147(self):
#         input = """class WAP {
#             static void main(int arg){
#                 int a=5;
#                 a.foo().a.f();
#                 x := (a.b[0]).a;
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,247))

#     def test148(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d) {
#                 int a = 0;
#                 int b = 0;
#                 for a := 5 to 10 do
#                     if a % 2 then
#                         b := b + 2;
#                     else
#                         b := b * 2;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 248))

# #     def test149(self):
# #         input = r"""
# #         class WAP {
# #             WAP(int a, b, c; string d; boolean e) {
# #                 a := 0;
# #                 b := 0;
# #                 for a := 5 to 10 do
# #                     for b := 5 to 10 do
# #                         for b := 5 to 10 do
# #                             for c := 15 downto 10 do
# #                                 break;
# #             }
# #         }
# #         """
# #         expect = r"""successful"""
# #         self.assertTrue(TestParser.test(input, expect, 249))

#     def test150(self):
#         input = r"""
#         class WAP {
#             WAP() {
#                 return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(a,b,c,d) + this.foo(2,3,4);
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 250))

#     def test151(self):
#         input = r"""
#         class WAP {
#             static int a = 0;
#             boolean[10000] a, b;
#             bool a = true;
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 251))

#     def test152(self):
#         input = r"""
#         class WAP {
#             static int a = 0;
#             boolean[10000] a, b;
#             bool a = true;
#             int func(int a, b; float c) {
#                 string e;
#                 final float[1] arr;
#                 float f;
#                 arr[2 + this.foo(2)] = 0;
#                 e := "avc" ^ "jlacsjl";
#                 f = 12E10 - 20.0003;

#             }
#         }
#         """
#         expect = r"""Error on line 10 col 37: ="""
#         self.assertTrue(TestParser.test(input, expect, 252))

#     def test153(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d; boolean e) {
#                 int a = 0;
#                 b := 0;
#                 for a := 5 to 10 do
#                     continue
#             }
#         }
#         """
#         expect = r"""Error on line 8 col 12: }"""
#         self.assertTrue(TestParser.test(input, expect, 253))

#     def test154(self):
#         input = r"""class WAP {
#                 float a = 0, b = 1, c = 2, d = 10 + a;
#             }"""
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 254))

#     def test155(self):
#         input = r"""
#         WAP(int a, b, c; string d; boolean e) {
#                 for a := 5 to 10 do
#                     for b := 15 downto 1 do
#                         for c := 0 downto -10 do
#                             if c == 0 then
#                                 if d == "" then
#                                     if e == false then
#                                         if a == b + c % c then
#                                             c := -1;
#         }
#         """
#         expect = r"""Error on line 2 col 8: WAP"""
#         self.assertTrue(TestParser.test(input, expect, 255))

#     def test156(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d; boolean e) {
#                 for a := 5 to 10 do
#                     for b := 15 downto 1 do
#                         for c := 0 downto -10 do
#                             if c == 0 then
#                                 if d == "" then
#                                     if e == false then
#                                         d := d ^ "abc";
#                                         c = 4;
#             }
#         }
#         """
#         expect = r"""Error on line 11 col 42: ="""
#         self.assertTrue(TestParser.test(input, expect, 256))

#     def test157(self):
#         input = r"""
#         class WAP {
#             static int a = 0;
#             boolean[10000] a, b;
#             bool a = true;
#             string funcint a, b, float c) {
#                 if a == 0 then
#                     b := b + 1;
#                 if b == 0 then
#                     b := b - a;
#                 else
#                     c := d - 5 * 9 % 3;
#                 if d == 0 then
#                     a := 0;
#                 else
#                     c := 12E-8 + 5;
#             }
#         }
#         """
#         expect = r"""Error on line 6 col 27: a"""
#         self.assertTrue(TestParser.test(input, expect, 257))

#     def test158(self):
#         input = r"""
#         class WAP {
#             int func(int a,b; string c,d) {
#                 if a == 0 then
#                     b := b + 1;
#                 if b == 0 then
#                     b := b - a;
#                 else
#                     c := d - 5 * 9 % 3;
#                 if d == 0 then{
#                     a := 0;
#                     d := d * b;
#                     c := c ^ d;
#                     e := e * f;
#                     g := g + h;}
#                 else return 0;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 258))

#     def test159(self):
#         input = r"""
#         class WAP {
#             static final int a = 0;
#             float b = 0;
#             static int funcA(int a; int b) {
#             }
#             static int funcB() {
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 259))

#     def test160(self):
#         input = r"""
#         class WAP {
#             int[2] ;
#         }
#         """
#         expect = r"""Error on line 3 col 19: ;"""
#         self.assertTrue(TestParser.test(input, expect, 260))

#     def test161(self):
#         input = r"""
#         class WAP {
#             static final int[2] b = {1,2,3,4,true,5.e4};
#             foo(boolean a){final int x,y = 0;}
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 261))

#     def test162(self):
#         input = r"""
#         class WAP {
#             int a,b,c=9,d ;
#             static int[6] k,d = {1,2,true,false},c, f = 10.e5;
#             final static int m = 3,n = 9;
#             static int[5] foo(float c,d; boolean g; int c){
#                 A a = new X();
#                 B b = new X(2,3)[x.foo(m)];
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 262))

#     def test163(self):
#         input = r"""
#         class WAP {
#             A a = 9; Boo b = this.a; foo c = new X();
#             static ABC foo(float c,d; boolean g; int c){
#                 A a = new X();
#                 B b = new X(2,3)[x.foo(m)];
#                 A a,b,c;
#                 B c,d,e;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 263))

#     def test164(self):
#         input = r"""
#         class WAP {
#             M m = new Num(a,b,c,a+c,a[x.foo()+2*5/3]);
#             static ABC foo(float c,d; boolean g; int c){
#                 return true;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 264))

#     def test165(self):
#         input = r"""
#         class WAP {
#             int m,n = this.Geometry();
#             BOO k,c = !(a && b || c);
#             A a = -(!a + c*2/5 + b%2 + !(a == b.foo()[5])) ;
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 265))

#     def test166(self):
#         input = r"""
#         class ABC {
#             int c = !((a>=b) && (c<d) != 5 || -(abc && (c>=d)));
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 266))

#     def test167(self):
#         input = r"""
#         class ABC {
#             B b = new X(!a, -b+a, c || a && m)[m+n];
#             static int foo(float m,n; B b){}
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 267))

#     def test168(self):
#         input = r"""
#         class ABCD {
#             B[5] b = this.name;
#             boolean[6] a,b = {1,2,3,4,5.5}, c = new X();
#             static B foo(float m,n; B b,c ; A[6] a){}
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 268))

#     def test169(self):
#         input = r"""
#         class ABCD {
#             string a = a\2 + 7 > 8 + 3 ;
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 269))

#     def test170(self):
#         input = r"""
#         class ABCD {
#             string a = a\2 + 7 > 8*5 + 3 ;
#             A[5] a = x.m()[7] + a*b[x.foo() + !(c*d) - (b||-c && !m);
#         }
#         """
#         expect = r"""Error on line 4 col 68: ;"""
#         self.assertTrue(TestParser.test(input, expect, 270))

#     def test171(self):
#         input = r"""
#         class foo {
#             Ab[5] n = this.Geometry(x.foo(5)[4]*(!m) + (s >= m || m+-n));
#             H[5] function(A a,b,c; H n){
#                 int m = h;
#                 #B b, h = 40, k, d = {3,true,false,5.e5,5.8e+12};
#                 int a;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 271))

#     def test172(self):
#         input = r"""
#         class foo {
#             Ab[5] n = this.Geometry(x.foo(5)[4]*(!m) + (s >= m || m+-n));
#             H[5] function(A a,b,c; H n){
#                 int k = 9;
#                 m := n;
#                 int n;
#             }
#         }
#         """
#         expect = r"""Error on line 7 col 16: int"""
#         self.assertTrue(TestParser.test(input, expect, 272))

#     def test173(self):
#         input = r"""
#         class foo {
#             int function(A a,b,c; H n){
#                 int k = 9, m =10;
#                 m := n;
#                 return x.foo();
#                 int n;
#             }
#         }
#         """
#         expect = r"""Error on line 7 col 16: int"""
#         self.assertTrue(TestParser.test(input, expect, 273))

#     def test174(self):
#         input = r"""
#         class foo {
#         int x,y;
#         static final int a = 10;
#             int function(A a,b,c; H n){
#                 a.a().a := 12;
#                 m := n;
#                 return x.foo();
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 274))

#     def test175(self):
#         input = r"""
#         class foo {
#         int x,y;
#         static final int a = 10;
#             static int function(A a,b,c; H n){
#                 final int a = 9;
#                 {}{}
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 275))

#     def test176(self):
#         input = r"""
#         class foo {
#             foo(){{}{}}
#             int a,b,c;
#         }
#         class foo{static int z,b = true;}
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 276))

#     def test177(self):
#         input = r"""
#         class foo {

#         }
#         class foo{static int z,b = true;}
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 277))

#     def test178(self):
#         input = r"""
#         class foo {
#             int foo(int a,b,c){
#                 for i:=5 to 9 do io.printf(5);
#                 }
#         }
#         class foo{static int z,b = true;}
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 278))

#     def test179(self):
#         input = r"""
#         class foo {
#             int foo(int a,b,c){
#                 for i := 5 to 9 do io.printf(5);
#                 if a == 8 then { a:= b; x.foo();}
#                 }
#         }
#         class foo{static int z,b = true;}
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 279))

#     def test180(self):
#         input = r"""
#         class foo {
#             int a,b = true, c = false, e = {34,56,true,false};
#             final float a,m,d = 9;
#         }
#         class foo{static int z,b = true;}
#         class main{}
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 280))

#     def test181(self):
#         input = r"""
#         class Rectangle extends Geometry {
#             B b = 9;
#             float getArea(){
#                 final int c;
#                 int[5] ab;
#                 a[0]:= 5.3e6 + c.foo(x);
#                 return this.length*this.width*2;
#                 int a = 7;
#             }
#         }
#         """
#         expect = r"""Error on line 9 col 16: int"""
#         self.assertTrue(TestParser.test(input,expect,281))

#     def test182(self):
#         input = r"""
#         class foo{
#             static final int x, y = 7;
#             final int m = 9*a ,k = x.m()[6*a];
#             int main(){ x.b[2] := 8*x.m()[3]; return true;}
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,282))

#     def test183(self):
#         input = r"""
#         class foo {
#             static final int x = 0*0, y, z = 9;
#             final static int[5] b,c;
#             int[5] cam(){
#                 if i == 0 then
#                     if b >= 0 then c:= 9;
#                     else return 2 + x.foo(8);
#                 else if !node then continue;
#                      else if c == 2 then return this.name;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,283))

#     def test184(self):
#         input = r"""
#         class foo {
#             static final int x = 0*0, y, z = 9;
#             final static float[5] hcmut,hcmute;
#             int[5] cam(){
#                 K k,m,n;
#                 A a,b,c;
#                 a := {5,7};
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,284))

#     def test185(self):
#         input = r"""
#         class foo {
#             int[5] cam(){
#                 K k,m,n;
#                 A a,b,c;
#                 a := {5,7};
#             }
#             foo(){{}{}}
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,285))

#     def test186(self):
#         input = r"""
#         class foo {
#             int x.foo() = 9;
#             int[5] cam(){
#             }
#             foo(){{}{}}
#         }
#         """
#         expect = r"""Error on line 3 col 17: ."""
#         self.assertTrue(TestParser.test(input,expect,286))

#     def test187(self):
#         input = r"""
#         class foo {
#             int[5] cam(){
#             }
#             foo(){{}{}}
#             B.boo(a) = 8*j;
#         }
#         """
#         expect = r"""Error on line 6 col 13: ."""
#         self.assertTrue(TestParser.test(input,expect,287))

#     def test188(self):
#         input = r"""
#         class foo {
#             int[5] cam(){
#             }
#             foo(){{}{}}
#             int[5] b[5];
#         }
#         """
#         expect = r"""Error on line 6 col 20: ["""
#         self.assertTrue(TestParser.test(input,expect,288))

#     def test189(self):
#         input = r"""
#         class foo {
#             string s ="huhuhu";
#             int[5] cam(){int a,b[5];}
#             }
#             foo(){{}{}}
#             int[5] b;
#         }
#         """
#         expect = r"""Error on line 4 col 32: ["""
#         self.assertTrue(TestParser.test(input,expect,289))

#     def test190(self):
#         input = r"""
#         class foo {
#             string s ="huhuhu", l = true;
#             int[5] cam(){int a,b;}
#             }
#             foo;
#         }
#         """
#         expect = r"""Error on line 6 col 12: foo"""
#         self.assertTrue(TestParser.test(input,expect,290))

#     def test191(self):
#         input = r"""
#         class foo {
#             int[5] cam.foo(){int a,b;}
#             }
#             foo;
#         }
#         """
#         expect = r"""Error on line 3 col 22: ."""
#         self.assertTrue(TestParser.test(input,expect,291))

#     def test192(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d; boolean e) {
#                 a := 0;
#                 b := 0;
#                 for a := 5 to 10 do
#                     for b := 5 to 10 do
#                         break;
#             }
#         }"""
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,292))

#     def test193(self):
#         input = r"""
#         class WAP {
#             WAP() {
#                 return a[b[2]]*a[b]+this.length+this.width / 2 * x.foo(a,b,c,d) + this.foo(2,3,4);
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,293))

#     def test194(self):
#         input = r"""
#         class WAP {
#             void func(int a,b,c,d) {
#                 if a == b + c then
#                     for d := 0 to 10 do
#                         c := c + 1 / 3 % d;
#                 else
#                     for d := 0 to 10 do
#                         c := c - 1 * 2018E+10;
#             }
#             void func2(string e, f) {
#                 return e ^ f ^ "c" ^ "";
#             }
#             boolean func3(boolean g, h) {
#                 h := false;
#                 return g == true;
#             }
#         }
#         class WAP2 {
#             int width = 0;
#             int length = 0;
#             WAP2() {
#                 WAP pg1 = new WAP();
#                 return this.width * this.length;
#             }
#             static int func() {
#                 return "";
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input,expect,294))

#     def test195(self):
#         input = r"""
#         class WAP {
#             void func(int a,b) {
#                 a.a()[5] := 5;
#                 return a == b % 2;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 295))

#     def test196(self):
#         input = r"""
#         class WAP {
#             static int a = 0;
#             boolean[10000] a, b;
#             bool a = true;
#             string func(int a, b, float c) {
#                 return 0;
#             }
#         }
#         """
#         expect = r"""Error on line 6 col 34: float"""
#         self.assertTrue(TestParser.test(input, expect, 296))

#     def test197(self):
#         input = r"""
#         class WAP {
#             int a = 0;
#             int b = 0;
#             float c = 0;
#             int func(int a, b; float c) {
#                 string e;
#                 final float[1] arr;
#                 arr[2 + this.foo(2)] := 0;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 297))

#     def test198(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d; boolean e) {
#                 a := 0;
#                 b := 0;
#                 for a := 5 to 10 do
#                     for b := 15 downto 1 do
#                         for c := 0 downto -10 do
#                             if c == 0 then
#                                 if d == "" then
#                                     if e == false then
#                                         d := d ^ "abc";
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 298))

#     def test199(self):
#         input = r"""
#         class WAP {
#             WAP(int a, b, c; string d; boolean e) {
#                 for a := 5 to 10 do
#                     if b == 0 then
#                         return a[b[c[2]]] + 3;
#                     else
#                         return a[b + x.foo(a)] + 3;
#             }
#         }
#         """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.test(input, expect, 299))

    def test200(self):
        input = """
            class BKoolClass extends Dang {
                boolean rang;
                static void main(){
                    io.writeInt(3);
                }
            }
            class Dang{
                int a=4;
            }
            
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))

    


