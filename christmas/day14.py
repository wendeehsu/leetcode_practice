file1 = open('input.txt', 'r')
Lines = file1.readlines()

ROW_COUNT = len(Lines)
ans = 0

for col in range(len(Lines[0].replace("\n",""))):
    rubric = ROW_COUNT
    ptr = 0
    local_ans = 0
    while ptr < ROW_COUNT:
        if Lines[ptr][col] == 'O':
            local_ans += rubric
            rubric -= 1
        elif Lines[ptr][col] == '#':
            rubric = ROW_COUNT - ptr - 1
        ptr += 1
    print(local_ans)
    ans += local_ans
print("ans ->", ans)
