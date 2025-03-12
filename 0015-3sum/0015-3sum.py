class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []

        for index, val in enumerate(nums):
            if index > 0 and val == nums[index-1]:
                continue
            
            leftP = index + 1
            rightP = len(nums) -1

            while leftP < rightP:
                
                curSum = val + nums[leftP] + nums[rightP]

                if curSum > 0:
                    rightP -= 1
                elif curSum < 0:
                    leftP += 1
                else:
                    answer.append([val, nums[leftP], nums[rightP]])
                    leftP += 1
                    while leftP < rightP and nums[leftP] == nums[leftP - 1]:
                        leftP += 1
                    
                    
        return answer

        
        