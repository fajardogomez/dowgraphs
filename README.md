# dowgraphs
Draw graphs of double occurrence words and compute their Betti numbers. The Python scripts here can be used to construct prodsimplicial complexes on arbitrary directed graphs and compute Betti numbers, or build word graphs corresponding to double occurrence words and then compute Betti numbers on the resulting complex.

#### Table of Contents  
- [Math Background](#math-background)
  - [Prodsimplicial Cells](#prodsimplicial-complexes)  
  - [Double Occurrence Words](#double-occurrence-words) 
  - [Word Graphs](#word-graphs)
- [Code Use Examples](#code-use-examples)
  - [General Directed Graphs](#general-directed-graphs)
  - [DOW Properties](#dow-properties) 
## Math Background
More detailed explanation available in [arxiv](https://arxiv.org/abs/2305.05818). 

### Prodsimplicial Complexes
The $n$-_dimensional simplicial digraph_, denoted by $\Delta^n$, is the cell whose 1-skeleton is the digraph with vertices $V(\Delta^n) = \{v_0, v_1, \ldots, v_n\}$ and edges $E(\Delta^n) = \lbrace[v_i,v_j] \ | \ 0 \leq i < j \leq n\rbrace$. 
<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/bb2613dd-3ac0-4f68-8e90-70f2db48a2b4" width=50%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/a91cf798-dde4-427c-ac3d-e634d83637e2" width=50%>
  <img alt="Simplices in dimensions 0, 1, and 2." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/a91cf798-dde4-427c-ac3d-e634d83637e24">
</picture>
</p>

An $N$-_dimensional prodsimplicial cell_ $P$ is the $N$-cell that is a product of simplices $\displaystyle\prod_{i=1}^k \Delta_i^{n_i} = \Delta_1^{n_1} \times \cdots \times \Delta_k^{n_k}$ where $n_i>0$ for all $1\leq i \leq k$ and $N= \displaystyle\sum_{i=1}^kn_i$. Its 1-skeleton is the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product_of_graphs) of simplicial digraphs. That is, a graph of the form $\Delta_1^{n_1} \square \cdots \square \Delta_k^{n_k}$. We abuse the notation and identify a prodsimplicial cell $P$ with the Cartesian product of simplicial digraphs.

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/819c8756-a97d-4f3d-aba3-d11759327ff8" width=50%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/0a5b00cb-f9e0-4312-9285-f545910b7670" width=50%>
  <img alt="All 3 dimensional simplices." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/0a5b00cb-f9e0-4312-9285-f545910b7670">
</picture>
</p>

Given any directed graph $G$, we build a _prodsimplicial complex_ by attaching all the induced subgraphs of $G$ that are isomorphic to the Cartesian product of simplices. This process can be done inductively on the dimension of the cells. The process is shown in the figure below.

a) When $n=0$ we attach vertices,
b) when $n=1$ we attach edges, 
c) when $n=2$ we attach squares and triangles, 
d) when $n=3$ we attach cubes, triangular prisms and tetrahedra. 

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/10cc2943-ef6f-4c23-950e-412413da620b" width=50%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/01319c9d-520e-4990-adf0-8d2bdfddf9f7" width=50%>
  <img alt="Inductively building a prodsimplicial complex on a directed graph." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/01319c9d-520e-4990-adf0-8d2bdfddf9f7">
</picture>
</p>

Identifying all prodsimplicial cells in the complex for each dimension allows us to compute the boundary operator. For simplices, we have the formula
$$\partial_n(\Delta^n) = \displaystyle \sum_{i=0}^n (-1)^i [v_0,v_1,\ldots, v_{i-1},\hat{v_i},v_{i+1},\ldots, v_n],$$ where $\hat{v_i}$ indicates that vertex $v_i$ has been deleted from the simplex. For a prodsimplicial cell $P$ as described above we use
$$\partial_N(P) = \displaystyle\sum_{i=1}^k (-1)^{\alpha(i)} \displaystyle [\overline{\partial_{n_i} \Delta^{n_i}}],$$ where 
$$\alpha(i) =\displaystyle \sum_{\ell=1}^{i-1} n_\ell$$ is the sum of the dimensions of the factors preceding the $i$-th factor and 
$$[\overline{\partial_{n_i} \Delta^{n_i}}]=\Delta^{n_1} \square \Delta^{n_2}\square \cdots \square \Delta^{n_{i-1}} \square \partial_{n_i} \left(\Delta^{n_{i}}\right) \square \Delta^{n_{i+1}} \square \cdots \square \Delta^{n_k}.$$ 

The $n$-th Betti number, $\beta_n$, of a complex $\mathcal{K}$ can be obtained from the boundary operator through 
$$\beta_n(\mathcal{K}) = \text{rank}(H_n(\mathcal{K})) = \text{rank}(Z_n(\mathcal{K})) - \text{rank}(B_n(\mathcal{K})).$$
When $\partial_n$ and $\partial_{n+1}$ are written as matrices, we can compute $\beta_n$ as
$$\beta_n = \text{nullity}(\partial_n) - \text{rank}(\partial_{n+1}.)$$

Betti numbers are topological invariants counting "loops," "holes," or "cavities" of different dimensions.

### Double Occurrence Words
Double occurrence words (DOWs) are sequences of symbols from an alphabet such that every symbol from an ordered alphabet $\Sigma$ appears exactly zero or two times. We denote the set of all double occurrence words on $\Sigma$ by $\Sigma_{DOW}$. Similarly, we define single occurrence words (SOWs) and $\Sigma_{SOW}$. The set of symbols in a DOW $w$ is denoted by $\Sigma[w]$. A DOW $w$ is in _ascending order_ if symbols are labeled according to their order of appearance. We say two DOWs are _equivalent_ if they can be written as the same word in ascending order via symbol-to-symbol bijections. The _reverse_ of a word $w = a_1 a_2 \ldots a_{n-1} a_n$ where $a_i \in \Sigma$ is the word $w^R$ obtained by writing its symbols in reverse order: $w^R = a_n a_{n-1} \ldots a_2 a_1$. 

In all examples, we use $\Sigma = \mathbb{N}^\ast$, $\epsilon$ to denote the empty word, add commas to separate symbols where it improves legibility or reduces ambiguity. The DOW $w = 121323$, with $\Sigma[w] = \{1,2,3\}$, is in ascending order while $w^R = 323121$ is not. Both words are equivalent via the permutation $(13)$.

Let $x,y,z \in \Sigma^\ast$ and $u \in (\Sigma \setminus \Sigma[w])_{SOW}$. We say the word $uu$ is a _repeat word_ in $w = xuyuz$ and the word $xyz$ is obtained from $w$ by a _repeat deletion_ denoted $d_u(w) = xyz$. Similarly, the word $uu^R$ is a _return word_ in $w = xuy u^Rz$ and the word $xyz$ is obtained from $w$ by a _return deletion_, also denoted $d_u(w) = xyz$. Repeat or return words, $uu$ or $uu^R$, where $u$ consists of a single symbol are called _trivial_. Repeat or return words are said to be _maximal_ if they are not contained in longer repeat or return words. We use $M_w^{SOW}$ to denote the set of SOWs $u$ such that either $uu$ is a maximal repeat word in $2$ or $ww^R$ is a maximal return word in $w$.

### Word Graphs
The set $D(w) = \displaystyle \bigcup_{u \in M_w^{SOW} } \lbrace v \ | \ v \text{ is in ascending order and }v \sim d_u(w)\rbrace$ is called the _set of immediate successors of_ $w$. If there exists a sequence of words $w=w_1, w_2, \ldots, w_n = w'$ such that $w_i\sim d_{u_{i}}(w_{i-1})$ for some choice of $u_i \in M^{SOW}_{w_i}$, we call $w'$ a _successor_ of $w$. Note that the empty word $\epsilon$ is a successor of all words.

The _global word graph_ $G_n=(V,E)$ _of double occurrence words of size_ $n$ is the graph defined by:

* $V(G_n)=\Sigma_{DOW}^{\leq n}/_\sim$;
* $E(G_n) = \displaystyle\bigcup_{w\in V} E_w$, where $E_w = \lbrace[w,v]\ | v \in D(w)\rbrace$. 

We denote the edges of a directed graph $u \rightarrow v$ as $[u,v]$. For a vertex $w$ in $G_n$, we define the _word graph rooted at $w$_, denoted $G_w$, as the induced subgraph of the global word graph containing as vertices $w$ and all of its successors. 

If we let $w= 1234152345$, it has maximal repeat and return words $11,2323,$ and $4554$. Deleting them yields $d_{1}(w) = 23452354\sim 12341243$ $d_{23}(w) = 145541\sim 123321$, and $d_{45}(w) = 123231$, creating the first set of edges out of $w$. Repeating this process with the resulting DOWs until $\epsilon$ is reached yields the graph

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/328a44f7-ca70-4052-b9e7-a130337b19fc" width=50%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/9cc213a5-9eae-4d16-a0e8-ae466f10db94" width=50%>
  <img alt="Word graph rooted at 1234152345." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/9cc213a5-9eae-4d16-a0e8-ae466f10db94">
</picture>
</p>

## Code Use Examples

### General Directed Graphs
We can initialize any graph as a `netowrkx` DiGraph object using `add_edge` and `add_node`, and then convert it into a prodsimplicial complex. Note that while it's fine for `networkx`, many of the methods rely on the assumption that vertices are labeled with strings. In the example below, `n_cellss(2)` returns a dictionary with all 2-dimensional prodsimplicial cells (here a triangle), and `betti_number(1)` returns $\beta_1$ of the complex. Since the triangle is a simplex and would be filled in, its value is zero. For arbitrary directed graphs, `draw()` will use the spring layout.

```python
import networkx as nx
from prodcells import PCELL

G = nx.DiGraph()
G.add_edge('1','2') 
G.add_edge('2','3')
G.add_edge('1','3')

pcellG = PCELL(G)
print(pcellG.n_cells(2))
print(pcellG.betti_number(1))
pcellG.draw()
```
Outputs:
```python
[{'graph': <networkx.classes.digraph.DiGraph object at 0x000002127EA9C4C0>, 'isom': {'0': '1', '1': '2', '2': '3'}, 'part': (2,), 'orientation': -1, 'vertices': '1_2_3'}]
0
```
<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/a786ae60-502d-4ac9-aa42-4ba8c47ebb3d" width=30%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/633e9e1b-2c0f-4b0d-8cb1-ce93c0562e56" width=30%>
  <img alt="Image of the graph defined by the added edges." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/633e9e1b-2c0f-4b0d-8cb1-ce93c0562e56">
</picture>
</p>
The `draw()` method can take optional arguments like mode (for light or dark color theme) or filename (so that the output .svg and .png files get more creative names than 'graph.svg' and 'graph.png'). 

If using `SageMath`, the following can be used to compute full homology groups (including torsion):
```python
from sage import *
import networkx as nx
from prodcells import PCELL

def hom_gps(G, gens=False, chk=True):
    pcellG = PCELL(G)
    i=0
    done = False
    complex_dict = dict()
    while done == False:
        bop = pcellG.boundary_op(i)
        # When n_cells is empty one dimension of the boundary operator matrix
        # will be zero. This is the last matrix needed.
        if i > 0 and bop.shape[0]*bop.shape[1] == 0:
            done = True
        # Making sure the matrices have the right dimensions
        complex_dict[i] = matrix(bop.shape[0], bop.shape[1], bop.toarray())
        i += 1
    # Degree=-1 because boundary operator goes from C_{n} to C_{n-1}
    C = ChainComplex(complex_dict, degree=-1, base_ring = ZZ, check=chk)
    hom_gps = C.homology(generators=gens)
    return hom_gps
```

## DOW Properties
We can initialize an instance of the `DOW` class from any string of alphanumeric symbols separated by commas where each symbol appears twice. The optional arguments `min_chars` and `asc_order` are used to decide whether or not to relabel the symbols using the least available characters and/or rewrite in asceneding order. 

```python
from dow import DOW
dow1 = DOW('4,2,1,a,b,2,1,4,b,a')
dow2 = DOW('4,2,1,a,b,2,1,4,b,a', min_chars=False)
dow3 = DOW('4,2,1,a,b,2,1,4,b,a', min_chars=False, asc_order=False)
print(dow1.W)
print(dow2.W)
print(dow3.W)
```
Outputs
```python
1,2,3,a,b,2,3,1,b,a
1,2,4,a,b,2,4,1,b,a
4,2,1,a,b,2,1,4,b,a
```

Some functions in the class are used to generate DOWs with specific properties. For example, `getdows(n)` returns a list of all DOWs on $n$ symbols using positive integers as symbols, and `tangled(n)` returns the tangled cord on $n$ symbols. Class methods include `find_patterns()`, which returns SOWs $u$ such that $uu$ or $uu^R$ is a maximal repeat or return word, and `separation`, which computes another property of DOWs as studied [here](https://www.worldscientific.com/doi/10.1142/S0129054120500343). 

Putting everything together, we can produce DOWs, construct their word graphs and then compute the Betti numbers of the corresponding prodsimplicial complex:

```python
import downew as d
from wordgraphnew import *
# Generate the tangled cord 1,2,1,3,2,4,3,4 and then compute the first Betti number for the resulting word graph
G = word_graph(d.tangled(4))
pcellG = PCELL(G)
print(pcellG.betti_number(1))

# Draw word graphs for '4,2,1,a,b,2,1,4,b,a' playing with the relabeling settings
draw_dow('4,2,1,a,b,2,1,4,b,a',asc_order=False, min_chars = False)
draw_dow('4,2,1,a,b,2,1,4,b,a', min_chars = False)
draw_dow('4,2,1,a,b,2,1,4,b,a')
```

Strictly following the definition of the word graph, we should use `asc_order=True` but it is set as an optional argument. If set to `False`, the resulting word graph may not be equivalent anymore. The three graphs generated by the code above are
  <table>
  <tr>
    <td>Without using least characters or ascending order.</td>
     <td>Not using least characters, but in ascending order.</td>
     <td>Using least characters in ascending order.</td>
  </tr>
  <tr>
  <td>
  <p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/0959955b-3eb6-477e-8715-16414f825918" width=100%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/7e411c37-d806-4702-a7a7-b71050075770" width=100%>
  <img alt="Without using least characters or ascending order." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/7e411c37-d806-4702-a7a7-b71050075770">
  </picture>
  </p>
    </td>
    <td>
  <p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/3890072b-e3fc-43da-8653-c5e34504fa7d" width=100%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/ed4e00a0-36a6-4745-a711-86a688feba3c" width=100%>
  <img alt="Without using least characters, in ascending order." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/ed4e00a0-36a6-4745-a711-86a688feba3c">
  </picture>
  </p>
    </td>
    <td>
  <p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/12d3aa9b-d39b-4e02-85b6-d238911f4ad1" width=100%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/a292522c-f25e-494b-b44a-d5d5675215cd" width=100%>
  <img alt="Least characters and in ascending order." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/a292522c-f25e-494b-b44a-d5d5675215cd">
  </picture>
  </p>
    </td>
  </tr>
  </table>
