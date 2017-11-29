from multiprocessing import Pool
import math

def match(args1,args2):
    return args1==args2

def chunks(l, n, val):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield (l[i:i + n],val)

def linear_search(zipped):
    array, value = zipped[0], zipped[1]
    iteration = 1
    for idx, val in enumerate(array):
        if match(val,value): 
            break
        iteration +=1  
    return iteration

def split_search(array,value,k):
    chunked = list(chunks(array,k,value))
    pool    = Pool()
    results = pool.map(linear_search, chunked)
    return results

def main():
    original_array = [42, 5, 81, 25, 44, 90, 49, 22, 96, 62, 86, 77, 27, 37, 73, 28, 85, 60, 56]
    
    lin_res = linear_search((original_array,85))
    split_res = split_search(original_array,85,5)

    print("res 1: ", lin_res)
    print("res 2: ", min(split_res) + math.ceil(len(original_array)/5))

if __name__ == "__main__":
    main()