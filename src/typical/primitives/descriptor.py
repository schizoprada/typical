# ~/typical/src/typical/primitives/descriptor.py
from __future__ import annotations
import typing as t

from typical.logs import log

B = t.TypeVar('B')
R = t.TypeVar('R')

class Descriptor(t.Generic[B, R]):
    """
    Base descriptor with typed access.

    Provides __get__, __set_name__ machinery.
    Subclasses implement __access__ for instance-level resolution.
    """
    __ref__: B
    __term__: str = "" # label / key / attr / etc
    __owner__: t.Optional[type]

    def __access__(self, obj: t.Any, **kwargs) -> R:
        raise NotImplementedError("Subclasses of Descriptor must implement __access__")

    def __new__(cls, ref: B, *args, **kwargs) -> t.Self:
        d = super().__new__(cls)
        d.__ref__ = ref
        return d

    def __set_name__(self, own: type, name: str) -> None:
        log.debug(f"(Descriptor.__set_name__) {own.__name__}.{name}")
        self.__term__ = name
        self.__owner__ = own

    @t.overload
    def __get__(self, o: None, ot: type) -> t.Self: ...
    @t.overload
    def __get__(self, o: t.Any, ot: type) -> R: ...
    def __get__(self, o, ot=None):
        if o is None: return self
        return self.__access__(o, )

class __descr:
    def ref(self, d: Descriptor) -> B: return d.__ref__
    def term(self, d: Descriptor) -> str: return d.__term__
    def owned(self, d: Descriptor) -> bool: return (d.__owner__ is not None)
    def owner(self, d: Descriptor) -> t.Optional[type]: return d.__owner__
    def accessible(self, d: Descriptor) -> bool:
        try:
            d.__access__(None)
            return True
        except NotImplementedError:
            return False
descr = __descr()
