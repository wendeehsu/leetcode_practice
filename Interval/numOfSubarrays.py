from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    qualified = 0
    local_sum = 0

    for i in range(k):
        local_sum += arr[i]
    
    if local_sum / k >= threshold:
        qualified += 1

    for i in range(k, len(arr)):
        local_sum -= arr[i-k]
        local_sum += arr[i]
        if local_sum / k >= threshold:
            qualified += 1
        print(arr[i], "q ->", qualified)

    return qualified
        


arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k, threshold))
