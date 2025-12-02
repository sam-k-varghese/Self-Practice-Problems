# upper traingle of given matrix

arr = [[11, 12, 5, 2], [15, 6,10,8], [10, 8, 12, 5], [12,15,8,6]]

def upper_traingle(nums):
    rows = len(nums)
    col = len(nums[1])
    for i in range(0, rows):
        for j in range(0, col):
            if j >= i :
                print(nums[i][j], end ="  ")
            else:
                print("*",  end ="  ")
        print()

upper_traingle(arr)


# transpose a matrix

def tarnspose_mat(nums):
    rows = len(nums)
    col = len(nums[1])
    res = [[0]*rows for i in range(col) ]
    print(res)
    for i in range(0, rows):
        for j in range(0, col):
            res[j][i] = nums[i][j]
    return res

print(tarnspose_mat(arr))
