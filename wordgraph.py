import networkx as nx

from dow import DOW
from prodcells import PCELL
def word_graph(word, asc_order = True, min_chars = True):
    """
    Creates the word graph rooted at word.

    Parameters
    ----------
    word : str
        Should correspond to a DOW, a sequence of symbols separated by commas.
    asc_order : bool, optional
        If True, will relable the word in ascending order. The default is True.
    min_chars : bool, optional
        If True, will use the least possible symbols. The default is True.

    Returns
    -------
    graph : nx.DiGraph()
        Directed graph connecting DOWs if one can be obtained from the other 
        by deleting maximal repeat or return words.

    """
    dow = DOW(word, asc_order, min_chars)
    #loop_reduced_word = dow.remove_loops()
    ao_word = dow.W
    if ao_word != word:
        print(word + ' is equivalent to '+ao_word)
    graph = nx.DiGraph()
    edges = edge_pairs(word, asc_order, min_chars)
    node_dict = dict()
    if len(edges)>0:
        for edge in edges:
            (e1, e2) = edge
            # Each node is defined by node label and layer number
            (n1,l1) = e1  
            (n2,l2) = e2
            if n1.W not in node_dict or node_dict[n1.W] < l1:
                node_dict[n1.W] = l1
            if n2.W not in node_dict or node_dict[n2.W] < l2:
                node_dict[n2.W] = l2
            graph.add_edge(n1.W, n2.W)
        for n in node_dict:
            graph.add_node(n,layer=node_dict[n])
    else:
        label = word.replace(',','')
        graph.add_node(label)
    
    return graph

def draw_dow(dow,mode='light',asc_order = True, min_chars = True, **kwargs):
    """
    Draws a word graph for a given DOW (given as a str). 

    Parameters
    ----------
    dow : str
        String corresponding to a DOW.
    mode : str, optional
        Valid arguments are 'light' and 'dark,' which make edges and labels 
        black or white, respectively. The default is 'light'.
    **kwargs : str, optional 
        filename: str
            Default is dow
        layer_by: str
            Changes the appearance of the multipartite graph. Default is
            'layer,' which places w at the top and new vertices in levels
            below it by order of appearance in the reduction process.

    Returns
    -------
    None.

    """
    kwargs.setdefault('layer_by','layer')
    if 'layer_by' in kwargs:
        lb = kwargs['layer_by']
    l = int(len(dow.split(','))/2)
    PCELL(word_graph(dow, asc_order = asc_order, min_chars = min_chars)).draw(mode=mode, filename=dow, wordlen = l, layer_by=lb)

def betti_nums(word):
    """
    Computes Betti numbers 0, 1 and 2 for the prodismplicial complex
    associated with the DOW represented by word.
    """
    G = word_graph(word)
    cellG = PCELL(G)
    ret = list()
    i = 1
    while i < 3:
        bi = cellG.betti_number(i)
        ret.append(bi)
        i+=1
    return ret

def add_layer(wordset, layernum, asc_order = True, min_chars = True):
    """
    Add one more layer of edges to the word graph

    Parameters
    ----------
    wordset : set
        Set of DOWs to reduce.
    layernum : int
        Indicates (roughly) the length from the root node.

    Returns
    -------
    ret : set of pairs
        Each pair is of the form ((x, x_layer_number),(y,y_layer_number))
        where (x,y) corresponds to an edge on the graph.

    """        
    ret = set()
    for word in wordset:
        if len(word.W)>0:
            to_red = word.find_patterns()
            red = word.reduce(to_red, asc_order = asc_order, min_chars = min_chars)
            for x in red:
                word_add =(word, layernum)
                x_add = (x, layernum+1)
                ret.add((word_add,x_add))
    return ret

def edge_pairs(word, asc_order = True, min_chars = True):
    """
    Returns the edges of the word graph.

    Parameters
    ----------
    word : str
        The string should be a comma separated sequence of symbols 
        corresponding to a DOW.

    Returns
    -------
    ret : set
        Set of tuples (u,v) where v is obtained from u by deleting a 
        maximal repeat or return word.

    """
    dow = DOW(word, asc_order = asc_order, min_chars = min_chars)
    ret = set()
    layernum = 1
    wordset = {dow}
    leaves = set()
    leaveslist = list()
    # Computes the words that the initial word can be reduced to, these are
    # all 1 edge away from the root. The layer is a set of pairs.
    layer = add_layer(wordset, layernum, asc_order = asc_order, min_chars = min_chars)
    ret.update(layer)
    layernum += 1
    for tup in layer:
        leaves.add(tup[1][0])
    leaveslist.append(leaves)
    # Check for convergence: the last layer contains only the empty word, 
    # if it's not the last layer added compute more layers
    while len(leaveslist[-1]) > 0 and leaveslist[-1] !={''}:
        new_lvs = set()
        new_lay = add_layer(leaves, layernum, asc_order = asc_order, min_chars = min_chars)
        for tup in new_lay:
            new_lvs.add(tup[1][0])
        leaveslist.append(new_lvs)
        ret.update(new_lay)
        layernum += 1
        leaves = new_lvs
    return ret
