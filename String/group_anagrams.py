strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    sortedStrs = []
    for i in range(len(strs)):
        sortedStrs += [(i,sorted(strs[i]))]
    
    sortedStrs = sorted(sortedStrs, key=lambda x:x[1])
    groups = []
    index = -1
    currentStr = ""
    for i in range(len(sortedStrs)):
        if sortedStrs[i][1] == currentStr:
            groups[index] += [strs[sortedStrs[i][0]]]
        else:
            currentStr = sortedStrs[i][1]
            groups += [[strs[sortedStrs[i][0]]]]
            index += 1
    return groups

print(groupAnagrams(strs))
