# ~/typical/src/typical/utils/lit.py
"""
Utilities for working with Literal types at runtime.

Provides tools to convert Literal type definitions into runtime collections
and perform operations on Literal types like union, exclusion, and containment checks.
"""
from __future__ import annotations
import typing as t

from typical.logs import log
from typical.aliases import (
    LiteralType, Literally
)

class __literally:
    """
    Utility for converting Literal types to runtime collections.

    Extracts literal values from type definitions and converts them into
    standard Python collections (set, list, tuple, frozenset).

    Usage:
        Letter = Literal['a', 'b', 'c']
        letters_set: set = literally.set(Letter)
        letters_list: list = literally.list(Letter)
    """

    def to(self, lit: LiteralType, target: type):
        """
        Convert a Literal type to a runtime collection.

        Args:
            lit: A Literal type to extract values from
            target: Collection type to convert to

        Returns:
            Collection of the literal values

        Raises:
            ValueError: If target is not a callable type
        """
        if not callable(target): raise ValueError(f"target must be callable, got {target}")
        if not isinstance(target, type): raise ValueError(f"target must be a type, got {target}")
        return target(t.get_args(lit))

    def __call__(self, lit: LiteralType, target: type = list):
        """Convenience method - calls to() with default target=list."""
        return self.to(lit=lit, target=target)

    def set(self, lit: LiteralType) -> set[Literally]:
        """Convert Literal type to set of values."""
        return self.to(lit=lit, target=set)

    def list(self, lit: LiteralType) -> list[Literally]:
        """Convert Literal type to list of values."""
        return self.to(lit=lit, target=list)

    def tuple(self, lit: LiteralType) -> tuple[Literally]:
        """Convert Literal type to tuple of values."""
        return self.to(lit=lit, target=tuple)

    def frozenset(self, lit: LiteralType) -> frozenset[Literally]:
        """Convert Literal type to frozenset of values."""
        return self.to(lit=lit, target=frozenset)


literally = __literally()


class __literal:
    """
    Utilities for manipulating and inspecting Literal types.

    Provides operations for working with Literal type definitions including
    counting values, checking containment, combining literals, and excluding values.
    """

    def count(self, lit: LiteralType) -> int:
        """
        Count the number of values in a Literal type.

        Args:
            lit: A Literal type

        Returns:
            Number of literal values
        """
        return len(literally(lit))

    def contains(self, value: t.Any, lit: LiteralType) -> bool:
        """
        Check if a value exists in a Literal type.

        Args:
            value: Value to check for
            lit: A Literal type to check against

        Returns:
            True if value is in the literal, False otherwise
        """
        return value in literally(lit)

    def iterator(self, lit: LiteralType) -> t.Iterator[LiteralType]:
        """
        Iterate over values in a Literal type.

        Args:
            lit: A Literal type

        Yields:
            Each literal value
        """
        for l in literally(lit):
            yield l

    def union(self, *lits: LiteralType) -> tuple[Literally, ...]:
        """
        Combine values from multiple Literal types.

        Returns tuple of all unique values preserving order.
        Can be unpacked to create a new Literal type.

        Args:
            *lits: Variable number of Literal types to combine

        Returns:
            Tuple of unique values from all literals

        Usage:
            L1 = Literal['a', 'b']
            L2 = Literal['c', 'd']
            combined = literal.union(L1, L2)  # ('a', 'b', 'c', 'd')
        """
        # Flatten all literal values, use dict.fromkeys to dedupe while preserving order
        return tuple(dict.fromkeys([v for lit in lits for v in literally(lit)]))

    def exclude(self, lit: LiteralType, *exclusions: t.Any) -> tuple[Literally, ...]:
        """
        Remove specific values from a Literal type.

        Returns tuple of remaining values.

        Args:
            lit: A Literal type to filter
            *exclusions: Values to exclude

        Returns:
            Tuple of values not in exclusions

        Usage:
            Letter = Literal['a', 'b', 'c', 'd']
            remaining = literal.exclude(Letter, 'a', 'c')  # ('b', 'd')
        """
        # Convert exclusions to set for O(1) lookup
        return tuple(v for v in literally(lit) if v not in set(exclusions))


literal = __literal()
