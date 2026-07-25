# W,A T:O(N2), B T:O(N) 

# num = [13,46,24,52,20,9]
# num = [5,4,3,2,1, 1]
num = [1, 2, 3, 4]

n = len(num)
count = 0
for i in range(n):
    swap = 0
    for j in range(0, n - i -1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            swap = 1
            count += 1
    if swap == 0:
        break
print(num, count)