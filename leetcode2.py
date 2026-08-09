# 283. 移动零
# 本质双指针，慢指针lastpos，快指针current，快慢指针从零开始，快指针遍历数组
# 碰到不等于0的元素就跟慢指针交换元素，交换后慢指针实现自增
class Solution:
    def moveZeros(self,nums:list[int]) -> list[int]:
        lastpos=0                           #lastpos=0 无意义但代入nums[lastpos]就表示lastpos是从索引0开始运动实现位置交换
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current],nums[lastpos] = nums[lastpos],nums[current]
                lastpos += 1
        return nums
if __name__ == "__main__":
    sol=Solution()
    print(sol.moveZeros([9,3,4,0,2,0,1]))