class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr += [num]

    def findMedian(self) -> float:
        self.arr.sort()
        arr_length = len(self.arr)
        if arr_length % 2 == 0:
            return 0.5*(self.arr[arr_length//2] + self.arr[(arr_length//2)-1])
        return self.arr[(arr_length-1)//2]

obj = MedianFinder()
obj.addNum(1)
obj.addNum(4)
obj.addNum(5)
obj.addNum(0)
print(obj.arr)
print(obj.findMedian())