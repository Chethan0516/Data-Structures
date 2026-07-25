# Problem Statement: Given an integer array nums, rotate the array to the left by one.

# Brute T:O(N) S:O(N)

arr = [1, 2, 3, 4, 5] 
num = [0]*len(arr) 

for i in range(1, len(arr)):
    num[i-1] = arr[i]
num[len(arr)-1] = arr[0]
print(num)

# Optimal T:O(N) S:O(1)

arr = [1, 2, 3, 4, 5] 
temp = arr[0]
for i in range(1, len(arr)):
    arr[i-1] = arr[i]
arr[len(arr)-1] = temp
print(arr)