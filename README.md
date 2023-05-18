# dowgraphs
Draw graphs of double occurrence words and compute their Betti numbers. 

## Math Background
More detailed explanation available in [arxiv](https://arxiv.org/abs/2305.05818).
### Double Occurrence Words (DOWs)
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

### Prodsimplicial Cells
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
