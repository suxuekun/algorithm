class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        def copy(l):
            return [x for x in l]

        global results
        results = [];
        def backtrack(res,tar,y):
            global results
            if (tar ==0):
                results.append(res)
                return
            for x in candidates:
                if y<= x <=tar:
                    l = copy(res)
                    l.append(x)
                    backtrack(l,tar-x,x)
        backtrack([],target,0)
        return results
            