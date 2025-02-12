def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prp(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if gcd(nums[i], nums[j]) != 1:
                return False
    return True

def is_mrp(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result == 1
    
def main():
    print("Numbers: ", end='')
    nums = list(map(int, input().split()))
    if is_prp(nums):
        return "prp"
    elif is_mrp(nums):
        return "mrp"
    else:
        return "~"
    
if __name__ == "__main__":
    print(main())