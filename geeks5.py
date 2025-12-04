def sub_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k])
            print()
if __name__ == "__main__":
    arr = [1, 2, 3]
    sub_array(arr)