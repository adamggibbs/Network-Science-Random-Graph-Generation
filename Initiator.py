import numpy as np
import networkx as nx


class InitiatorMatrix():

    DEBUG = False

    def __init__(self, N, W=None):
        """ Initially, we will take in the number of nodes <N> """
        self.N = N
    #--------------------------------------------------------------#

    def getNumberOfNodes(self):
        return self.N
    #--------------------------------------------------------------#

    def setNumberOfNodes(self, n):
        self.N = n
    #--------------------------------------------------------------#

    def getValueAtIndex(self, v_1, v_2):
        return self.W[v_1, v_2]
    #--------------------------------------------------------------#

    def setValueAtIndex(self, new_value, n_1, n_2):
        self.W[n_1, n_2] = new_value
    #--------------------------------------------------------------#

    def getMatrixSum(self):
        """ sum over all indices """
        n = self.getNumberOfNodes()
        s = 0.0

        for row in range(n):
            for col in range(n):
                s+= self.getValueAtIndex(row, col)

        return int(s)
    #--------------------------------------------------------------#

    def make(self):
        """ constructs an initiator matrix """
        n = self.N
        # populate with all 0 by default
        initiator = np.zeros((n,n))
        self.W = initiator
    #--------------------------------------------------------------#    

    def makeStochasticMatrix(self, probability_array):
        """ take in an np array of probabilities and populate W"""

        n  = self.N
        length = n*n
        if (probability_array.shape[0] != length):
            raise IOError("\033[1m Probability Array must be of proper Dimension \033[0m")

        for row in range(n):
            for col in range(n):
                for k in range(length):
                    self.setValueAtIndex(probability_array[k], row, col)
    #--------------------------------------------------------------#

    def makeStochastic_AB_Matrix(self, alpha, beta, selfLoops=True):

    #--------------------------------------------------------------#

        if not 0.00 <= alpha <= 1.00:
            raise IOError("alpha must be a value equal to or between 0 and 1")
        if not 0.00 <= beta <= 1.00:
            raise IOError("beta must be a value equal to or between 0 and 1")

    #--------------------------------------------------------------#

        n = self.getNumberOfNodes()

        # switch 1,0 for alpha and beta while keeping any self loops

        for row in range(n):
            for col in range(n):
                if (row ==  col):
                    if selfLoops == False:
                        self.setValueAtIndex(alpha, row, col)
                elif self.getValueAtIndex(row, col) == 0:
                    self.setValueAtIndex(beta, row, col)
                else:
                    self.setValueAtIndex(alpha, row, col)

    #--------------------------------------------------------------#
    def makeStochastic_AB_MatrixFromGraph(self, G, alpha, beta):
        """ construct a stochastic initiator natrix from graph, <G> """
        A = nx.to_numpy_matrix(G)

        # <n> = number of nodes
        n = A.shape[0]

        init = InitatorMatrix(n)
        init.make()

        for row in range(n):
            for col in range(n):
                init.setValueAtIndex(A[row, col], row, col)
        init.makeStochastic_AB_Matrix(alpha, beta)

        return init

    #--------------------------------------------------------------#

    def addEdge(self, n_1, n_2, edge=1):
        n_1 = int(n_1)
        n_2 = int(n_2)
        if edge == 0 or edge == float('inf'):
            raise ValueError(" \033[m1 Edge value out of bounds \033[m0")

        self.W[n_1, n_2] = edge
    #--------------------------------------------------------------#

    def addSelfLoops(self):
        n = self.getNumberOfNodes()
        for i in range(n):
            self.addEdge(i, i)
    #--------------------------------------------------------------#



