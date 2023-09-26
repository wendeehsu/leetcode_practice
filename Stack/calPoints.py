from typing import List

def calPoints(operations: List[str]) -> int:
    stack = []
    for item in operations:
        if item == "+":
            num1 = stack[-1]
            num2 = stack[-2]
            stack.append(num1 + num2)

        elif item == "D":
            num = stack[-1]
            num *= 2
            stack.append(num)

        elif item == "C":
            stack.pop()
        
        else:
            stack.append(int(item))
        # print(item, "->", stack)
    
    return sum(stack)
        


ops = ["5","C"]
print(calPoints(ops))
