from __future__ import annotations

import re
from dataclasses import dataclass

import cappa
import pytest
from typing_extensions import Annotated

from tests.utils import backends, parse


@dataclass
class Foo:
    ...


@dataclass
class Args:
    subcommand: Annotated[Foo, cappa.Subcommand(group="Yup")]


@backends
def test_required_missing(backend, capsys):
    with pytest.raises(cappa.Exit) as e:
        parse(Args, "--help", backend=backend)
    assert e.value.code == 0

    help = capsys.readouterr().out
    assert re.match(r".*Yup:?[\n\s]+\{foo\}.*", help, re.DOTALL)
