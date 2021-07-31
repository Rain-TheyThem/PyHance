class dictionary(dict):
    """
    An extension of the built-in dict data type. This class adds methods to:
    - index into the dictionary, with options to return the key, value, or key-value pair at the specified index
    - get the index of an item in the dictionary, with options to return the index of the key, value, or key-value pair specified
    """
    def __init__(self, contents):
        self.c = dict(contents)

    def __repr__(self):
        return str(self.c)

    def item_at(self, index, item_type="key"):
        """
        A method to index into the dictionary, with options to return the key, value, or key-value pair at the specified index.

        Parameters
        ----------
        - index: the index of the key/value/pair you would like to get
        - item_type (defaults to key): the type of item you would like to get. Can be:
            - key
            - value
            - pair
        
        Exceptions
        ----------
        This method throws a TypeError when the type of the index argument isn't int, a ValueError when the dictionary index is out of range, and a ValueError when the item_type argument isn't one of the acceptable values.
        """
        if type(index) != int:
            raise TypeError("Type of argument index must be int")

        if item_type == "key":
            # iterate over a list with the indexes of the keys,
            # and the keys of the dictionary (formatted into a list)
            for item_index, key in enumerate(list(self.c.keys())): 
                # Return the current key if the current index
                # is the same as the index passed in the index argument
                if item_index == index:
                    return key
            # If the index passed to the method is never equal to the index of one of the keys,
            # raise a ValueError because the index isn't in the dictionary
            raise ValueError("dictionary index out of range")

        # If the caller wants to get a value at a specified index
        elif item_type == "value":
            # iterate over a list with the indexes of the values,
            # and the values of the dictionary (formatted into a list)
            for item_index, value in enumerate(list(self.c.values())):
                # Return the current key if the current index
                # is the same as the index passed in the index argument
                if item_index == index:
                    return value
            # If the index passed to the method is never equal to the index of one of the keys,
            # raise a ValueError because the index isn't in the dictionary    
            raise ValueError("dictionary index out of range")

        # If the caller wants to get a value at a specified index
        elif item_type == "pair":
            # iterate over a list with the indexes of the values,
            # and the values of the dictionary (formatted into a list)
            for item_index, key in enumerate(list(self.c.keys())):
                if item_index == index:
                    return {key: self.c[key]}
            # If the index passed to the method is never equal to the index of one of the keys,
            # raise a ValueError because the index isn't in the dictionary
            raise ValueError("dictionary index out of range")
        
        # If item_type isn't one of the acceptable values (key, value, or pair), raise a ValueError
        else:
            raise ValueError(
                "Invalid argument item_type, the value must be key, value or pair."
            )


    def index_of(self, item, item_type="key"):
        """
        A method to get the index of an item in the dictionary, with options to return the index of the key, value, or key-value pair specified.

        Parameters
        ----------
        - item: the item to get the index of
        - item_type (defaults to key): the type of item you would like to get the index of. Can be:
            - key
            - value
            - pair
        
        Exceptions
        ----------
        This method throws a ValueError when the item isn't in the dictionary, and it throws a ValueError when the item_type argument isn't one of the acceptable options.
        """

        if item_type == "key":
            # iterate over a list with the indexes of the keys,
            # and the keys of the dictionary (formatted into a list)
            for index, key in enumerate(list(self.c.keys())):
            # Return the current index if the current key
            # is the same as the key passed in the item argument
                if key == item:
                    return index
            # If the key passed to the method is never equal to one of the keys in the dictionary,
            # raise a ValueError because the key isn't in the dictionary
            raise ValueError("key not in dictionary")

        elif item_type == "value":
            # iterate over a list with the indexes of the values,
            # and the values of the dictionary (formatted into a list)
            for index, value in enumerate(list(self.c.values())):
                # Return the current index if the current value
                # is the same as the value passed in the item argument
                if value == item:
                    return index
            # If the key passed to the method is never equal to one of the keys in the dictionary,
            # raise a ValueError because the key isn't in the dictionary
            raise ValueError("value not in dictionary")

        elif item_type == "pair":
            # iterate over a list with the indexes of the key-value pairs,
            # and the keys of the dictionary (formatted into a list)
            for index, key in enumerate(list(self.c.keys())):
                # Return the current index if the current key-value pair
                # is the same as the pair passed in the item argument
                if {key: self.c[key]} == item:
                    return index
            # If the key-value pair passed to the method is never equal to one of the pairs in the dictionary,
            # raise a ValueError because the pair isn't in the dictionary
            raise ValueError("key-value pair not in dictionary")
        
        # If item_type isn't one of the acceptable values (key, value, or pair), raise a ValueError
        else:
            raise ValueError(
                "Invalid argument item_type, the value must be key, value or pair."
            )
