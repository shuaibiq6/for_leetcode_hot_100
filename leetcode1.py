#两数之和
# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那两个整数并返回他们的数组下标。
#哈希表  值：索引也就是key：value    定义的nums是 索引：值 因此出现nums[i]表示的是i索引对应的nums值
# 而hashmap[nums[i]]索引的是一个值
#值和索引都是确定的，只不过对应关系相反
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}                              #定义一个空的哈希表
        for i in range(len(nums)):              #遍历整个nums
            if target-nums[i] in hashmap:       #如果值已经被存入
                return [i,hashmap[target-nums[i]]]   #命中之后直接return保证返回结果只有一组
            else:
                hashmap[nums[i]] = i    #没有命中情况下nums[i]和i分别存入哈希表
# return [i,hashmap[target-nums[i]]]   返回的两个索引值前者来自nums列表后者来自哈希表
# 后者根据target-nums[i]得到值，返回索引
#初始hashmap是空的，所以正常执行应该是先else再命中执行return                    
#调用调试
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))    # 输出 [1, 0]
    print(sol.twoSum([3, 2, 4], 6))         # 输出 [2, 1]
    print(sol.twoSum([3, 3], 6))            # 输出 [1, 0]