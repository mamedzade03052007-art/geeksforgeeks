def isSorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True
if __name__ == "__main__":
    arr = [  ]
    if isSorted(arr):
        print("True")
    else:
        print("False")