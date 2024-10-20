import numpy as np
from manim import ThreeDScene, Create, Transform
from manim import FunctionGraph, ParametricFunction, Line, VGroup, NumberPlane
from manim import ThreeDAxes, Axes, Dot
from manim import WHITE, YELLOW, RED, GREEN, BLUE, GRAY
from manim import UP, DOWN, DEGREES

from scene_methods import (prepare_grid, prepare_axes, prepare_camera, prepare_potential_graph,
                           energy_levels, prepare_energy_levels)

class QuantumHarmonicOscillator(ThreeDScene):
    def construct(self):

        # 00. Configure the camera
        prepare_camera(self)

        # 01. Add XYZ axes and a grid - aligned on the same point.
        axes = prepare_axes()
        origin = axes.c2p(0, 0, 0)
        grid = prepare_grid(origin)

        # origin_dot = Dot(origin, color=RED)

        # 02. Create the potential function graph V(x)
        potential_graph = prepare_potential_graph(origin)

        # 03.2 Calculate energy levels
        energy_level_lines = prepare_energy_levels(origin)
        self.play(Create(axes), Create(grid), Create(potential_graph), *[Create(line) for line in energy_level_lines])
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
