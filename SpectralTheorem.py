from manim import *

class SpectralTheorem(Scene):
    def construct(self):

        self.camera.background_color = "#ece6e2"

        # first component properties
        spectralTheorem1 = Tex(r"Consider a $\textbf{real}$ (or $\textbf{complex}$) vector space $V$ of dimension $n$,", color=BLACK).scale(0.75).shift(UP * 2.3)
        spectralTheorem2 = Tex(r"and let $T$ be a $\textbf{self-adjoint}$ (or $\textbf{normal}$) linear operator on $V$.", color=BLACK).scale(0.75).next_to(spectralTheorem1, DOWN, buff=0.1)
        spectralTheorem3 = Tex(r"$\quad$Then, the eigenvectors $\{v_1,\dots ,v_n\}$ of $T$ with eigenvalues", color=BLACK).scale(0.75).next_to(spectralTheorem2, DOWN, buff=0.7)
        spectralTheorem4 = Tex(r"$\{\lambda_1,\dots,\lambda_n\}$ form an $\textbf{orthonormal basis}$ for $V$. Moreover,", color=BLACK).scale(0.75).next_to(spectralTheorem3, DOWN, buff=0.1)
        spectralTheorem5 = Tex(r"$T$ is equal to the $\textbf{sum of the projections}$ onto the $\textbf{eigen-}$", color=BLACK).scale(0.75).next_to(spectralTheorem4, DOWN, buff=0.1)
        spectralTheorem6 = Tex(r"$\textbf{vectors}$, weighted by the $\textbf{eigenvalues}$:", color=BLACK).scale(0.75).next_to(spectralTheorem5, DOWN, buff=0.1)
        spectralTheoremTex = MathTex(r"T=\sum_{i=1}^n \lambda_i P_{v_i}.", color=BLACK).scale(1.2).shift(DOWN).next_to(spectralTheorem6 , DOWN)

        self.play(Write(spectralTheorem1))
        self.play(Write(spectralTheorem2))
        self.play(Write(spectralTheorem3))
        self.play(Write(spectralTheorem4))
        self.play(Write(spectralTheorem5))
        self.play(Write(spectralTheorem6))
        self.play(Write(spectralTheoremTex))
        self.wait(1)