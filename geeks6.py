def reverse_array(arr):
    res = []
    res = arr[::-1]
    return res
if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    print(" ".join(map(str, reverse_array(arr))))