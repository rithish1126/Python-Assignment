# Python-Assignment
Problem Statement :

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.
 


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.






Observation: We notice that all the O’s form islands or groups and X’s do so too, So now we need to make all the O’s present to X’s that are surrounded in four directions by X islands. Now we notice that the O’s that are to the side of the square can not obviously be surrounded by X’s so all the O islands that have one or more Os that border the side of the square can not be surrounded by Xs however the other islands will be turned to X.

Step one: find all the Os in the borders
Step two: Do a Depth first search from the above Os and turn them to Y
Step Three: Then Make the other O’s Xs and the Y’s Os
Code:-
class Solution(object):
  
   def solve(self, board):
       n=len(board)
       m=len(board[0])
       def dfs(board,i,j,n,m):
           if(i>=n or i<0 or j>=m or j<0 or board[i][j]!='O' ):
               return
           board[i][j]='Y'
           dfs(board,i-1,j,n,m)
           dfs(board,i+1,j,n,m)
           dfs(board,i,j-1,n,m)
           dfs(board,i,j+1,n,m)
       for i in range (0,n):
           for j in range (0,m):
               if (board[i][j]=='O' and (i in [0,n-1] or j in [0,m-1])):
                   dfs(board,i,j,n,m)
       for i in range (0,n):
           for j in range (0,m):
               if(board[i][j]=='Y'):
                   board[i][j]='O'
               else:
                   board[i][j]='X'  
