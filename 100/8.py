# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array 
# or not. If present print the index of the element or print -1.

arr = [1, 2, 3, 4, 5]
num = 3

i, j = 0, len(arr) - 1
while i < j:
    if arr[i] + arr[j] == num:
        print(i, j)
        break
    elif arr[i] + arr[j] > num:
        j -= 1
    elif arr[i] + arr[j] < num:
        i += 1

