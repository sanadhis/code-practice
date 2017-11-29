def reverse_string(string):
    char_arr   = list(string)
    new_string = []
    for _ in range(len(char_arr)):
        new_string.append(char_arr.pop())
    
    return "".join(new_string)

if __name__ == "__main__":
    test_string  = "Hello world it's me"
    result       = reverse_string(test_string)

    print(result)