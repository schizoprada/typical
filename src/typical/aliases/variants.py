# ~/typical/src/typical/aliases/variants.py
"""
Type variable definitions and groupings for generic type hints.

Provides both standalone and grouped TypeVars for common typing patterns.
Grouped variants (e.g., Pair.K, Pair.V) signal related usage and improve
auto-completion while reducing namespace pollution.
"""
from __future__ import annotations
import typing as t


## basic/universal ##

T = t.TypeVar('T')
"""Generic type variable for single-type generics."""

N = t.TypeVar('N', int, float, complex)
"""Numeric type variable constrained to numeric types."""


## collections/pairings/mappings ##

class Pair:
    """Type variables for key-value pairs (dicts, mappings, etc)."""
    K = t.TypeVar('K')  # Key
    V = t.TypeVar('V')  # Value


## containers ##

class Container:
    """Type variables for container types with variadic element types."""
    TS = t.TypeVarTuple('TS')
    """Variadic type variable for homogeneous or heterogeneous sequences."""


class Sequential:
    """Type variables for sequential container element types."""
    S = t.TypeVar('S')  # Sequential element type
    """Element type for sequences (lists, tuples, etc). Distinct from T to avoid ambiguity."""


## callables & signatures ##

class Signature:
    """Type variables for callable signatures and function types."""
    P = t.ParamSpec('P')  # Parameters
    R = t.TypeVar('R')    # Return type


## variance ##
class Variance:
    """Covariant and contravariant type variables for variance-aware generics."""
    Co = t.TypeVar('Co', covariant=True)
    Contra = t.TypeVar('Contra', contravariant=True)
