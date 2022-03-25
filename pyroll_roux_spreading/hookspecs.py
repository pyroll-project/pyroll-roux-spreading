import sys

from pyroll import RollPass


@RollPass.hookspec
def roux_parameter_c1(roll_pass):
    """Gets the Roux spreading model parameter c1."""


@RollPass.hookspec
def roux_parameter_c2(roll_pass):
    """Gets the Roux spreading model parameter c2."""


RollPass.plugin_manager.add_hookspecs(sys.modules[__name__])
