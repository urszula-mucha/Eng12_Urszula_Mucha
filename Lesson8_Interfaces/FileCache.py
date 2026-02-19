class FileCache:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.cache = {}

    #If cache doesn't contain a character then add it
    def readchar(self, position):
        if position not in self.cache:
            self.fp.seek(position)
            self.cache[position] = self.fp.read(1)