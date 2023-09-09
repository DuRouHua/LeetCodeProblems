class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            if i and nums[i] == nums[i-1]: 
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if (nums[j] + nums[k] > - nums[i]):
                    k-=1
                elif (nums[j] + nums[k] < - nums[i]):
                    j+=1
                else:
                    ans.append([nums[i], nums[j],nums[k]])
                    while (j < k and nums[j] == nums[j+1]):
                        j+=1
                    while (j < k and nums[k] == nums[k-1]):
                        k-=1
                    j+=1
                    k-=1
        return ans
        