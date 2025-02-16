def rotate90(treasure):
    return list(zip(*treasure[::-1]))

def check_pattern(game_map, treasure, x, y): 
    for i in range(len(treasure)):
        for j in range(len(treasure[0])):
            if y + i >= len(game_map) or x + j >= len(game_map[0]):
                return False
            if treasure[i][j] != game_map[y + i][x + j]:
                return False
    return True

def main():
    # parsing input 
    treasure = []
    first_input_treasure = input()
    treasure.append([int(x) for x in first_input_treasure])
    for i in range(len(first_input_treasure) - 1):
        treasure.append([int(x) for x in input()])
    
    game_map = []
    first_input_map = input()
    game_map.append([int(x) for x in first_input_map])
    for i in range(len(first_input_map) - 1):
        game_map.append([int(x) for x in input()])

    # check each coordinate
    temp_treasure = treasure
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            for t in range(4):
                temp_treasure = rotate90(temp_treasure)
                if check_pattern(game_map, temp_treasure, i, j):
                    print(str(i) + " " + str(j))
                    return

if __name__ == "__main__":
    main()