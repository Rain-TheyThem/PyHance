class string(str):
    def __init__(self, string):
        self.s = str(string)

    def __repr__(self):
        return self.s

    def remove(self, string):
        return self.s.replace(string, "")

    def copy(self):
        newstr = ""
        return newstr.join(self.s)