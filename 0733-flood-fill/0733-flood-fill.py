class Solution:
    def __init__(self):
        self.visited={}
        self.answer=None
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel_color=image[sr][sc]
        self.answer=image
        self.helper(image,sr,sc,color,pixel_color)
        return self.answer
                
        
    def helper(self,image,i,j,color,pixel_color):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=pixel_color or (i,j) in self.visited:
            return
        image[i][j]=color
        self.answer[i][j]=color
        self.visited[(i,j)]=1
        self.helper(image,i+1,j,color,pixel_color)
        self.helper(image,i,j+1,color,pixel_color)
        self.helper(image,i,j-1,color,pixel_color)
        self.helper(image,i-1,j,color,pixel_color)