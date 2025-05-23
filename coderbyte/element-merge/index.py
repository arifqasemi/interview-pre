def ElementMerger(arr):
    while len(arr) > 1:
        arr =[abs(arr[i+1] -arr[i]) for i in range(len(arr)-1)]
    print(arr[0])

# Test case
print(ElementMerger([4, 5, 1, 2, 7])) 
