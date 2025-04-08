from sys import stdin

def linearSearch(arr, n, val):
    for i in range(n):
        if arr[i] == val:
            return i
    return -1