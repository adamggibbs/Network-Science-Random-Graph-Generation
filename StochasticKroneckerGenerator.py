import numpy as np
import networkx as nx
import math
import random

DEBUG = True

def convertFromArrayToGraph(param):
    G = nx.to_networkx_graph(param)
    return G
#--------------------------------------------------------------#

def removeSelfLoops(graph, number_of_nodes):
    G = graph
    N = number_of_nodes

    for row in range(N):
        for col in range(N):
            if (row == col):
                G[row, col] = 0
    return G

#--------------------------------------------------------------#

def generateStochasticKroneckerGraph( initiator, k, deleteSelfLoops=False, \
                                     directed=False, nonUnitEdge=False, edges=0):
    N_init = initiator.getNumberOfNodes()
    N      = int(math.pow(N_init, k))
    matrix_dimension = initiator.getNumberOfNodes()
    matrix_sum       = initiator.getMatrixSum()

    if nonUnitEdge:
        number_of_edges = edges
        if number_of_edges > N*N:
            raise ValueError("More edges requested than is possible with N fixed")
    else:
        # number of _predicted_ edges
        number_of_edges = math.pow(matrix_sum, k)

    collisions = 0

    #--------#
    if DEBUG:
        print("EDGES: ", number_of_edges)
        print("NODES: ", N)
    #--------#

    vector_for_recursive_probability = []

    cumulative_mass = 0.0

    for row in range(matrix_dimension):
        for col in range(matrix_dimension):
            p = initiator.getValueAtIndex(row,col)
            if p > 0.0:
                cumulative_mass += p
                if DEBUG:
                    print("CM/MS: ", cumulative_mass/matrix_sum)
                vector_for_recursive_probability.append((cumulative_mass/matrix_sum, row, col))

    # populate nodes
    K = np.zeros((N,N))

    # populate edges
    e = 0

    while e < number_of_edges:
        r = N
        row = 0
        col = 0
        index = (0,0)
        for t in range(k):
            p = random.uniform(0,1)
            n = 0
            while p > vector_for_recursive_probability[n][0]:
                n += 1
            mrow = vector_for_recursive_probability[n][1]
            mcol = vector_for_recursive_probability[n][2]
            r /= matrix_dimension
            row += mrow*r
            col += mcol*r
            
        if K[int(row), int(col)] == 0:
            K[int(row), int(col)]=1
            e+=1
            if not directed:
                if row != col:
                    K[int(col), int(row)] = 1
                    e+=1
        else:
            collisions +=1

    if DEBUG:
        print("COLLISIONS:", collisions)

    if deleteSelfLoops:
        K = removeSelfLoops(K, N)
    K  = convertFromArrayToGraph(K)
    return K

#-------------------------------------------------------------------------------------------------#



    #--------------------------------------------------------------#




