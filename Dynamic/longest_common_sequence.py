text1 = "wendee"
text2 = "edw"

# create empty matrix
dp_matrix = []
for i in range(len(text2)+1):
    dp_matrix += [[0] * (len(text1) + 1)]

# print(dp_matrix)

for i in range(len(text1)-1,-1,-1):
    for j in range(len(text2)-1,-1,-1):
        """
        Case 1: text1[i] == text2[j]: dp_matrix[i][j] = dp_matrix[i+1][j+1]+1
        Case 2: text1[i] != text2[j]:
                decide to take letter from text1 or text2
                dp_matrix[i][j] = max(dp_matrix[i+1][j],dp_matrix[i][j+1])
        """
        if text1[i] == text2[j]:
            dp_matrix[j][i] = dp_matrix[j+1][i+1]+1
        else:
            dp_matrix[j][i] = max(dp_matrix[j+1][i],dp_matrix[j][i+1])

print(dp_matrix[0][0])