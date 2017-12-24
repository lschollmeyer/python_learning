from random import randint

def create_array(length=10, maxint=100):
    new_arr=[randint(0,maxint) for _ in range(length)]
    return new_arr

def benchmark(sort_name, n=[10, 100, 1000, 10000]):
    from time import time
    
    #c_sort=sort_name()

    c_sort_time=[] #compare sort
    sort_base_time=[] #sort baseline
  
    for length in n:
        arr=create_array(length, length)

        time_start=time()
        s=sorted(arr)
        time_stop=time()

        sort_base_time.append(time_stop - time_start)

        time_start=time()
        c=sort_name.sort(arr)
        time_stop=time()

        c_sort_time.append(time_stop - time_start)

    print("n \tBuilt-In\t"+sort_name.name)
    print("_________________________________________________")
    for i, cur_n in enumerate(n):
        print("%d\t%0.7f \t%0.7f"%(cur_n, sort_base_time[i], c_sort_time[i]))