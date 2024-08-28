class Solution:
    # def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    #     hw = {}
    #     hl = {}
    #     for i in matches:
    #         w = i[0]
    #         l = i[1]
    #         hw[w] = 1
    #         if not hl.get(l):
    #             hl[l] = 0
    #         hl[l] +=1
    #     for i in hw:
    #         if not hl[i]:
    #             h


    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        h = {}
        for i in matches:
            w = i[0]
            l = i[1]
            if not h.get(w):
                h[w] = [0,0]
            h[w][0] +=1
            if not h.get(l):
                h[l] = [0,0]
            h[l][0] +=1
            h[l][1] +=1
        answers = [[],[]]
        for i in h:
            if h[i][0] >0:
                if h[i][1] ==0:
                    answers[0].append(i)
                if h[i][1] ==1:
                    answers[1].append(i)
        answers[0].sort()
        answers[1].sort()
        return answers