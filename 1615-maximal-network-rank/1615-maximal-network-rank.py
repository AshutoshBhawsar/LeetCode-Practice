class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Brute Force
        hmap=collections.defaultdict(set)
        roadmap={}
        for i,j in roads:
            hmap[i].add(j)
            hmap[j].add(i)
            roadmap[str(i)+str(j)]=1
        
        answer=0
        for i in range(n):
            for j in range(i+1,n):
                temp=len(hmap[i])+len(hmap[j])
                if j in hmap[i]:
                    temp-=1
                    
                answer=max(temp,answer)
        return answer
            