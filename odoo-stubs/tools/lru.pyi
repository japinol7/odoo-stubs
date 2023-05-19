from collections import OrderedDict
from typing import Any

class LRU:
    count: int
    d: OrderedDict
    def __init__(self, count: int, pairs: tuple[Any, Any] = ...) -> None: ...
    def __contains__(self, obj) -> bool: ...
    def get(self, obj, val: Any | None = ...): ...
    def __getitem__(self, obj): ...
    def __setitem__(self, obj, val) -> None: ...
    def __delitem__(self, obj) -> None: ...
    def __len__(self) -> int: ...
    def pop(self, key): ...
    def clear(self) -> None: ...
