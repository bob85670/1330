def nCk(n, k):
    if k == 0:
        print(f"{n}C0 = 1")
        return 1
    if n == k:
        print(f"{n}C{k} = 1")
        return 1
        
    print(f"{n}C{k} = {n-1}C{k-1} + {n-1}C{k}")
    left = nCk(n-1, k-1)
    right = nCk(n-1, k)
    result = left + right
    print(f"{n}C{k} = {result}")
    return result

def main():
    n = int(input())
    k = int(input())
    nCk(n, k)

if __name__ == "__main__":
    main()