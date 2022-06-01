import numpy as np

def createAuxMatrix(R, C, S, M):
    for i in range(R):
        temp = []
        for j in range(C):
            if i==0:
                temp += M[i][j],
            elif j==0:
                temp += M[i][j],
            else:
                temp += 0,
        S += temp,
    return S

def fillAux(R, C, S, M):
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
    return S

def findMax(R, C, S):
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    return [max_of_s, max_i, max_j]
    
def generateMatrixOf(R, C, N):
    M = []
    for i in range(R):
        arr = []
        for j in range(C):
            arr.append(N)
        M.append(arr)
    return M

def matrixToString(M, R, C):
    s = ''
    for i in range(R):
        for j in range(C):
            s += str(M[i][j])
            if j != C-1:
                s += ','
        if i != R-1:
            s += '.'
    return s

def main():
    Rval = [5, 10, 1000]
    Cval = {
        5 : [3],
        10 : [10],
        1000 : [1500],
    }

    for R in Rval:
        for C in Cval[R]:

            #fileNameM = './MatrizesTeste/ControlFlow/findMax/matrizM_R' + str(R) + 'C' + str(C) + '_0.txt'
            fileNameS = './MatrizesTeste/ControlFlow/findMax/matrizS_R' + str(R) + 'C' + str(C) + '_0.txt'
            fileNameF = './MatrizesTeste/ControlFlow/findMax/matrizF_R' + str(R) + 'C' + str(C) + '_0.txt'

            with open(fileNameS, 'w') as s, open(fileNameF, 'w') as f:

                M = generateMatrixOf(R, C, 0)
                #M = np.mod(np.random.permutation(R*C).reshape(R,C),2)
                #m.write(matrixToString(M, R, C))

                S = createAuxMatrix(R, C, [], M)
                #s.write(matrixToString(S, R, C))

                S = fillAux(R, C, S, M)
                s.write(matrixToString(S, R, C))

                F = findMax(R, C, S)
                f.write(str(F[0]) + ',' + str(F[1]) + ',' + str(F[2]))

if __name__ == '__main__':
    main()