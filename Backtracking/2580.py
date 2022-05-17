from re import T
import sys
from tokenize import blank_re
arr = []
blank = []
for _ in range(9):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
print(arr)

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))  #빈칸 체크 
print(blank)

def rowcheck(x,a):
    for i in range(9):
        if(a == arr[x][i]):
            return False
        return True
# def rectcheck():



# def colcheck():
