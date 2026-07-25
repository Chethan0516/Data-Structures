# arr = [13,46,24,52,20,9]
arr = [5,4,3,2,1, 1]
# arr = [1, 2, 3, 4]

n = len(arr)
for i in range(1,n):
    for j in range(i, 0, -1):
        while arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
print(arr)

# ------


arr = [13,46,24,52,20,9]
# arr = [5,4,3,2,1, 1]
# arr = [1, 2, 3, 4]
n = len(arr)

for j in range(1, n):
    i = j
    while i>0 and arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
print(arr)