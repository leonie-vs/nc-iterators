class NCEnumerate:
    def __init__(self, lst, start=0):
        
        self.iterable = lst
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        try:
            output = self.start, self.iterable[self.start]
            self.start += 1

        
        except IndexError:
            raise StopIteration
        
        return output
        


