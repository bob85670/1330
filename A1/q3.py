def evalDistance(qX, qY, dX, dY):
    return True if abs(dX - qX) + abs(dY - qY) > 10 else False


def main():
    farDogList = []
    userNum = int(input("Number of User: "))
    lastStr = ""
    for i in range(1, userNum + 1):
        print("Position of User " +  str(i) + " :", end='')
        curUserX, curUserY = map(int, input().split())
        puppyNum = int(input("Number of puppies for User " + str(i) + " :"))
        for j in range(1, puppyNum + 1):
            print("Position of Puppy "+ str(j) + ": ", end='')
            puppyX, puppyY = map(int, input().split())
            if evalDistance(curUserX, curUserY, puppyX, puppyY):
                farDogList.append((i, j))
    
    if farDogList:
        for k in range(len(farDogList)):
            if k == len(farDogList) - 1:
                lastStr += "Puppy " + str(farDogList[k][1]) + "(User " + str(farDogList[k][0]) + ")" + " too far."
            else:
                lastStr += "Puppy " + str(farDogList[k][1]) + "(User " + str(farDogList[k][0]) + ")" + " and "
        print(lastStr)
    else:
        print("No puppy is too far.")



if __name__ == "__main__":
    main()