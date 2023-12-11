m=int(input("Enyter The Number Row"))
n=int(input("Enter The Numebr of Col"))
matrix=[]
for i in range(m):
    Row=[]
    for j in range(n):
        Row.append(int(input()))
    matrix.append(Row)

for i in range(m):
    for j in range(n):
        print(matrix[i][j] ,end=" ")
    print()