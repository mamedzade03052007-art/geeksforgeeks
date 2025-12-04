def Rotate_array(arr, d):
    n = len(arr)
    res = []
    d = d%n
    res = arr[-1*d:] + arr[0:n-d]
    return res
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(" ".join(map(str, Rotate_array(arr, d))))