import sys

from pyroll import RollPass


@RollPass.hookspec
def friction_coefficient(roll_pass):
    """Gets the friction coefficient."""

@RollPass.hookspec
def marini_parameter_a(roll_pass):
    """Gets the Marini spreading model parameter a."""


@RollPass.hookspec
def marini_parameter_b(roll_pass):
    """Gets the Marini spreading model parameter b."""


RollPass.plugin_manager.add_hookspecs(sys.modules[__name__])
