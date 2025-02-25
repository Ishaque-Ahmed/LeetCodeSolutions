class Solution(object):
    def spiralOrder(self, matrix):
        spiralOrder = []

        while matrix:
            spiralOrder += matrix.pop(0)
            # print(spiralOrder)
            
            if matrix and matrix[0]:
                for row in matrix:
                    # print(row)
                    spiralOrder.append(row.pop()) 
            
            if matrix:
                spiralOrder += (matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    # print(row)
                    spiralOrder.append(row.pop(0))
        # print(spiralOrder)

        return spiralOrder
        