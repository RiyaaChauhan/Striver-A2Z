def leftRotateByOne(arr):
    return arr[1:] + arr[:1]  # Rotate using slicing


'''
or
'''

def leftRotateByOne(arr):
    n = len(arr)
    temp = arr[0]  # Store first element
    for i in range(1, n):
        arr[i - 1] = arr[i]  # Shift left
    arr[-1] = temp  # Place first element at the end
    return arr