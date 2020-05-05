import sys
import networkx as nx
import matplotlib.pyplot as plt
import random
import csv
import pylab
from matplotlib.pyplot import pause


"""
CLI arguments:
        < N > : population of network, node count
        < E > : number of edges in network
        < M > : population of local world
        < alpha> : decay factor
        < gens > : generations

Algorithm Explained: (***)

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

"""

# set true if you wish to see text output, false if not
VERBOSE  = True
# to see graphical visualization for each gen
GRAPHICS = True
# for pylab graphics: set to false on u**ix systems
PYLAB    = False
# used for debuging, keep false for easier to read CLI output
DEBUG    = False
# higher for faster animation, lower for slower: recommended at 70
FRAMERATE  = 70


def parse(read_arguments=True):

    arguments = dict()

    if len(sys.argv) == 1:
        raise ValueError('{:>8}'.format('Please specify all instance parameters or put DEFAULT as sole argument'))
    if len(sys.argv) == 2 and sys.argv[1] == "DEFAULT":
        arguments = { 'N':100,
                     'E':250,
                     'M': 6 ,
                     'alpha': 0.3,
                     'gens': 900
                    }
        return arguments
    print('{:^15}'.format(color.BOLD + "Instance Parameters:" + color.END))

    if VERBOSE and read_arguments:
        print('{:<8} {:<13} {:<15}'.format(color.GREEN + "Network Population " + color.END + ": ",  color.BLUE +  "N" +  color.END + ": ", sys.argv[1]))
        print('{:<8} {:<13} {:<15}'.format(color.GREEN + "Edge Count" + color.END + ": ",  color.BLUE +  "E" +  color.END + ": ", sys.argv[2]))
        print('{:<8} {:<13} {:<15}'.format(color.GREEN + "Local Population" + color.END + ":",  color.BLUE +  "M" + color.END + ": ", sys.argv[3]))
        print('{:<8} {:<13} {:<15}'.format(color.GREEN +  "Decay Factor" +  color.END + ": ", color.BLUE +  "alpha" +  color.END + ": ", sys.argv[4]))
        print('{:<8} {:<13} {:<15}'.format(color.GREEN +  "Generations" +  color.END + ": ", color.BLUE +  "gens" +  color.END + ": ", sys.argv[5]))

    arguments['N'] = sys.argv[1]
    arguments['E'] = sys.argv[2]
    arguments['M'] = sys.argv[3]
    arguments['alpha'] = sys.argv[4]
    arguments['gens'] = sys.argv[5]

    return arguments

def populate(arguments):

    # parse arguments dict.
    N = int(arguments['N'])
    E = int(arguments['E'])

    G = nx.Graph()

    for i in range(N):
        # x,y = index, time added
        G.add_node((i, 0))

    for e in range(E):
        u = (random.randint(0,N),0)
        v = (random.randint(0,N),0)

        if G.has_edge(u,v):
            G[u][v]['weight']+=1

        else:
            G.add_edge(u,v,weight=1)

    if VERBOSE:
        print('{:<8}'.format(color.BOLD + "Graph Data:" + color.END))
        print('{:<8} {:<13}'.format(color.BLUE + "NodeList" + color.END, color.RED + str(G.nodes()) + color.END))
        print('{:<8} {:<13}'.format(color.BLUE + "EdgeList" + color.END, color.RED + str(G.edges()) + color.END))

    return G

