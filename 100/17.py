# Kadane's Algorithm : Maximum Subarray Sum in an Array
# A subarray is a contiguous non-empty sequence of elements within an array.


# T: O(N3)
arr = [2, 3, 5, -2, 7, -4]  

maxi = float('-inf')
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sum = 0
        for z in range(i, j+1):
            sum += arr[z]
        maxi = max(sum, maxi)
print(maxi)


# Better T: O(N2)
arr = [2, 3, 5, -2, 7, -4]  
maximum = 0
for i in range(len(arr)):
    num = 0
    for j in range(i, len(arr)):
        num += arr[j]
        maximum = max(num, maximum)
print(maximum)

# Optimal T: O(N)

arr = [2, 3, 5, -2, 7, -4] 

maximum = 0
num =  0

for i in range(len(arr)):
    num += arr[i]
    if num > maximum:
        maximum = num
    if num < 0:
        num = 0
print(maximum)