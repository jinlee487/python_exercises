# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
# (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))
# 이 문제는 지금까지 심사문제 중에서 가장 어렵습니다. 
# 처음 풀어보는 경우 대략 두 시간은 걸립니다. 시간을 두고 천천히 고민해서 풀어보세요. 
# 지금까지 학습한 내용을 모두 동원해야 풀 수 있으며 막힐 때는 지금까지 학습한 내용을 다시 복습하면서 힌트를 찾아보세요.


def check(x,y,N,M):
    if x<0 or N<=x or y<0 or M<=y:
        return False
    return True

xarr = [-1,-1,-1,1,1,1,0,0]
yarr = [-1,1,0,-1,1,0,-1,1]

N,M = map(int,input().split(" "))
matrix = []
for i in range(0,N):
    matrix.append([char for char in input()])

for x in range(0,N):
    for y in range(0,M):
        if matrix[x][y]=='*':
            continue
        count = 0
        for i in range(0,8):
            nx = xarr[i]+x
            ny = yarr[i]+y
            if check(nx,ny,N,M)!=True:
                continue
            if matrix[nx][ny]=='*':
                count += 1
        matrix[x][y] = count

for i in matrix:
    for j in i:
        print(j,end="")
    print("")        