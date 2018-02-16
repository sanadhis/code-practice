# Complete the function below.

def maxLength(a, k):
    # to keep track of longest phrase
    result          = [0]
    
    # to accumulate character length
    totalCharacters = 0
    
    # to accumulate number of words in phrase
    numberOfWords   = 0
    
    for index in range(len(a)):
        # add the number of characters for each word
        totalCharacters = totalCharacters + a[index]
        if (totalCharacters) <= k:
            # keep track of longest phrase possible
            numberOfWords = numberOfWords + 1
            # last element of result stores the maximum value of longest phrase possible
            result.append(max(numberOfWords,result[-1]))
        else:
            # FIFO, if exceed k, remove from the first element added to total characters
            totalCharacters -= a[index-numberOfWords]
    
    # return maximum length of longest phrase
    return result[-1]       
            
