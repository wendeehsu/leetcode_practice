from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    if len(popped) != len(pushed):
        return False   

    while len(popped) > 0:
        item = popped.pop(0)
        print(item, popped)
        try:
            index = pushed.index(item)
            pushIndex = index - 1
            popIndex = 0
            while pushIndex >= 0:
                if popped[popIndex] not in pushed[:pushIndex+1]:
                    popIndex += 1
                else:
                    if popped[popIndex] != pushed[pushIndex]:
                        return False
                    else:
                        popIndex += 1
                        pushIndex -= 1
            pushed.pop(index)
        except:
            return False
    return True


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
# popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))