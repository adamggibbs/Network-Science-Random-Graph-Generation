LWNDM_README.txt

This is a Local-World Node-Deletion Model (LWNDM) Generator.

This generator makes graphs based on the Local-World Node-Deletion Model. It is an evolving network model, so an initial graph is created and the evolution of the network is modeled based on the foundations of the local world model with the extension of node deletion. 

The first Local-World Model was proposed in 2003 and works by adding nodes based on preferential attachment as in the Barabsi-Albert Model. However, instead of an incoming node linking to m existing nodes within the entire graph with the probability degree(i)/sum_degrees for each node i, a random set of M existing nodes is selected to form the local-world. Then the incoming node is linked to m nodes within the local world with probability degree(i)/sum_local_degrees. This means that for any node within the graph it has a probability of (M/N)*(degree(i)/sum_local_degrees) for all nodes i in the graph G where N is size of the graph and M is the size of the local world. This comes from the probability M/N of a node being selected to be in the local world and probability degree(i)/sum_local_degrees of being selected by the incoming node. The idea behind the local world model is that when a new actor comes into a network, it'll only know about a small portion of the network and if it joins the network it'll be through one of the nodes within the small portion of the network it knows. This small portion of the network is known as the local world. 

The node-deletion aspect of the model expands on this local-world model by adding in the network dynamic that actors leave networks all the time. So, with a probability p at each time step t, the network adds a node as a standard local-world model would. However, with a probability 1-p, the network deletes a random node and all its adjacent edges. This creates a more dynamic and realistic change in topology of the network over time, and characteristic properties of real networks such a power law degree distributions and small diameters (of the main connected component) still hold.

Some characteristic properties of this model are as follows. First, the probability p greatly influences the resulting graph. Any probability 0 <= p < 0.5 results in a shrinking graph over time. And if the intial network is very small, it can lead to a graph of size 0, or all nodes with degree 0 after many node deletions. A probability p = 0.5 results in a changed network topology, but very little change in size over many time steps. And a probability 0.5 < p <= 1 results in a growing graph. It should also be noted that for p = 1, this model becomes the regular local-world model. Also, the intial graph given does not matter. It could be any intial graph and the LWNDM can model its evolution. In this generator, a small initial graph of size m0 is created where node 1, node 2, ..., node m0 are connected to node 0.. In this evolving network, many nodes can become disconnected if all its neighbors are deleted and sometimes the graph becomes completely disconnected or the size of the graph becomes 0, this becomes more likely as p decreases. 

The program is called using

    generate_local_world_node_deletion_graph(t, m0, M, m, p)

It will output a graph of varying sizes with a plot of its degree distribution and a visualization. 

Parameters:
    t - the number of time steps to be performed. One time step equates to one addition or deletion
    m0 - the size of the intial ER graph
    M - the size of the local world that contains the nodes an incoming node can link to, it should be noted that M does not necessarilly have to be true that M < m0
    m - the number of nodes an incoming node links to, it must hold that m < M
    p - the probability at each time step that a node is added (such that 1-p is the probability that a node is deleted at a time step t)

Psuedo-code:

1. create an intial graph of m0 nodes that is connected.
2. for t time steps:
    a. with probability p:
        i. with a uniform probability amongst all nodes, randomly select M nodes from the graph to form the local world. If M > size of the graph, select all nodes in the graph.
        ii. select m nodes from the local world each with a probability degree(i)/sum_local_degrees for each node i in the local world
        iii. add a node to the graph
        iv. for each of the m selected nodes from the local world, add an edge between that node and the new node
    b. with probability 1-p:
        i. With a uniform probability amongst all nodes, select one node from the graph
        ii. delete that node and all its adjacent edges. If that was the last node in the graph, stop the evolution as the network as dissolved.
3. return the graph

