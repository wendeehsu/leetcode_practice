tmpHead = [1,2,3,4,5]

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

head = createNode(0, tmpHead)

def reOrder(head):
    nodeList = []
    while head != None:
        nodeList += [head]
        head = head.next

    if len(nodeList) > 2:
        startIndex = 0
        endIndex = len(nodeList)-1
        reverse = False
        while startIndex != endIndex:
            if reverse:
                nodeList[endIndex].next = nodeList[startIndex]
                endIndex -= 1
            else:
                nodeList[startIndex].next = nodeList[endIndex]
                startIndex += 1
            reverse = not reverse
        if len(nodeList) % 2 == 0:
            nodeList[endIndex].next = None
        else:
            nodeList[startIndex].next = None

        head = nodeList[0]
    
    return head

q = reOrder(head)
while q != None:
    print(q.val)
    q = q.next