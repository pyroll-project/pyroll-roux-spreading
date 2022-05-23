import logging
import numpy as np
from pyroll.core import RollPass


@RollPass.hookimpl
def equivalent_height_change(roll_pass: RollPass):
    return roll_pass.in_profile.equivalent_rectangle.height - roll_pass.out_profile.equivalent_rectangle.height


@RollPass.hookimpl
def roux_parameter_a(roll_pass: RollPass):
    return (1 + 5 * (0.35 - roll_pass.equivalent_height_change / roll_pass.in_profile.equivalent_rectangle.height) ** 2) * np.sqrt(
        roll_pass.in_profile.equivalent_rectangle.height / roll_pass.equivalent_height_change - 1)


@RollPass.hookimpl
def roux_parameter_b(roll_pass: RollPass):
    return (roll_pass.in_profile.equivalent_rectangle.width / roll_pass.in_profile.equivalent_rectangle.height - 1) * (
            roll_pass.in_profile.equivalent_rectangle.width / roll_pass.in_profile.equivalent_rectangle.width) ** (2 / 3)


@RollPass.hookimpl
def spread(roll_pass: RollPass):
    log = logging.getLogger(__name__)

    first_factor = (roll_pass.in_profile.equivalent_rectangle.height - roll_pass.out_profile.equivalent_rectangle.height)

    second_factor = 1 / ((1 - roll_pass.equivalent_height_change / roll_pass.in_profile.equivalent_rectangle.height) + (3 * roll_pass.roux_parameter_a) / (
            (2 * roll_pass.roll.working_radius) / roll_pass.in_profile.equivalent_rectangle.height) ** (3 / 4))

    third_factor = (roll_pass.in_profile.equivalent_rectangle.width / roll_pass.in_profile.equivalent_rectangle.height) / (
            1 + 0.57 * roll_pass.roux_parameter_b)

    spread = 1 + (first_factor * second_factor * third_factor) / roll_pass.in_profile.equivalent_rectangle.width

    log.debug(f"Spread after Marini spreading model: {spread}.")

    return spread
