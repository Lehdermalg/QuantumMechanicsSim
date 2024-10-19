from manim import *
from manim.opengl import *


class OpenGLScene(Scene):
    def construct(self):
        hello_world = Text("Hello World")
        self.play(Write(hello_world))
        # self.play(
        #     self.camera.animate.set_euler_angles(
        #         theta=-10*DEGREES,
        #         phi=50*DEGREES
        #     )
        # )
        self.play(FadeOut(hello_world))

        # Adjust the camera position for better viewing
        # self.camera.set_euler_angles(phi=70 * DEGREES, theta=-30 * DEGREES)

        surface = OpenGLSurface(
            lambda u, v: (u, v, u*np.sin(v) + v*np.cos(u)),
            u_range=(-3, 3),
            v_range=(-3, 3),
        )
        surface_mesh = OpenGLSurfaceMesh(surface)

        self.add(surface_mesh)
        self.play(Create(surface_mesh))
        self.play(FadeTransform(surface_mesh, surface, run_time=5))


if __name__ == "__main__":
    scene = OpenGLScene()
    scene.render()
