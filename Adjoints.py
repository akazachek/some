from manim import *

class Adjoints(Scene):
    def construct(self):

        self.camera.background_color = "#ece6e2"

        # inner product definition

        adjointDefStart = MathTex(r"\langle {{ T }} x,y\rangle = \langle {{ T }} x,y\rangle", color = BLACK)
        adjointDefEnd = MathTex(r"\langle {{ T }} x,y\rangle=\langle x, {{ T }}^{\! \ast} y\rangle", color = BLACK)
        adjointDefStart.set_color_by_tex("T", RED)
        adjointDefEnd.set_color_by_tex("T", RED)

        # matrix definition
        
        operatorMatrix = MathTex(r"T=\begin{pmatrix} a & b \\ c & d \end{pmatrix}", color = BLACK)
        operatorMatrix.shift(2 * LEFT)
        adjointMatrixStart = MathTex(r"?=T^\ast", color = BLACK)
        adjointMatrixMiddle = MathTex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}^\ast = T^\ast", color = BLACK)
        adjointMatrixMiddle2 = MathTex(r"\begin{pmatrix} \bar{a} & \bar{b} \\ \bar{c} & \bar{d} \end{pmatrix}^t=T^\ast", color = BLACK)
        adjointMatrixEnd = MathTex(r"\begin{pmatrix} \bar{a} & \bar{c} \\ \bar{b} & \bar{d} \end{pmatrix}=T^\ast", color = BLACK)

        adjointMatrixStart.next_to(operatorMatrix, RIGHT, buff = 2)
        adjointMatrixMiddle.next_to(operatorMatrix, RIGHT, buff = 1)
        adjointMatrixMiddle2.next_to(operatorMatrix, buff = 1)
        adjointMatrixEnd.next_to(operatorMatrix, RIGHT, buff = 1)

        # first

        self.add(adjointDefStart)
        self.wait(1)
        self.play(TransformMatchingTex(adjointDefStart, adjointDefEnd))
        self.wait(2)
        self.play(TransformMatchingTex(adjointDefEnd, adjointDefStart))
        self.wait(2)
        self.play(TransformMatchingTex(adjointDefStart, adjointDefEnd))
        self.wait(1)
        self.play(FadeOut(adjointDefEnd))
        self.wait(1)

        # second

        self.play(FadeIn(operatorMatrix))
        self.wait(1)
        self.play(FadeIn(adjointMatrixStart))
        self.wait(2)
        self.play(Transform(adjointMatrixStart, adjointMatrixMiddle))
        self.wait(2)
        self.play(Transform(adjointMatrixStart, adjointMatrixMiddle2))
        self.wait(2)
        self.play(Transform(adjointMatrixStart, adjointMatrixEnd))
        self.wait(2)
        self.play(FadeOut(operatorMatrix), FadeOut(adjointMatrixStart))
        self.wait(1)
    