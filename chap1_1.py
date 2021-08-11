from manim import *
import numpy as np

# https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html
# https://docs.manim.community/en/stable/examples.html
class linop(Scene):
    def construct(self):
        # Construct Mobjects
        self.camera.background_color = "#ece6e2"
        axes = Axes(
            x_range= [-5,5],
            y_range= [-5,5],
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

        eqn1 = MathTex( "\\vec{v}"," = a","\\vec{e_1}"," + b ","\\vec{e_2}",color = BLACK )
        eqn1.set_color_by_tex("\\vec{e_", RED)

        eqn2 = MathTex(" T(","\\vec{v}",") = aT(","\\vec{e_1}",") + bT(","\\vec{e_2}",") ", color=BLACK)
        eqn2.set_color_by_tex("\\vec{e_", RED)

        v = Arrow(axes.c2p(0,0,0), axes.c2p(1,1,0), color=GREEN, buff=0, stroke_width=3.5)
        e1 = Arrow(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=RED, buff=0, stroke_width=3.5)
        e2 = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), color=RED, buff=0, stroke_width=3.5)
        # l = Line(axes.c2p(0,0,0), axes.c2p(1,1,0), color=RED  )
        dot = Dot(axes.c2p(0,0,0),color=GREEN)
        # Animation
        self.play(Write(eqn1))
        self.wait()
        self.play(TransformMatchingTex(eqn1, eqn2))
        self.wait()
        self.play(
            Unwrite(eqn2)
        )
        self.play(
           GrowFromCenter(axes))
        self.wait()
        self.play(Write(v), Write(e1), Write(e2))
        self.wait()
        M1=np.array([[1, 1], [0, -1]])
        M2=np.array([[-1, 0], [2, 1]])
        M = np.array([[1, 1], [0, 1]])
        I = np.linalg.inv(np.dot(M2,M1))
        self.play(
            axes.animate.apply_matrix( M1),
            e1.animate.apply_matrix(M1),
            e2.animate.apply_matrix(M1),
            v.animate.apply_matrix(M1)
                  )
        self.wait()
        self.play(
            axes.animate.apply_matrix(M2),
            e1.animate.apply_matrix(M2),
            e2.animate.apply_matrix(M2),
            v.animate.apply_matrix(M2)
        )
        self.wait()
        self.play(
            axes.animate.apply_matrix(I),
            e1.animate.apply_matrix(I),
            e2.animate.apply_matrix(I),
            v.animate.apply_matrix(I)
        )
        self.wait()
        self.play(FadeOut(v))
        self.play(
            e1.animate.apply_matrix(M),
            e2.animate.apply_matrix(M)
        )
        self.wait()