class sol():

    def rec_insertion(self, arr, i, n):
        if i == n: return arr
        j = i
        while j>0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1 
        return self.rec_insertion(arr, i+1, n)

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    n = len(arr)
    re = sol().rec_insertion(arr, 0, n)
    print(re)