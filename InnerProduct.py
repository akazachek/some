from manim import *

class InnerProduct(Scene):
    def construct(self):

        # first component properties
        linearityText = Text("Linear in the first slot:").scale(1).shift(2 * UP)

        firstAdditiveTeX = MathTex(r"\langle {{ x }}+{{ y }},z\rangle=\langle {{ x }}+{{ y }},z\rangle")
        firstAdditiveTeX.next_to(linearityText, DOWN, buff=1).scale(2)
        firstAdditiveTeX.set_color_by_tex("x", RED)
        firstAdditiveTeX.set_color_by_tex("y", BLUE)
        firstAdditiveTeXSplit = MathTex(r"\langle {{ x }}+{{ y }},z\rangle=\langle {{ x }},z\rangle+\langle {{ y }},z\rangle")
        firstAdditiveTeXSplit.next_to(linearityText, DOWN, buff=1).scale(2)
        firstAdditiveTeXSplit.set_color_by_tex("x", RED)
        firstAdditiveTeXSplit.set_color_by_tex("y", BLUE)

        firstHomogenousTeX = MathTex(r"\langle {{ \lambda }}x,y\rangle=\langle {{ \lambda }}x,y\rangle")
        firstHomogenousTeX.next_to(firstAdditiveTeX, DOWN, buff=1).scale(2)
        firstHomogenousTeX.set_color_by_tex(r"\lambda", GREEN)
        firstHomogenousTeXSplit = MathTex(r"\langle {{ \lambda }}x,y\rangle={{ \lambda }}\langle x,y\rangle")
        firstHomogenousTeXSplit.next_to(firstAdditiveTeX, DOWN, buff=1).scale(2)
        firstHomogenousTeXSplit.set_color_by_tex(r"\lambda", GREEN)

        # second component properties
        antilinearityText = Text("Anti-linear in the second slot:").scale(1).shift(2 * UP)

        secondAdditiveTeX = MathTex(r"\langle x, {{ y }} + {{ z }}\rangle=\langle x,{{ y }} + {{ z }}\rangle")
        secondAdditiveTeX.next_to(antilinearityText, DOWN, buff=1).scale(2)
        secondAdditiveTeX.set_color_by_tex("y", RED)
        secondAdditiveTeX.set_color_by_tex("z", BLUE)
        secondAdditiveTeXSplit = MathTex(r"\langle x, {{ y }} + {{ z }}\rangle=\langle x, {{ y }}\rangle+\langle x, {{ z }}\rangle")
        secondAdditiveTeXSplit.next_to(antilinearityText, DOWN, buff=1).scale(2)
        secondAdditiveTeXSplit.set_color_by_tex("y", RED)
        secondAdditiveTeXSplit.set_color_by_tex("z", BLUE)

        secondConjHomogenousTeX = MathTex(r"\langle x, {{ \lambda }}y\rangle=\langle x, {{ \lambda }}y\rangle")
        secondConjHomogenousTeX.next_to(secondAdditiveTeX, DOWN, buff=1).scale(2)
        secondConjHomogenousTeX.set_color_by_tex(r"\lambda", GREEN)
        secondConjHomogenousTeXSplit = MathTex(r"\langle x, {{ \lambda }} y\rangle= \bar{ {{ \lambda }} }\langle x,y\rangle")
        secondConjHomogenousTeXSplit.next_to(secondAdditiveTeX, DOWN, buff=1).scale(2)
        secondConjHomogenousTeXSplit.set_color_by_tex(r"\lambda", GREEN)

        # positive definiteness 

        posdefText = Text("Postive-definiteness:").scale(1)

        nonzeroTeX = MathTex(r"x {{ \neq }} 0\Longrightarrow \langle x,x\rangle {{ > }} 0")
        nonzeroTeX.next_to(posdefText, DOWN, buff=1).scale(2)
        nonzeroTeX.set_color_by_tex(r"\neq", RED)
        nonzeroTeX.set_color_by_tex(">", BLUE)

        zeroTeX = MathTex("x", "=", r"0\Longrightarrow \langle x,x\rangle", "=", "0")
        zeroTeX.next_to(posdefText, DOWN, buff=1).scale(2)
        zeroTeX[1].set_color(RED)
        zeroTeX[3].set_color(BLUE)

        # animation

        # first
        self.add(linearityText, firstAdditiveTeX, firstHomogenousTeX)
        self.wait(1)
        self.play(Transform(firstAdditiveTeX, firstAdditiveTeXSplit))
        self.wait(2)
        self.play(Transform(firstHomogenousTeX, firstHomogenousTeXSplit))
        self.wait(2)
        self.play(FadeOut(linearityText), FadeOut(firstAdditiveTeX), FadeOut(firstHomogenousTeX))
        self.wait(1)
        # second
        self.play(FadeIn(antilinearityText), FadeIn(secondAdditiveTeX), FadeIn(secondConjHomogenousTeX))
        self.wait(1)
        self.play(Transform(secondAdditiveTeX, secondAdditiveTeXSplit))
        self.wait(2)
        self.play(Transform(secondConjHomogenousTeX, secondConjHomogenousTeXSplit))
        self.wait(2)
        self.play(FadeOut(antilinearityText), FadeOut(secondAdditiveTeX), FadeOut(secondConjHomogenousTeX))
        self.wait(1)
        # third
        self.play(FadeIn(posdefText), FadeIn(nonzeroTeX))
        self.wait(1)
        self.play(Transform(nonzeroTeX, zeroTeX))
        self.wait(2)
        self.play(FadeOut(posdefText), FadeOut(nonzeroTeX))
        self.wait(1)
    