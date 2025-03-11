class Solution(object):
    def sortedSquares(self, nums):
        answerArray = collections.deque()

        leftP = 0
        rightP = len(nums)-1

        while leftP <= rightP:
            leftValue = abs(nums[leftP])
            rightValue = abs(nums[rightP])   

            if leftValue > rightValue:
                answerArray.appendleft(leftValue * leftValue)
                leftP += 1
            else: 
                answerArray.appendleft(rightValue * rightValue)
                rightP -= 1

        return list(answerArray)