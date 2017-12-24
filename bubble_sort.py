"""
https://en.wikipedia.org/wiki/Bubble_sort

"""
from sort_objects import benchmark, create_array

class bubble_sort(object):
    def __init__(self, name="Bubble Sort"):
        self.name = name

    def sort(self, arr):
        swapped=True
        while swapped:
            swapped=False
            for i in range(1,len(arr)):
                if arr[i-1]>arr[i]:
                    arr[i], arr[i-1]=arr[i-1], arr[i]
                    swapped=True
        return arr

bs = bubble_sort()

benchmark(bs, n=[10, 100, 1000, 10000])
