def main():
    treasure = []
    first_input_treasure = input()
    treasure.append([int(x) for x in first_input_treasure])
    for i in range(len(first_input_treasure) - 1):
        treasure.append([int(x) for x in input()])
    print(treasure)
    
    game_map = []
    first_input_map = input()
    game_map.append([int(x) for x in first_input_map])
    for i in range(len(first_input_map) - 1):
        game_map.append([int(x) for x in input()])
    print(game_map)

    

if __name__ == "__main__":
    main()