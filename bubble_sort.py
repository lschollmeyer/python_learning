from random import randint

def create_array(length=10, maxint=100):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

#a = create_array()

def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i], arr[i-1]=arr[i-1], arr[i]
                swapped=True
    return arr

a = create_array()
print(a)
print(bubble_sort(a))
assert bubble_sort(a) == sorted(a)
#print(a)