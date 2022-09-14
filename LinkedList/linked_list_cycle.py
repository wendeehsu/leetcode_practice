headInput = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# create List
def createNode(index):
    if index >= len(headInput):
        return None
    else:
        newNode = ListNode(headInput[index])
        newNode.next = createNode(index+1)
        return newNode

# traverse linked list
head = createNode(0)
hasCycle = False
walker = runner = head
while walker != None and runner != None:
    walker = walker.next
    runner = runner.next.next
    if walker == runner:
        hasCycle = True
        break

print(hasCycle)