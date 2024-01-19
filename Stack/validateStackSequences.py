from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    if len(popped) != len(pushed):
        return False   

    stack = []
    pointer = 0
    for item in pushed:
        stack.append(item)
        while len(stack) > 0 and stack[-1] == popped[pointer]:
            stack.pop(-1)
            pointer += 1
    return pointer == len(popped)

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
# popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))