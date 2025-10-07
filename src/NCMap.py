class NCMap:
    def __init__(self, func, list):
        self.func = func
        self.list = list
        self.index = 0

        print(self.func)
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        try:
            result = self.func(self.list[self.index])
            self.index +=1
            return result
        except IndexError:
            raise StopIteration












def demo():
    pass

e = NCMap(demo, ['a', 'b', 'c', 'd'])