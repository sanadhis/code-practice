def binary_search(array,value):
    print(array)
    n = len(array)
    mid = int(n/2)
    if value == array[mid]:
        return mid
    
    if value > array[mid]:
        return binary_search(array[mid:],value)
    else:
        return binary_search(array[0:mid],value)

if __name__ == "__main__":
    array = [42, 5, 81, 25, 44, 90, 49, 22, 96, 62, 86, 77, 27, 37, 73, 28, 85, 60, 56]
    sorted_array = sorted(array)
    
    value = 77
    print(sorted_array)

    res = binary_search(sorted_array,value)

    print(res)