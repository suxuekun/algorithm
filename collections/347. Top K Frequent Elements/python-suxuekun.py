class Solution:
    
    def bucket_solution(self,nums,k):
        cnt = Counter(nums);
        
        n = len(nums)
        l = len(cnt)
        
        m = n-l+1
        
        buckets = [[] for _ in range(m+1)]
        
        for num,freq in cnt.items():
            buckets[freq].append(num)
                              
        res = []
        for i in range(m,0,-1):
            if not buckets[i]:
                continue
            c = len(buckets[i])
            if len(res)+c <= k:
                res += buckets[i]
                if len(res) == k:
                    break
            else:
                for t in range(k - len(res) +1):
                    res.append(buckets[i][t])
        return res
    
    def maxheap_solution(self,nums,k):
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap)
            ans.append(num)
        return ans
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.maxheap_solution(nums,k)
        return self.bucket_solution(nums,k)
            
        