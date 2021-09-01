def linearSearch(array, seekValue, compareCallback):
    result = []
    for idx in range(len(array)):
        if compareCallback(array[idx], seekValue) == 0 :
            result.append(idx)
    return result

