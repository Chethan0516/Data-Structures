# Given an array of integers, rotating array of elements by k elements either left or right.

def right(nums, k, n):
    temp = nums[-k:]
    for i in range(n-k-1, -1, -1):
        nums[i+k] = nums[i]
    for i in range(k):
        nums[i] = temp[i]
    return nums

def left(nums, k, n):
    temp = nums[:k]
    for i in range(k, n):
        nums[i-k] = nums[i]
    for i in range(k):
        nums[n-k+i] = temp[i]
    print(nums)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    k = 2
    k %= n
    print(right(arr,k,n))
    print(left(arr, k, n))