# Find the Majority Element that occurs more than N/2 times

# T, S: O(N)
# arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
arr = [1, 1, 1, 2, 1, 2]  

count = {}
for i in range(len(arr)):
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1
for key, values in count.items():
    if values > len(arr) / 2:
        print(key)
print(count)

# Optimal T: O(N), S:(1)

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]  

num = count = 0
for i in arr:
    if count == 0:
        num = i
        count += 1
    elif num == i:
        count += 1
    else:
        count += 1
count = arr.count(num)
if count > len(arr) // 2:
    print(num)