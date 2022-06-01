import unittest

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

    return max_of_s, max_i, max_j

class createAuxMatrixTests(unittest.TestCase):
    
    # Path 1 unfeasable - C não pode ser 0 quando R != 0
 
    def test_path2_1(self):

        expectedTemp = []
        S = []
        M = [[1]]
        C = 1
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path2_2(self):

        expectedTemp = []
        S = []
        M = [[0, 0, 0, 0, 0], 
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1]]
        C = 5
        R = 3

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    if j == 0:
                        self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path2_3(self):

        expectedTemp = []
        S = []
        M = [[1, 1, 0, 0, 1], 
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
        C = 5
        R = 5

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    if j == 0:
                        self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    # Path 3 unfeasable - temp não pode vir do node 4 diretamente para o 9, 
    # visto que o if i == 0 tem precedencia sobre o else e i é sempre iniciado a 0

    # Matriz 1x1
    def test_path4_1(self):

        S = []
        M = [[1]]
        C = 1
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path4_2(self):

        S = []
        M = [[0, 1, 0, 0, 1]]
        C = 5
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path4_3(self):

        S = []
        M = [[1, 0, 1, 0, 0, 1, 1, 1, 0, 1]]
        C = 10
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path5_1(self):

        S = []
        M = [[1], [0]]
        C = 1
        R = 2

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                    expectedTemp = temp
                else:
                    temp += 0,
            if (i != 0):
                self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path5_2(self):

        S = []
        M = [[1], [0], [1], [1], [0]]
        C = 1
        R = 5

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                    expectedTemp = temp
                else:
                    temp += 0,
            if (i != 0):
                self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path5_3(self):

        S = []
        M = [[0], [0], [1], [1], [0], [1], [0], [0], [0], [1]]
        C = 1
        R = 10

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    temp += M[i][j],
                    expectedTemp = temp
                else:
                    temp += 0,
            if (i != 0):
                self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path6_1(self):

        S = []
        M = [[1, 0]]
        C = 2
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    if j != 0:
                        self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path6_2(self):

        S = []
        M = [[0, 1, 0, 0, 0, 1, 1, 0, 1, 1]]
        C = 10
        R = 1

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    if j != 0:
                        self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            self.assertEqual(expectedTemp, temp)
            S += temp,

    def test_path6_3(self):

        S = []
        M = [[1, 1, 0, 0, 1], 
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
        C = 5
        R = 5

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    if j != 0:
                        self.assertEqual(expectedTemp, temp)
                    temp += M[i][j],
                    expectedTemp = temp
                elif j==0:
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,
    
    def test_path7_1(self):

        S = []
        M = [[1], [0]]
        C = 1
        R = 2

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i == 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path7_2(self):

        S = []
        M = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
        C = 3
        R = 3

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i == 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path7_3(self):

        S = []
        M = [[1, 1, 0, 0, 0], 
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0]]
        C = 5
        R = 5

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i == 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    # Path 8 unfeasable: o i == 0 tem sempre precedencia sobre o j == 0, logo, não dá para ir do node 9 para o 8

    def test_path9_1(self):

        S = []
        M = [[1], [0]]
        C = 1
        R = 2

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i != 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path9_2(self):

        S = []
        M = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
        C = 3
        R = 3

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i != 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,

    def test_path9_3(self):

        S = []
        M = [[1, 1, 0, 0, 0], 
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0]]
        C = 5
        R = 5

        for i in range(R):
            temp = []
            for j in range(C):
                if i==0:
                    temp += M[i][j],
                elif j==0:
                    if i != 1:
                        self.assertEqual([], temp)
                    temp += M[i][j],
                else:
                    temp += 0,
            S += temp,


