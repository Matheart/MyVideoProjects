from manimlib.imports import *
from manim_sandbox.utils.imports import *
# 5min = 300s
class HText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Regular',
        'size' : 0.5,
    }

class Quote(Scene):
    def construct(self):
        quote =HText("幾何是世界上最美麗的語言").scale(2).to_edge(UP)
        quote.set_color([RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE])
        author = HText("———— 鲁迅").next_to(quote,DOWN).align_to(quote,RIGHT).shift(RIGHT)
        im = ImageMobject(r"C:\Users\Artanis\Downloads\luxun.jpg").scale(1.5)

        sentence1 = HText("她看似简单，却又千变万化，让人沉迷其中")
        sentence2 = HText("下面让我们一起来欣赏几条著名的几何定理").next_to(sentence1,DOWN)
        sentence3 = HText("再度重温那些熠熠发光的几何瑰宝").next_to(sentence2,DOWN)

        sentence1[3:5].set_color(BLUE)
        sentence1[8].set_color(RED)
        sentence1[9].set_color(ORANGE)
        sentence1[10].set_color(YELLOW)
        sentence1[11].set_color(GREEN)
        sentence2[15:19].set_color(RED)
        sentence3[6:10].set_color(YELLOW)
        sentence3[11:15].set_color(ORANGE)

        self.play(FadeIn(quote))
        self.wait(1.5)
        self.play(FadeInFrom(author,DOWN))
        self.wait(0.5)
        self.play(FadeIn(im))
        self.wait(1.5)
        self.play(FadeOut(im))
        self.play(Write(sentence1))
        self.wait(1.5)
        self.play(Write(sentence2))
        self.wait(2)
        self.play(Write(sentence3))
        self.wait(2)
        self.play(FadeOut(VGroup(quote,author,sentence1,sentence2,sentence3)))
# 展示名言
# Transform 接下来就让我们来欣赏几个有名的几何定理吧！

