class sol():
    def re_bubble(self, arr, n):
        if n == 1:
            return arr
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return self.re_bubble(arr, n-1)

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    n = len(arr)
    re = sol().re_bubble(arr, n)
    print(re)