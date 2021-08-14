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
                "numbers_to_include": range(-5,6,1)
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


        M = np.array([ [0,2], [2,0] ])
        Ma=set_matrix_color(Matrix(M))

        v = Matrix([[1],[2]])
        v = set_matrix_color(v)
        v1 = Vector(axes1.c2p(1,2,0), stroke_width=2, color = RED , buff=0 )
        eig1 = Vector(axes1.c2p(1,1,0),stroke_width=2, color=BLUE_E, buff=0 )
        eig2 = Vector(axes1.c2p(-1, 1, 0),stroke_width=2,  color=BLUE_E, buff=0)

        labels1 = VGroup( MathTex("\\vec{v}", color=RED).scale(0.6).next_to(v1, UP),
                         MathTex("\\text{eigenvector 1}", color=BLUE_E ).scale(0.6).next_to(eig1, RIGHT),
                         MathTex("\\text{eigenvector 2}", color=BLUE_E).scale(0.6).next_to(eig2, LEFT)
                         )

        intro = VGroup(Ma, v)

        proj1 = Vector(axes1.c2p(-1/2,1/2,0), stroke_width=2, color = GREY , buff=0 )
        proj2 = Vector(axes1.c2p(3/2, 3/2, 0), stroke_width=2, color=GREY, buff=0)

        eig1_after = Vector(axes1.c2p(1, -1, 0),stroke_width=2,  color=GREY, buff=0)
        eig2_after = Vector(axes1.c2p(3, 3, 0), stroke_width=2, color=GREY, buff=0)

        v_after = Vector(axes1.c2p(4, 2, 0), stroke_width=2, color=RED, buff=0)
        # Animation

        self.play(Write(intro[0]))
        self.wait(3)
        self.play(
            intro.animate.arrange()
        )
        self.wait(3)
        self.play(FadeOut(intro))
        self.play(Create(axes1))

        self.play(
            self.camera.frame.animate.scale(0.6),
            Write(labels1),
            Write(v1),
            Write(eig1),
            Write(eig2)
        )
        self.wait(3)
        self.play(
            Unwrite(labels1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(eig1, proj2),
            ReplacementTransform(eig2, proj1)
        )
        self.wait()

        self.play(Write(Ma.to_corner(LEFT+UP)))
        self.wait(2)
        self.play(
            Restore(self.camera.frame),
            ReplacementTransform(v1,v_after),
            ReplacementTransform(proj1, eig1_after),
            ReplacementTransform(proj2,eig2_after)
        )
        self.wait()
        self.play(eig1_after.animate.shift(axes1.c2p(3,3,0)))
        self.wait(3)
        self.play(
            ShrinkToCenter( axes1),
            Unwrite(eig2_after),
            Unwrite(eig1_after),
            Unwrite(v_after),
            Unwrite(Ma)
        )
        self.wait()