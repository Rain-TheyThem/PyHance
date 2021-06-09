class list_(list):
    def __init__(self, contents):
        self.li = list(contents)
    def __repr__(self):
        return str(self.li)
    def index_of(self, item):
        for index in range(len(self.li)):
            if self.li[index] == item:
                return index
        raise ValueError("Item not in list")