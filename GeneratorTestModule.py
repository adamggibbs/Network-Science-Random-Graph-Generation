from Initiator import InitiatorMatrix
import StochasticKroneckerGenerator

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def getGraph(G):
    g  = G
    cc = nx.connected_components(g)
    mag_cc = nx.number_connected_components(g)

    return g, cc, mag_cc

#-------------------------------------------------#

def generateStatistics(G):
    (g, cc, mag_cc) = getGraph(G)
    closeness = nx.closeness_centrality(g)
    betweenness = nx.betweenness_centrality(g)
    degree      = nx.degree_centrality(g)
    density     = nx.density(g)

    statistics = {'closeness':closeness, 'betweeness':betweenness \
                  ,'mag_cc':mag_cc, 'degree': degree, 'density':density}

    return statistics

#-------------------------------------------------#

_V_ = 5

initiator = InitiatorMatrix(_V_)
initiator.make()

initiator.addEdge(0,1)
initiator.makeStochastic_AB_Matrix(0.4, 0.6)

k = 6

print("seed matrix size: ")
print(_V_)
print("iterations: ")
print(k)

G = StochasticKroneckerGenerator.generateStochasticKroneckerGraph(initiator, k, True)

print("=== GRAPH GENERATION COMPLETE ===")

bipartite = nx.is_bipartite(G)

print("Is Bipartite: ")
print(bipartite)

connected = nx.is_biconnected(G)

print("Is Connected: ")
print(connected)

nx.draw_networkx(G, node_color = 'red', pos=nx.spring_layout(G), node_size = 10, with_labels=False)
plt.show()

print("Generating statistics...")
statistics = generateStatistics(G)
print(statistics)

print("Generating Histogram...")
print("NO HISTOGRAM TO PLOT")

