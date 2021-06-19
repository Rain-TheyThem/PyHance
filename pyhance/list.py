class list_(list):
    def __init__(self, contents):
        self.li = list(contents)
    def __repr__(self):
        return str(self.li)
    def remove_all(self, item):
        self.li = [citem for citem in self.li if citem != item]
