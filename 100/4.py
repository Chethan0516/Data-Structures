# Problem Statement: Given an integer array sorted in non-decreasing order, 
# remove the duplicates in place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, 
# then the first k elements of the array should hold the final result. 
# It doesn't matter what you leave beyond the first k elements.


# Brute

arr = [1,1,2,2,2,3,3]
seen = set()
index = 0
for i in range(len(arr)):
    if arr[i] not in seen:
        seen.add(arr[i])
        arr[index] = arr[i]
        index += 1
print(seen)
print(arr[:index])



# Optimal
arr = [1,1,2,2,2,3,3]
l = 1
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        arr[l] = arr[i]
        l += 1
        
print(arr[:l])

