RDPM_README.txt

This is a Random Dot Product Model (RDPM) Generator.

This generator is specifically the first RDPM proposed which is the Dense RDPM. There are Sparse and Multiple RDPMs, which involve changing probability distributions and the alpha parameter for the Sparse model and adding additional vectors for each node in the Multiple model.

In a sparse RDPM, each node is assigned a d-dimensional vector and the probability that two nodes are connected via an edge is the dot product of their two vectors. This creates a more realistic correlation of nodes as nodes of similar vectors are more likely to connect since more similar nodes--the angle between them is small--and more popular nodes--nodes of a higher magnitudes--result in greater dot products and a higher probability of connecting. In this way, the vectors are known as characteristic vectors. Since this is a Random Dot Product Model, the vectors are randomly assigned. Due to this, the probability distribution that the elements of the vector are chosen from greatly determine the network topology and they must be normalized in such a way that the dot product always maps to a valid probability on the interval [0,1]. In this generator the elements of the vector are from a transformation of the uniform(0,1) distribution. This model tends to result in very dense networks which is not always applicable but has been found to accurately model current trends in online social networks.

The program creates a Dense RDPM using the following method

    generate_rdpm_graph(N, d, a)

It will output a graph of N nodes with a plot of its degree distribution and some graph statistics including edges, average degree distribution, and the diameter of the largest connected component. 

Parameters:
    N - number of nodes in the desired graph
    d - dimension of vectors assigned to each nodes
        *This affects the clustering and communities within a graph.
        *More dimensions allows for the dot product to have more variability
        *This parameter will affect the degree distribution
        *At high values of d, a "bend" in the degree distribution occurs at a certain high degree k
    a - The alpha parameter that manipulates the probability distribution so the dot product maps to a valid probability on the interval [0,1]
        *This parameter will affect the degree distribution greatly

Psuedo-code:
1. add N nodes to the graph
2. randomly assign a d-dimensional vector to each node in the graph
3. for each node i in the graph:
    a. for each node j > i in the graph:
        i. calculate the dot-product between i and j and store it as a probability p
        ii. with that probability p, flip a biased coin to determine if there will be an edge between i and j  
4. return the graph

