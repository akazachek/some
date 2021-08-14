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
        axes = Axes(
            x_range= [-5,5],
            y_range= [-5,5],
            x_length=15,
            y_length=15,
            tips= False,
            axis_config={
                "color":BLACK,
                "include_numbers": True

            }
        )
        for num in axes.get_x_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        for num in axes.get_y_axis().numbers:
            num.set_color(BLACK)
            num.scale(0.7)

        eqn1 = MathTex( "\\vec{v}"," = a","\\vec{e_1}"," + b ","\\vec{e_2}",color = BLACK )
        eqn1.set_color_by_tex("\\vec{e_", RED)

        eqn2 = MathTex(" T(","\\vec{v}",") = aT(","\\vec{e_1}",") + bT(","\\vec{e_2}",") ", color=BLACK)
        eqn2.set_color_by_tex("\\vec{e_", RED)

        v = Vector(axes.c2p(1,1,0), color=GREEN, stroke_width=3.5)
        e1 = Vector(axes.c2p(1, 0, 0), color=RED, stroke_width=3.5)
        e2 = Vector(axes.c2p(0, 1, 0), color=RED, stroke_width=3.5)

        # Animation
        self.play(Write(eqn1))
        self.wait()
        self.play(TransformMatchingTex(eqn1, eqn2))
        self.wait()
        self.play(
            Unwrite(eqn2)
        )
        self.play(
           GrowFromCenter(axes))
        self.wait()
        self.play(Write(v), Write(e1), Write(e2))
        self.wait()
        M1=np.array([[1, 1], [0, -1]])
        M1_inv = np.linalg.inv(M1)
        Ma1 = Matrix( M1).to_corner(LEFT+UP)
        for bra in Ma1.get_brackets():
            bra.set_color(BLACK)
        for e in Ma1.get_entries():
            e.set_color(BLACK)

        M2=np.array([[-1, 0], [2, 1]])
        M2_inv = np.linalg.inv(M2)
        Ma2 = Matrix(M2).to_corner(LEFT + UP)
        for bra in Ma2.get_brackets():
            bra.set_color(BLACK)
        for e in Ma2.get_entries():
            e.set_color(BLACK)

        M = np.array([[1, 1], [0, 1]])
        Ma = Matrix(M).to_corner(LEFT + UP)
        for bra in Ma.get_brackets():
            bra.set_color(BLACK)
        for e in Ma.get_entries():
            e.set_color(BLACK)

        # I = np.linalg.inv(np.matmul(M2,M1))

        new_e1_label = Matrix([[1], [0]]).scale(0.7).next_to(e1, RIGHT + DOWN) #Automate this somehow
        new_e2_label = Matrix([[1], [1]]).scale(0.7).next_to(e2, RIGHT+ UP) #Automate
        for bra in new_e1_label.get_brackets():
            bra.set_color(BLACK)
        for e in new_e1_label.get_entries():
            e.set_color(BLACK)
        for bra in new_e2_label.get_brackets():
            bra.set_color(BLACK)
        for e in new_e2_label.get_entries():
            e.set_color(BLACK)

        self.play(
            axes.animate.apply_matrix( M1),
            e1.animate.apply_matrix(M1),
            e2.animate.apply_matrix(M1),
            v.animate.apply_matrix(M1),
            Write(Ma1)
                  )
        self.wait()
        self.play(
            FadeOut(Ma1),
            axes.animate.apply_matrix(M1_inv),
            e1.animate.apply_matrix(M1_inv),
            e2.animate.apply_matrix(M1_inv),
            v.animate.apply_matrix(M1_inv)
        )
        self.wait()
        self.play(
            Write(Ma2),
            axes.animate.apply_matrix(M2),
            e1.animate.apply_matrix(M2),
            e2.animate.apply_matrix(M2),
            v.animate.apply_matrix(M2)
        )
        self.wait()
        self.play(
            FadeOut(Ma2),
            axes.animate.apply_matrix(M2_inv),
            e1.animate.apply_matrix(M2_inv),
            e2.animate.apply_matrix(M2_inv),
            v.animate.apply_matrix(M2_inv)
        )
        self.wait()
        self.play(FadeOut(v))
        self.play(
            Write(Ma),
            e1.animate.apply_matrix(M),
            e2.animate.apply_matrix(M),
            Write(new_e1_label),
            Write(new_e2_label)
        )
        e1_trans = np.matmul(M,np.array([1,0]))
        e2_trans = np.matmul(M,np.array([0,1]))
        new_cord = e1_trans + e2_trans
        new_v = Vector(axes.c2p(new_cord[0],new_cord[1],0 ), stroke_width=3.5, color=GREEN)
        new_v_label = Matrix( [[2],[1]]).scale(0.7).next_to(new_v,UP+RIGHT)

        for bra in new_v_label.get_brackets():
            bra.set_color(BLACK)
        for e in new_v_label.get_entries():
            e.set_color(BLACK)

        self.wait()
        self.play(
            Write(new_v),
            Write(new_v_label)
        )

        self.wait()
        self.play(
            FadeOut(axes),
            FadeOut( e1 ),
            FadeOut(e2),
            FadeOut(new_v)
        )
        self.wait()
        self.play(
            Ma.animate.move_to([0,0,0])
        )
        self.play(
            Ma.get_columns()[0].animate.set_color([PURE_RED, YELLOW_C])
        )
        self.play(
            new_e1_label.animate.move_to(Ma.get_columns()[0]), run_time=1
        )
        self.play(
            FadeOut(new_e1_label), run_time=0.5
        )
        self.wait()
        self.play(
            Ma.get_columns()[0].animate.set_color(BLACK),
            Ma.get_columns()[1].animate.set_color([PURE_RED, YELLOW_C])
        )
        self.play(
            new_e2_label.animate.move_to(Ma.get_columns()[1]), run_time=1
        )
        self.play(
            FadeOut(new_e2_label), run_time=0.5
        )

        v_label = Matrix([[1],[1]])
        for bra in v_label.get_brackets():
            bra.set_color(BLACK)
        for e in v_label.get_entries():
            e.set_color(BLACK)


        eqn3 = VGroup( Ma,v_label.to_corner(DOWN+LEFT),MathTex("=",color=BLACK).to_corner(UP+RIGHT), new_v_label )
        self.play(
            FadeIn( eqn3[1] ),
            FadeIn( eqn3[2] ),
            new_v_label.animate.scale(1 / 0.7),
            Ma.get_columns()[1].animate.set_color(BLACK),
        )
        self.play(
            eqn3.animate.arrange()
        )

        self.wait()