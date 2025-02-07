def main():
    while (True):
        print("a b: ", end='')
        a, b = map(int, input().split())
        if a > 0 and b > 0 and a < b:
            break
    while (True):
        print("Divisor: ", end='')
        divisor = list(map(int, input().split()))
        divisor = sorted(list(set(divisor)))
        for i in range(len(divisor)):
            if divisor[i] < 0 or divisor[i] > b:
                break
        else:
            break
        continue

    print("M ", end='')
    for i in divisor:
        print(i, end=' ')
    print("")

    for k in range(a, b):
        print(k, end =' ')
        for j in divisor:
            print(1, end =' ') if k % j == 0 else print(0, end=' ')
        print("")
    

if __name__ == "__main__":
    main()