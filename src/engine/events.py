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
    """
    Base class for all execution trace events.

    An Event represents a single, atomic fact about an algorithm's execution.
    Subclasses define the specific type of action (e.g., comparison, swap).

    Events contain no behavior and are interpreted by the Player.
    """
    pass

@dataclass(frozen=True)
class Compare(Event):
    """
    Indicates that two elements were compared.

    Attributes:
        i (int): Index of the first element.
        j (int): Index of the second element.
    """
    i: int
    j: int

@dataclass(frozen=True)
class Swap(Event):
    """
    Indicates that two elements were swapped.

    Attributes:
        i (int): Index of the first element.
        j (int): Index of the second element.
    """
    i: int
    j: int

@dataclass(frozen=True)
class SetPointer(Event):
    """
    Sets or moves a named pointer to a specific index.

    These "pointers" are defined only by the algorithm and is
    interpreted by the Player and Renderer.

    Attributes:
        name (str): Name of the pointer.
        location (int): Target location:
                            - index of arrays
                            - node id for graphs or trees
    """
    name: int
    location: int