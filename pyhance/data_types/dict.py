class dictionary(dict):
    def __init__(self, key_value_pairs):
        self.d = dict(key_value_pairs)

    def key_at(self, index):
        if index < 0:
            index = len(self.d)
        for key_index, key in enumerate(self.d.keys()):
            if key_index == index:
                return key
        raise IndexError("dictionary index out of range")

    def value_at(self, index):
        if index < 0:
            index = len(self.d)
        for value_index, value in enumerate(self.d.values()):
            if value_index == index:
                return value
        raise IndexError("dictionary index out of range")

    def item_at(self, index):
        if index < 0:
            index = len(self.d)
        for item_index, key in enumerate(self.d.keys()):
            if item_index == index:
                return {key: self.d[key]}
        raise IndexError("dictionary index out of range")
    
    def index_of_key(self, key):
        for key_index, current_key in enumerate(self.d.keys()):
            if current_key == key:
                return key_index
        raise IndexError("dictionary index out of range")
    
    def index_of_value(self, value):
        for value_index, current_key in enumerate(self.d.values()):
            if current_key == value:
                return value_index
        raise IndexError("dictionary index out of range")
    
    def index_of_item(self, item):
        for item_index, current_key in enumerate(self.d.items()):
            if current_key == item:
                return item_index
        raise IndexError("dictionary index out of range")