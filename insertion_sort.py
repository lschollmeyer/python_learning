from sort_objects import benchmark, create_array

class insertion_sort():
    def __init__(self, name="Insertion Sort"):
        self.name=name

    def sort(self, arr):
        #we start loop at second element (index 1) since the first item is already sorted
        for j in range(1,len(arr)):
            key = arr[j] #The next item we are going to insert into the sorted section of the array

            i = j-1 #the last item we are going to compare to
            #now we keep moving the key back as long as it is smaller than the last item in the array
            while (i > -1) and key < arr[i]: #if i == -1 means that this key belongs at the start
                arr[i+1]=arr[i] #move the last object compared one step ahead to make room for key
                i=i-1 #observe the next item for next time.
            #okay i is not greater than key means key belongs at i+1
            arr[i+1] = key
        return arr

if __name__=="__main__":
    ins=insertion_sort()
    result=benchmark(ins, n=[10, 100, 1000, 10000])
    print(result)