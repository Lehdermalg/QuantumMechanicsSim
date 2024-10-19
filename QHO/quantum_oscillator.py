import numpy as np
from manim import ThreeDScene, Scene, Create, Transform
from manim import FunctionGraph, ParametricFunction, Line, VGroup
from manim import ThreeDAxes, Axes, Dot
from manim import WHITE, YELLOW, BLUE, RED, GRAY
from manim import UP, DOWN, DEGREES


class QuantumHarmonicOscillator(ThreeDScene):
    def construct(self):

        # 00. Add XYZ axes
        # tda = ThreeDAxes()
        self.set_(theta=0, phi=30 * DEGREES)

        # 01. Add XZ axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE}
        )
        origin = axes.c2p(0, 0)
        origin_dot = Dot(origin, color=RED)
        # self.play(Create(axes))

        # 02.1 Define the potential function V(x)
        def potential(x):
            return 0.5 * x**2  # Dimensionless units

        # 02.2 Create the potential function graph
        potential_graph = FunctionGraph(
            potential,
            x_range=[-3, 3, 0.01],  # Adjust range as needed
            color=GRAY
        )
        # self.play(Create(potential_graph))

        # 03.1 Define the wavefunction
        def wavefunction(_x, _t):
            n = 0  # Ground state for now
            # Hermite polynomial (using scipy for convenience)
            from scipy.special import hermite
            Hn = hermite(n)
            norm = (1 / (np.pi**(1/4) *
                         np.sqrt(2**n *
                                 np.math.factorial(n))))
            psi = (norm *
                   Hn(_x) *
                   np.exp(-_x**2 / 2) *
                   np.exp(-1j * (n + 0.5) * _t))
            return psi

        # 03.2 Calculate energy levels
        energy_levels = [0.5 + n for n in range(3)]  # First 3 energy levels

        # 03.3 Create energy level indicators
        energy_level_lines = [
            Line(
                start=np.array([-3, energy_level, 0]),
                end=np.array([3, energy_level, 0]),
                color=YELLOW
            )
            for energy_level in energy_levels
        ]
        # self.play(*[Create(line) for line in energy_level_lines])

        # 04.1 Create the wavefunction visualization (shifted to the ground state energy level)
        wavefunction_graph_R = ParametricFunction(
            lambda _: np.array([_,
                                wavefunction(_, 0).real + energy_levels[0],
                                0]),
            t_range=np.array([-3, 3, 0.01]),
            color=BLUE
        )
        wavefunction_graph_I = ParametricFunction(
            lambda _: np.array([_,
                                wavefunction(_, 0).imag + energy_levels[0],
                                0]),
            t_range=np.array([-3, 3, 0.01]),
            color=RED
        )
        # self.play(Create(wavefunction_graph))

        # 04.2 Group the potential graph and energy level lines
        wf_group = VGroup(axes,
                          potential_graph,
                          *energy_level_lines,
                          wavefunction_graph_R,
                          wavefunction_graph_I).move_to(origin_dot)

        # 04.3 Play the animations
        self.play(Create(wf_group))  # Move to origin

        # 04.4. Animate the wavefunction evolution (in the XZ projection)
        # Calculate the period of the ground state wavefunction
        period = 2 * np.pi / (0 + 0.5)
        # for t in np.arange(0, period, 0.1):
        for t in np.arange(0, period, 0.1):
            wavefunction_graph_Rt = ParametricFunction(
                lambda _: np.array([_,
                                    wavefunction(_, t).real + energy_levels[0],
                                    0]),
                t_range=np.array([-3, 3, 0.01]),
                color=BLUE
            ).move_to(origin_dot)
            wavefunction_graph_It = ParametricFunction(
                lambda _: np.array([_,
                                    wavefunction(_, t).imag + energy_levels[0],
                                    0]),
                t_range=np.array([-3, 3, 0.01]),
                color=RED
            ).move_to(origin_dot)
            self.play(Transform(wavefunction_graph_R, wavefunction_graph_Rt),
                      Transform(wavefunction_graph_I, wavefunction_graph_It),
                      run_time=0.1)

        # self.interactive_embed()
        self.wait()


if __name__ == "__main__":
    scene = QuantumHarmonicOscillator()
    scene.render()
