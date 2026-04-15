from manim import *

# Basic scene - every animation is a Scene class
class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))


# Shapes and transformations
class Shapes(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED).shift(RIGHT * 2)

        self.play(Create(circle), Create(square))
        self.wait(0.5)

        # Transform circle into square
        self.play(Transform(circle, square))
        self.wait(1)


# Math equations
class MathExample(Scene):
    def construct(self):
        eq1 = MathTex(r"e^{i\pi} + 1 = 0")
        eq2 = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")

        self.play(Write(eq1))
        self.wait(1)
        self.play(eq1.animate.shift(UP * 2))
        self.play(Write(eq2))
        self.wait(2)


# Graph/function plotting
class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1, 5],
            axis_config={"include_numbers": True}
        )

        graph = axes.plot(lambda x: x**2, color=YELLOW)
        label = axes.get_graph_label(graph, label="x^2")

        self.play(Create(axes))
        self.play(Create(graph), Write(label))
        self.wait(2)


# Moving objects
class Movement(Scene):
    def construct(self):
        dot = Dot(color=RED)

        self.play(Create(dot))
        self.play(dot.animate.shift(RIGHT * 3))
        self.play(dot.animate.shift(UP * 2))
        self.play(dot.animate.move_to(ORIGIN))
        self.wait(1)
