def checkISBNValid(isbn):
    firstTwelveDigits = str(isbn)[:-1]
    weightSum = 0
    remainder = 0
    for i in range(0, 12):
        if i % 2 == 0:
            weightSum += int(firstTwelveDigits[i]) * 1
        else:
            weightSum += int(firstTwelveDigits[i]) * 3
    remainder = weightSum % 10
    check_digit = 10 - remainder if remainder != 0 else 0
    return check_digit == int(str(isbn)[-1])

def main():
    isbn = int(input())
    return "Valid" if checkISBNValid(isbn) else "Invalid"

if __name__ == "__main__":
    print(main())
    