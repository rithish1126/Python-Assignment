n=int(input("Enter the number of rows"))
m=int(input("Enter the number of columns"))
board=[]
for i in range(0,n):
    temp=[]
    for j in range (0,m):
        temp.append(input())
    board.append(temp)
n=len(board)
m=len(board[0])
print(board)
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
print(board)
        
        
