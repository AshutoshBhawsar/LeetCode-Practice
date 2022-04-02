class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        hmap={}
        result=[]
        for item in items:
            if item[0] not in hmap:
                hmap[item[0]]=[item[1]]
            else:
                hmap[item[0]].append(item[1])
        for key,values in hmap.items():
            if len(values)>5:
                values=sorted(values,reverse=True)[:5]
            avg1=sum(values)//len(values)
            result.append([key,avg1])
        return result