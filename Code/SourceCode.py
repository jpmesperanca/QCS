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
            

def fillAux(R, C, S, M):
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

                
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

    return max_of_s, max_i, max_j

''' 
def printMaxSubSquare(M, max_of_s, max_i, max_j):

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print (M[i][j], end = " ")
        print("")
'''

def main(M):
    R = len(M)
    C = len(M[0])
    S = []

    createAuxMatrix(R, C, S, M)
    fillAux(R, C, S, M)
    max_of_s, max_i, max_j = findMax(R, C, S)

    #printMaxSubSquare(M, max_of_s, max_i, max_j)


if __name__ == '__main__':
    M = [[0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

    main(M)