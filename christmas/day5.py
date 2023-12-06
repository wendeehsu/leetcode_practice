import bisect

# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
seeds = "2880930400 17599561 549922357 200746426 1378552684 43534336 155057073 56546377 824205101 378503603 1678376802 130912435 2685513694 137778160 2492361384 188575752 3139914842 1092214826 2989476473 58874625"
seeds = list(map(lambda x: int(x), seeds.split()))
print("seeds->", seeds)

maps = []
for line in Lines:
    # print(line[0], "><")
    if "map" in line:
        print(line.split()[0])
        maps = []
    elif line[0].isnumeric():
        des, src, nums = line.split()
        maps += [[int(src), int(nums), int(des)]]
    else:
        print("===== start processing =====")
        maps.sort()
        print(maps)
        for i, seed in enumerate(seeds):
            index = bisect.bisect_left(maps,[seed,0,0])
            print(seed, ":", index)
            if index > 0:
                # included before
                prev = maps[index-1]
                if prev[0] + prev[1] - 1 >= seed:
                    seeds[i] = prev[2] + seed - prev[0]
                    print(seed, "new ->", seeds[i])
                    continue
            # included in current
            if seed == maps[index][0]:
                seeds[i] = maps[index][2]
                print(seed, "new 1 ->", seeds[i])
                continue
            # not included
        print(seeds)
        # break
            
print("fianl ->", min(seeds))
