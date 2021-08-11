from manim import *
import numpy as np

# https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html
# https://docs.manim.community/en/stable/examples.html
class ortho(Scene):
    def construct(self):
        # Construct Mobjects
        self.camera.background_color = "#ece6e2"
        axes = NumberPlane(
            x_range= [-5,5],
            y_range= [-5,5],
            x_length=15,
            y_length=15,
            tips= False,
            axis_config={
                "include_numbers":True
            }
        )

        axes.get_axes().set_color(BLACK)
        for num in axes.get_x_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        for num in axes.get_y_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        M = [ [1,2], [2,1] ]
        # Animation
        self.play(
           GrowFromCenter(axes))
        self.wait()

        # M1=np.array([[0, 1], [1, 0]])
        # M1_inv = np.linalg.inv(M1)
        # Ma1 = Matrix( M1).to_corner(LEFT+UP)
        # for bra in Ma1.get_brackets():
        #     bra.set_color(BLACK)
        # for e in Ma1.get_entries():
        #     e.set_color(BLACK)
        #
        # M2=np.array([[1, 5], [5, 1]])
        # M2_inv = np.linalg.inv(M2)
        # Ma2 = Matrix(M2).to_corner(LEFT + UP)
        # for bra in Ma2.get_brackets():
        #     bra.set_color(BLACK)
        # for e in Ma2.get_entries():
        #     e.set_color(BLACK)
        #
        # M = np.array([[2, -5], [-5, 2]])
        # M_inv = np.linalg.inv(M)
        # Ma = Matrix(M).to_corner(LEFT + UP)
        # for bra in Ma.get_brackets():
        #     bra.set_color(BLACK)
        # for e in Ma.get_entries():
        #     e.set_color(BLACK)
        #
        # self.play(
        #     axes.animate.apply_matrix(M1),
        #     Write(Ma1)
        #           )
        # self.wait()
        # self.play(
        #     FadeOut(Ma1),
        #     axes.animate.apply_matrix(M1_inv),
        # )
        # self.wait()
        # self.play(
        #     Write(Ma2),
        #     axes.animate.apply_matrix(M2)
        # )
        # self.wait()
        # self.play(
        #     FadeOut(Ma2),
        #     axes.animate.apply_matrix(M2_inv)
        # )
        # self.wait()
        # self.play(
        #     Write(Ma),
        #     axes.animate.apply_matrix(M)
        # )
        # self.wait()
        # self.play(
        #     FadeOut(Ma),
        #     axes.animate.apply_matrix(M_inv)
        # )
        # self.wait()