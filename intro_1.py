from manim import *


def set_matrix_color(M):
    for bra in M.get_brackets():
        bra.set_color(BLACK)
    for e in M.get_entries():
        e.set_color(BLACK)
    return M


class NormalExamples(Scene):

    def construct(self):

        # axes
        self.camera.background_color = "#ece6e2"
        # example 1
        M1 = Matrix( [[0,3],[3,0]] )
        M1= set_matrix_color(M1)

        M2 = Matrix([[-1, 1], [1, -1]])
        M2 = set_matrix_color(M2)

        M3 = Matrix([[ r"\sqrt{-2}", 99], [99, r"\sqrt{-2}"]])
        M3 = set_matrix_color(M3)

        matrices = VGroup(M1,M2,M3).arrange_in_grid(3,1)

        # animation
        self.play(Write(matrices), run_time=3)
        self.wait()