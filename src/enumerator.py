class NCEnumerate:
    def __init__(self, lst, start=0):
        
        self.iterable = lst
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        output = self.start, self.iterable[self.start]
        self.start += 1
        return output
        







# def enumerates(iterable, start=0):
#     n = start
#     for elem in iterable:
#         yield n, elem
#         n += 1

# list = ['a','b','c']

# item = enumerates(list, start=1)
# print(next(item))
# print(next(item))