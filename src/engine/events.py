"""
Event definitions for algorithm execution tracing.

This module defines the Event hierarchy used to record what happened
during an algorithm's execution, independent of visualization or UI.

Events are:
- Immutable
- Ordered
- Interpreted by a Player to update VizState
- Rendered separately by a Renderer

Algorithms emit Events.
Events do not contain rendering, timing, or UI logic.
"""

from dataclasses import dataclass

class Event:
    pass

@dataclass(frozen=True)
class Compare(Event):
    i: int
    j: int

@dataclass(frozen=True)
class Swap(Event):
    i: int
    j: int

@dataclass(frozen=True)
class SetPointer(Event):
    name: int
    index: int