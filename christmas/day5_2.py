import bisect

# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
seeds = "2880930400 17599561 549922357 200746426 1378552684 43534336 155057073 56546377 824205101 378503603 1678376802 130912435 2685513694 137778160 2492361384 188575752 3139914842 1092214826 2989476473 58874625"
seeds = list(map(lambda x: int(x), seeds.split()))
newSeeds = []
for i in range(0, len(seeds),2):
    newSeeds += [[seeds[i], seeds[i+1]]]
seeds = newSeeds
print("newSeeds->", seeds)

maps = []
for line in Lines:
    if "map" in line:
        print(line.split()[0])
        maps = []
    elif line[0].isnumeric():
        des, src, nums = line.split()
        maps += [[int(src), int(nums), int(des)]]
    else:
        print("===== start processing =====")
        maps.sort()
        # print(maps)
        ptr = 0
        while ptr < len(seeds):
            seed = seeds[ptr]
            index = bisect.bisect_left(maps,[seed[0],0,0])
            print(seed, ":", index)
            if index > 0:
                # included in before
                prev = maps[index-1] # [98,3,50]
                if prev[0] + prev[1] - 1 >= seed[0]:
                    print('prev', prev)
                    # 1. fully include: seeds[ptr] = [99,2]
                    if prev[0] + prev[1] - 1 >= seed[0] + seed[1] -1:
                        seeds[ptr][0] = prev[2] + seed[0] - prev[0]
                        print("fully include ->", seeds[ptr])
                        ptr += 1
                        continue
                    # 2. cutted, need insert: seeds[ptr] = [99,5]
                    else:
                        ori_start = seeds[ptr][0] # 99
                        ori_len = seeds[ptr][1] # 5
                        exceed_len = seed[0] + seed[1] - (prev[0] + prev[1]) # 3
                        seeds[ptr][0] = prev[2] + seed[0] - prev[0]
                        seeds[ptr][1] = ori_len - exceed_len # 2
                        exceed_seed = [ori_start + seeds[ptr][1], exceed_len]
                        print(seed, "cutted new ->", seeds[ptr])
                        print(seed, "exceed_seed ->", exceed_seed)
                        seeds.insert(ptr+1, exceed_seed)
                        ptr += 1
                        continue
            # included in current
            current = maps[index] # [98,3,50]
            if seed[0] == current[0]: 
                if seed[1] <= current[1]: # seed = [98,2]
                    seeds[ptr][0] = current[2]
                    print("same fully include ->", seeds[ptr])
                    ptr += 1
                    continue
                else: # seed = [98,5]
                    ori_start = seeds[ptr][0] # 98
                    ori_len = seeds[ptr][1] # 5
                    exceed_len = ori_len - current[1] # 2
                    seeds[ptr][0] = current[2]
                    seeds[ptr][1] = current[1] # 3
                    exceed_seed = [ori_start + seeds[ptr][1], exceed_len]
                    print(seed, "cutted new ->", seeds[ptr])
                    print(seed, "exceed_seed ->", exceed_seed)
                    seeds.insert(ptr+1, exceed_seed)
                    ptr += 1
                    continue
            # (80,2,21) (98,3,50)
            if seed[0] + seed[1]-1 < current[0]: # seed = (85,2)
                print("not include", seed, current)
                ptr += 1
            if seed[0] + seed[1]-1 >= current[0]: # seed = (95,9)
                # new: (95,3) (98,6)
                ori_len = seed[1] # 9
                seeds[ptr][1] = current[0]-seed[0] # 3
                exceed_seed = [current[0], ori_len - seeds[ptr][1]]
                seeds.insert(ptr+1, exceed_seed)
                print("trimmed", seed, "->", seeds[ptr], seeds[ptr+1])
                ptr += 1
                continue

        print(seeds)
        # break

print("fianl ->", min(list(map(lambda x: x[0], seeds))))
