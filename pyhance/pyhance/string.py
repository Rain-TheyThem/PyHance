class string(str):
    """
    A custom string class that keeps all of the methods of the built-in str class, while providing additional functionality.
    """
    def __init__(self, string):
        self.s = str(string)

    def __repr__(self):
        return self.s

    def remove(self, string, maxremovals=-1):
        return self.s.replace(string, "", maxremovals)
    
    def reverse(self):
        return self.s[::-1]

    def copy(self):
        newstr = ""
        return newstr.join(self.s)
