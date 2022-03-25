import sys

import numpy as np
from pyroll import RollPass


@RollPass.hookimpl
def roux_parameter_c1(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    out_equivalent_height = roll_pass.ideal_out_profile.equivalent_rectangle.height
    equivalent_height_change = in_equivalent_height - out_equivalent_height

    return (1 + 5 * (0.35 - equivalent_height_change / in_equivalent_height) ** 2) * np.sqrt(
        in_equivalent_height / equivalent_height_change - 1)


@RollPass.hookimpl
def roux_parameter_c2(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    in_equivalent_width = roll_pass.in_profile.equivalent_rectangle.width

    return (in_equivalent_width / in_equivalent_height - 1) * (in_equivalent_width / in_equivalent_width) ** (2 / 3)


@RollPass.hookimpl
def width_change(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    out_equivalent_height = roll_pass.ideal_out_profile.equivalent_rectangle.height
    equivalent_height_change = in_equivalent_height - out_equivalent_height

    in_equivalent_width = roll_pass.in_profile.equivalent_rectangle.width

    out_equivalent_width = in_equivalent_width + (in_equivalent_height - out_equivalent_height) * 1 / (
            (1 - equivalent_height_change / in_equivalent_height) + (3 * roll_pass.roux_parameter_c1) / (
            2 * roll_pass.roll_radius / in_equivalent_height) ** (3 / 4)) * (in_equivalent_width / in_equivalent_height) / (
        1 + 0.57 * roll_pass.roux_parameter_c2)

    out_profile_width = (out_equivalent_width * roll_pass.ideal_out_profile.height
                         / roll_pass.ideal_out_profile.equivalent_rectangle.height)

    width_change = out_profile_width - roll_pass.in_profile.rotated.width

    return width_change


RollPass.plugin_manager.register(sys.modules[__name__])