class fillAuxTests(unittest.TestCase):

    def test_path1_1(self):

        expectedS = [[1, 1], 
                    [1, 0]]
        S = [[1, 1], 
            [1, 0]]
        M = [[1, 1], 
            [1, 1]]
        C = 2
        R = 2

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0

    def test_path1_2(self):

        expectedS = [[0, 0], 
                    [0, 0]]
        S = [[0, 0], 
            [0, 0]]
        M = [[0, 0], 
            [0, 1]]
        C = 2
        R = 2

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0

    def test_path1_3(self):

        expectedS = [[1, 1, 0, 0, 1], 
                    [1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0]]

        S = [[1, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]

        M = [[1, 1, 0, 0, 1], 
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0]]

        C = 5
        R = 3

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if (j == 1 and i == 1):
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0

    def test_path2_1(self):

        expectedS = [[1, 1, 0], 
                    [1, 2, 0]]

        S = [[1, 1, 0], 
            [1, 0, 0]]

        M = [[1, 1, 0], 
            [1, 1, 1]]

        C = 3
        R = 2

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if j != 1:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0

    def test_path2_2(self):

        expectedS = []

        S = [[1, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]

        M = [[1, 1, 0, 0, 1], 
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]

        C = 5
        R = 5

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if expectedS != []:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                    expectedS = S[:]
                else:
                    S[i][j] = 0

    def test_path2_3(self):

        expectedS = []

        S = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

        M = [[0, 0, 0, 0, 0], 
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1]]

        C = 5
        R = 3

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if expectedS != []:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                    expectedS = S[:]
                else:
                    S[i][j] = 0
 
    def test_path3_1(self):

        expectedS = [[1, 1, 0], 
                    [1, 0, 0]]

        S = [[1, 1, 0], 
            [1, 0, 0]]

        M = [[1, 1, 0], 
            [1, 0, 1]]

        C = 3
        R = 2

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if j != 1:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0

    def test_path3_2(self):

        expectedS = []

        S = [[1, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]

        M = [[1, 1, 0, 0, 1], 
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1]]

        C = 5
        R = 5

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if expectedS != []:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0
                    expectedS = S[:]

    def test_path3_3(self):

        expectedS = []

        S = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

        M = [[0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1]]

        C = 5
        R = 3

        for i in range(1, R):
            for j in range(1, C):
                if (M[i][j] == 1):
                    if expectedS != []:
                        self.assertEqual(expectedS, S)
                    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
                else:
                    S[i][j] = 0
                    expectedS = S[:]

class findMaxTests(unittest.TestCase):

    def test_path1_1(self):

        expectedMaxS = 1
        S = [[1, 1], 
            [1, 2]]
        C = 2
        R = 2

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

    def test_path1_2(self):

        expectedMaxS = 0
        S = [[0, 1], 
            [1, 0]]
        C = 2
        R = 2

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

    def test_path1_3(self):

        expectedMaxS = 1
        S = [[1, 1, 1, 0, 1], 
            [1, 2, 2, 0, 1],
            [1, 2, 3, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]]
        C = 5
        R = 5

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

    # Path 2 não corre porque o código não suporta R = 0
    '''
    def test_path2(self):

        expectedMaxS = 0
        S = [[]]
        C = 0
        R = 0

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j
        self.assertEqual(expectedMaxS, max_of_s)
    '''

    def test_path3_1(self):

        S = [[0, 1]]
        C = 2
        R = 1

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):                    
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

        self.assertEqual(1, max_of_s)
    
    def test_path3_2(self):

        S = [[0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
        C = 5
        R = 3

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):                    
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

        self.assertEqual(0, max_of_s)

    def test_path3_3(self):

        S = [[1, 1, 1, 0, 1], 
            [1, 2, 2, 0, 1],
            [1, 2, 3, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]]
        C = 5
        R = 5

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):                    
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    max_i = i
                    max_j = j

        self.assertEqual(3, max_of_s)

    def test_path4_1(self):

        expectedMaxS = -1
        S = [[1, 1], 
            [1, 2]]
        C = 2
        R = 2

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):  
                if expectedMaxS != -1:                  
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    expectedMaxS = max_of_s
                    max_i = i
                    max_j = j
                else:
                    expectedMaxS = -1

    def test_path4_2(self):

        expectedMaxS = -1
        S = [[0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
        C = 5
        R = 3

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):  
                if expectedMaxS != -1:                  
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    expectedMaxS = max_of_s
                    max_i = i
                    max_j = j
                else:
                    expectedMaxS = -1

    def test_path4_3(self):

        expectedMaxS = -1
        S = [[1, 1, 1, 0, 1], 
            [1, 2, 2, 0, 1],
            [1, 2, 3, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]]
        C = 5
        R = 5

        max_of_s = S[0][0]
        max_i = 0
        max_j = 0
        
        for i in range(R):
            for j in range(C):  
                if expectedMaxS != -1:                  
                    self.assertEqual(expectedMaxS, max_of_s)
                if (max_of_s < S[i][j]):
                    max_of_s = S[i][j]
                    expectedMaxS = max_of_s
                    max_i = i
                    max_j = j
                else:
                    expectedMaxS = -1
                    
if __name__ == '__main__':
    unittest.main()