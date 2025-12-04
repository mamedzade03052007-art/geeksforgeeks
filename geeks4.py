def Redub(arr):
    res = []
    res.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            res.append(arr[i])
    return res
if __name__ == "__main__":
    arr = [1,2,2,3,4,4,5,5,5,6]
    print(" ".join(map(str, Redub(arr))))