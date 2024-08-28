class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        
        # 反向mapping ，value==>index
        idx = {j:i for i,j in enumerate(nums) }
        # 长度
        n = len(nums);
        # 结果全给1
        res = [1]*n
        # 记录路径（从node开始的所有父亲节点）
        route = {}
        # 取value为1的点，记录该点
        node = i = idx.get(1);
        
        #没有1就直接返全1的结果了
        if node == None:
            return res;
        #有1，则向上爬1的parent路径并记录在route里
        while i != -1:
            route[i] = True
            i = parents[i]
        #从2开始
        for v in range(2,n+1):
            i = idx.get(v)
            #如果没有对应值则结束（中间缺少值的情况，例如123 567，缺4，到4就停了）
            if i == None:
                v = v-1;
                break;
            #如果有对应值，从i向上爬，直到找到i和node共同的父亲节点（route内的节点）
            while i!=-1 :
                if route.get(i):
                    # 找到共同父亲节点后，把上一个node向上爬树到该节点，路径上都赋值给当前值
                    while True:
                        res[node] = v
                        if node == i:
                            break;
                        # 丢弃交叉节点以下的节点（route为当前node的所有父亲节点，所以删除路过的节点）
                        route[node] = False;
                        node = parents[node]
                    break     
                i = parents[i]
        #跟节点给最大值
        res[0] = v+1;
        return res