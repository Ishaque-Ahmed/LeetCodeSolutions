class Solution(object):
    def longestMountain(self, arr):
        answer = 0

        for i in range (1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i+1]:
                leftP = rightP = i

                while leftP > 0 and arr[leftP] > arr [leftP - 1]:
                    leftP -= 1
                
                while rightP < len(arr) - 1 and arr[rightP] > arr[rightP + 1]:
                    rightP += 1
                
                answer =  max(answer, rightP - leftP + 1)
        return answer
        