def genesis(G, arguments):

    pylab.ion()

    # input params
    N = int(arguments['N'])
    E = int(arguments['E'])
    M = int(arguments['M'])
    alpha = float(arguments['alpha'])
    generations = int(arguments['gens'])

    node_positions = nx.spring_layout(G)

    #(***)
    for t in range(1, generations+1):

        N = len(G.nodes())
        E = len(G.edges())

        G, node_positions = evolve(G, N, E, M, alpha, t, node_positions)

        if GRAPHICS and not PYLAB:
            nx.draw_networkx_nodes(G, pos=node_positions,node_color='grey', label=True,node_size=200)
            nx.draw_networkx_edges(G, pos=node_positions, edge_color='grey', label=True)
            nx.draw_networkx_labels(G,pos=node_positions,font_size=10)
            plt.show()
            pause(FRAMERATE*0.00066)

        if DEBUG:
            print(color.GREEN + "finished evolution: " + str(t))

        if GRAPHICS and PYLAB:
            graph = get_graph(G, node_positions)
            graph.canvas.draw()
            pylab.draw()
            pause(0.5)
            pylab.close(graph)

        if DEBUG:
            print(color.RED + color.BOLD + "at time " + str(t) + ": ")

        if DEBUG and False:
            a = open("error_log_after_evolve.txt", "w")

            a.write(str(node_positions) + "\n")
            a.write(str(G.nodes())+ "\n \n" +  str(G.edges()))
            a.close()

        if DEBUG and False:
            f = open("error_log_before_evolve.txt", "w")

            f.write(str(node_positions) + "\n")
            f.write(str(G.nodes()) + "\n \n" +  str(G.edges()))
            f.close()

        if DEBUG:
            print(color.GREEN + "finished generation: " + str(t))

    else:
        print(G)

    if False:
        print(color.RED + "Node " + color.BOLD + str(n) + " added at time " + color.BLUE + str(t) + color.END)
        print(color.GREEN + color.BOLD + "local(n)" + color.END + ": " + str(local_world))

def evolve(G, N, E, M, alpha, t, node_positions):

        # For each generation, add new node n, with index V(G)+1 and t_n = t 
        n = (N +1,t)
        # out degree of n
        mu = random.randint(1,M-1)

        # randomly select small world of M nodes from G
        local_world = random.sample(list(G.nodes()), M)

        G.add_node(n)

        # add node to position dict
        node_positions[n] = (random.uniform(-1,1),random.uniform(-1,1))


        while G.degree(n) < mu:
            for u in local_world:
                # for each node in local world, connect to n via e w.p.:
                # s(t_u,t)*(t-t_u)^-alpha/sum([s(t_i,t)*(t-t_i)^-alpha for i in local(n)]

                st_ut = sum([G[u][i]['weight'] for i in G.neighbors(u)])
                num   = st_ut * pow((t-u[1]),-1*alpha)
                s     = []
                for v in local_world:
                    s.append(sum([G[v][i]['weight'] for i in G.neighbors(v)])*pow((t-v[1]),-1*alpha))
                if sum(s) == 0:
                    p = 1
                else:
                    p = num/sum(s)
                
                pr = random.uniform(0,1)*p
                r = random.uniform(0,1)

                if DEBUG:
                    print(color.RED + "pr: " + str(pr))
                    print(color.RED + "r: " + str(r))

                if r < pr:
                    if VERBOSE:
                        print(color.GREEN + "edge:" + str((n,u)) + "added to " + color.BLUE + "G")
                    G.add_edge(n,u, weight = 1)
            

        # weight distribution reaction to addition of n 
        for gamma in G.neighbors(n):
            delta = random.choice(list(G.neighbors(n)))
            if G.has_edge(gamma,delta):
                G[gamma][delta]['weight']+=1
            else:
                G.add_edge(gamma,delta, weight = 1)
    
        if VERBOSE:
            print(color.RED + "Node " + color.BOLD + str(n) + " added at time " + color.BLUE + str(t) + color.END)
            print(color.GREEN + color.BOLD + "local(n)" + color.END + ": " + str(local_world))

        return G, node_positions

def get_graph(G, node_positions):
    fig = pylab.figure()
    nx.draw(G, pos=node_positions)
    return fig

def main():
    # genesis(graph, populated by parse() arguments, parse() arguments)
    genesis(populate(parse()), parse(read_arguments=False))


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

if __name__ == "__main__":
    main()
