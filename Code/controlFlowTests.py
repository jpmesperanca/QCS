import unittest

dirBBCAM = './MatrizesTeste/ControlFlow/createAuxMatrix/'
dirBBFA = './MatrizesTeste/ControlFlow/fillAux/'
dirBBFM = './MatrizesTeste/ControlFlow/findMax/'

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
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
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

    # Path 2 non-feasable 
    # Path 4 non-feasable
    # Path 5 non-feasable

    def test_path1(self):

        M = [[]]
        F = []
        self.assertEqual(F, createAuxMatrix(0, 0, [], M))

    def test_path3_1(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1C1.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1C1.txt')
        self.assertEqual(F, createAuxMatrix(1, 1, [], M))

    def test_path3_10(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1C10.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1C10.txt')
        self.assertEqual(F, createAuxMatrix(1, 10, [], M))

    def test_path3_1000(self):

        M = readMatrixFromFile(dirBBCAM + 'matrizM_R1C1000.txt')
        F = readMatrixFromFile(dirBBCAM + 'matrizF_R1C1000.txt')
        self.assertEqual(F, createAuxMatrix(1, 1000, [], M))

class fillAuxTests(unittest.TestCase):

    def test_path1_0x0(self):

        M = [[]]
        F = []
        self.assertEqual(F, fillAux(0, 0, [], M))

    def test_path1_1x1_1(self):

        M = [[1]]
        F = [[1]]
        self.assertEqual(F, fillAux(1, 1, [[1]], M))
    
    def test_path1_1x1_2(self):

        M = [[0]]
        F = [[0]]
        self.assertEqual(F, fillAux(1, 1, [[0]], M))

    # Path 2 non-feasable

    def test_path3_5x3(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R5C3_1.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R5C3_1.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R5C3_1.txt')
        self.assertEqual(F, fillAux(5, 3, S, M))

    
    def test_path3_10x10(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R10C10_1.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R10C10_1.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R10C10_1.txt')
        self.assertEqual(F, fillAux(10, 10, S, M))
    
    def test_path3_1000x1500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1000C1500_1.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1000C1500_1.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1000C1500_1.txt')
        self.assertEqual(F, fillAux(1000, 1500, S, M))

    def test_path4_5x3(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R5C3_0.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R5C3_0.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R5C3_0.txt')
        self.assertEqual(F, fillAux(5, 3, S, M))

    
    def test_path4_10x10(self):
        
        M = readMatrixFromFile(dirBBFA + 'matrizM_R10C10_0.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R10C10_0.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R10C10_0.txt')
        self.assertEqual(F, fillAux(10, 10, S, M))
    
    def test_path4_1000x1500(self):

        M = readMatrixFromFile(dirBBFA + 'matrizM_R1000C1500_0.txt')
        S = readMatrixFromFile(dirBBFA + 'matrizS_R1000C1500_0.txt')
        F = readMatrixFromFile(dirBBFA + 'matrizF_R1000C1500_0.txt')
        self.assertEqual(F, fillAux(1000, 1500, S, M))

class findMaxTests(unittest.TestCase):

    # ERROR
    #def test_0(self):
    #    M = [[]]
    #    F = [[-1, -1, -1]]
    #    self.assertEqual(F, findMax(0, 0, []))

    # Path 2 non-feasable

    def test_path3_5x3(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R5C3_0.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R5C3_0.txt')
        self.assertEqual(F, findMax(5, 3, S))

    
    def test_path3_10x10(self):
        
        S = readMatrixFromFile(dirBBFM + 'matrizS_R10C10_0.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R10C10_0.txt')
        self.assertEqual(F, findMax(10, 10, S))
    
    def test_path3_1000x1500(self):

        S = readMatrixFromFile(dirBBFM + 'matrizS_R1000C1500_0.txt')
        F = readMatrixFromFile(dirBBFM + 'matrizF_R1000C1500_0.txt')
        self.assertEqual(F, findMax(1000, 1500, S))

    def test_path4(self):

        S = [[1]]
        F = [[1, 0, 0]]
        self.assertEqual(F, findMax(1, 1, S))

if __name__ == '__main__':
    unittest.main()