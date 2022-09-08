class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# create List of ListNode
def createListNode(currentList, index):
    if index >= len(currentList):
        return None
    else:
        return ListNode(currentList[index], createListNode(currentList,index+1))

rawlists = [[1,4,5],[1,3,4],[2,6]]
lists = []
for sublist in rawlists:
    lists += [createListNode(sublist,0)]

for i in lists:
    index = i
    while index != None:
        index = index.next

# main function
finalList = []
# flat -> sort -> list again
for sublist in lists:
    currentIndex = sublist
    while currentIndex != None:
        finalList += [currentIndex.val]
        currentIndex = currentIndex.next

finalList.sort()
print(createListNode(finalList, 0))