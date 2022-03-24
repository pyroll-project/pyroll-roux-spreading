import sys

import numpy as np
from pyroll import RollPass


@RollPass.hookimpl
def friction_coefficient(roll_pass):
    return 0.35


@RollPass.hookimpl
def marini_parameter_a(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    out_equivalent_height = roll_pass.ideal_out_profile.equivalent_rectangle.height
    equivalent_height_change = in_equivalent_height - out_equivalent_height

    return np.sqrt(equivalent_height_change) / (2 * roll_pass.friction_coefficient * roll_pass.roll_radius)


@RollPass.hookimpl
def marini_parameter_b(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    out_equivalent_height = roll_pass.ideal_out_profile.equivalent_rectangle.height
    equivalent_height_change = in_equivalent_height - out_equivalent_height

    return np.sqrt(equivalent_height_change / roll_pass.roll_radius)


@RollPass.hookimpl
def width_change(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    out_equivalent_height = roll_pass.ideal_out_profile.equivalent_rectangle.height
    equivalent_height_change = in_equivalent_height - out_equivalent_height

    in_equivalent_width = roll_pass.in_profile.equivalent_rectangle.width

    out_equivalent_width = in_equivalent_width + \
                           (2 * equivalent_height_change * in_equivalent_width * (roll_pass.roll_radius - in_equivalent_height / 2)
                            * roll_pass.marini_parameter_b) / \
                           (in_equivalent_height * in_equivalent_width + (in_equivalent_width * (in_equivalent_height + out_equivalent_height) / 2 *
                                                                          (1 + roll_pass.marini_parameter_a) / (1 - roll_pass.marini_parameter_a)) *
                            (0.91 * (in_equivalent_width + 3 * in_equivalent_height)) / (4 * in_equivalent_height) +
                            2 * out_equivalent_height * roll_pass.roll_radius * roll_pass.marini_parameter_b)

    out_profile_width = (out_equivalent_width * roll_pass.ideal_out_profile.height
                         / roll_pass.ideal_out_profile.equivalent_rectangle.height)

    width_change = out_profile_width - roll_pass.in_profile.rotated.width

    return width_change


RollPass.plugin_manager.register(sys.modules[__name__])
