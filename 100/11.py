# Problem: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..

# arr = [1, 1, 0, 1, 1, 1]
arr = [1, 0, 1, 1, 0, 1]
count = 0
t = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
        if count > t:
            t = count
    else:
        count = 0

print(t)