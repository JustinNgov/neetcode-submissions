class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle =[[1]]
        for i in range(numRows-1):
            prev = triangle[-1]
            new_row =[1]
            for j in range(len(prev) - 1):
                new_row.append(prev[j] + prev[j+1])
            new_row.append(1)

            triangle.append(new_row)
        return triangle