# Kadane's algorithm :: Time O(N), Space O(1)
# Find the maximum sub array

num = [-2,1,-3,4,-1,2,1,-5,4]

cur_sum = max_sum = float("-inf")
for i in num:
    cur_sum += i
    if cur_sum < 0: cur_sum = 0
    max_sum = max(cur_sum, max_sum)

print(max_sum)

# ----------

num = [-2,1,-3,4,-1,2,1,-5,4]

cur_sum = max_sum = num[0]
for i in range(1, len(num)):
    cur_sum += num[i]
    cur_sum = max(cur_sum, num[i])
    max_sum = max(cur_sum, max_sum)

print(max_sum)

#-----------------------------------
# Brute Force O(n*n)

num = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = 0
for i in range(len(num)):
    cur_sum = 0
    for j in range(i, len(num)):
        cur_sum = cur_sum + num[j]
        max_sum = max(max_sum, cur_sum)

print(max_sum)

#--------------------------------------------
# Sllinding window

# ??