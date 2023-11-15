from typing import List
import heapq

def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    nums = list(zip(nums1,nums2))
    nums = sorted(nums, key=lambda x:x[1], reverse=True)
    localheap = []
    localSum = 0
    for i in range(k):
        localSum += nums[i][0]
        heapq.heappush(localheap, nums[i])

    ans = localSum * nums[k-1][1]
    for i in range(k,len(nums)):
        removed = heapq.heappop(localheap)
        heapq.heappush(localheap, nums[i])
        localSum -= removed[0]
        localSum += nums[i][0]
        ans = max(ans, localSum* nums[i][1])
    
    return ans


nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
print(maxScore(nums1, nums2, k))