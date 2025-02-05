def main():
    occupy = []
    len = int(input("Length of riverfront: "))
    animals = int(input("Number of animals: "))
    if animals == 0:
        print(str(len))
        return
    for i in range(1, animals + 1):
        print("Animal " + str(i) + ": ", end='')
        start, end = map(int, input().split())
        occupy.append([start, end])

    # merge occupied river
    occupy.sort()
    mergedOccupy = [occupy[0]]
    for start, end in occupy:
        lastEnd = mergedOccupy[-1][1]
        if start <= lastEnd:
            mergedOccupy[-1][1] = max(lastEnd, end)
        else:
            mergedOccupy.append([start, end])
    
    # find available river number
    count = 0
    for pair in mergedOccupy:
        start, end = pair
        count += (end - start + 1)
    print(len - count)


if __name__ == "__main__":
    main()