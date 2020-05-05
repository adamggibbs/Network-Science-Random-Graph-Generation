BB_README.txt

This is a Bianconi-Barabasi Model (BB) Generator.

This generator creates a Bianconi-Barabasi Graph. The BB Model, also known as the Fitness Model, is an extension of the Barabasi-Albert (BA) preferential attachment model that was created as the first evolving network model using the preferential attachment idea. The limitations of the BA model led to the creation of the BB model.

The BA model starts with an initial graph of size m0 where nodes 1 to m0 are connected via an edge to node 0 so node 0 has a degree m0-1 and nodes 1 to m0 have a degree 1. Then N-m0, where N is the final size of the graph, nodes are added to the graph and for each incoming node, it is linked to m nodes in the existing graph. The probability that a node i in the existing graph is linked to by the incoming node is proportional to its degree such that the probability is degree(i)/sum_degrees. This results in the rich gets richer idea such that nodes that enter the network sooner are more likely to get a higher degree. 

This rich-gets-richer idea and early-actor idea became challenged when the internet saw companies like google and then facebook enter the network later but still manage to become the highest-degree nodes. So the idea of fitness came into play. Each node has a fitness n which along with its degree determines the likelihood that another new node will link to it. The BB model took this idea and extended the BA model such that when each node is introduced to the network, it is randomly assigned a fitness attribute. Then the probability that an incoming node links to an existing node i is fitness(i)*degree(i) / sum_fitness*degrees. This allows a high fitness actor entering the network late to have a greater chance of becoming a high degree node.

With the BB model, we expect nodes of higher fitness and nodes that entered the network earlier to trend toward higher degrees. So if you look at the degree vs fitness plot you'll notice nodes of higher fitness tend to have higher degrees and with the degree vs time you'll see the nodes that entered the graph earlier tend to have higher degrees. Then if you look at the plot of degree vs fitness/time you'll see a very rough trend to a line from the bottom left corner (low fitness and late entry) of the graph to the top right (high fitness and early entry) of the graph. This shows the influence of fitness on a network. This also means that when modeling an evolving network, it is very important that fitness be estimated correctly. But in terms of studying its influence, models can just randomly assign fitness values to nodes.

The program creates a Bianconi-Barabasi Model using the following method

    generate_fitness_graph(N, m0, m)

It will output a graph of N nodes with a plot of its degree distribution and some graph statistics including degree distributions vs fitness, time, and a combination. 

Parameters:
    N - number of nodes in the desired graph
    m0 - intial number of nodes in the graph before preferential attachment ensues
    m - number of existing nodes each incoming node is linked to 

Psuedo-code:
1. add m0 nodes to the graph
    a. add an edge between node 1, node 2, ..., node m0 and node 0
    b. assign a random fitness from the uniform(0,1) distribution to each of the m0 initial nodes
2. for t time steps:
    a. select m nodes with a probability fitness(i)*degree(i) / sum_fitness*degrees for each existing node i in the graph
    b. add a node to the graph
    c. assign a random fitness to the new node
    d. add an edge between the new node and each of the m selected nodes
3. return the graph

