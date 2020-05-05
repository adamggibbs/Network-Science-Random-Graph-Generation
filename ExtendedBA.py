import networkx as nx
import random as fj
import matplotlib.pyplot as plt
import pandas as pd
from math import *
import gzip
import csv
import operator
import numpy as np
from collections import OrderedDict

'''
In this iteration of a Barabasi Albert graphs, we run experiments to see how BA 
graph characteristics change as the various parameters in the graph increase/ decrease. 
Check README.txt for code documentation. 
'''

#Param combinations to be tested
n = [10, 20, 30, 40, 50]
m = [5, 10, 15, 20, 25]
p = [0.1, 0.3, 0.5, 0.7, 0.9]
q = [0.8, 0.6, 0.4, 0.2, 0.05]

#make graphs
graphs = []

for param1,param2,param3,param4 in zip(n, m, p, q):
    graphs.append(nx.extended_barabasi_albert_graph(param1,param2,param3,param4))

#Function to obtain graphs' average degree and expected average degree

def graph_statistics(g,p):
    
    k = 0
    
    for i in range(0, len(g.nodes())):
        k = k + g.degree(i)
    print("The average degree, <k> = " + str(k/len(g.nodes())))
    print("The expected average degree is " + str(p*(len(g.nodes())-1)))
    
    return

#Obtain statistics for all generated graphs

for prob,graph in zip(p, graphs):
    graph_statistics(graph, prob)


#Obtain degree distributions

def plot_degree_distribution(g):
    degree_dict = dict(g.degree())
    degree_ordered = OrderedDict(sorted(degree_dict.items(), key=lambda x: x[1], reverse=True))
    degree_sequence = list(degree_ordered.values())
    prob, bin_edges = np.histogram(degree_sequence, bins=range(1,np.max(degree_sequence)+2), density=True)
    plt.loglog(bin_edges[:-1], prob, '.', marker='x')
    plt.title("Probability density function")
    plt.xlabel("degree")
    plt.ylabel("probability")
    plt.show()

for graph in graphs:
    plot_degree_distribution(graph)