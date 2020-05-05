This paradigm of the BA model was chosen for further exploration because of its flexibility and generalizability in the exploration of evolving networks. However, it is different from the basic Barabasi Albert model in the way it handles growth and preferential attachment. The preferential attachment model is wholly dependent on the parameters chosen by the user, unlike traditional BA models where the probability depends on the degree of the node. 

Worth noting here is how the adjustment of the preferential attachment mechanism destroys the network's scale free property. The explanation below obtained from the networkx github repository further explains what the different parameters mean and how tweaking them will affect the structure of the resulting network.

An extended Barabási–Albert model graph is a random graph constructed
using preferential attachment. The extended model allows new edges,
rewired edges or new nodes. Based on the probabilities $p$ and $q$
with $p + q < 1$, the growing behavior of the graph is determined as:

1) With $p$ probability, $m$ new edges are added to the graph,
starting from randomly chosen existing nodes and attached preferentially at the other end.

2) With $q$ probability, $m$ existing edges are rewired
by randomly choosing an edge and rewiring one end to a preferentially chosen node.

3) With $(1 - p - q)$ probability, $m$ new nodes are added to the graph
with edges attached preferentially.

When $p = q = 0$, the model behaves just like the Barabási–Alber mo

Parameters
----------
n : int
    Number of nodes
m : int
    Number of edges with which a new node attaches to existing nodes
p : float
    Probability value for adding an edge between existing nodes. p + q < 1
q : float
    Probability value of rewiring of existing edges. p + q < 1
seed : integer, random_state, or None (default)
    Indicator of random number generation state.
    See :ref:`Randomness<randomness>`.

Returns
-------
G : Graph

Raises
------
NetworkXError
    If `m` does not satisfy ``1 <= m < n`` or ``1 >= p + q``

References
----------
.. [1] Albert, R., & Barabási, A. L. (2000)
   Topology of evolving networks: local events and universality
   Physical review letters, 85(24), 5234.