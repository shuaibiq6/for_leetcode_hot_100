# #### 题目描述
# 283. 移动零
# 给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。
# **请注意** ，必须在不复制数组的情况下原地对数组进行操作。

# 示例
# ```
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# ```
# 本质双指针，慢指针lastpos，快指针current，快慢指针从零开始，快指针遍历数组
# 碰到不等于0的元素就跟慢指针交换元素，交换后慢指针实现自增
class Solution:
    def moveZeros(self,nums:list[int]) -> list[int]:
        lastpos=0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current],nums[lastpos] = nums[lastpos],nums[current]
                lastpos += 1
        return nums
if __name__ == "__main__":
    sol=Solution()
    print(sol.moveZeros([9,3,4,0,2,0,1]))