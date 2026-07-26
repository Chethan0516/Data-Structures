# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. 
# Find the union of two sorted arrays.

# The union of two arrays can be defined as the common and distinct elements in the two arrays.


# Approach: Map 
n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]

freq = {}
for i in range(n):
    freq[arr1[i]] = freq.get(arr1[i], 0) + 1
for i in range(m):
    freq[arr2[i]] = freq.get(arr2[i], 0) + 1
print(freq)
values = sorted(freq.keys())
print(values)

# Approach: set
n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]

seen = set()
for i in range(n):
    if arr1[i] not in seen:
        seen.add(arr1[i])
for i in range(m):
    if arr2[i] not in seen:
        seen.add(arr2[i])
print(seen)

# Approach: set
n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]

values = set(arr1) | set(arr2)
print(values)

# Optimal T:O(M+N) S:O(M+N)
n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]



# Optimal T:O(M+N) S:O(M+N)
n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]

temp = [0]*(m+n)

i = j =0
z = 0
while i < m and j < n:
    if arr1[i] < arr2[j]:
        temp[z] = arr1[i]
        i += 1
    else:
        temp[z] = arr2[j]
        j += 1

    z += 1
while i < m:
    temp[z] = arr1[i]
    z += 1
    i += 1
while j < n:
    temp[z] = arr2[j]
    z += 1
    j += 1

print(temp)