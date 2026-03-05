# ~/typical/src/typical/utils/overloads.py
"""
Utilities for organizing overloaded function definitions.

Provides helpers for managing multiple variant definitions of functions,
methods, and decorators under the same name for type checker support.
"""
from __future__ import annotations
import typing as t

from typical.logs import log
from typical.aliases import Call, Decorator
from typical.utils.intro import extract, asynchronous, synchronous

class __overloader:
    """
    Meta-decorator that adds overload support to any decorator.

    Takes a decorator/router and returns a new decorator that:
    1. Applies the original decorator's logic
    2. Marks functions as overloads for type checkers

    Usage:
        def my_router(hint):
            def decorator(fn):
                # registration logic
                return fn
            return decorator

        route = overloader(my_router)

        @route(int)
        def handler(x: int): ...

        @route(str)
        def handler(x: str): ...
    """
    def __init__(self, o: Call) -> None:
        self.o = o

    def __call__(self, *args, **kwargs) -> Call:
        od = self.o(*args, **kwargs)
        def rt(fn: Call) -> Call:
            return t.overload(od(fn))
        return rt

overloader = __overloader

if __name__ == "__main__":
    def typerouter(hint: type):
        """Simple router that registers handlers by type"""
        def decorator(fn: Call) -> Call:
            # In real impl: register fn for this type hint
            # For demo: just return fn
            print(f"Registered {fn.__name__} for type {hint}")
            return fn
        return decorator

    route = overloader(typerouter)

    @route(int)
    def x(a: int): pass

    @route(str)
    def x(a: str): pass
