def frequent_int(array):
    count = {}
    for i in array:
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1
    maximum = max(count, key=count.get)
    return (maximum, count[maximum])    

if __name__ == "__main__":
    array  = [2, 6, 2, 7, 6, 5, 4, 4, 4, 2, 6, 7, 7, 2, 6, 5, 10, 10, 5]
    result = frequent_int(array)
    print(result)