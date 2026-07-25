# Problem Statement: Given an array, we have to find the largest element in the array.

class sol():

    def __init__(self, arr):
        self.arr = arr

    def largest(self):
        j = 0
        for i in range(len(self.arr)):
            if self.arr[i] > self.arr[j]:
                j = i
        return arr[j]

if __name__ == "__main__":
    arr = [2, 5, 1, 3, 0]
    obj = sol(arr)
    print(obj.largest())