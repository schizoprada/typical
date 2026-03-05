# ~/typical/src/typical/utils/intro.py
from __future__ import annotations
import inspect, typing as t

from typical.logs import log
from typical.aliases import (
    Call, Sync, Async
)

def asynchronous(fn: Call) -> bool: return inspect.iscoroutinefunction(fn)
def synchronous(fn: Call) -> bool: return (not asynchronous(fn))

class __extract:
    """Extract components from callables."""

    def call(self, obj: t.Any) -> t.Optional[Call]:
        """Extract callable from object (handles bound methods, etc)."""
        if callable(obj): return obj
        if hasattr(obj, '__call__'): return obj.__call__
        return None

    def hints(self, fn: Call, returns: bool = True) -> dict[str, t.Any]:
        """Get type hints for callable (resolves forward refs)."""
        if not returns:
            return {k:v for k,v in t.get_type_hints(fn).items() if k != 'return'}
        return t.get_type_hints(fn)

    def signature(self, fn: Call) -> inspect.Signature:
        """Get signature object from callable."""
        return inspect.signature(fn)

    def params(self, fn: Call) -> dict[str, inspect.Parameter]:
        """Extract parameters as dict mapping name -> Parameter."""
        return dict(self.signature(fn).parameters)

    def returned(self, fn: Call) -> t.Any:
        sig = self.signature(fn)
        if sig.return_annotation == inspect.Signature.empty:
            return None
        return sig.return_annotation
extract = __extract()


def ispredicate(fn: t.Any, strict: bool = False) -> bool:
    if not callable(fn): return False
    if (ret:=extract.returned(fn)) is None: return (not strict) # strict=True -> False / strict=False -> True
    if (ret is bool): return True
    if (t.get_origin(ret) is t.Awaitable):
        args = t.get_args(ret)
        return (bool(args) and (args[0] is bool))
    return False
