from manim import *


def set_matrix_color(M):
    for bra in M.get_brackets():
        bra.set_color(BLACK)
    for e in M.get_entries():
        e.set_color(BLACK)
    return M


class Solution(Scene):

    def construct(self):

        # axes
        self.camera.background_color = "#ece6e2"
        x = MathTex(r" \left\{ \text{linear operators} \right\} \longleftrightarrow  \left\{ \text{matrices} \right\}  ", color=BLACK)

        # animation
        self.play(Write(x))
        self.wait()