from typing import List

def generateMatrix(n: int) -> List[List[int]]:
    # init matrix
    result = []
    for i in range(n):
        result += [[0]*n]
    
    row_index = 0
    col_index = -1
    mode = 0 # 0 ->/ 1 v / 2 <- / 3 ^
    i = 1
    while i < n*n +1:
        if mode == 0 and col_index + 1 < n \
            and result[row_index][col_index + 1] == 0:
            col_index += 1
            result[row_index][col_index] = i
            i += 1
        elif mode == 1 and row_index + 1 < n \
            and result[row_index+1][col_index] == 0:
            row_index += 1
            result[row_index][col_index] = i
            i += 1
        elif mode == 2 and col_index - 1 >= 0 \
            and result[row_index][col_index-1] == 0:
            col_index -= 1
            result[row_index][col_index] = i
            i += 1
        elif mode == 3 and row_index - 1 >= 0 \
            and result[row_index-1][col_index] == 0:
            row_index -= 1
            result[row_index][col_index] = i
            i += 1
        else:
            print("update mode", mode, row_index, col_index)
            if mode == 3:
                mode = 0
            else:
                mode += 1

    return result

print(generateMatrix(4))