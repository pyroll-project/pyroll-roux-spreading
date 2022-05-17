import logging
from pathlib import Path

import pytest

import pyroll.core
import pyroll.ui
from pyroll.ui.reporter import Reporter

THIS_DIR = Path(__file__).parent


def test_solve(tmp_path: Path, caplog):
    import pyroll.ui.cli.res.input_trio as input_py
    import pyroll.roux_spreading

    caplog.set_level(logging.DEBUG, logger="roux_spreading")

    sequence = input_py.sequence

    pyroll.core.solve(sequence, input_py.in_profile)

    report = pyroll.ui.Reporter().render(input_trio.sequence)

    rendered = report.render(sequence)
    print()

    report_file = tmp_path / "report.html"
    report_file.write_text(rendered)
    print(report_file)

    print("\nLog:")
    print(caplog.text)
