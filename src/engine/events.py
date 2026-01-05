from dataclasses import dataclass

class Event:
    pass

@dataclass
class Compare(Event):
    i: int
    j: int

@dataclass
class Swap(Event):
    i: int
    j: int

@dataclass
class SetPointer(Event):
    name: int
    index: int