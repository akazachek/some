from manim import *

class Adjoints(Scene):
    def construct(self):

        self.camera.background_color = "#ece6e2"

        # inner product definition of adjoint

        adjointDefStart = MathTex(r"\langle {{ T }} x,y\rangle = \langle {{ T }} x,y\rangle", color = BLACK)
        adjointDefEnd = MathTex(r"\langle {{ T }} x,y\rangle=\langle x, {{ T }}^{\! \ast} y\rangle", color = BLACK)
        adjointDefStart.set_color_by_tex("T", RED)
        adjointDefEnd.set_color_by_tex("T", RED)

        # matrix definition of adjoint
        
        operatorMatrix = MathTex(r"A=\begin{bmatrix} a & b \\ c & d \end{bmatrix}", color = BLACK)
        operatorMatrix.shift(2 * LEFT)
        adjointMatrixStart = MathTex(r"?=A^\ast", color = BLACK)
        adjointMatrixMiddle = MathTex(r"\begin{bmatrix} a & b \\ c & d \end{bmatrix}^\ast = A^\ast", color = BLACK)
        adjointMatrixMiddle2 = MathTex(r"\begin{bmatrix} \bar{a} & \bar{b} \\ \bar{c} & \bar{d} \end{bmatrix}^t=A^\ast", color = BLACK)
        adjointMatrixEnd = MathTex(r"\begin{bmatrix} \bar{a} & \bar{c} \\ \bar{b} & \bar{d} \end{bmatrix}=A^\ast", color = BLACK)

        adjointMatrixStart.next_to(operatorMatrix, RIGHT, buff = 2)
        adjointMatrixMiddle.next_to(operatorMatrix, RIGHT, buff = 1)
        adjointMatrixMiddle2.next_to(operatorMatrix, buff = 1)
        adjointMatrixEnd.next_to(operatorMatrix, RIGHT, buff = 1)

        # normal definition

        noncommMatrices = MathTex(r"\begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\neq\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}", color=BLACK)
        noncommMatricesMultiplied = MathTex(r"\begin{bmatrix} 1 & 3 \\ 0 & 3 \end{bmatrix}\neq \begin{bmatrix} 1 & 5 \\ 0 & 3 \end{bmatrix}", color=BLACK)

        normalDef = MathTex(r"T T^\ast= T^\ast T", color=BLACK).scale(2)
        normalDefText = Text("Normal", color=BLACK).next_to(normalDef, DOWN * 2).scale(1)

        saDef = MathTex(r"T = T^\ast", color=BLACK).scale(2)
        saDefText = Text("Self-adjoint", color=BLACK).next_to(normalDef, DOWN * 2).scale(1)
        
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

        # third

        self.play(FadeIn(noncommMatrices))
        self.wait(2)
        self.play(Transform(noncommMatrices, noncommMatricesMultiplied))
        self.wait(2)
        self.play(FadeOut(noncommMatrices))
        self.wait(1)
        self.play(FadeIn(normalDef))
        self.wait(2)
        self.play(Write(normalDefText))
        self.wait(2)
        self.play(FadeOut(normalDef), FadeOut(normalDefText))
        self.wait(1)
        self.play(FadeIn(saDef))
        self.wait(2)
        self.play(Write(saDefText))
        self.wait(2)
    