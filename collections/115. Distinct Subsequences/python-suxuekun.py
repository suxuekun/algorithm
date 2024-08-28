class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)
        d = []
        c = {}
        for i in range(tl):
            if (c.get(t[i]) == None):
                c[t[i]] = {
                    'c1':0,
                    'c2':0,
                    'c':1,
                }
            c[t[i]]['c1']+=1
        for j in range(sl):
            if (c.get(s[j]) != None):
                c[s[j]]['c2'] +=1
        
        for k in c:
            e = c[k];
            e['c'] = e['c2']-e['c1']+1;
        
        skip = {}
        for i in range(tl):
            d.append([])
            if (skip.get(t[i]) == None):
                skip[t[i]] = 0;
            else:
                skip[t[i]]+=1
            skipped = 0;
            for j in range(sl):
                
                
                if (t[i] == s[j]):
                    if skipped < skip[t[i]]:
                        skipped +=1
                        continue
                    pos = j;
                    d[i].append([pos,0])
                    if len(d[i]) >= c[t[i]]['c']:
                        break;
                        
        for j in range(len(d[0])):
            d[0][j][1] = 1;
        # for i in range(len(d)):
        #     print(d[i])
            
        for i in range(1,len(d)):
            hash_k = 0;
            last_element = [0,0];
            for j in range(len(d[i])):
                element = d[i][j];
                pos = element[0]
                element[1] = last_element[1];
                for k in range(hash_k,len(d[i-1])):
                    pre_element = d[i-1][k]
                    # print(hash_k,'--',i-1,k,'---',i,j,pre_element,d[i])
                    pre_pos = pre_element[0]
                    if pre_pos >= pos:
                        k=k-1;
                        break;
                    element[1]+=pre_element[1]
                hash_k = k+1;
                last_element = element
        sum = 0
        # for i in range(len(d)):
        #     print(d[i])
        for j in range(len(d[-1])):
            sum += d[-1][j][1];
        return sum;

#     b   0 2 4  1 1 1    
#     a   1 5    1 3
#     g   3 6    1 2
    
    
#     b 0 1 3     
#     a 1 1 2
#     b 2 1 2
            
        
#     r 0 1 1 1         
#     a 1 1 1 1
#     b 2 2 3 (3-2+1) = 2
#     i 4 1 1 1
#     t 5 1 1 1
        
#     r  0       1
#     a  1       1
#     b  2 3     1 1
#     b  3 4     1 2
#     i  5       3
#     t  6       3
    
    
#     a  0 2 4          1 1 1
#     b  3 5 6 7 8      2 3 3 3 3
#     b  3 5 6 7 8      0 1 2 3 4
#     b  3 5 6 7 8      0 1 2 3 4
#     b  3 5 6 7 8      0 1 2 3 4
#     c  1 9            0 5
#     d  10             
            
        
        