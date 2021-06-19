class string(str):
    def __init__(self, string):
        self.s = str(string)
    
    def __repr__(self):
        return self.s
    
    def remove(self, string):
        self.s = self.s.replace(string, "")
        return self.s
    
    def copy(self):
        newstr = ""
        return newstr.join(self.s)
