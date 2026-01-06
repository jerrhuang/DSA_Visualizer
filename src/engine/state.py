"""
Visualization state definitions.

This module defines the data model representing the current snapshot of what
should be drawn by the renderer at any point in time.

VizState is updated by the Player as it applies Events, and it is read by the
Renderer/UI to draw the visualization. This module must remain UI-agnostic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

@dataclass
class VizState:
    """
    Current visualization snapshot for array-based algorithms.

    This class stores only the information needed to render the visualization
    at a given step. It is intentionally generic so it can be reused across
    different algorithms (sorting, searching, two-pointers, sliding window).

    Attributes:
        values:
            The current list of values being visualized. This is the "data"
            that bars/boxes represent on screen.

        highlights:
            Indices that should be visually emphasized at the current step
            (e.g., two elements being compared, a selected pivot, etc.).

        pointers:
            Named pointers to indices in `values`. The algorithm defines pointer
            names (e.g., "L", "R", "mid", "i", "j"), and the renderer displays
            them generically.

        active_range:
            Optional inclusive range (l, r) that indicates the algorithm's
            current focus region within `values` (e.g., binary search bounds,
            quicksort partition range). If None, no range is emphasized.

        labels:
            Optional per-index tags that describe special roles for elements
            (e.g., "sorted", "pivot", "min"). Renderers may map these to colors
            or icons. Multiple labels per index are allowed.
        
         message:
            Optional human-readable description of the current step, suitable
            for an event log panel (e.g., "Compare i=2 and j=3").
    """
    
    values: List[int] = field(default_factory=list)
    highlights: Set[int] = field(default_factory=set)
    pointers: Dict[str, int] = field(default_factory=dict)
    active_range: Optional[Tuple[int, int]] = None
    labels: Dict[int, Set[str]] = field(default_factory=dict)
    message: Optional[str] = None