class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(board, word, z, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[z] != board[i][j]:
                return
            #print(word[z])
            
            if len(word) == z+1:
                return True
            temp=board[i][j]
            board[i][j]="0"
            a=helper(board, word, z + 1, i + 1, j)
            board[i][j]=temp
            
            temp=board[i][j]
            board[i][j]="0"
            b=helper(board, word, z + 1, i, j + 1)
            board[i][j]=temp
            
            temp=board[i][j]
            board[i][j]="0"
            c=helper(board, word, z + 1, i - 1, j)
            board[i][j]=temp
            
            temp=board[i][j]
            board[i][j]="0"
            d=helper(board, word, z + 1, i, j - 1)
            board[i][j]=temp
            return a or b or c or d

        for i in range(len(board)):
            for j in range(len(board[0])):
                flag = helper(board, word, 0, i, j)
                if flag:
                    return True
        return False