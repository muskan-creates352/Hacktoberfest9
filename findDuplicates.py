class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []   #return time of func will never count in space coplexitxity
        for num in nums:
            index = abs(num) - 1
            if nums[index]<0:
                duplicates.append(abs(num))
            else:
                nums[index] *= -1
        return duplicates
