import random
path_log = []
def generateMatrix(m,n):
    inc = 0
    row = []
    gen_mat = []
    for i in range(0,m):
        for j in range(0,n):
            element = (m*n) + inc
            row.append(element)
            inc-=1
        gen_mat.append(row)
        row = []
    return gen_mat

def annealing(mat,i,j,m,n,path):
    T = 100
    c = 0.1
    opt = [0,1]
    curr = mat[i][j]
    possibleEle = [[i,j+1],[i+1,j]]
    while curr != 1:
        draw = random.choice(possibleEle)
        if draw[0]<m and draw[1]<n:
            nex_i = draw[0]
            nex_j = draw[1]
            pos_next_curr = mat[nex_i][nex_j]
            del_E = curr - pos_next_curr
            if pos_next_curr == 1:
                path.append(pos_next_curr)
                break
            else:
                T = 0.9*T
                if del_E > 0 or random.choice(opt) < 2.718^((-c*del_E)/T):
                    path.append(pos_next_curr)
                    annealing(mat,nex_i,nex_j,m,n,path)
                else:
                    continue
            break
        else:
            continue

    return path

a = int(input('Row (define m)'))
b = int(input('column (define n)'))
matrix = generateMatrix(a,b)
for ele in matrix:
    print ('\n',ele,'\n')

path_log.append(a*b)
k = annealing(matrix,0,0,a,b,path_log)
print('path followed',k)
