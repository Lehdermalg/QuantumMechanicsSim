from typing import Optional

import numpy as np
from manim import NumberPlane, ThreeDAxes, FunctionGraph, GRAY, UP, ThreeDScene, RIGHT, LEFT, DOWN
from manim import RED, GREEN, BLUE
from manim import DEGREES


def prepare_camera(scene: ThreeDScene):
    scene.set_camera_orientation(
        phi=20 * DEGREES,
        gamma=0 * DEGREES,
        theta=20 * DEGREES
    )
    scene.move_camera(frame_center=[4, -2, 6])


def prepare_axes() -> ThreeDAxes:
    _axes = ThreeDAxes(
        x_range=[-5, 6, 1],
        y_range=[-1, 9, 1],
        z_range=[0, 6, 1],
        x_length=11,
        y_length=11,
        z_length=6,
        axis_config={
            "include_numbers": True,
        },
        x_axis_config={"color": RED, "stroke_width": 2},
        y_axis_config={"color": GREEN, "stroke_width": 2},
        z_axis_config={"color": BLUE, "stroke_width": 2},
    )
    # _axes.get_axis_labels(x_label='x', y_label='y', z_label='z')
    return _axes


def prepare_grid(origin_point: Optional[np.ndarray] = None) -> NumberPlane:
    _grid = NumberPlane(
        x_range=[-5, 15, 1],
        y_range=[-2, 9, 1],
        x_length=20,
        y_length=12,
        background_line_style={
        "stroke_color": BLUE,
        "stroke_width": 1,
        "stroke_opacity": 0.4
        },
    )
    if origin_point is not None:
        _grid.move_to(origin_point)
        _B = _grid.c2p(0, 0, 0)
        _grid.shift(LEFT * (_B - origin_point)[0])
        _grid.shift(DOWN * (_B - origin_point)[1])

    return _grid


def potential(x):
    return 0.5 * x ** 2  # Dimensionless units


def prepare_potential_graph(origin_point: Optional[np.ndarray] = None) -> FunctionGraph:
    # 02.2 Create the potential function graph
    _potential_graph = FunctionGraph(
        potential,
        x_range=[-4, 4, 0.01],  # Adjust range as needed
        color=GRAY
    )
    if origin_point is not None:
        _potential_graph.move_to(origin_point)
        _top, _bottom = _potential_graph.get_top(), _potential_graph.get_bottom()
        _potential_graph.shift(UP * 0.5 * (_top - _bottom))

    return _potential_graph
