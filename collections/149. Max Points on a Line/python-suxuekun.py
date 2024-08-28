class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points);
        m = 0;
        for i in range(l):
            if (l-i) <= m:
                break;
            h = {}
            p0=points[i]
            for j in range(i+1,l):
                p1 = points[j]
                dx = p1[0] - p0[0];
                dy = p1[1] - p0[1];
                if dx ==0:
                    dt = 100000;
                else:
                    dt = dy/dx
                h[dt] = h.get(dt,0) +1
                m = max(m,h[dt])
        return m + 1
                
                    
                
        