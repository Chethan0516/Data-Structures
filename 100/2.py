# Problem Statement: Given an array, find the second smallest and second largest element in the array. 
# Print ‘-1’ in the event that either of them doesn’t exist.

def second_largest(arr):
    if len(arr) < 2: return arr
    first = second = float('-inf')
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    return second

def second_smallest(arr):
    if len(arr) < 2: return arr
    first = second = float('inf')
    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i] != first:
            second = arr[i]
    return second

if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]
    print(second_largest(arr))
    print(second_smallest(arr))