import math

def jumpSearch(sortedArray, seekElement, compareCallback):
    if len(sortedArray) == 0:
        return -1
    
    jumpSize = math.floor(math.sqrt(len(sortedArray)))
    
    blockStart, blockEnd = 0, jumpSize
    
    while(compareCallback(seekElement, sortedArray[min(blockEnd, len(sortedArray)) - 1]) > 0):
        blockStart, blockEnd = blockEnd, blockEnd + jumpSize
        if blockStart > len(sortedArray):
            return -1 
    
    for idx in range(blockStart, len(sortedArray)):
        if compareCallback(seekElement, sortedArray[idx]) == 0:
            return idx

    return -1