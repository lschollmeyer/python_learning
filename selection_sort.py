
from sort_objects import benchmark

class selection_sort():
    def __init__(self, name="Selection Sort"):
        self.name=name

    def sort(self, arr):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if(arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]

        return arr
if __name__=="__main__":
    ss = selection_sort()
    results = benchmark(ss, n=[10, 100, 1000, 10000])
    print(results)