from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

headInput = []
# create List
def createNode(index):
    if index >= len(headInput):
        return None
    else:
        newNode = ListNode(headInput[index])
        newNode.next = createNode(index+1)
        return newNode

def swapNodes(head, k: int):
    newHead = head
    count = 0
    first, second = head, head

    while head != None:
        if count + 1 == k:
            first = head
        head = head.next
        count += 1

    findIndex = count - k
    while findIndex != 0:
        second = second.next
        findIndex -= 1
    # print(first.val, second.val)

    tmp = second.val
    second.val = first.val
    first.val = tmp

    # while newHead != None:
    #     print(newHead.val)
    #     newHead = newHead.next
    return newHead


headInput = [7,9,6,6,7,8,3,0,9,5]
k = 1
head = createNode(0)
print(swapNodes(head, k))