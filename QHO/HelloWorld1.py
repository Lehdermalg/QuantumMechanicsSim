from manim import *


class HelloWorld(Scene):
    def construct(self):
        # Add some simple geometry
        circle = Circle()
        square = Square()

        text = Text("Hello World", font_size=72)
        text2 = Text("If you learn math and programming, you'll do THIS!", font_size=36)
        text.to_edge(UP)

        self.add(circle, square)
        self.play(Write(text, run_time=3))
        self.play(Transform(text[4], circle, run_time=5))
        self.play(Transform(text, text2, run_time=5))

        square.to_edge(UP)


if __name__ == "__main__":
    scene = HelloWorld()
    scene.render()
