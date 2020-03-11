RDPM_README.txt

This is a Random Dot Product Model (RDPM) Generator.

This generator is specifically the first RDPM proposed which is the Dense RDPM. There are Sparse and Multiple RDPMs, which involve changing probability distributions and the alpha parameter for the Sparse model and adding additional vectors for each node in the Multiple model. In phase 3 I may introduce more parameters to create sparse graphs, however, creating a sparse graph sacrifices other characteristics like degree distribution and shrinking diameter. 

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

