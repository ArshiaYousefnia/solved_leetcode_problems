class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            leng = len(triangle[i])
            for j in range(1, leng - 1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i][leng - 1] += triangle[i - 1][leng - 2]
        
        return min(triangle[len(triangle) - 1])
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         fringe = [(0, 0, triangle[0][0])]
#         n = len(triangle) - 1

#         minimum = None

#         while len(fringe) != 0:
#             result = self.expand_node(fringe, triangle, n)
#             if result != None:
#                 if minimum is None:
#                     minimum = result
#                 else:
#                     minimum = min(result, minimum)
        
#         return minimum
    
#     def expand_node(self, fringe, triangle, n):
#         node = fringe.pop()

#         if node[0] == n:
#             return node[2]
        
#         fringe += [(node[0] + 1, node[1], node[2] + triangle[node[0] + 1][node[1]]), 
#         (node[0] + 1, node[1] + 1, node[2] + triangle[node[0] + 1][node[1] + 1])
#         ]

#         return None


        