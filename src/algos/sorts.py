"""
Sorting algorithm implementations that emit execution trace events.

This module contains pure sorting algorithms that do NOT perform any
visualization or UI logic. Each algorithm operates on a copy of the
input data and emits a sequence of Events describing what happened
during execution.

Design principles:
- Algorithms are pure and deterministic.
- No algorithm mutates the caller's input.
- Algorithms emit Events instead of directly mutating VizState.
- The returned Event list can be replayed step-by-step by a Player.

All sorting algorithms in this module follow the same interface:
    sort(values: list[int]) -> list[Event]
"""

from typing import List
from engine.events import Event, Compare, Swap

def bubble_sort(values: List[int]) -> List[Event]:
    """
    Bubble sort algorithm with event emission.

    Repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. After each pass,
    the largest remaining element is placed at its correct position
    at the end of the list.

    This function:
    - Operates on a copy of the input list
    - Emits Compare and Swap events
    - Returns an ordered list of Events representing execution

    Args:
        values (List[int]): The input list to be sorted.

    Returns:
        List[Event]: A chronological list of execution trace events.
    """
    events = List[Event]
    arr = values.copy()
    
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            events.append(Compare(j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                events.append(Swap(j, j + 1))
    
    return events

def insertion_sort(values: List[int]) -> List[Event]:
    """
    Insertion sort algorithm with event emission.

    Builds the sorted list one element at a time by inserting each
    new element into its correct position within the already-sorted
    prefix of the list.

    Args:
        values (List[int]): The input list to be sorted.

    Returns:
        List[Event]: A chronological list of execution trace events.
    """
    raise NotImplementedError

def selection_sort(values: List[int]) -> List[Event]:
    """
    Selection sort algorithm with event emission.

    Repeatedly selects the minimum element from the unsorted portion
    of the list and swaps it with the first unsorted element.

    Args:
        values (List[int]): The input list to be sorted.

    Returns:
        List[Event]: A chronological list of execution trace events.
    """
    raise NotImplementedError

def merge_sort(values: List[int]) -> List[Event]:
    """
    Merge sort algorithm with event emission.

    Uses a divide-and-conquer strategy to recursively split the list,
    sort each half, and merge the results.

    Note:
        Merge sort will likely require additional Event types such as
        SetValue or Range events to properly visualize overwrites.

    Args:
        values (List[int]): The input list to be sorted.

    Returns:
        List[Event]: A chronological list of execution trace events.
    """
    raise NotImplementedError