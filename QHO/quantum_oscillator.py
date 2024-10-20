import numpy as np
from manim import ThreeDScene, Scene, Create, Transform
from manim import FunctionGraph, ParametricFunction, Line, VGroup, NumberPlane
from manim import ThreeDAxes, Axes, Dot
from manim import WHITE, YELLOW, RED, GREEN, BLUE, GRAY
from manim import UP, DOWN, DEGREES

from scene_methods import prepare_grid, prepare_axes

class QuantumHarmonicOscillator(ThreeDScene):
    def construct(self):

        # 00. Add XYZ axes
        # tda = ThreeDAxes()
        if True:
            self.set_camera_orientation(
                phi=30 * DEGREES,
                gamma=0 * DEGREES,
                theta=-60 * DEGREES
            )

        # 01. Add XYZ axes and a grid - aligned on the same point.
        grid = prepare_grid()
        axes = prepare_axes()

        origin = axes.c2p(0, 0, 0)
        grid.move_to(origin)
        self.play(Create(axes), Create(grid))
        # origin_dot = Dot(origin, color=RED)

        # # 02.1 Define the potential function V(x)
        # def potential(x):
        #     return 0.5 * x**2  # Dimensionless units
        #
        # # 02.2 Create the potential function graph
        # potential_graph = FunctionGraph(
        #     potential,
        #     x_range=[-3, 3, 0.01],  # Adjust range as needed
        #     color=GRAY
        # ).rotate_about_origin(90 * DEGREES)
        # # self.play(Create(potential_graph))
        #
        # # 03.1 Define the wavefunction
        # def wavefunction(_x, _t):
        #     n = 0  # Ground state for now
        #     # Hermite polynomial (using scipy for convenience)
        #     from scipy.special import hermite
        #     Hn = hermite(n)
        #     norm = (1 / (np.pi**(1/4) *
        #                  np.sqrt(2**n *
        #                          np.math.factorial(n))))
        #     psi = (norm *
        #            Hn(_x) *
        #            np.exp(-_x**2 / 2) *
        #            np.exp(-1j * (n + 0.5) * _t))
        #     return psi
        #
        # # 03.2 Calculate energy levels
        # energy_levels = [0.5 + n for n in range(3)]  # First 3 energy levels
        #
        # # 03.3 Create energy level indicators
        # energy_level_lines = [
        #     Line(
        #         start=np.array([-3, energy_level, 0]),
        #         end=np.array([3, energy_level, 0]),
        #         color=YELLOW
        #     )
        #     for energy_level in energy_levels
        # ]
        # # self.play(*[Create(line) for line in energy_level_lines])
        #
        # # 04.1 Create the wavefunction visualization (shifted to the ground state energy level)
        # wavefunction_graph = ParametricFunction(
        #     lambda _: np.array([wavefunction(_, 0).real + energy_levels[0],
        #                         _,
        #                         0]),
        #                         # wavefunction(_, 0).imag]),
        #     t_range=np.array([-3, 3, 0.01]),
        #     color=BLUE
        # )
        # # self.play(Create(wavefunction_graph))
        #
        # # 04.2 Group the potential graph and energy level lines
        # wf_group = VGroup(axes,
        #                   potential_graph,
        #                   *energy_level_lines,
        #                   wavefunction_graph).move_to(origin_dot)
        #
        # # 04.3 Play the animations
        # self.play(Create(wf_group))
        #
        # # 04.4. Animate the wavefunction evolution (in the XZ projection)
        # # Calculate the period of the ground state wavefunction
        # period = 360 * DEGREES
        # # for t in np.arange(0, period, 0.1):
        # for t in np.arange(0, 3.60, 0.20):
        #     wavefunction_graph_t = ParametricFunction(
        #         lambda _: np.array([wavefunction(_, t).real + energy_levels[0],
        #                             _,
        #                             0]),
        #                             # wavefunction(_, t).imag + energy_levels[0]]),
        #         t_range=np.array([-3, 3, 0.01]),
        #         color=BLUE
        #     ).move_to(wavefunction_graph)
        #     self.play(Transform(wavefunction_graph, wavefunction_graph_t),
        #               run_time=0.1)
        #     self.set_camera_orientation(
        #         gamma=0 * DEGREES,
        #         phi=-30 * DEGREES,
        #         theta=0 * DEGREES
        #     )

        self.interactive_embed()
        self.wait()


if __name__ == "__main__":
    scene = QuantumHarmonicOscillator()
    scene.render()
