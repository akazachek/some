from manim import *

def shiftMethod(self):
    return self.shift(4 * LEFT)

class DotProduct(Scene):

    def construct(self):

        # axes
        self.camera.background_color = "#ece6e2"
        axes = Axes(
            x_range= [-2,5],
            y_range= [-2,5],
            x_length=15,
            y_length=15,
            tips= False,
            axis_config={
                "color":BLACK,
                "include_numbers": True
            }
        )
        for num in axes.get_x_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        for num in axes.get_y_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        # first vectors
        u = Arrow(axes.c2p(0,0,0), axes.c2p(1,2,0), color=RED, buff=0, stroke_width=3.5)
        uNode = MathTex("u", color=RED).next_to(u, UP * 0.5 + RIGHT * 0.25)
        v = Arrow(axes.c2p(0, 0, 0), axes.c2p(3, 1, 0), color=RED, buff=0, stroke_width=3.5)
        vNode = MathTex("v", color=RED).next_to(v, RIGHT * 0.8 + UP * 0.4)
        uvAngle = Arc(radius = 1, arc_center = axes.c2p(0,0,0), start_angle=0.3454, angle=0.7536, color=RED)

        uvDot1 = MathTex(r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}\cdot \begin{bmatrix} 3 \\ 1 \end{bmatrix}", color=BLACK).shift(RIGHT * 4 + UP * 3)
        uvDot2 = MathTex(r"= 1\cdot 3+2\cdot 1", color=BLACK).next_to(uvDot1, DOWN).shift(LEFT * 0.2)
        uvDot3 = MathTex("=5", color=BLACK).next_to(uvDot2, DOWN).shift(LEFT)
        uvDotProd = VGroup(uvDot1, uvDot2, uvDot3)

        # second vectors
        uPrime = Arrow(axes.c2p(0,0,0), axes.c2p(-0.67,2,0), color=RED, buff=0, stroke_width=3.5)
        uPvAngle1 = Line(axes.c2p(0.3,0.1,0), axes.c2p(0.18,0.46,0), color=RED)
        uPvAngle2 = Line(axes.c2p(0.18,0.46,0), axes.c2p(-0.12,0.36,0), color=RED)
        uPvAngle = VGroup(uPvAngle1, uPvAngle2)

        uPvDot1 = MathTex(r"\begin{bmatrix} -\frac{2}{3} \\ 2\end{bmatrix}\cdot \begin{bmatrix} 3 \\ 1 \end{bmatrix}", color=BLACK).shift(RIGHT * 4 + UP * 3)
        uPvDot2 = MathTex(r"= -\frac{2}{3}\cdot 3+2\cdot 1", color=BLACK).next_to(uPvDot1, DOWN).shift(LEFT * 0.2)
        uPvDot3 = MathTex("=0", color=BLACK).next_to(uPvDot2, DOWN).shift(LEFT * 1.45)
        uPvDotProd = VGroup(uPvDot1, uPvDot2, uPvDot3)
        uPvDotProdAnim = AnimationGroup(
            *[Transform(uvDotProd[i], uPvDotProd[i]) for i in range(3)]
        )

        # norm
        vNorm1 = MathTex(r"||v||^2 = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} 3 \\ 1\end{bmatrix}", color=BLACK).shift(RIGHT * 4 + UP * 3)
        vNorm2 = MathTex(r"=3\cdot 3+1\cdot 1", color=BLACK).next_to(vNorm1, DOWN).shift(RIGHT * 0.83)
        vNorm3 = MathTex(r"=10", color=BLACK).next_to(vNorm2, DOWN).shift(LEFT * 0.9)
        vNorm = VGroup(vNorm1, vNorm2, vNorm3)
        vNorm4 = MathTex(r"||v||=\sqrt{10}", color=BLACK).shift(RIGHT * 4 + UP * 3)

        # animation
        self.play(GrowFromCenter(axes))
        self.play(Write(u), Write(uNode), Write(v), Write(vNode))
        self.play(Write(uvAngle))
        self.wait(1)
        for i in range(3):
            self.play(Write(uvDotProd[i]))
            self.wait(0.3)
        self.wait(3)
        self.play(Transform(u, uPrime), Transform(uvAngle, uPvAngle), uPvDotProdAnim, ApplyFunction(shiftMethod, uNode))
        self.wait(3)
        self.play(FadeOut(u), FadeOut(uvAngle), FadeOut(uvDotProd), FadeOut(uNode))
        self.wait(1)
        for i in range(3):
            self.play(Write(vNorm[i]))
            self.wait(0.3)
        self.play(FadeOut(vNorm[1]), FadeOut(vNorm[2]), Transform(vNorm[0], vNorm4))
        self.wait(2)