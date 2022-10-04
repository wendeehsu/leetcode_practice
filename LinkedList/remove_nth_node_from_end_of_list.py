tmpHead = [1,2,3,4,5]
n = 2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(startNode):
    sublist = []
    while startNode != None:
        sublist += [startNode.val]
        startNode = startNode.next
    print(sublist)

# create List
def createNode(index, targetList):
    if index >= len(targetList):
        return None
    else:
        newNode = ListNode(targetList[index])
        newNode.next = createNode(index+1,targetList)
        return newNode

def removeNthFromEnd(head, n):
    length = 0
    node = head
    while node != None:
        length += 1
        node = node.next
    
    numToRemove = length - n
    counter = 0
    newHead = currentHead = ListNode(0)
    while head != None:
        if counter != numToRemove:
            currentHead.next = head
            head = head.next
        else:
            currentHead.next = head.next
            if head.next:
                head = head.next.next
            else:
                head = None
        currentHead = currentHead.next
        counter += 1

    return newHead.next

head = createNode(0,[1,2,3])
a = removeNthFromEnd(head,3)
printList(a)