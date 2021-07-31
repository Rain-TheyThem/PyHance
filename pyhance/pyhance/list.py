class list_(list):
    def __init__(self, contents):
        self.li = list(contents)

    def __repr__(self):
        return str(self.li)

    def remove_all(self, item):
        """
        A method to remove all occurences of an item in the list
        """
        self.li = [citem for citem in self.li if citem != item]
