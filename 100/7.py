# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array 
# to the end of the array and move non-negative integers to the front by maintaining their order.


# Brute force

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
temp = [0]*len(arr)
j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        temp[j] = arr[i]
        j += 1 
for i in range(len(arr)):
    arr[i] = temp[i]
print(arr)


# Optimal 

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

i, j = 0, len(arr) - 1
while i < j:
    if arr[i] == 0:
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
        i += 1
    else:
        i += 1

print(arr)

# 

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr) 