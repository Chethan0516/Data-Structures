# Problem Statement: Given an array of size n, 
# write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) 
# order or not. If the array is sorted then return True, Else return False.

# Brute force

def sort_check(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    res = sort_check(arr)
    print(res)

# Optimal

def quick_sort(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    res = sort_check(arr)
    print(res)