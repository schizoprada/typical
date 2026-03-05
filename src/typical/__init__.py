"""
typical
"""
__author__ = "Joel Yisrael"
__version__ = "0.0.0"

VERSION = tuple(map(int, __version__.split('.')))

from .aliases import (
    T, N, Pair,
    Container,
    Sequential,
    Signature,
    Variance,
    Sync, Async, Call,
    Factory, Predicate,
    Decorator, LiteralType,
    Literally
)

from .utils import (
    literal, literally,
    extract, ispredicate
)
