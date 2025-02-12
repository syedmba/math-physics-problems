# arr = []
arr = [0, 0, 0, 1, 1, 1, -1, -1]
# N = int(input("enter arr length: "))
# for i in range(N):
#     arr.append(int(input()))

p = {-1: 0, 0: 0, 1: 0}

i1, i2, i3 = 0, 0, 0
allThree = True
while True:
    found = [False, False, False]
    
    while not found[0] or not found[1] or not found[2]:
        print(f"i1: {i1} and found = {found}")
        if i1 == len(arr) or i2 == len(arr) or i3 == len(arr):
            allThree = False
            break
        if not found[arr[i1]]:
            p[arr[i1]] = i1
            found[arr[i1]] = True
        i1 += 1
    
    if not allThree:
        break
    
    pos = sorted([p[-1], p[0], p[1]])
    arr[pos[0]] = -1
    arr[pos[1]] = 0
    arr[pos[2]] = 1

    print(arr)
    


        

