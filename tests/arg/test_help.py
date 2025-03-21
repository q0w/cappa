from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Union

import cappa
import pytest
from cappa.output import Exit
from typing_extensions import Annotated

from tests.utils import parse


@pytest.mark.help
def test_explicit_parse_function(capsys):
    @dataclass
    class ArgTest:
        numbers: Annotated[int, cappa.Arg(parse=int, help="example")]

    with pytest.raises(Exit):
        parse(ArgTest, "--help")

    stdout = capsys.readouterr().out
    assert "numbers     example" in stdout


@pytest.mark.help
def test_choices_in_help(capsys):
    @dataclass
    class ArgTest:
        numbers: Annotated[
            Union[Literal[1], Literal[2]], cappa.Arg(parse=int, help="example")
        ]

    result = parse(ArgTest, "1")
    assert result == ArgTest(1)

    with pytest.raises(Exit):
        parse(ArgTest, "--help")

    stdout = capsys.readouterr().out
    assert "Valid options: 1, 2" in stdout
