class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.helper(image,sr,sc,newColor,image[sr][sc])        
        return image
    
    def helper(self,image,i,j,newColor,sameColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=sameColor or image[i][j]==newColor:
            return
        image[i][j]=newColor
        self.helper(image,i+1,j,newColor,sameColor)
        self.helper(image,i,j+1,newColor,sameColor)
        self.helper(image,i-1,j,newColor,sameColor)
        self.helper(image,i,j-1,newColor,sameColor)
        
        