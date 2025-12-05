def cost(n,a):
    return (n-1)*min(a)
if __name__ == "__main__":
    a = [4,3,2]
    n = len(a)
    print(cost(n,a))