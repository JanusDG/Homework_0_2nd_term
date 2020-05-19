class Node:
    """ Class For node representation """
    __slots__ = "_data", "_next", "_key"
    def __init__(self, key, data, next_item=None):
        """ (Node, anyType, anyType, Node/NoneType) -> NoneType
        Create new Node
        """
        self._key = key
        self._data = data
        self._next = next_item

    def _data_node(self):
        """ (Node) -> anyType
        Return the data of Node
        """
        return self._data

    def __str__(self):
        """ (Node) -> str
        Return the string representation of Node
        """
        return f"{self._data}"    
    
class Dictionary:
    """ Class for dictionary ADT representation """
    def __init__(self):
        """ (Dictionary) -> NoneType
        Create new Dictionary
        """
        self._head = None

    def _add(self, key, value):
        """ (Dictionary, anyType, anyType) -> NoneType
        adds item into the
        begginning of the sequence
        """
        if self._head == None:
            self._head = Node(None, None)
            self._head._next = Node( key, value)
        else:
            temp = self._head._next 
            self._head._next = Node(key,value)
            self._head._next._next = temp
    
    @property
    def keys(self):
        """ (Dictionary) -> list
        property for keys
        """
        return [item._key for item in self]
    
    @property
    def values(self):
        """ (Dictionary) -> list
        property for values
        """
        return [item._data for item in self]

    @property
    def items(self):
        """ (Dictionary) -> list
        property for items
        """
        return [(item._key, item._data) for item in self]

    def remove(self):
        """ (Dictionary) -> anyType
        removes the first item in a sequence
        """
        if self._head == None:
            return None
        removed = self._head._data
        self._head = self._head._next
        return removed 

    def __len__(self):
        """ (Dictionary) -> int
        returns the lenght of multiset
        """
        i = 0
        if self._head is None:
            return 0

        current = self._head._next
        if current == None:
            return 0
        while current._data is not None:
            i += 1
            if current._next:
                current = current._next
            else:
                break
        return i

    def __eq__(self, other):
        """ (Dictionary, Dictionary) -> bool
        the eq() method
        if self and other is Dictionary 
        with the same values returns True
        else - False
        """
        if not isinstance(other, Dictionary):
            raise TypeError
        if len(self) != len(other):
            return False
        ind1 = 0
        for item1 in self:
            ind2 = 0
            for item2 in other:
                if ind1 == ind2 and item1._data == item2._data:
                    ind2 += 1
                    continue
                if ind1 == ind2 and item1._data != item2._data:
                    return False
                ind2 += 1
            ind1 += 1
        return True

    def __iter__(self):
        """ (Dictionary) -> Dictionary
        enables iteration in multiset
        the exapmle of iter() was taken from 
        https://www.programiz.com/python-programming/iterator
        """
        self.n = 1
        self.cur = self._head
        return self

    def __next__(self):
        """
        generator in multiset
        """
        if self.n <= len(self):
            self.cur = self.cur._next
            result = self.cur
            self.n += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        """ (Dictionary, anyType) -> anyType
        Return the value for this key
        """
        for item in self:
            if item._key == key:
                return item._data_node()

    def __setitem__(self, key, value):
        """ (Dictionary, anyType, anyType) -> NoneType
        Set the value for this key
        """
        if key not in self.keys:
            self._add(key,value)
        else:
            for item in self:
                if item._key == key:
                    item._data = value

    def __str__(self):
        """ (Dictionary) -> str
        Return the string representation of Dictionary
        """
        rez = "{"
        for item in self:
            key_str = value_str = ''
            if isinstance(item._key, str):
                key_str += '"'
            if isinstance(item._data, str):
                value_str += '"'
            rez += key_str + str(item._key) + key_str + ": "
            rez += value_str + str(item) + value_str + ", "
        rez = rez[:-2]
        rez += "}"
        return rez
