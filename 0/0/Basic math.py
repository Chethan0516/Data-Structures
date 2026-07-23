# $ Reverse a number
class Solution:
    def rev(self, num):
        rev_di = 0
        while num > 0:
            rev = num % 10
            rev_di = rev_di * 10 + rev
            num = num // 10
        return rev_di

obj = Solution()
num = 12345
print(obj.rev(num))

# ----------------------------------------
# $ Palindorm
num = 121
if str(num) == str(num)[::-1]:
    print(True)
else:
    print(False)

# --------------------------------

num = original = 121
reverse = 0
while num > 0:
    rev = num % 10
    reverse = reverse * 10 + rev
    num = num // 10
print(reverse)
if reverse == original:
    print(True)
else:
    print(False)

# ---------------------------------

# $ Amstrong sumber
n = original = 153
k = len(str(n))
sum = 0
while n > 0:
    rev = n % 10
    sum = sum + (rev ** k)
    n = n // 10
print(sum)
if sum == original:
    print(True)
else:
    print(False)

# ------------------------------------