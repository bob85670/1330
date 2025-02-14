

def main():
    treasure = []
    first_input_treasure = input()
    treasure.append(list(map(int, first_input_treasure)))
    i = len(first_input_treasure) - 1
    while (i):
        if (i == 0):
            break
        treasure.append(list(map(int, input())))
        i -= 1
    print(treasure)


if __name__ == "__main__":
    main()