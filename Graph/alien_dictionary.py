# words = ["wrth","wrf","wrf","er","ett","rftt"]
# words = ["wrt","wrtkj"]
words = ["z","x","a","zb","zx"]

def traverse(words):
    mapping = {}
    inCount = {}
    # init inCount
    for i in set(''.join(words)):
        inCount[i] = 0

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if word1 == word2:
            continue
        index = 0
        while index < len(word1) \
            and index < len(word2) \
            and word1[index] == word2[index]:
            index += 1

        if index >= len(word2):
            return ""

        if index < len(word1):
            alphabet = word1[index]
            if word2[index] in mapping \
                and alphabet in mapping[word2[index]]:
                return ""

            if alphabet in mapping:
                if word2[index] not in mapping[alphabet]:
                    mapping[alphabet].add(word2[index])
                    inCount[word2[index]] += 1
            else:
                mapping[alphabet] = set(word2[index])
                inCount[word2[index]] += 1

    result = []
    while len(inCount) > 0:
        currentResult = []
        for i in inCount:
            if inCount[i] == 0: # leading
                currentResult += [i]
                try:
                    for sub in mapping[i]:
                        inCount[sub] -= 1
                except:
                    continue
        
        if len(currentResult) == 0: # cycle
            return ""
        result += currentResult
        for i in currentResult:
            del inCount[i]
    return ''.join(result)
    
print("order ->",traverse(words))