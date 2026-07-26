# Sort an array of 0s, 1s and 2s

# T:O(N), S: O(1)
arr = [1, 0, 2, 1, 0]

zero = one = two = 0
for n in arr:
    if n == 0:
        zero += 1
    elif n == 1:
        one += 1
    else:
        two += 1

index = 0 
for i in range(zero):
    arr[index] = 0
    index += 1
for i in range(one):
    arr[index] = 1
    index += 1
for i in range(two):
    arr[index] = 2
    index += 1
print(arr)

# optimal O(N), S:O(1)

arr = [1, 0, 2, 1, 0]

l, m, h = 0, 0, len(arr) - 1
while m <= h:
    if arr[m] == 0:
        arr[m], arr[l] = arr[l], arr[m]
        l += 1
        m += 1
    elif arr[m] == 1:
        m += 1
    else:
        arr[m], arr[h] = arr[h], arr[m]
        h -= 1

print(arr)