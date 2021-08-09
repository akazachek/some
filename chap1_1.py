from manim import *
import numpy as np

#https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html
# https://docs.manim.community/en/stable/examples.html
class linop(Scene):
    def construct(self):
        axes = NumberPlane(
            x_range= [-10,10],
            y_range= [-10,10]
        )
        self.add(axes)
        self.play(axes.animate.apply_matrix( [[1, 1], [0, 1]] ))
        self.wait()