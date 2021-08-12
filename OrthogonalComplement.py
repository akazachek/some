from manim import *

def grayObject(self):
    return self.set_color(GRAY)

class OrthogonalComplement(Scene):

    def construct(self):

        # axes
        self.camera.background_color = "#ece6e2"
        axes = Axes(
            x_range= [-1,2],
            y_range= [-1,2],
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

        # unit vector and linear subspace
        v = Arrow(axes.c2p(0, 0, 0), axes.c2p(0.75, 0.66144, 0), color=RED, buff=0, stroke_width=3.5)
        vNode = MathTex("v", color=RED).next_to(v, 0.8 * RIGHT).shift(UP * 1.3)
        vSpanLeft = DashedLine(axes.c2p(-1.5,-1.323,0), axes.c2p(0,0,0), color=RED)
        vSpanRight = DashedLine(axes.c2p(0.75,0.66144,0), axes.c2p(1.5,1.323,0), color=RED)

        # vector to project
        u = Arrow(axes.c2p(0,0,0), axes.c2p(0.4,0.8,0), color=BLUE, buff=0, stroke_width=3.5)
        uGhost = Arrow(axes.c2p(0,0,0), axes.c2p(0.4,0.8,0), color=GRAY, buff=0, stroke_width=3.5)
        uNode = MathTex("u", color=BLUE).next_to(u, 0.3 * UP).shift(RIGHT * 0.6)
        
        # projections
        uProject = Arrow(axes.c2p(0,0,0), axes.c2p(0.6219,0.5484,0), color=BLUE, buff=0, stroke_width=3.5)
        uProjectNode = MathTex("P_vu", color=BLUE).next_to(uProject, 0.1 * RIGHT).shift(0.7 * UP)
        uOrtho = Arrow(axes.c2p(0.6219,0.5484,0), axes.c2p(0.4,0.8,0), color=ORANGE, buff=0, stroke_width=3.5)
        uOrthoOrigin = Arrow(axes.c2p(0,0,0), axes.c2p(-0.2219,0.2516), color=ORANGE, buff=0, stroke_width=3.5)

        # ortho complement
        vCompSpanLeft = DashedLine(axes.c2p(-0.2219,0.2516, 0), axes.c2p(-1.3314,1.5096,0), color=ORANGE)
        vCompSpanRight = DashedLine(axes.c2p(0,0,0), axes.c2p(1.9971,-2,2644,0), color=ORANGE)
        vCompNode = MathTex("v^{\perp}", color=ORANGE).next_to(vCompSpanLeft, RIGHT).shift(2.2 * LEFT)
        rightAngle1 = Line(axes.c2p(-0.0496,0.056,0), axes.c2p(0.0099,0.1088,0), color=ORANGE, stroke_width=3.5)
        rightAngle2 = Line(axes.c2p(0.0595,0.053,0), axes.c2p(0.0099,0.1088,0), color=ORANGE, stroke_width=3.5)

        # animation
        self.play(GrowFromCenter(axes))
        self.play(Write(v), Write(vNode))
        self.wait(1)
        self.play(FadeIn(vSpanLeft), FadeIn(vSpanRight))
        self.wait(2)
        self.play(Write(u), Write(uNode))
        self.wait(1)
        self.play(ApplyFunction(grayObject, uNode), TransformFromCopy(u, uGhost), Transform(u, uProject), FadeIn(uProjectNode))
        self.wait(1)
        self.play(Write(uOrtho))
        self.wait(1)
        self.play(Transform(uOrtho, uOrthoOrigin))
        self.wait(1)
        self.play(FadeIn(vCompSpanLeft), FadeIn(vCompSpanRight), Write(vCompNode), Write(rightAngle1), Write(rightAngle2))
        self.wait(2)