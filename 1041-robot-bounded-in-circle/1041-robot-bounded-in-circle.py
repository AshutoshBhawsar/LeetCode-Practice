class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x,y=0,0
        dirX,dirY=0,1
        for i in instructions:
            if i=='G':
                x+=dirX
                y+=dirY
            elif i=='L':
                dirX,dirY=-1*dirY,dirX
            else:
                dirX,dirY=dirY,-1*dirX
        return (x,y)==(0,0) or (dirX,dirY)!=(0,1)