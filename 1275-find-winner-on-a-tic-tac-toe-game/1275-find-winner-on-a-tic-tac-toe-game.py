class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        m=len(moves)
        n=3
        row=[0]*n
        col=[0]*n
        diag=0
        antiDiag=0
        player=1
        for r,c in moves:
            row[r]+=player
            col[c]+=player
            if r==c:
                diag+=player
            if r+c==n-1:
                antiDiag+=player
            if abs(row[r])==n or abs(col[c])==n or abs(diag)==n or abs(antiDiag)==n:
                if player==1:
                    return "A"
                else:
                    return "B"
            
            
            player*=-1

        return "Draw" if m==n*n else "Pending"