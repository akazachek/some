from manim import *

class NormalExamples(Scene):

    def construct(self):

        # axes
        self.camera.background_color = "#ece6e2"
        axes = Axes(
            x_range= [-3,3],
            y_range= [-3,3],
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

        # example 1
        matrix1 = MathTex(r"\begin{bmatrix} 0 & 3 \\ 3 & 0 \end{bmatrix}", color=BLACK).shift(LEFT * 4.3 + UP * 3)
        matrix1e1 = Arrow(axes.c2p(0,0,0), axes.c2p(-1,1,0), color=BLUE, buff=0, stroke_width=3.5)
        matrix1e2 = Arrow(axes.c2p(0,0,0), axes.c2p(1,1,0), color=BLUE, buff=0, stroke_width=3.5)
        matrix1right1 = Line(axes.c2p(-0.1,0.1,0), axes.c2p(0,0.2,0), color=BLUE, stroke_width=3.5)
        matrix1right2 = Line(axes.c2p(0.1,0.1,0), axes.c2p(0,0.2,0), color=BLUE, stroke_width=3.5)

        # example 2
        matrix2 = MathTex(r"\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}", color=BLACK).shift(LEFT * 4.3 + UP * 3)
        matrix2e1 = Arrow(axes.c2p(0,0,0), axes.c2p(1,-1,0), color=ORANGE, buff=0, stroke_width=3.5)
        matrix2e2 = Arrow(axes.c2p(0,0,0), axes.c2p(-1,-1,0), color=ORANGE, buff=0, stroke_width=3.5)
        matrix2right1 = Line(axes.c2p(0.1,-0.1,0), axes.c2p(0,-0.2,0), color=ORANGE, stroke_width=3.5)
        matrix2right2 = Line(axes.c2p(-0.1,-0.1,0), axes.c2p(0,-0.2,0), color=ORANGE, stroke_width=3.5)

        # example 3
        matrix3 = MathTex(r"\begin{bmatrix} -\sqrt{2} & 99 \\ 99 & -\sqrt{2} \end{bmatrix}", color=BLACK).shift(LEFT * 4.3 + UP * 3)
        matrix3e1 = Arrow(axes.c2p(0,0,0), axes.c2p(-1,1,0), color=PURPLE, buff=0, stroke_width=3.5)
        matrix3e2 = Arrow(axes.c2p(0,0,0), axes.c2p(1,1,0), color=PURPLE, buff=0, stroke_width=3.5)
        matrix3right1 = Line(axes.c2p(-0.1,0.1,0), axes.c2p(0,0.2,0), color=PURPLE, stroke_width=3.5)
        matrix3right2 = Line(axes.c2p(0.1,0.1,0), axes.c2p(0,0.2,0), color=PURPLE, stroke_width=3.5)

        # animation
        self.play(GrowFromCenter(axes))
        self.play(Write(matrix1))
        self.wait(1)
        self.play(Write(matrix1e1), Write(matrix1e2))
        self.wait(1)
        self.play(Write(matrix1right1), Write(matrix1right2))
        self.wait(2)
        self.play(FadeOut(matrix1), FadeOut(matrix1e1), FadeOut(matrix1e2), FadeOut(matrix1right1), FadeOut(matrix1right2))
        self.wait(1)
        self.play(Write(matrix2))
        self.wait(1)
        self.play(Write(matrix2e1), Write(matrix2e2))
        self.wait(1)
        self.play(Write(matrix2right1), Write(matrix2right2))
        self.wait(2)
        self.play(FadeOut(matrix2), FadeOut(matrix2e1), FadeOut(matrix2e2), FadeOut(matrix2right1), FadeOut(matrix2right2))
        self.wait(1)
        self.play(Write(matrix3))
        self.wait(1)
        self.play(Write(matrix3e1), Write(matrix3e2))
        self.wait(1)
        self.play(Write(matrix3right1), Write(matrix3right2))
        self.wait(2)
        self.play(FadeOut(matrix3), FadeOut(matrix3e1), FadeOut(matrix3e2), FadeOut(matrix3right1), FadeOut(matrix3right2))
        self.wait(1)