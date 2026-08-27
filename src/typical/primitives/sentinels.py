# ~/typical/src/typical/primitives/sentinels.py
"""
Sentinel values for unambiguous missing/empty markers.
"""
from __future__ import annotations
import typing as t


class Sentinel:
    """
    Unique marker value distinct from None, False, 0, etc.

    Usage:
        MISSING = Sentinel('MISSING')
        UNSET = Sentinel('UNSET')

        if value is MISSING: ...
    """
    __slots__ = ('_name',)

    def __init__(self, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return self._name

    def __str__(self) -> str:
        return self._name

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return hash(self._name)

    def __eq__(self, other: t.Any) -> bool:
        return (self is other)

    def __copy__(self) -> 'Sentinel':
        return self

    def __deepcopy__(self, memo: dict) -> 'Sentinel':
        return self


class Unset(Sentinel): pass
class Missing(Sentinel): pass
class NotApplicable(Sentinel): pass

UNSET = Unset('UNSET')
MISSING = Missing('MISSING')
NOTAPPLICABLE = NotApplicable('NOTAPPLICABLE')
NA = NOTAPPLICABLE
