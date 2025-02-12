from typing import List


def get_numbers(grid):
    ans = []
    for row in grid:
        num = ""
        for x in row:
            num += str(x)
        ans.append(num)
    cols = ["" for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)): # grid is n * n
            cols[j] += grid[i][j]
    ans = ans + cols
    diag = ""
    for i in range(len(grid)):
        diag += grid[i][i]
    ans.append(diag)
    diag = ""
    for i in range(len(grid)):
        diag += grid[i][len(grid)-1-i]
    ans.append(diag)
    return ans

def compute_cost(grid: List[List[int]]):
    

    occurrence_dict = {}
    cost = 0
    nums = get_numbers(grid)
    for num in nums:
        for digit in num:
            if digit in occurrence_dict:
                cost += occurrence_dict[digit]
                occurrence_dict[digit] += 1
            else:
                occurrence_dict[digit] = 1   
    return cost




def get_all_primes_less_than_n(n):
    nums = set([i for i in range(2, n)])
    primes = []
    while True:
        # print(f"nums is {nums}")
        if len(nums) == 0:
            return primes
        x = list(nums)[0]
        # print(f"x is {x}")
        primes.append(x)
        for j in range(2, n//x + 1):
            # print(f"going to remove {x*j}")
            if x*j in nums:
                nums.remove(x*j)
        nums.remove(x)
        
def get_all_k_digit_primes(k):
    primes = get_all_primes_less_than_n(10**k)
    low = 0
    high = len(primes) - 1
    while low < high - 1:
        mid = (low + high)//2
        if primes[mid] >= 10**(k-1):
            high = mid
        else:
            low = mid
    return primes[high:]


def find_solutions():
    def is_valid(nums, primes):
        
        for num in nums:
            if int(num) not in primes:
                return False, -1
        summation = 0
        
        
        for num in nums:
            othersum = 0
            for digit in num:
                othersum += int(digit)
            if othersum != summation:
                return False, -1
            
        return True, summation

    primes = set(get_all_k_digit_primes(5))
    sums = {}
    for prime in primes:
        summ = sum([int(x) for x in str(prime)])
        if summ in sums:
            sums[summ].append(prime)
        else:
            sums[summ] = [prime]
    print(sums)
    for x in sums:
        print(x)
        



    # nums = get_numbers(grid)


    

# print(get_all_primes_less_than_n(100000))
# print(get_all_k_digit_primes(5))
find_solutions()
        

