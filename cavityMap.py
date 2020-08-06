def cavityMap(grid):
    l,l1=[],[]
    n=len(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(int(grid[i][j]))
        l1.append(l)
        l=[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if(int(l1[i][j]) > int(l1[i+1][j]) and int(l1[i][j]) > int(l1[i-1][j]) and int(l1[i][j]) > int(l1[i][j+1]) and int(l1[i][j]) > int(l1[i][j-1])):
                l1[i][j]=1000000000
    return(l1)


n = int(input())
grid = []
for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

result = cavityMap(grid)

for i in range(n):
    for j in range(n):
        if(result[i][j]==1000000000):
            print('X',end='')
        else:
            print(str(result[i][j]),end='')
    print()

