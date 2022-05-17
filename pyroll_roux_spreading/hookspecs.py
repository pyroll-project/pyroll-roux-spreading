from pyroll.core import RollPass


@RollPass.hookspec
def equivalent_height_change(roll_pass):
    """Height change for equivalent rectangle of the roll pass"""


@RollPass.hookspec
def roux_parameter_a(roll_pass):
    """Gets the Roux spreading model parameter A."""


@RollPass.hookspec
def roux_parameter_b(roll_pass):
    """Gets the Roux spreading model parameter B."""
