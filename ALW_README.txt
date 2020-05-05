# AgingLocalWorld.py
# README

# import dependencies:

 sys
 networkx 
 matplotlib
 random
 csv
 pylab

# CLI arguments:
        < N > : population of network, node count
        < E > : number of edges in network
        < M > : population of local world : M < N
        < alpha> : decay factor E [0,1)
        < gens > : generations

# To run program:

python3 AginLocalWorld.py <N> <E> <M> <alpha> <gens>

or

python3 AgingLocalWorld.py DEFAULT (to populate with default args)

# runtime settings:

VERBOSE:   true | false : to see text ourput during runtime
GRAPHICS:  true | false : to see graph viz.
DEBUG:     true | false: for debugging/log data`
PYLAB:     true | false: to use pylab graphics, recommended: False
FRAMERATE E range(0,500): recommended 70-100

# Algorithm Explained: (***)

        > Initialize initial configuration of <N> nodes and <E> edges
        with edge weight, <w> = 1.
        > At each generation:
            1. randomly select local world with population <M> from given 
               configuration. For incoming node <n> denote M \subset V as local(n).
            2. Add new node <n> with <mu> edges to local(n), with <m> positive integer-
               valued random variable selected from {m_1, .... , m_q} with P(mu = m_i) = p_i >= 0
               where max_i, m_i < M, i <= i <= q and normalized over q. For each new edge, connect
               to node i with striength-age preferential attachment probaility.
                        let a new node be added at time t_n 
                        s(t_n, t) = the strength of node n at timestep t >= n
                        alpha     = decay factor
                        beta(i)   = [s(t_i, t)*(t-t_i)^-alpha]
                        
                        pr((i,n) C E) = beta(i) / sum over j in local(n) of beta(j)

            3. Let each node i in neighborhood of n establish a new edge with node j, randomly 
               selected from neighbors(n). If there is already a connection let w_ij <- w_ij+1


