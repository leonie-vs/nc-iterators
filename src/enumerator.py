class NCEnumerate:
    def __init__(self, lst):
        
        self.iterable = lst

    def __iter__(self):
        return self

    def __next__(self):
        # implement me
        pass






# def enumerates(iterable, start=0):
#     n = start
#     for elem in iterable:
#         yield n, elem
#         n += 1

# list = ['a','b','c']

# item = enumerates(list, start=1)
# print(next(item))
# print(next(item))