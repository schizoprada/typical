# ~/typical/src/typical/data/serial.py
"""
[DOCSTRING]
"""
from __future__ import annotations
import abc, typing as t

SerialT = t.TypeVar(
    'SerialT',
    int, str, bytes,
    t.Any, list[t.Any],
    dict[str, t.Any],
    default=t.Any
)

class Serializable(abc.ABC, t.Generic[SerialT]):
    """
    [DOCSTRING]
    """
    __slots__ = ()

    @classmethod
    @abc.abstractmethod
    def __deserialize__(cls, data: SerialT, **kwargs) -> t.Self:
        """Reconstruct the class instance from its serialized form."""
        ...

    @abc.abstractmethod
    def __serialize__(self, **kwargs) -> SerialT:
        """Convert the class instance into its serialized form."""
        ...

    @classmethod
    def __serialtype__(cls) -> t.Any:
        """Dynamically inspects the subclass to find its SerializedT target."""
        for base in getattr(cls, "__orig_bases__", []):
            if t.get_origin(base) is Serializable:
                if (args:=t.get_args(base)):
                    return args[0]
        return t.Any
