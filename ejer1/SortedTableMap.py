from SorteTableMapAbstract import ABC
class SortedTableMap(ABC,mapbase):
    
    def __init__(self) -> None:
        """ Crea la lista Python donde se almacenarán todas las entradas como una lista
        vacía. """
        self._table : List[MapBase._Item] = []
    
    def __len__(self) -> int:
        """ Devuelve la cantidad de entradas en el Mapeo.
        Returns:
        int: devuelve la longitud de la lista self._table
        """
        return len(self._table)
    
    def __repr__(self) -> str:
        """ Convierte en str el Mapeo.
        Returns:
        str: Convierte en str el Mapeo invocando a self.__str__()
        """
        return str(self)
    
    def __str__(self) -> str:
        """ Convierte en str el Mapeo.
        Returns:
        str: Concatena la versión en str de todas las entradas del Mapeo.
        """
        pass
    
    def __getitem__(self, k: Any) -> Any:
        """ Devuelve el valor asociado a la clave k en el Mapeo.
        Args:
        k (Any): clave del ítem que hay que buscar.
        Raises:
        KeyError: Arroia KeyError cuando la clave no pertenece al Mapeo.
        Returns:
        Any: Devuelve el _value del ítem cuya clave coincide con k.
        """
        i= self._find_index(k, 0, len(self._table) - 1)
        if i== len(self._table) or self._table[i]._key != k:
            raise KeyError('Key Error:' + repr(k))
        return self._table[i]._value

    def __setitem__(self, k: Any, v: Any) -> None:
        """ Establece como v como el nuevo valor del ítem con clave k.
        Args:
        k (Any): clave que se va a buscar en el mapeo.
        v (Any): valor para asignar al ítem con clave que k.
        """
        i = self._find_index(k, 0, len(self._table) - 1)
        if i < len(self._table) and self._table[i]._key == k:
            # reassign value
            self._table[i]._value = v
        else:
            # adds new item
            self._table.insert(i, self._Item(k, v))

    

    
    def __delitem__(self, k: Any) -> None:
        """ Elimina del Mapeo el ítem con clave k.
        Args:
        k (Any): clave que se va a buscar en los ítems del Mapeo.
        Raises:
        KeyError: Es arroiado cuando la clave k no se encuentra en el mapeo.
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        # delete item
        self._table.pop(j)

    

    
    def __iter__(self) -> Generator[Any, None, None]:
        """ Devuelve un generator sobre el Mapeo que devuelve todas las claves.
        Yields:
        Generator[Any, None, None]: devuelve todas las claves del Mapeo.
        """

    pass

    
    def iter_items(self) -> Generator[Any, None, None]:
        """ Devuelve un generator sobre el Mapeo que devuelve todos los ítems.
        Yields:
        Generator[Any, None, None]: devuelve todas los ítems del Mapeo.
        """

    pass