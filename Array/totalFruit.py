from typing import List

def totalFruit(fruits: List[int]):
    maxFruit = 0

    def isValid(dic, toAdd):
        if toAdd in dic:
            return True
        elif len(dic) < 2:
            return True
        return False

    left, right = 0, 0
    dic = {}
    while right < len(fruits):
        while right < len(fruits) and isValid(dic, fruits[right]):
            if fruits[right] in dic:
                dic[fruits[right]] += 1
            else:
                dic[fruits[right]] = 1
            maxFruit = max(maxFruit,sum(dic.values()))
            right += 1
        
        if right >= len(fruits):
            break
        
        while left < right and isValid(dic, fruits[right]) == False:
            if dic[fruits[left]] == 1:
                del dic[fruits[left]]
            else:
                dic[fruits[left]] -= 1
            left += 1

    return maxFruit

fruits = [1,2,3,2,2,2,1]
print(totalFruit(fruits))