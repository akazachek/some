from manim import *

class InnerProduct(Scene):
    def construct(self):

        linearText = Text("First slot linearity:").scale(1)

        linearTeX = MathTex(r"\langle {{ x }}+{{ y }},z\rangle=\langle {{ x }}+{{ y }},z\rangle").next_to(linearText, DOWN, buff=1).scale(2)
        linearTeX.set_color_by_tex("x", RED)
        linearTeX.set_color_by_tex("y", BLUE)

        linearTeXSplit = MathTex(r"\langle {{ x }}+{{ y }},z\rangle=\langle {{ x }},z\rangle+\langle {{ y }},z\rangle").next_to(linearText, DOWN, buff=1).scale(2)
        linearTeXSplit.set_color_by_tex("x", RED)
        linearTeXSplit.set_color_by_tex("y", BLUE)

        self.add(linearText, linearTeX)
        self.wait(1)
        self.play(Transform(linearTeX, linearTeXSplit))
        self.wait(3)
    