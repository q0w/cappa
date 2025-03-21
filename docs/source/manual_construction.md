# Manual Construction

The general intention of the library is that you use the inference system to
produce the most natural mapping between the source class definition and the
output CLI.

However, there's nothing preventing the manual construction of the command
definition, which allows one to completely decouple the CLI-specific annotations
from the class in question, if much more manually.

```python
from dataclasses import dataclass

import cappa
from cappa.annotation import parse_list


@dataclass
class Foo:
    bar: str
    baz: list[int]


command = cappa.Command(
    Foo,
    arguments=[
        cappa.Arg(name="bar", parse=str),
        cappa.Arg(name="baz", parse=parse_list(int), num_args=-1),
    ],
    help="Short help.",
    description="Long description.",
)


result = cappa.parse(command, argv=["one", "2", "3"])
# result == Foo(bar="one", baz=[2, 3])
```

There are a number of built-in parser functions used to build up the existing
inference system. [parse_value](cappa.annotation.parse_value) the the main
entrypoint used by cappa internally, but each of the parser factory functions
below make up the component built-in parsers for each type.

For inherent types, like `int`, `float`, etc. Their constructor may serve as
their own parser.

```{eval-rst}
.. autoapimodule:: cappa.annotation
   :members: parse_value, parse_list, parse_tuple, parse_literal, parse_none, parse_set, parse_union
```
