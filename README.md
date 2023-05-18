# dowgraphs
Draw graphs of double occurrence words and compute their Betti numbers. 

## Math Background
More detailed explanation available in [arxiv](https://arxiv.org/abs/2305.05818.
### Double Occurrence Words (DOWs)
Double occurrence words (DOWs) are sequences of symbols from an alphabet such that every symbol from an ordered alphabet $\Sigma$ appears exactly zero or two times. We denote the set of all double occurrence words on $\Sigma$ by $\Sigma_{DOW}$. Similarly, we define single occurrence words (SOWs) and $\Sigma_{SOW}$. The set of symbols in a DOW $w$ is denoted by $\Sigma[w]$. A DOW $w$ is in _ascending order_ if symbols are labeled according to their order of appearance. We say two DOWs are _equivalent_ if they can be written as the same word in ascending order via symbol-to-symbol bijections. The _reverse_ of a word $w = a_1 a_2 \ldots a_{n-1} a_n$ where $a_i \in \Sigma$ is the word $w^R$ obtained by writing its symbols in reverse order: $w^R = a_n a_{n-1} \ldots a_2 a_1$. 

In all examples, we use $\Sigma = \mathbb{N}^*$, $\epsilon$ to denote the empty word, add commas to separate symbols where it improves legibility or reduces ambiguity. The DOW $w = 121323$, with $\Sigma[w] = \{1,2,3\}$, is in ascending order while $w^R = 323121$ is not. Both words are equivalent via the permutation $(13)$.

Let $x,y,z \in \Sigma^*$ and $u \in (\Sigma \setminus \Sigma[w])_{SOW}$. We say the word $uu$ is a _repeat word_ in $w = xuyuz$ and the word $xyz$ is obtained from $w$ by a _repeat deletion_ denoted $d_u(w) = xyz$. Similarly, the word $uu^R$ is a _return word_ in $ w = xuy u^Rz$ and the word $xyz$ is obtained from $w$ by a _return deletion_, also denoted $d_u(w) = xyz$. Repeat or return words, $uu$ or $uu^R$, where $u$ consists of a single symbol are called _trivial_. Repeat or return words are said to be _maximal_ if they are not contained in longer repeat or return words.

### Word Graphs
We denote the edges of a directed graph $u \rightarrow v$ as $[u,v]$. A _word graph rooted at_ $w$ is a graph whose set of vertices is a collection of ascending order words equivalent to those obtained through iterated deletions of maximal repeat or return words from $w$. If we let $w= 1234152345$, it has maximal repeat and return words $11,2323,$ and $4554$. Deleting them yields $d_{1}(w) = 23452354\sim 12341243$ $d_{23}(w) = 145541\sim 123321$, and $d_{45}(w) = 123231$, which creates the first set of edges out of $w$. Repeating this process with the resulting DOWs until $\epsilon$ is reached yields the graph

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/328a44f7-ca70-4052-b9e7-a130337b19fc" width=50%>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/fajardogomez/dowgraphs/assets/109635630/9cc213a5-9eae-4d16-a0e8-ae466f10db94" width=50%>
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://github.com/fajardogomez/dowgraphs/assets/109635630/9cc213a5-9eae-4d16-a0e8-ae466f10db94">
</picture>
</p>

