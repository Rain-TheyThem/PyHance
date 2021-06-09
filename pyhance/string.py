class string(str):
    def __init__(self, string):
        self.s = str(string)
    def remove(self, string):
        self.s = self.s.replace(string, "")
        return self.s
    def __repr__(self):
        return self.s