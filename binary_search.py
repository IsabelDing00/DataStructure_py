class Solution(object):
    # def sortedSquares(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     new_list = []
    #     for num in nums:
    #         j = num ** 2
    #         new_list.append(j)
    #         print(new_list)
    #
    #     new_list.sort()
    #
    #     return new_list

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = [0] * n
        i = 0
        for num in nums:
            ans[i] = nums[(i + k ) % n]
            i += 1
        return ans

#
# list1 = [1, 3, 5, 6]
# s = Solution()
# print(s.sortedSquares(list1))
#
# list2 = [0] * 5
# print(list2)
# print(3%7)
list3 = [1,2,3,4,5,6,7]
s = Solution()
print(s.rotate(list3, 3))