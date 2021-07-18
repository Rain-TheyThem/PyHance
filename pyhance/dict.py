class dictionary(dict):
    """
    A custom dictionary class with all of the method from the built-in data type dict, while adding additional methods
    """
    def __init__(self, key_value_pairs):
        self.d = dict(key_value_pairs)

    def key_at(self, index):
        """
        A method for indexing into the keys of the dictionary (finding the key at the specified index)
        """
        if type(index) != int:
            raise TypeError(
                f"index parameter was expecting int, {type(index)} when was passed"
            )
        if index < 0:
            index = len(self.d)
        for key_index, key in enumerate(self.d.keys()):
            if key_index == index:
                return key
        raise IndexError("dictionary index out of range")

    def value_at(self, index):
        """
        A method for indexing into the values of the dictionary (finding the value at the specified index)
        """
        if type(index) != int:
            raise TypeError(
                f"index parameter was expecting int, {type(index)} when was passed"
            )
        if index < 0:
            index = len(self.d)
        for value_index, value in enumerate(self.d.values()):
            if value_index == index:
                return value
        raise IndexError("dictionary index out of range")

    def item_at(self, index):
        """
        A method for indexing into the key-value pairs of the dictionary (finding the key-value pair at the specified index)
        """
        if type(index) != int:
            raise TypeError(
                f"index parameter was expecting int, {type(index)} when was passed"
            )
        if index < 0:
            index = len(self.d)
        for item_index, key in enumerate(self.d.keys()):
            if item_index == index:
                return {key: self.d[key]}
        raise IndexError("dictionary index out of range")

    def key_index(self, key):
        """
        A method for getting the index of a key
        """
        for key_index, current_key in enumerate(self.d.keys()):
            if current_key == key:
                return key_index
        raise ValueError(f"'{key}'' not in dictionary")

    def value_index(self, value):
        """
        A method for getting the index of a value
        """
        for value_index, current_key in enumerate(self.d.values()):
            if current_key == value:
                return value_index
        raise ValueError(f"'{value}' not in dictionary")

    def item_index(self, item):
        """
        A method for getting the index of a key
        """
        for item_index, current_key in enumerate(self.d.items()):
            if {current_key[0]: self.d[current_key[0]]} == item:
                return item_index
        raise ValueError(f"'{item}' not in dictionary")
