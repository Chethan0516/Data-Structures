# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.


# T: O(N2), S: O(1)

arr = [4, 1, 2, 1, 2]

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        print(arr[i])

# T, S = O(N)
arr = [2,2, 2,1,1, 4]

seen = {}
for i in range(len(arr)):
    seen[arr[i]] = seen.get(arr[i], 0) + 1
print(seen)
for x, y in seen.items():
    if y == 1:
        print(x)

print(seen.keys())
print(seen.values())

# Optimal T: O(N) S: O(1)

arr = [4, 1, 2, 1, 2]

xor = 0
for i in arr:
    xor ^= i
print(xor)