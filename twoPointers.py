class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        print(j)
        while i < j:
            print(nums, i)
            if nums[i] == 0:
                print("before del: %s" % nums)
                del nums[i]
                print("after del: %s" % nums)
                nums.append(0)
            i+=1
        return nums

list1 = [0,0,1]
s = Solution()
result = s.moveZeroes(list1)
print(result)