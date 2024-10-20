from manim import NumberPlane, ThreeDAxes
from manim import RED, GREEN, BLUE


def prepare_grid() -> NumberPlane:
    return NumberPlane(
        x_range=[-5, 5, 1],
        y_range=[-5, 5, 1],
        x_length=10,
        y_length=10,
        background_line_style={
            "stroke_color": BLUE,
            "stroke_width": 1,
            "stroke_opacity": 0.4
        },
    )


def prepare_axes() -> ThreeDAxes:
    _axes = ThreeDAxes(
        x_range=[-5, 6, 1],
        y_range=[-5, 6, 1],
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