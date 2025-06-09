def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        left = i -1
        while left >= 0 and arr[left] > current:
            arr[left + 1] = arr[left]
            left -= 1
        
        arr[left +1] = current

    return arr
nums = [4,2,1,3]

print(insertionSort(nums)) 