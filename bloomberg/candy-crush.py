def candy_crush(string):
    char_pointer = string[0]
    result_string = ""
    counter = 1
    for c in string[1:]:
        if not c == char_pointer:
            result_string += char_pointer
            char_pointer = c
        else:
            counter += 1
        
        if counter == 3:
            counter = 1
            char_pointer = ""

    result_string += counter * c
    print(result_string)

def main():
    candy_strings = ["ABAAAC","BBBCA","AAAABC","EEEEE"]
    for string in candy_strings:
        candy_crush(string)

if __name__ == "__main__":
    main()