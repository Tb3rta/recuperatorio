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
        j = self.indice(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error:" + repr(k))
        return self._table[j]._value


    def __setitem__(self, k: Any, v: Any) -> None:
        j = self.indice(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            # reassign value
            self._table[j]._value = v
        else:
            # adds new item
            self._table.insert(j, self._Item(k, v))

    
    def __delitem__(self, k: Any) -> None:
        j = self.indice(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)


    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key

    
    def iter_items(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item



    def indice(self, k, bajo, alto):
        if alto < bajo:
            return alto + 1
        else:
            media = (bajo + alto) // 2
            if k == self._table[media]._key:
                return media
            elif k < self._table[media]._key:
                return self.indice(k, bajo, media - 1)
            else:
                return self.indice(k, bajo + 1, alto)
    