class sol():
    @staticmethod
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    @staticmethod
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = sol.partition(arr, low, high)
            sol.quicksort(arr, low, pivot_index-1)
            sol.quicksort(arr, pivot_index+1, high)

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    re = sol.quicksort(arr, 0, len(arr)-1)
    print(re)
    print(*arr)