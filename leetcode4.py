# 三数之和时间复杂度o（n**2）空间复杂度o（1）
# 题目描述
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 下标最后一位等于len-1
class Solution:
    def threeSum(nums:list[int]) -> list[list[int]]:
        nums.sort()                    #数组排序，保证三个指针的方向感
        res:list[list[int]] = []       #定义res，用来接受和为0的元素
        n = len(nums)                  #n为数组长度用来定义left和right
        for i in range(n-2):           #i的遍历范围是从下标0开始到倒数第三位，因为最少留两个数字给right和left
            if nums[i] > 0:            #i下标对应三数中最小的数，如果nums[i] > 0则无意义
                print("三数之和大于零，数组不成立")
                break
            if i > 0 and nums[i] == nums[i - 1]:     #如果i遍历时有两个相同元素直接跳过，保证输出唯一
                continue
            left,right = i+1 ,n-1                    #根据i和n定义left和right的初始位置
            while left < right :
                s = nums[i] + nums[left] +nums[right]#求出三数之和
                if  s < 0 :                           #三数之和小于零时只移动left，保证三数之和变大
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: #left遍历遇到两个连续相等的数时继续往后遍历
                        left += 1
                elif s > 0 :                           #三数之和大于零时只移动right，保证三数之和变小
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1                   
                else:                                   #三数之和等于零时把元素添加进res
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1       #三数之和出现0之后必须同时移动，如果只单一的移动left或right，只会比0大或比0小，不会等于0
                    while left < right and nums[left] == nums[left - 1]:#遍历遇到两个连续相等的数时继续遍历
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res