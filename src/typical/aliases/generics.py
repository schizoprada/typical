# ~/typical/src/typical/aliases/generics.py
"""
Generic type aliases and parameterized type utilities.
"""
from __future__ import annotations
import typing as t

## literal types ##
LiteralType = type[t.Literal]
_LT = t.TypeVarTuple('_LT')

type Literally = t.Literal[*_LT]  # type: ignore
"""
Type alias for variadic Literal types.

Allows extracting literal values at runtime via typing.get_args().
"""
