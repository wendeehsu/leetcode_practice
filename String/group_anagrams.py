strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    sortedStrs = {}
    for i in range(len(strs)):
        currentStr = ''.join(sorted(strs[i]))
        if currentStr not in sortedStrs:
            sortedStrs[currentStr] = [strs[i]]
        else:
            sortedStrs[currentStr] += [strs[i]]

    return list(sortedStrs.values())

print(groupAnagrams(strs))
