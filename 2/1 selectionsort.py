num = [13,46,24,52,20,9]
num = [5,4,3,2,1, 1]

# It breaks at duplicates and T: O(n2) S:O(N)
for i in range(len(num)):
    m = min(num[i::])
    ind = num.index(m)
    num[i], num[ind] = num[ind], num[i]

print(num)

# T:O(N2) S:O(N)
for i in range(len(num) - 1):
    min_index = i
    for j in range(i+1, len(num)):
        if num[j] < num[min_index]:
            min_index = j
    num[i], num[min_index] = num[min_index], num[i]
print(num)