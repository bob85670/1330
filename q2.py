def evalDistance(qX, qY, dX, dY):
    return True if abs(dX - qX) + abs(dY - qY) > 10 else False

def main():
    farDogList = []
    lastStr = ""
    print("Position of Queenie: ", end='')
    queenX, queenY = map(int, input().split())
    puppyNum = int(input("Number of puppies: "))
    for i in range(1, puppyNum + 1):
        print("Position of Puppy ", i, ": ", end='')
        dogX, dogY = map(int, input().split())
        if evalDistance(queenX, queenY, dogX, dogY):
            farDogList.append(i)

    print(farDogList)
    if farDogList:
        for j in range(len(farDogList)):
            if j == len(farDogList) - 1:
                lastStr += "Puppy " + str(farDogList[j]) + " is too far."
            else:
                lastStr += "Puppy " + str(farDogList[j]) + " and "
        print(lastStr)
    else:
        print("No puppy is too far.")
            

if __name__ == "__main__":
    main()