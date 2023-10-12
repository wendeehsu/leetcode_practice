from typing import List

def maxSubarraySumCircular(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    # 1. find max in normal case
    max_index = 0
    global_max = nums[0]
    current_max = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        current_max = max(current_max + num, num)
        global_max = max(global_max, current_max)
    print("1. global max", global_max)        

    # 2. find min in normal case
    min_index = 0
    global_min = nums[0]
    current_min = nums[0]
    for i in range(1,len(nums)):
        num = nums[i]
        current_min = min(current_min + num, num)
        global_min = min(global_min, current_min)
    print("2. global max", sum(nums) - global_min)

    if sum(nums) == global_min:
        return global_max
    return max(global_max, sum(nums) - global_min)



    # # merge array
    # pointer = 0
    # while pointer < len(nums):
    #     if nums[pointer] == 0:
    #         nums.pop(pointer)
    #     if pointer < len(nums)-1:
    #         if nums[pointer] * nums[pointer+1] > 0:
    #             nums[pointer] += nums[pointer+1]
    #             nums.pop(pointer+1)
    #         else:
    #             pointer += 1
    #     else:
    #         if nums[0] * nums[pointer] > 0:
    #             nums[0] += nums[pointer]
    #             nums.pop(pointer)
    #         break

    # if nums[0] < 0:
    #     nums.append(nums[0])
    #     nums.pop(0)
    # print(nums)

    # # find max
    # max_index = -1
    # max_num = -1
    # for i, num in enumerate(nums):
    #     if num > max_num:
    #         max_num = num
    #         max_index = i
    
    # if len(nums) < 2:
    #     return max_num

    # # explor left
    # left = max_index - 1
    # right = max_index +1
    # while True:
    #     if left == 0:
    #         left = len(nums) -1 # back
    #     if right == len(nums) -1:
    #         right = 0
    #     left_explore = nums[left] + nums[left-1]
    #     right_explore = nums[right] + nums[right+1]

    #     if max(left_explore, right_explore) < 0:
    #         break
    #     elif left_explore >= right_explore and left_explore > 0:
    #         max_num += left_explore
    #         left -= 2
        


    # return max_num


# nums = [-10,1,-2,3,5,-2,-4,9]
nums = [-5,-3,-5]
print(maxSubarraySumCircular(nums))