# Subject:
# There are some ropes of different lengths, given a desired number of ropes, find the maximum length of the rope that can be cut up to at least the desired number of ropes.
# Note: The rope cannot be spliced.
# In the following example, len indicates the length, and target indicates the number of expected numbers.

# Example 1:
# 	Input: len = {802, 743, 457, 539}, target=11.
# 	Output: 200; (You can't cut 11 ropes at 201.)

# Example 2:
# 	Input: len = {1, 1, 1}, target=4;
# 	Output: 0

def rope(lenlist, target):

    low = 1
    high = max(lenlist)

    if not isPossible(lenlist, 1, target):
        return 0
    
    while low < high - 1:
        if isPossible(lenlist, int((low + high)/2), target):
            low = int((low + high)/2)
        else:
            high = int((low + high)/2)

    return low


def isPossible(lenlist, lengthCut, target):
    ans = 0
    for rope in lenlist:
        ans += rope//lengthCut
    if ans >= target:
        return True
    return False

print(rope([802, 743, 457, 539],11))
print(rope([1, 1, 1], 4))
