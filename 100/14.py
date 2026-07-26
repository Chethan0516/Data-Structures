# Two Sum : Check if a pair with given sum exists in Array

arr = [2,6,5,8,11]
target = 14
# arr = [2,6,5,8,11]
# target = 15

# Brute force T: O(N2)

j = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == target:
            print("True")
            print(i, j)


# Better T: O(N), S: O(N)

seen = {}
for i in range(len(arr)):
    value = target - arr[i]
    if value in seen:
        print("res")
        print(value, arr[i], end='')
    seen[arr[i]] = i
print(seen)


# or

seen = {}
for key, value in enumerate(arr):
    num = target - value
    if num in seen:
        print(key, seen[num])
    seen[value] = key