class Morley(Scene): # 莫利定理V
    def construct(self):
        name = HText("莫利定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        A_cor = np.array([-0.16366,2.65642,0])
        B_cor = np.array([-4.18019,-1.90557,0])
        C_cor = np.array([6.84173,-1.7828,0])
        D_cor = np.array([0.25857,-0.57909,0])
        E_cor = np.array([0.78603,0.58575,0])
        F_cor = np.array([-0.48648,0.46013,0])

        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        D = Dot(D_cor)
        E = Dot(E_cor)
        F = Dot(F_cor)
        Tri = MyTriangle(A_cor, B_cor, C_cor)

        AF = Line(A_cor, F_cor).set_color(PURPLE)
        AE = Line(A_cor, E_cor).set_color(PURPLE)
        BF = Line(B_cor, F_cor).set_color("#FF1493")
        BD = Line(B_cor, D_cor).set_color("#FF1493")
        CD = Line(C_cor, D_cor).set_color(ORANGE)
        CE = Line(C_cor, E_cor).set_color(ORANGE)

        DE = Line(D_cor, E_cor).set_color(RED)
        EF = Line(E_cor, F_cor).set_color(RED)
        FD = Line(F_cor, D_cor).set_color(RED)

        A1 = Arc(start_angle = 228.0/180.0*PI, angle = PI*33.0/180.0, radius = 1).move_arc_center_to(A_cor).set_color(PURPLE)
        A2 = Arc(start_angle = 228.0/180.0*PI + PI*33.0/180.0, angle = PI*33.0/180.0, radius = 1.1).move_arc_center_to(A_cor).set_color(PURPLE)
        A3 = Arc(start_angle = 228.0/180.0*PI + 2*PI*33.0/180.0, angle = PI*33.0/180.0, radius = 1.2).move_arc_center_to(A_cor).set_color(PURPLE)   

        B1 = Arc(angle = PI*16.0/180.0, radius = 1).move_arc_center_to(B_cor).set_color("#FF1493")
        B2 = Arc(start_angle = PI*16.0/180.0, angle = PI*16.0/180.0, radius = 1.1).move_arc_center_to(B_cor).set_color("#FF1493")
        B3 = Arc(start_angle = 2*PI*16.0/180.0, angle = PI*16.0/180.0, radius = 1.2).move_arc_center_to(B_cor).set_color("#FF1493")      

        C1 = Arc(start_angle = PI - PI*11.0/180.0,angle = PI*11.0/180.0, radius = 1).move_arc_center_to(C_cor).set_color(ORANGE)
        C2 = Arc(start_angle = PI - 2*PI*11.0/180.0, angle = PI*11.0/180.0, radius = 1.1).move_arc_center_to(C_cor).set_color(ORANGE)
        C3 = Arc(start_angle = PI - 3*PI*11.0/180.0, angle = PI*11.0/180.0, radius = 1.2).move_arc_center_to(C_cor).set_color(ORANGE)   

        sentence1 = HText("将三角形的三个内角三等分").to_edge(DOWN)     
        sentence2 = HText("靠近某边的两条三分角线相交得到的交点").to_edge(DOWN)  
        sentence3 = HText("可以构成一个正三角形").to_edge(DOWN)  

        sentence3[-4:].set_color(RED)

        self.play(Write(name),Write(Tri))
        self.wait(1.5)
        self.play(Write(sentence1))
        self.wait(1)
        self.play(Write(VGroup(AF,AE,BF,BD,CD,CE)))
        self.wait(1)
        self.play(Write(VGroup(A1,A2,A3,B1,B2,B3,C1,C2,C3)))
        self.wait(0.5)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        self.play(Write(VGroup(D,E,F)))
        self.wait(1)
        self.play(ReplacementTransform(sentence2,sentence3))
        self.wait(1)
        self.play(Write(VGroup(DE,EF,FD)))
        self.wait(1)
        self.play(FadeOut(VGroup(name,Tri,sentence3,D,E,F,DE,EF,FD,A1,A2,A3,B1,B2,B3,C1,C2,C3,AF,AE,BF,BD,CD,CE)))

class Pascal(Scene): # 帕斯卡定理
    def construct(self):
        name = HText("帕斯卡定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        self.play(Write(name))

        A_cor = np.array([0.7*-5.11065,0.7*0.80133+0.4,0])
        B_cor = np.array([0.7*-0.44563,0.7*3.14788+0.4,0])
        C_cor = np.array([0.7*1.91699,0.7*2.79849+0.4,0])
        F_cor = np.array([0.7*3.50996,0.7*-0.94572+0.4,0])
        D_cor = np.array([0.7*-2.82738,0.7*-3.75749+0.4,0])
        E_cor = np.array([0.7*1.08207,0.7*-3.16638+0.4,0])
        P_cor = np.array([0.7*-1.95283,0.7*-1.22191+0.4,0])
        Q_cor = np.array([0.7*-0.24229,0.7*-0.18529+0.4,0])
        R_cor = np.array([0.7*1.66077,0.7*0.96798+0.4,0])

        A = Dot(A_cor).set_color(BLUE)
        B = Dot(B_cor).set_color(BLUE)
        C = Dot(C_cor).set_color(BLUE)
        D = Dot(D_cor).set_color(BLUE)
        E = Dot(E_cor).set_color(BLUE)
        F = Dot(F_cor).set_color(BLUE)
        P = Dot(P_cor).set_color("#FFD700")
        Q = Dot(Q_cor).set_color("#FFD700")
        R = Dot(R_cor).set_color("#FFD700")

        A_label = TexMobject("A_1").next_to(A_cor,UP+0.3*LEFT)
        B_label = TexMobject("A_2").next_to(B_cor,UP)
        C_label = TexMobject("A_3").next_to(C_cor,UP)
        D_label = TexMobject("B_1").next_to(D_cor,LEFT+0.2*DOWN)
        E_label = TexMobject("B_2").next_to(E_cor,DOWN)
        F_label = TexMobject("B_3").next_to(F_cor,DOWN+0.1*RIGHT)
        P_label = TexMobject("P").next_to(P_cor,LEFT)
        Q_label = TexMobject("Q").next_to(Q_cor,DOWN)
        R_label = TexMobject("R").next_to(R_cor,RIGHT)

        AE = Line(A_cor, E_cor).set_color(RED)
        AF = Line(A_cor, F_cor).set_color(RED)
        BD = Line(B_cor, D_cor).set_color(ORANGE)
        BF = Line(B_cor, F_cor).set_color(ORANGE)
        CD = Line(C_cor, D_cor).set_color(GREEN)
        CE = Line(C_cor, E_cor).set_color(GREEN)
        PR = Line(P_cor, R_cor).set_color("#FFD700")

        func = ParametricFunction(lambda t: np.array([0.7*(-0.96105+4.69853*np.cos(t)-0.88612*np.sin(t)),0.7*(-0.33879+1.27883*np.cos(t)+3.25567*np.sin(t))+0.4,0]), t_min = -PI, t_max = PI).set_color(PINK)
        
        sentence1 = VGroup(HText("在圆锥曲线上任取六点"),TexMobject("A_1,A_2,A_3,B_1,B_2,B_3")).arrange_submobjects(RIGHT/2).to_edge(DOWN)
        sentence2 = VGroup(HText("设"),TexMobject("A_{1}B_{2}"),HText("和"),TexMobject("A_{2}B_{1}"),HText("交于"),TexMobject("P,A_{2}B_{3}"),HText("和"),TexMobject("A_{3}B_{2}"),HText("交于"),TexMobject("Q,A_{1}B_{3}"),HText("和"),TexMobject("A_{3}B_{1}"),HText("交于"),TexMobject("R")).arrange_submobjects(RIGHT/2).scale(0.9).to_edge(DOWN)
        sentence3 = HText("则P,Q,R共线").to_edge(DOWN)
        sentence3[-2:].set_color("#FFD700")

        self.play(FadeIn(func))
        self.wait(1.5)
        self.play(Write(sentence1))
        self.wait(0.5)
        self.play(Write(VGroup(A,B,C,D,E,F,A_label,B_label,C_label,D_label,E_label,F_label)))
        self.wait(1)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        self.play(Write(VGroup(AE,AF,BD,BF,CD,CE)))
        self.wait(1)
        self.play(Write(VGroup(P,Q,R,P_label,Q_label,R_label)))
        self.wait(0.5)
        self.play(ReplacementTransform(sentence2,sentence3))
        self.wait(1)
        self.play(Write(PR))
        self.wait(1.5)
        self.play(FadeOut(VGroup(sentence3,name,func,A,B,C,D,E,F,A_label,B_label,C_label,D_label,E_label,F_label,
                                 AE,AF,BD,BF,CD,CE,P,Q,R,PR,P_label,Q_label,R_label)))

class Brianchon(Scene): # 布利安桑定理V
    def construct(self):
        name = HText("布利安桑定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        self.play(Write(name))

        A_cor = np.array([0.6329*0.7,3.25077*0.7+0.4,0])
        B_cor = np.array([6.30535*0.7,0.25257*0.7+0.4,0])
        C_cor = np.array([.97401*0.7,-3.63714*0.7+0.4,0])
        D_cor = np.array([-3.69609*0.7,-2.59471*0.7+0.4,0])
        E_cor = np.array([-5.60648*0.7,-0.26338*0.7+0.4,0])
        F_cor = np.array([-4.00487*0.7,2.6*0.7+0.4,0])
        intr_cor = np.array([-1.84905*0.7,-0.10063*0.7+0.4,0])

        func = ParametricFunction(lambda t: np.array([0.7*(-0.49228+4.66989*np.cos(t)+0.06272*np.sin(t)),0.7*(-0.07136-0.095*np.sin(t)+3.08281*np.sin(t))+0.4,0]), t_min = -PI, t_max = PI).set_color(PINK)

        poly = Polygon(A_cor, B_cor, C_cor, D_cor, E_cor, F_cor).set_color(BLUE)
        A = Dot(A_cor).set_color(BLUE)
        B = Dot(B_cor).set_color(BLUE)
        C = Dot(C_cor).set_color(BLUE)
        D = Dot(D_cor).set_color(BLUE)
        E = Dot(E_cor).set_color(BLUE)
        F = Dot(F_cor).set_color(BLUE)
        intr = Dot(intr_cor).set_color("#FFD700")
        AD = Line(A_cor, D_cor).set_color(RED)
        BE = Line(B_cor, E_cor).set_color(ORANGE)
        CF = Line(C_cor, F_cor).set_color(YELLOW)

        sentence1 = HText("对于六条边和圆锥曲线相切的六边形").to_edge(DOWN)
        sentence2 = HText("它的三条对角线共点").to_edge(DOWN)
        sentence1[6:10].set_color(PINK)
        sentence1[-3:].set_color(BLUE)
        sentence2[-2:].set_color("#FFD700")

        self.play(FadeIn(poly),FadeIn(func),Write(sentence1))
        self.play(Write(VGroup(A,B,C,D,E,F)))
        self.wait(1.5)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        self.play(Write(VGroup(AD,BE,CF)))
        self.wait(0.5)
        self.play(Write(intr))
        self.wait(2)
        self.play(FadeOut(VGroup(poly,func,sentence2,A,B,C,D,E,F,AD,BE,CF,intr,name)))

class FiveCircle(Scene): # 五圆定理V
    def construct(self):
        name1 = HText("五圆定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name2 = HText("五连定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name3 = HText("五圆定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name2[1].set_color(RED)

        self.play(Write(name1))

        Acentr_cor = np.array([-0.19907*1.2,2.02821*1.2,0])
        Bcentr_cor = np.array([0.92373*1.2,1.09053*1.2,0])
        Ccentr_cor = np.array([0.31317*1.2,-0.71996*1.2,0])
        Dcentr_cor = np.array([-1.69789*1.2,-0.25283*1.2,0])
        Ecentr_cor = np.array([-1.68105*1.2,1.41655*1.2,0])

        Circ = Circle(radius = 1.48688*1.2, color = RED).move_to(np.array([-0.46154*1.2,0.56253*1.2,0]))
        circ1 = Circle(radius = 0.81683*1.2, color = ORANGE).move_to(Acentr_cor)
        circ2 = Circle(radius = 0.69622*1.2, color = "#0000CD").move_to(Bcentr_cor)
        circ3 = Circle(radius = 1.32293*1.2, color = "#00BFFF").move_to(Ccentr_cor)
        circ4 = Circle(radius = 0.89546*1.2, color = "#00FF00").move_to(Dcentr_cor)
        circ5 = Circle(radius = 0.85229*1.2, color = "#ADFF2F").move_to(Ecentr_cor)
        
        A1_cor = np.array([.53367*1.2,1.66723*1.2,0])
        B1_cor = np.array([1.01649*1.2,.40051*1.2,0])
        C1_cor = np.array([-1.00588*1.2,-0.82113*1.2,0])
        D1_cor = np.array([-1.94775*1.2,.60707*1.2,0])
        E1_cor = np.array([-1.01154*1.2,1.94395*1.2,0])

        A2_cor = np.array([.28674*1.2,1.37154*1.2,0])
        B2_cor = np.array([.43204*1.2,.59761*1.2,0])
        C2_cor = np.array([-0.82623*1.2,-0.04773*1.2,0])
        D2_cor = np.array([-1.43073*1.2,0.60815*1.2,0])
        E2_cor = np.array([-0.83446*1.2,1.51489*1.2,0])

        P_cor = np.array([0.01548*1.2,2.81636*1.2,0])
        Q_cor = np.array([1.61093*1.2,1.20224*1.2,0])
        R_cor = np.array([.90184*1.2,-1.9047*1.2,0])
        S_cor = np.array([-2.37304*1.2,-0.84106*1.2,0])
        T_cor = np.array([-2.47567*1.2,1.72473*1.2,0])

        A1 = Dot(A1_cor).set_color("#FFD700")
        B1 = Dot(B1_cor).set_color("#FFD700")
        C1 = Dot(C1_cor).set_color("#FFD700")
        D1 = Dot(D1_cor).set_color("#FFD700")
        E1 = Dot(E1_cor).set_color("#FFD700")
        A2 = Dot(A2_cor).set_color("#9932CC")
        B2 = Dot(B2_cor).set_color("#9932CC")
        C2 = Dot(C2_cor).set_color("#9932CC")
        D2 = Dot(D2_cor).set_color("#9932CC")
        E2 = Dot(E2_cor).set_color("#9932CC")
        Acentr = Dot(Acentr_cor).set_color(GREEN)
        Bcentr = Dot(Bcentr_cor).set_color(GREEN)
        Ccentr = Dot(Ccentr_cor).set_color(GREEN)
        Dcentr = Dot(Dcentr_cor).set_color(GREEN)
        Ecentr = Dot(Ecentr_cor).set_color(GREEN)
        P = Dot(P_cor).set_color("#FFD700")
        Q = Dot(Q_cor).set_color("#FFD700")
        R = Dot(R_cor).set_color("#FFD700")
        S = Dot(S_cor).set_color("#FFD700")
        T = Dot(T_cor).set_color("#FFD700")

        A2B2 = Line(A2_cor, B2_cor).set_color("#FF1493")
        B2C2 = Line(B2_cor, C2_cor).set_color("#FF1493")
        C2D2 = Line(C2_cor, D2_cor).set_color("#FF1493")
        D2E2 = Line(D2_cor, E2_cor).set_color("#FF1493")
        E2A2 = Line(E2_cor, A2_cor).set_color("#FF1493")

        A2P = Line(A2_cor, P_cor).set_color("#FF1493")
        A2Q = Line(A2_cor, Q_cor).set_color("#FF1493")
        B2Q = Line(B2_cor, Q_cor).set_color("#FF1493")
        B2R = Line(B2_cor, R_cor).set_color("#FF1493")
        C2R = Line(C2_cor, R_cor).set_color("#FF1493")
        C2S = Line(C2_cor, S_cor).set_color("#FF1493")
        D2S = Line(D2_cor, S_cor).set_color("#FF1493")
        D2T = Line(D2_cor, T_cor).set_color("#FF1493")
        E2T = Line(E2_cor, T_cor).set_color("#FF1493")
        E2P = Line(E2_cor, P_cor).set_color("#FF1493")

        sentence1 = HText("五个顺次相交的圆").to_edge(DOWN)
        sentence2 = HText("若其圆心和一个交点位于第六个圆上").to_edge(DOWN)
        sentence3 = HText("那么将另一个交点两两连接并延长和圆相接，可以构成五角星").to_edge(DOWN)
        sentence3[-3:].set_color("#FF1493")

        self.play(FadeIn(VGroup(circ1,circ2,circ3,circ4,circ5)),Write(sentence1))
        self.wait(1)
        self.play(ReplacementTransform(name1,name2))
        path = "D:\\manim-master\\manimlib\\files\\"
        sanlian1 = SVGMobject(path + 'video_icon.svg', color=ORANGE).set_width(circ1.get_width()*0.8).move_to(circ1).shift(0.1*UP)
        sanlian2 = SVGMobject(path + 'good.svg', color="#0000CD").set_width(circ2.get_width()*0.8).move_to(circ2).shift(0.1*UP)
        sanlian3 = SVGMobject(path + 'coin.svg', color="#00BFFF").set_width(circ3.get_width()*0.8).move_to(circ3)
        sanlian4 = SVGMobject(path + 'favo.svg', color="#00FF00").set_width(circ4.get_width()*0.8).move_to(circ4).shift(0.1*UP)
        sanlian5 = SVGMobject(path + 'share.svg', color="#ADFF2F").set_width(circ5.get_width()*0.8).move_to(circ5).shift(0.1*UP)
        self.play(FadeIn(sanlian1),FadeIn(sanlian2),FadeIn(sanlian3),FadeIn(sanlian4),FadeIn(sanlian5))
        self.wait(2)
        self.play(ReplacementTransform(name2,name3))
        self.play(FadeOut(sanlian1),FadeOut(sanlian2),FadeOut(sanlian3),FadeOut(sanlian4),FadeOut(sanlian5))
        
        self.play(Write(VGroup(A1,B1,C1,D1,E1,Acentr,Bcentr,Ccentr,Dcentr,Ecentr)))
        self.wait(1.5)
        self.play(ReplacementTransform(sentence1, sentence2))
        self.wait(1)
        self.play(Write(Circ))
        self.wait(2)
        self.play(Write(VGroup(A2,B2,C2,D2,E2)))
        self.wait(1)
        self.play(ReplacementTransform(sentence2,sentence3))
        self.wait(1)
        self.play(Write(VGroup(A2B2,B2C2,C2D2,D2E2,E2A2)))
        self.wait(0.5)
        self.play(Write(VGroup(A2P,A2Q,B2Q,B2R,C2R,C2S,D2S,D2T,E2T,E2P)))
        self.play(Write(VGroup(P,Q,R,S,T)))
        self.wait(2.5)

        self.play(FadeOut(VGroup(sentence3,circ1,circ2,circ3,circ4,circ5,Circ,
                                 A2,B2,C2,D2,E2,A2B2,B2C2,C2D2,D2E2,E2A2,
                                 A2P,A2Q,B2Q,B2R,C2R,C2S,D2S,D2T,E2T,E2P,
                                 A1,B1,C1,D1,E1,name3,P,Q,R,S,T,Acentr,Bcentr,Ccentr,Dcentr,Ecentr)))

class SevenCircle(Scene): # 七圆定理V
    def construct(self):
        name = HText("七圆定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)

        self.play(Write(name))

        circ = Circle(radius = 3.86875*0.8).shift(0.5*UP)
        circ1 = Circle(radius = 1.21*0.8).move_to(np.array([-0.4786*0.8,2.61597*0.8+0.5,0])).set_color(ORANGE)
        circ2 = Circle(radius = 0.89437*0.8).move_to(np.array([1.623211*0.8,2.51209*0.8+0.5,0])).set_color("#ADFF2F")
        circ3 = Circle(radius = 1.26888*0.8).move_to(np.array([2.54021*0.8,0.55428*0.8+0.5,0])).set_color("#32CD32")
        circ4 = Circle(radius = 1.55629*0.8).move_to(np.array([1.24069*0.8,-1.95396*0.8+0.5,0])).set_color("#00FFFF")
        circ5 = Circle(radius = 1.06378*0.8).move_to(np.array([-1.32672*0.8,-2.47658*0.8+0.5,0])).set_color("#00008B")
        circ6 = Circle(radius = 1.72751*0.8).move_to(np.array([-2.13986*0.8,0.19363*0.8+0.5,0])).set_color(PURPLE)

        A_cor = np.array([-0.64936*0.8,3.81386*0.8+0.5,0])
        B_cor = np.array([2.25239*0.8,3.14546*0.8+0.5,0])
        C_cor = np.array([3.78423*0.8,0.80426*0.8+0.5,0])
        D_cor = np.array([1.98423*0.8,-3.32115*0.8+0.5,0])
        E_cor = np.array([-1.92816*0.8,-3.35401*0.8+0.5,0])
        F_cor = np.array([-3.86639*0.8,0.13514*0.8+0.5,0])

        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        D = Dot(D_cor)
        E = Dot(E_cor)
        F = Dot(F_cor)
        intr = Dot(np.array([0.56542*0.8,0.52274*0.8+0.5,0])).set_color("#FFD700")

        AD = Line(A_cor, D_cor)
        BE = Line(B_cor, E_cor)
        CF = Line(C_cor, F_cor)

        sentence1 = HText("给定一个大圆").to_edge(DOWN)
        sentence2 = HText("里面的六个小圆均内切于大圆,且每相邻两个小圆均外切").to_edge(DOWN)
        sentence3 = HText("则连接相对的内切点所成的三条线段共点").to_edge(DOWN)

        sentence1[4:6].set_color(RED)
        sentence2[11:13].set_color(RED)
        sentence3[-2:].set_color("#FFD700")

        self.play(Write(circ),Write(sentence1))
        self.wait(1)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        self.play(Write(VGroup(circ1,circ2,circ3,circ4,circ5,circ6)))
        self.wait(2)
        self.play(Write(A),Write(B),Write(C),Write(D),Write(E),Write(F))
        self.wait(0.5)
        self.play(ReplacementTransform(sentence2,sentence3))
        self.wait(1)
        self.play(Write(AD),Write(BE),Write(CF))
        self.wait(0.5)
        self.play(Write(intr))
        self.wait(2)
        self.play(FadeOut(VGroup(circ,sentence3,name,circ,circ1,circ2,circ3,circ4,circ5,circ6,AD,BE,CF,intr,A,B,C,D,E,F)))

class VanAubel(Scene): # 凡奥贝尔定理V
    def construct(self):
        name1 = HText("凡奥贝尔定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        A_cor = np.array([-0.3692+1.5,2.3573,0])
        B_cor = np.array([0.99753+1.5,2.02007,0])
        C_cor = np.array([1.6+1.5,0.3,0])
        D_cor = np.array([-1.3+1.5,0.4,0])
        A1_cor = np.array([-0.032+1.5,3.724,0])
        A2_cor = np.array([1.334+1.5,3.387,0])
        B1_cor = np.array([2.8+1.5,2.6,0])
        B2_cor = np.array([3.37+1.5,0.84,0])
        C1_cor = np.array([1.5+1.5,-2.6,0])
        C2_cor = np.array([-1.4+1.5,-2.5,0])
        D1_cor = np.array([-3.3+1.5,1.3,0])
        D2_cor = np.array([-2.4+1.5,3.3,0])
        A_centr_cor = np.array([0.5+1.5,2.9,0])
        B_centr_cor = np.array([2.2+1.5,1.4,0])
        C_centr_cor = np.array([0.1+1.5,-1.1,0])
        D_centr_cor = np.array([-1.8+1.5,1.8,0])
        ints_cor = np.array([0.36+1.5,1.6,0])

        A_centr = Dot(A_centr_cor).set_color(RED)
        B_centr = Dot(B_centr_cor).set_color(RED)
        C_centr = Dot(C_centr_cor).set_color(RED)
        D_centr = Dot(D_centr_cor).set_color(RED)
        ints = Dot(ints_cor).set_color("#FFD700")

        AcCc = Line(A_centr_cor, C_centr_cor).set_color(RED)
        BcDc = Line(D_centr_cor, B_centr_cor).set_color(RED)

        Zhi1 = Line(np.array([0.37+1.5,1.77,0]),np.array([0.535+1.5,1.755,0]),stroke_width=2)
        Zhi2 = Line(np.array([0.535+1.5,1.755,0]),np.array([0.52+1.5,1.59,0]),stroke_width=2)


        AB = Line(A_cor, B_cor)
        BC = Line(B_cor, C_cor)
        CD = Line(C_cor, D_cor)
        DA = Line(D_cor, A_cor)

        AA1 = Line(A_cor, A1_cor).set_color(ORANGE)
        A1A2 = Line(A1_cor, A2_cor).set_color(ORANGE)
        A2B = Line(A2_cor, B_cor).set_color(ORANGE)

        BB1 = Line(B_cor, B1_cor).set_color(GREEN)
        B1B2 = Line(B1_cor, B2_cor).set_color(GREEN)
        B2C = Line(B2_cor, C_cor).set_color(GREEN)

        CC1 = Line(C_cor, C1_cor).set_color(PURPLE)
        C1C2 = Line(C1_cor, C2_cor).set_color(PURPLE)
        C2D = Line(C2_cor, D_cor).set_color(PURPLE)

        DD1 = Line(D_cor, D1_cor).set_color(BLUE)
        D1D2 = Line(D1_cor, D2_cor).set_color(BLUE)
        D2A = Line(D2_cor, A_cor).set_color(BLUE)

        sentence1 = HText("对于任意一个四边形").to_edge(DOWN)
        sentence2 = HText("在其边外侧构造正方形").to_edge(DOWN)
        sentence3 = HText("将相对正方形的中心连起，得到两条线段").to_edge(DOWN)
        sentence4 = HText("线段的长度相等且互相垂直").to_edge(DOWN)

        sentence3[7:9].set_color(RED)
        sentence3[-2:].set_color(RED)
        sentence4[:2].set_color(RED)

        self.play(FadeIn(AB),FadeIn(BC),FadeIn(CD),FadeIn(DA),Write(name1))
        self.play(Write(sentence1))
        self.wait(1.5)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        AB.set_color(ORANGE)
        BC.set_color(GREEN)
        CD.set_color(PURPLE)
        DA.set_color(BLUE)
        self.play(FadeIn(VGroup(AA1,A1A2,A2B,BB1,B1B2,B2C,CC1,C1C2,C2D,DD1,D1D2,D2A)))
        self.wait(1)
        self.play(ReplacementTransform(sentence2,sentence3))
        self.play(Write(A_centr),Write(B_centr),Write(C_centr),Write(D_centr))
        self.wait(1)
        self.play(Write(AcCc),Write(BcDc))
        self.wait(1)
        self.play(ReplacementTransform(sentence3,sentence4))
        self.wait(0.5)
        self.play(Write(ints))
        self.play(Write(Zhi1),Write(Zhi2))
        self.wait(1.5)
        self.play(FadeOut(VGroup(AA1,A1A2,A2B,BB1,B1B2,B2C,CC1,C1C2,C2D,DD1,D1D2,D2A,sentence4,Zhi1,Zhi2,A_centr,B_centr,C_centr,D_centr,
                                 ints,AcCc,BcDc,AB,BC,CD,DA,name1)))

class NinePointCircle(Scene): # 九点圆V
    def construct(self):
        name = HText("九点圆").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        A_cor = np.array([0.97*1.5, (0.84+1+1.0/3)*1.5,0])
        B_cor = np.array([-3.02*1.5,(-1.58+1+1.0/3)*1.5,0])
        C_cor = np.array([0.33*1.5,(-1.68+1+1.0/3)*1.5,0])
        H_A_cor = np.array([0.89*1.5,(-1.69+1+1.0/3)*1.5,0])
        H_B_cor = np.array([0.15*1.5,(-2.38+1+1.0/3)*1.5,0])
        H_C_cor = np.array([-0.61*1.5,(-0.12+1+1.0/3)*1.5,0])
        Tri = MyTriangle(A_cor, B_cor, C_cor)
        H_cor = Tri.get_orthocenter()
        M_A_cor, M_B_cor, M_C_cor = Tri.get_three_mid()
        M_AH_cor = np.array([0.92*1.5,(-0.86+1)*1.5+0.5,0])
        M_BH_cor = np.array([-1.08*1.5,(-2.07+1)*1.5+0.5,0])
        M_CH_cor = np.array([0.6*1.5,(-2.12+1)*1.5+0.5,0])

        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        H_A = Dot(H_A_cor, color=RED)
        H_B = Dot(H_B_cor, color=ORANGE)
        H_C = Dot(H_C_cor, color=YELLOW)
        H = Dot(H_cor,color="#9400D3")
        H_label = TextMobject("H",color="#9400D3").next_to(H,DOWN)

        M_A = Dot(M_A_cor).set_color("#00FFFF")
        M_B = Dot(M_B_cor).set_color("#00FFFF")
        M_C = Dot(M_C_cor).set_color("#00FFFF")
        O9Circle = Tri.get_O9Circle().set_color("#00FF00")
        O9 = Dot(O9Circle.get_center(),color="#00FF00")
        O9_label = TexMobject("O_9",color="#00FF00").next_to(O9,LEFT)

        A_label = TextMobject("A").next_to(A,UP)
        B_label = TextMobject("B").next_to(B,LEFT)
        C_label = TextMobject("C").next_to(C,LEFT+DOWN)
        H_A_label = TexMobject("H_A",color=RED).next_to(H_A,RIGHT)
        H_B_label = TexMobject("H_B",color=ORANGE).next_to(H_B,DOWN)
        H_C_label = TexMobject("H_C",color=YELLOW).next_to(H_C,UP)      

        AH_A = Line(A_cor, H_A_cor, color=RED)
        BH_B = Line(B_cor, H_B_cor, color=ORANGE)
        CH_C = Line(C_cor, H_C_cor, color=YELLOW)

        CH_A = Line(C_cor, H_A_cor)
        CH_B = Line(C_cor, H_B_cor)
        C_H = Line(C_cor, H_cor).set_color(YELLOW)
        H_BH = Line(H_B_cor, H_cor).set_color(ORANGE)
        H_AH = Line(H_A_cor, H_cor).set_color(RED)

        M_AH = Dot(M_AH_cor).set_color("#DC143C")
        M_BH = Dot(M_BH_cor).set_color("#DC143C")
        M_CH = Dot(M_CH_cor).set_color("#DC143C")

        AB = Line(A_cor, B_cor)
        BC = Line(B_cor, C_cor)
        CA = Line(C_cor,A_cor)
        
        sentence1 = HText("三角形三条边的中点，三个垂足").to_edge(DOWN)
        sentence2 = HText("和垂心与顶点连线后形成的三个中点").to_edge(DOWN)
        sentence3 = HText("九点共圆").to_edge(DOWN).set_color("#00FF00")
        sentence1[7:9].set_color("#00FFFF")
        sentence1[12:14].set_color("#FF00FF")
        sentence2[14:16].set_color("#DC143C")

        self.play(Write(name))
        self.play(Write(AB),Write(BC),Write(CA))
        self.wait(0.5)
        self.play(Write(A),Write(B),Write(C),Write(A_label),Write(B_label),Write(C_label))
        self.wait(1)
        self.play(Write(M_A),Write(M_B),Write(M_C),Write(sentence1))
        self.wait(1.5)
        self.play(Write(AH_A),Write(CH_A))
        self.play(Write(H_A),Write(H_A_label))
        self.play(Write(BH_B),Write(CH_B))
        self.play(Write(H_B),Write(H_B_label))
        self.play(Write(CH_C))
        self.play(Write(H_C),Write(H_C_label))
        self.wait(0.5)
        self.play(Write(C_H),Write(H_BH),Write(H_AH))
        self.play(Write(H))
        self.play(Write(H_label),ReplacementTransform(sentence1,sentence2))
        self.wait(1.5)
        self.play(Write(M_AH),Write(M_BH),Write(M_CH))
        self.wait(2)
        self.play(Write(O9Circle),Write(O9),Write(O9_label),ReplacementTransform(sentence2,sentence3))
        self.wait(2)
        self.play(FadeOut(VGroup(AB,BC,CA,A,B,C,
                                 A_label,B_label,C_label,M_A,M_B,M_C,H_A,H_B,H_C,H_A_label,H_B_label,H_C_label,H,H_label,
                                 CH_C,M_AH,M_BH,M_CH,O9Circle,O9,O9_label,
                                 AH_A,CH_A,BH_B,CH_B,H_BH,H_AH,C_H,
                                 sentence3,name)))

class Fermat(Scene): # 费马点+莱斯特V
    def construct(self):
        name = HText("第一费马点").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name2 = HText("第二费马点").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name3 = HText("外心").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        name4 = HText("莱斯特定理").set_color("#FFD700").scale(1.5).to_edge(UP+LEFT)
        
        A_cor = np.array([0.97*0.9+1, 0.84*0.9+1.15,0])
        B_cor = np.array([-3.02*0.9+1,-1.58*0.9+1.15,0])
        C_cor = np.array([0.33*0.9+1,-1.68*0.9+1.15,0])
        P_cor = np.array([-1.43*0.9+1,-4.54*0.9+1.15,0])
        Q_cor = np.array([2.83*0.9+1,-0.97*0.9+1.15,0])
        R_cor = np.array([-3.12*0.9+1,3.09*0.9+1.15,0])
        P2_cor = np.array([-1.26*0.9+1,1.28*0.9+1.15,0])
        Q2_cor = np.array([-1.53*0.9+1,0.13*0.9+1.15,0])
        R2_cor = np.array([1.07*0.9+1,-3.83*0.9+1.15,0])
        F_1_cor = np.array([0.03*0.9+1,-1.26*0.9+1.15,0])
        F_2_cor = np.array([-0.63*0.9+1,1.16*0.9+1.15,0])

        Tri = MyTriangle(A_cor, B_cor, C_cor)
        O = Dot(Tri.get_circumcenter(),color="#00FFFF")
        O9 = Dot(Tri.get_O9Circle().get_center(),color="#00FF00")
        circ = Tri.get_circumcircle().set_color("#00FFFF")
        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        P = Dot(P_cor)
        Q = Dot(Q_cor)
        R = Dot(R_cor)
        P2 = Dot(P2_cor)
        Q2 = Dot(Q2_cor)
        R2 = Dot(R2_cor)
        four_circ = MyTriangle(Tri.get_circumcenter(), F_1_cor,F_2_cor).get_circumcircle().set_color(RED)

        A_label = TextMobject("A").next_to(A,UP)
        B_label = TextMobject("B").next_to(B,LEFT)
        C_label = TextMobject("C").next_to(C,0.7*RIGHT+0.6*DOWN)
        P_label = TextMobject("P").next_to(P,RIGHT+0.15*UP)
        Q_label = TextMobject("Q").next_to(Q,RIGHT)
        R_label = TextMobject("R").next_to(R,LEFT+DOWN)
        P2_label = TextMobject(r"P'").next_to(P2,0.1*LEFT+0.25*UP)
        Q2_label = TextMobject(r"Q'").next_to(Q2,0.5*LEFT)
        R2_label = TextMobject(r"R'").next_to(R2,RIGHT)
        O_label = TextMobject("O").next_to(O,LEFT)
        O9_label = TexMobject("O_9").next_to(O9,LEFT)


        AB = Line(A_cor, B_cor)
        BC = Line(B_cor, C_cor)
        CA = Line(C_cor,A_cor)

        AR = Line(A_cor, R_cor).set_color("#FF69B4")
        BR = Line(B_cor, R_cor).set_color("#FF69B4")
        BP = Line(B_cor, P_cor).set_color(GREEN)
        CP = Line(C_cor, P_cor).set_color(GREEN)
        AQ = Line(A_cor, Q_cor).set_color(ORANGE)
        CQ = Line(C_cor, Q_cor).set_color(ORANGE)

        AR2 = Line(A_cor, R2_cor).set_color("#FF69B4")
        BR2 = Line(B_cor, R2_cor).set_color("#FF69B4")
        BP2 = Line(B_cor, P2_cor).set_color(GREEN)
        CP2 = Line(C_cor, P2_cor).set_color(GREEN)
        AQ2 = Line(A_cor, Q2_cor).set_color(ORANGE)
        CQ2 = Line(C_cor, Q2_cor).set_color(ORANGE)       

        AP = Line(A_cor, P_cor)
        BQ = Line(B_cor, Q_cor)
        CR = Line(C_cor, R_cor)

        Q2F2 = Line(Q2_cor, F_2_cor)
        CF2 = Line(C_cor, F_2_cor)

        AP2 = Line(A_cor, P2_cor)
        BQ2 = Line(B_cor, Q2_cor)
        CR2 = Line(C_cor, R2_cor)

        F_1 = Dot(F_1_cor).set_color("#8A2BE2")
        F_1_label = TexMobject("F_1").next_to(F_1,UP).set_color("#8A2BE2")
        F_2 = Dot(F_2_cor).set_color("#8A2BE2")
        F_2_label = TexMobject("F_2").next_to(F_2,UP).set_color("#8A2BE2")

        sentence1 = HText("以三角形的每一边为底边,向外做三个正三角形").to_edge(DOWN)
        sentence2 = HText("连接AP,BQ,CR,交点即为第一费马点").to_edge(DOWN)

        sentence3 = HText("以三角形的每一边为底边,向内做三个正三角形").to_edge(DOWN)
        sentence4 = HText("连接AP',BQ',CR',交点即为第二费马点").to_edge(DOWN)
        sentence5 = HText("三角形外接圆的圆心即为外心").to_edge(DOWN)
        sentence6 = HText("将刚才得到的四个点都标出来").to_edge(DOWN)
        sentence7 = HText("我们会惊奇地发现这四个点也是共圆的").to_edge(DOWN)

        sentence1[-4:].set_color(RED)
        sentence2[-5:].set_color("#8A2BE2")

        sentence3[-4:].set_color(RED)
        sentence4[-5:].set_color("#8A2BE2")   
        sentence5[3:6].set_color("#00FFFF")    
        sentence5[-2:].set_color("#00FFFF")    
        sentence7[-3:-1].set_color(RED)

        self.play(Write(AB),Write(BC),Write(CA),Write(name))
        self.wait(0.5)
        self.play(Write(A),Write(B),Write(C),Write(A_label),Write(B_label),Write(C_label))
        self.wait(2.5)
        self.play(Write(sentence1))
        self.wait(1.5)
        AB.set_color("#FF69B4")
        self.wait(0.5)
        self.play(Write(AR),Write(BR))
        self.play(Write(R_label))
        self.wait(0.5)
        BC.set_color(GREEN)
        self.wait(0.5)
        self.play(Write(BP),Write(CP))
        self.play(Write(P_label))
        self.wait(0.5)
        CA.set_color(ORANGE)
        self.wait(0.5)
        self.play(Write(AQ),Write(CQ))
        self.play(Write(Q_label))
        self.wait(1)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.wait(1)
        self.play(Write(AP),Write(BQ),Write(CR))
        self.wait(1)
        self.play(Write(F_1),Write(F_1_label))
        self.wait(2)

        self.play(FadeOut(AP),FadeOut(BQ),FadeOut(CR),
                  FadeOut(VGroup(AR,BR,BP,CP,AQ,CQ,F_1,F_1_label,P_label,Q_label,R_label,sentence2)))
        self.play(ReplacementTransform(name,name2))
        self.play(Write(sentence3))
        self.wait(1.5)
        self.play(Write(AR2),Write(BR2))
        self.play(Write(R2_label))
        self.wait(0.5)
        self.play(Write(BP2),Write(CP2))
        self.play(Write(P2_label))
        self.wait(0.5)
        self.play(Write(AQ2),Write(CQ2))
        self.play(Write(Q2_label))
        self.wait(1)
        self.play(ReplacementTransform(sentence3,sentence4))
        self.wait(1)
        self.play(Write(AP2),Write(BQ2),Write(CR2))
        self.wait(1)
        self.play(Write(Q2F2),Write(CF2))
        self.play(Write(F_2),Write(F_2_label))
        self.wait(2)
        self.play(FadeOut(AP2),FadeOut(BQ2),FadeOut(CR2),
                  FadeOut(VGroup(AR2,BR2,BP2,CP2,AQ2,CQ2,F_2,F_2_label,P2_label,Q2_label,R2_label,sentence4,Q2F2,CF2)))
        self.play(ReplacementTransform(name2,name3))
        self.play(Write(sentence5))
        self.play(Write(O),Write(O_label))
        self.play(Write(circ))
        self.wait(2)
        self.play(FadeOut(circ),FadeOut(sentence5))
        self.wait(1)
        self.play(ReplacementTransform(name3,name4))
        self.play(Write(sentence6))
        self.play(Write(VGroup(F_1,F_1_label,F_2,F_2_label,O9,O9_label)))
        self.wait(2)
        self.play(ReplacementTransform(sentence6,sentence7))
        self.wait(0.5)
        self.play(Write(four_circ))
        self.wait(2.5)

class thx(Scene): # Thanks for watching + 三连动画V
    def construct(self):
        sentence1 = HText("这就是这个视频的全部内容了").set_color("#FFD700").scale(1.9).to_edge(UP)
        sentence2 = HText("如果喜欢的话不妨五连支持一下！").set_color("#FFD700").scale(1.9).to_edge(UP)

        path = "D:\\manim-master\\manimlib\\files\\"
        sanlian1 = SVGMobject(path + 'video_icon.svg', color=RED).scale(0.9).shift(5.8*LEFT).set_opacity(0.9)
        sanlian2 = SVGMobject(path + 'good.svg', color=PINK).scale(0.9).shift(2.9*LEFT)
        sanlian3 = SVGMobject(path + 'coin.svg', color=BLUE).scale(0.9)
        sanlian4 = SVGMobject(path + 'favo.svg', color=YELLOW).scale(0.9).shift(2.9*RIGHT).set_opacity(0.85)
        sanlian5 = SVGMobject(path + 'share.svg', color="#ADFF2F").scale(0.9).shift(5.8*RIGHT).set_opacity(0.85)

        self.play(Write(sentence1))
        self.wait(2)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.play(Write(VGroup(sanlian1,sanlian2,sanlian3,sanlian4,sanlian5)))
        self.wait(10)