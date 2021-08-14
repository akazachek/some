from manim import *
import numpy as np


def set_matrix_color(M):
    for bra in M.get_brackets():
        bra.set_color(BLACK)
    for e in M.get_entries():
        e.set_color(BLACK)
    return M

# https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html
# https://docs.manim.community/en/stable/examples.html
class ortho(MovingCameraScene):
    def construct(self):
        # Construct Mobjects
        self.camera.background_color = "#ece6e2"
        self.camera.frame.save_state()
        axes1 = NumberPlane(
            x_range= [-5,5],
            y_range= [-5,5],
            x_length=14,
            y_length=8,
            tips= False,
            axis_config={
                "numbers_to_include": range(-5,5,1)
            },
            background_line_style = {
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.3
            }
        )

        axes1.get_axes().set_color(BLACK)
        for num in axes1.get_x_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        for num in axes1.get_y_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        M = np.array([ [1,0], [2,2] ])
        Ma=set_matrix_color(Matrix(M))

        v = Matrix([[1],[1]])
        v = set_matrix_color(v)
        v1 = Vector(axes1.c2p(1,1,0), stroke_width=4, color = RED , buff=0 )
        eig1 = Vector(axes1.c2p(0,1,0),stroke_width=4, color=BLUE_E, buff=0 )
        eig2 = Vector(axes1.c2p(-1, 2, 0),stroke_width=4,  color=BLUE_E, buff=0)

        legend = VGroup( Dot(color=RED),
                         MathTex("\\vec{v}", color=RED),
                         Dot(color=BLUE_E),
                         MathTex("\\text{eigenvectors}", color=BLUE_E ),
                         Dot(color=GREY),
                         MathTex("\\text{projections}", color=GREY)
                         ).arrange_in_grid(rows=3,cols=2)


        intro = VGroup(Ma, v)

        proj1 = Vector(axes1.c2p(0,1,0), stroke_width=4, color = GREY , buff=0 )
        proj2 = Vector(axes1.c2p(-0.2, 0.4, 0), stroke_width=4, color=GREY, buff=0)

        eig1_after = Vector(axes1.c2p(0, 2, 0),stroke_width=4,  color=GREY, buff=0)
        eig2_after = Vector(axes1.c2p(-0.2, 0.4, 0), stroke_width=4, color=GREY, buff=0)

        v_after = Vector(axes1.c2p(1, 4, 0), stroke_width=4, color=RED, buff=0)
        # Animation

        self.play(Write(intro[0]))
        self.wait(3)
        self.play(
            intro.animate.arrange()
        )
        self.wait(3)
        self.play(FadeOut(intro))
        self.play(Create(axes1))
        self.play(self.camera.frame.animate.scale(0.45))
        self.play(
            Write(v1),
            Write(eig1),
            Write(eig2)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(eig1, proj1),
            ReplacementTransform(eig2, proj2)
        )
        self.wait()
        self.play(
            Write(Ma.to_corner(LEFT+UP)))
        self.wait(2)
        self.play(
            Restore(self.camera.frame),
            ReplacementTransform(v1,v_after),
            ReplacementTransform(proj1, eig1_after),
            ReplacementTransform(proj2,eig2_after)
        )
        self.wait()
        self.play(eig1_after.animate.shift(axes1.c2p(-0.2, 0.4, 0)))
        self.wait(3)
        self.play(
            ShrinkToCenter( axes1),
            Unwrite(eig2_after),
            Unwrite(eig1_after),
            Unwrite(v_after),
            Unwrite(Ma)
        )
        self.wait()