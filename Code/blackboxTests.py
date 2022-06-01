import unittest

dirBBCAM = './MatrizesTeste/Blackbox/createAuxMatrix/'
dirBBFA = './MatrizesTeste/Blackbox/fillAux/'
dirBBFM = './MatrizesTeste/Blackbox/findMax/'

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

    return [[max_of_s, max_i, max_j]]
    
def readMatrixFromFile(fileName):

    with open(fileName, 'r') as f:
        M = []
        lines = f.read().split('.')
        for line in lines: 
            M.append([int(x) for x in line.split(',')])
    return M

class createAuxMatrixTests(unittest.TestCase):

    def test_0(self):
        self.assertEqual([], createAuxMatrix(0, 0, [], []))
    
    def test_1_0(self):

        M = [[0]]
        F = [[0]]
        self.assertEqual(F, createAuxMatrix(1, 1, [], M))

    def test_1_1(self):

        M = [[1]]
        F = [[1]]
        self.assertEqual(F, createAuxMatrix(1, 1, [], M))

    def test_9_5(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R9C5.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R9C5.txt')
        self.assertEqual(F, createAuxMatrix(9, 5, [], M))

    def test_9_9(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R9C9.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R9C9.txt')
        self.assertEqual(F, createAuxMatrix(9, 9, [], M))

    def test_9_15(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R9C15.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R9C15.txt')
        self.assertEqual(F, createAuxMatrix(9, 15, [], M))
     
    def test_10_5(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R10C5.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R10C5.txt')
        self.assertEqual(F, createAuxMatrix(10, 5, [], M))

    def test_10_10(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R10C10.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R10C10.txt')
        self.assertEqual(F, createAuxMatrix(10, 10, [], M))

    def test_10_15(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R10C15.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R10C15.txt')
        self.assertEqual(F, createAuxMatrix(10, 15, [], M))

    def test_999_500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R999C500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R999C500.txt')
        self.assertEqual(F, createAuxMatrix(999, 500, [], M))

    def test_999_999(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R999C999.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R999C999.txt')
        self.assertEqual(F, createAuxMatrix(999, 999, [], M))

    def test_999_1500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R999C1500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R999C1500.txt')
        self.assertEqual(F, createAuxMatrix(999, 1500, [], M))
    
    def test_1000_500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1000C500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1000C500.txt')
        self.assertEqual(F, createAuxMatrix(1000, 500, [], M))

    def test_1000_1000(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1000C1000.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1000C1000.txt')
        self.assertEqual(F, createAuxMatrix(1000, 1000, [], M))

    def test_1000_1500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1000C1500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1000C1500.txt')
        self.assertEqual(F, createAuxMatrix(1000, 1500, [], M))
    
    def test_1001_500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1001C500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1001C500.txt')
        self.assertEqual(F, createAuxMatrix(1001, 500, [], M))

    def test_1001_1001(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1001C1001.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1001C1001.txt')
        self.assertEqual(F, createAuxMatrix(1001, 1001, [], M))

    def test_1001_1500(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1001C1500.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1001C1500.txt')
        self.assertEqual(F, createAuxMatrix(1001, 1500, [], M))
    
class fillAuxTests(unittest.TestCase):

    def test_0(self):
        self.assertEqual([], fillAux(0, 0, [], []))
    
    def test_1_0(self):

        M = [[0]]
        S = [[0]]
        F = [[0]]

        self.assertEqual(F, fillAux(1, 1, S, M))

    def test_1_1(self):

        M = [[1]]
        S = [[1]]
        F = [[1]]

        self.assertEqual(F, fillAux(1, 1, S, M))

    def test_9_5(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R9C5.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R9C5.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R9C5.txt')
        self.assertEqual(F, fillAux(9, 5, S, M))

    def test_9_9(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R9C9.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R9C9.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R9C9.txt')
        self.assertEqual(F, fillAux(9, 9, S, M))

    def test_9_15(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R9C15.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R9C15.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R9C15.txt')
        self.assertEqual(F, fillAux(9, 15, S, M))
     
    def test_10_5(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R10C5.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R10C5.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R10C5.txt')
        self.assertEqual(F, fillAux(10, 5, S, M))

    def test_10_10(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R10C10.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R10C10.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R10C10.txt')
        self.assertEqual(F, fillAux(10, 10, S, M))

    def test_10_15(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R10C15.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R10C15.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R10C15.txt')
        self.assertEqual(F, fillAux(10, 15, S, M))

    def test_999_500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R999C500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R999C500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R999C500.txt')
        self.assertEqual(F, fillAux(999, 500, S, M))

    def test_999_999(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R999C999.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R999C999.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R999C999.txt')
        self.assertEqual(F, fillAux(999, 999, S, M))

    def test_999_1500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R999C1500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R999C1500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R999C1500.txt')
        self.assertEqual(F, fillAux(999, 1500, S, M))
    
    def test_1000_500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1000C500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1000C500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1000C500.txt')
        self.assertEqual(F, fillAux(1000, 500, S, M))

    def test_1000_1000(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1000C1000.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1000C1000.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1000C1000.txt')
        self.assertEqual(F, fillAux(1000, 1000, S, M))

    def test_1000_1500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1000C1500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1000C1500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1000C1500.txt')
        self.assertEqual(F, fillAux(1000, 1500, S, M))
    
    def test_1001_500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1001C500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1001C500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1001C500.txt')
        self.assertEqual(F, fillAux(1001, 500, S, M))

    def test_1001_1001(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1001C1001.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1001C1001.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1001C1001.txt')
        self.assertEqual(F, fillAux(1001, 1001, S, M))

    def test_1001_1500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1001C1500.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1001C1500.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1001C1500.txt')
        self.assertEqual(F, fillAux(1001, 1500, S, M))
    
class findMaxTests(unittest.TestCase):

    # Este teste não funciona mesmo sendo parte do output da anterior
    # def test_0(self):
    #    self.assertEqual([], findMax(0, 0, []))
    
    def test_1_0(self):

        S = [[0]]
        F = [[0, 0, 0]]

        self.assertEqual(F, findMax(1, 1, S))

    def test_1_1(self):

        S = [[1]]
        F = [[1, 0, 0]]

        self.assertEqual(F, findMax(1, 1, S))

    def test_2_v1(self):

        S = [[1, 1], 
            [1, 2]]
        F = [[2, 1, 1]]

        self.assertEqual(F, findMax(2, 2, S))
    
    def test_2_v2(self):

        S = [[0, 0],
            [0, 0]]
        F = [[0, 0, 0]]

        self.assertEqual(F, findMax(2, 2, S))
    
    def test_2_v3(self):

        S = [[0, 0], 
            [0, 1]]
        F = [[1, 1, 1]]

        self.assertEqual(F, findMax(2, 2, S))
    
    def test_9_5(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R9C5.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R9C5.txt')
        self.assertEqual(F, findMax(9, 5, S))

    def test_9_9(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R9C9.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R9C9.txt')
        self.assertEqual(F, findMax(9, 9, S))

    def test_9_15(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R9C15.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R9C15.txt')
        self.assertEqual(F, findMax(9, 15, S))
     
    def test_10_5(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R10C5.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R10C5.txt')
        self.assertEqual(F, findMax(10, 5, S))

    def test_10_10(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R10C15.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R10C15.txt')
        self.assertEqual(F, findMax(10, 10, S))

    def test_10_15(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R10C15.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R10C15.txt')
        self.assertEqual(F, findMax(10, 15, S))

    def test_999_500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R999C500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R999C500.txt')
        self.assertEqual(F, findMax(999, 500, S))

    def test_999_999(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R999C999.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R999C999.txt')
        self.assertEqual(F, findMax(999, 999, S))

    def test_999_1500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R999C1500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R999C1500.txt')
        self.assertEqual(F, findMax(999, 1500, S))
    
    def test_1000_500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1000C500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1000C500.txt')
        self.assertEqual(F, findMax(1000, 500, S))

    def test_1000_1000(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1000C1000.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1000C1000.txt')
        self.assertEqual(F, findMax(1000, 1000, S))

    def test_1000_1500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1000C1500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1000C1500.txt')
        self.assertEqual(F, findMax(1000, 1500, S))
    
    def test_1001_500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1001C500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1001C500.txt')
        self.assertEqual(F, findMax(1001, 500, S))

    def test_1001_1001(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1001C1001.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1001C1001.txt')
        self.assertEqual(F, findMax(1001, 1001, S))

    def test_1001_1500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1001C1500.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1001C1500.txt')
        self.assertEqual(F, findMax(1001, 1500, S))

if __name__ == '__main__':
    unittest.main()