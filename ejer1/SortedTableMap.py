from SorteTableMapAbstract import ABC
from typing import Any, List,Generator
from python_ed_fcad_uner.data_structures import MapBase
class SortedTableMap(MapBase,ABC):
    
    def __init__(self) -> None:
        self._table: List[MapBase._Item] = []
    
    def __len__(self) -> int:
        return len(self._table)
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        res = ", ".join([str(x) for x in self.iter_items()])
        return f"UnsortedTableMap({res})"

    
    def __getitem__(self, k: Any) -> Any:
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))


    def __setitem__(self, k: Any, v: Any) -> None:
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    
    def __delitem__(self, k: Any) -> None:
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)


    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key

    
    def iter_items(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item

    