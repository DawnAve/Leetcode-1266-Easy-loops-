class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def visit(a,b,time):
            x = abs(a[0] - b[0])
            y = abs(a[1]-b[1])
            time += max(x,y)
            return time
        time = 0
        for i in range(len(points)-1):
            time = visit(points[i], points[i+1], time)
        return time

        
