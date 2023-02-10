n=int(input("Enter the number of rows")) #the number of rows required for the board
m=int(input("Enter the number of columns")) #the number of columns required for the board
board=[]
charsurround='X'
charnonsurround='O'
visitedchar='Y'
for i in range(0,n):     #taking input of the board row wise 
    temp=[]
    for j in range (0,m):
        temp.append(input())
    board.append(temp)
n=len(board)
m=len(board[0])
print(board)
def dfs(board,i,j,n,m): #DFS to go through all the four sides of the 'O' and mark them as viisted by marking them as 'Y'
    if(i>=n or i<0 or j>=m or j<0 or board[i][j]!='O' ): 
        return
    board[i][j]=vistedchar
    dfs(board,i-1,j,n,m)
    dfs(board,i+1,j,n,m)
    dfs(board,i,j-1,n,m)
    dfs(board,i,j+1,n,m)
for i in range (0,n):
  for j in range (0,m):   
    if (board[i][j]==charnonsurround and (i in [0,n-1] or j in [0,m-1])):  #checking if we are at the borders and find 'O' to do a dfs
        dfs(board,i,j,n,m) 
for i in range (0,n):
    for j in range (0,m):
        if(board[i][j]==visitedchar):   #then turn all non visited 'O's to X and the visited ones to 'O'
            board[i][j]=charnonsurround
        else:
            board[i][j]=charsurround
print(board)
        
        
