class Solution:
    def bbox(self,c):
        return [c[0]-c[2],c[1]-c[2],c[0]+c[2],c[1]+c[2]];
    def incircle(self,c,i,j):
        x = i-c[0];
        y = j-c[1];
        return c[2]**2 >= x**2 + y **2;
        
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        h = {}
        count = 0;
        for c in circles:
            bbox = self.bbox(c);
            for x in range(bbox[0],bbox[2]+1):
                for y in range(bbox[1],bbox[3]+1):
                    key = str(x)+"_"+str(y)
                    if h.get(key):
                        continue
                    if self.incircle(c,x,y):
                        count+=1
                        h[key] = True
        return count
                    
        