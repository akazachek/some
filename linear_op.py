from manim import *
import numpy as np

# https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html
# https://docs.manim.community/en/stable/examples.html

def set_matrix_color(M):
    for bra in M.get_brackets():
        bra.set_color(BLACK)
    for e in M.get_entries():
        e.set_color(BLACK)


class linop(Scene):
    def construct(self):
        # Construct Mobjects
        self.camera.background_color = "#ece6e2"

        eqn3 = MathTex( "A", r"(a\vec{v}_1 + b\vec{v}_2) =  ","a","A","\\vec{v}_1 +","b","A","\\vec{v}_2" , color=BLACK  )
        eqn3_trans = MathTex( "T", r"(a\vec{v}_1 + b\vec{v}_2) =  ","a","T","\\vec{v}_1 +","b","T","\\vec{v}_2" , color=BLACK  )

        eqn1 = MathTex( "\\vec{v}"," = a","\\vec{e_1}"," + b ","\\vec{e_2}",color = BLACK )
        eqn1.set_color_by_tex("\\vec{e_", RED)

        eqn2 = MathTex(" T(","\\vec{v}",") = aT(","\\vec{e_1}",") + bT(","\\vec{e_2}",") ", color=BLACK)
        eqn2.set_color_by_tex("\\vec{e_", RED)

        self.play(Write( eqn3 ))
        self.wait()
        self.play(
            TransformMatchingTex(eqn3, eqn3_trans)
        )
        self.wait()
        self.play(FadeOut(eqn3_trans))
        self.play(Write(eqn1))
        self.wait()
        self.play(TransformMatchingTex(eqn1, eqn2))
        self.wait()
        self.play(
            Unwrite(eqn2)
        )
