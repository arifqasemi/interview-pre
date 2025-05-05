def LargestFour(arr):
    arr.sort(reverse=True)
    return sum(arr[:4])
