# ~/typical/src/typical/aliases/calls.py
"""
Type aliases for callables, functions, and signatures.
"""
from __future__ import annotations
import typing as t

from typical.aliases.variants import Signature

## callable types (primitives) ##

type Sync[R] = t.Callable[..., R]
"""Synchronous callable returning R."""

type Async[R] = t.Callable[..., t.Awaitable[R]]
"""Asynchronous callable returning Awaitable[R]."""

type Call[R] = Sync[R] | Async[R]
"""Either synchronous or asynchronous callable returning R."""


## composed from primitives ##

type Factory[T] = Call[T]
"""Factory that produces instances of T (sync or async)."""

type Predicate[T] = Call[bool]
"""Callable that takes T and returns boolean (sync or async)."""

type Decorator[T: Call] = Sync[T]
"""Decorator that returns a callable (may take the callable directly or additional args first)."""
