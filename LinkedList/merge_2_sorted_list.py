list1_raw = [1,2,4]
list2_raw = [1,3,4]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# create List
def createNode(index, targetList):
    if index >= len(targetList):
        return None
    else:
        newNode = ListNode(targetList[index])
        newNode.next = createNode(index+1,targetList)
        return newNode

list1 = createNode(0, list1_raw)
list2 = createNode(0, list2_raw)

newHead = head = ListNode(0)

while list1 != None or list2 != None:
    if list1 == None or \
        (list1 and list2 and list2.val <= list1.val):
        head.next = list2
        list2 = list2.next
    else:
        head.next = list1
        list1 = list1.next

    head = head.next

print(newHead.next)