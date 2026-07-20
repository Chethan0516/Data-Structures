# Given an array arr = [2, 1, 5, 1, 3, 2] and k = 3, 
# find the maximum sum of any contiguous subarray of size 3.  

arr = [2, 1, 5, 1, 3, 2]
k = 3

sum_cur, max_sum = 0, 0
for i in range(3):
    sum_cur += arr[i]

for i in range(3, len(arr)):
    sum_cur += arr[i]
    sum_cur -= arr[i-3]
    max_sum = max(sum_cur, max_sum)
print(max_sum)

#-----------------------------

# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowels.

s = "abciiidef"
k = 3

vol = ['a', 'e', 'i', 'o', 'u']
# vol = {'a', 'e', 'i', 'o', 'u'}
count = 0

for i in range(k):
    if s[i] in vol:
        count += 1

max_count = count
for i in range(k, len(s)):
    if s[i] in vol:
        count += 1
    if s[i - k] in vol:
        count -= 1
    max_count = max(max_count, count)

print(max_count)

#---------------------------------------------

# Scenario: You are monitoring a temperature sensor. You need to alert engineering 
# if the average temperature stays above a danger threshold for a continuous period of time.
# Inputs:arr = [12, 15, 18, 20, 22, 14, 10, 25, 30]K = 3 (Window size of 3 seconds)
# threshold = 18 (Alert if the average temperature is (>= 18\))




# $ Maximum points can be obtained from cards that can be picked in reverese also but not in middle.

arr = [6, 2, 3, 4, 7, 2, 1, 7, 1]
k = 4
total = 0
for i in range(k):
    total += arr[i]

l, r = k - 1, -1
val = total
while l > 0:
    print(l, r)
    val = val + arr[r] - arr[l]
    total = max(total, val)
    r -= 1
    l -= 1
    
print(total)

# -------------------