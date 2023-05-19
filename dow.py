import string

# Double Occurrence Words
class DOW():
    W = None
    def __init__(self, W, asc_order = True, min_chars = True):
        """
        Initializes the attributes of the DOW, based on the symbol sequence.

        Parameters
        ----------
        W : str
            String representation of a DOW. E.g. 121323 can be represented as
            '1,2,1,3,2,3'. Symbols should be separated by commas. Symbols can 
            be letters, but should be single letters.
        asc_order : boolean, optional
            Automatically rewrites the DOW and in ascending order. 
            The default is True.
        min_chars : boolean, optional
            Automatically rewrites the word using the least possible symbols. 
            The default is True.

        Returns
        -------
        None.
        """
        
        self.W = str(W).replace(' ', '')
        self.sym_list = self.W.split(',')
        self.order = order_chars(list(set(self.sym_list)))
        self.error_check()
        self.update(asc_order = asc_order, min_chars = min_chars)        
        
    def update(self, asc_order = True, min_chars = True):
        """Update the attributes after relabeling/reordering."""
        if asc_order:
            self.ascending_order(min_chars)
        elif min_chars:
            self.W = ','.join(minimum_chars(self.sym_list))
        self.sym_list = self.W.split(',')
        self.order = order_chars(list(set(self.sym_list)))
        
    def error_check(self):
        """Check for common input errors."""
        if self.W != '':
            for x in self.sym_list:
                if (x.isalpha() == False) and (x.isdigit() == False):
                    raise ValueError('Use only alphanumeric characters.')
                elif x.isalpha() and len(x)>1:
                    raise ValueError('Use single letters as symbols.')
            
            if not isinstance(self.W, str):
                raise TypeError('Double ocurrence words should be strings of'\
                                ' symbols separated by commas')
            if not self.is_dow():
                raise ValueError('Make sure there are exactly two instances of'\
                             ' each symbol')
        
    def is_dow(self):
        """Check if the word has exactly n instances of each symbol."""
        seen = set()
        word_list = [x.strip('"') for x in self.sym_list]
        length = len(word_list)
        for i in range(length):
            if word_list[i] in seen:
                continue
            else:
                # Counts how many times a symbol appears
                d = word_list[i]
                seen.add(word_list[i])
                d_list = [x for x in word_list if x != d]
                if (len(word_list) - len(d_list) != 2) and self.W != '':
                    return False                    
        return True                
    
    def ascending_order(self, min_chars):
        """
        Rewrite the word in ascending order. 
        e.g. the DOW 212a1abb is not in ascending order. While both 121a2abb 
        and 242a4cc are, 121a2abb uses the least available characters and \
            242a4cc does not.

        Parameters
        ----------
        min_chars : boolean
            If True, symbol types are preserved but the least possible 
            character is used.

        Returns
        -------
        W : string
            The output should be in ascending order, using minimal characters
            if specified.
        """
        if len(self.W) == 0:
            return ''
        if min_chars:
            # Ordered list of unique symbos using least values
            letters = sorted(minimum_chars(self.order), reverse=True)
        else:
            # Ordered list of unique symbols
            letters = sorted(self.order, reverse=True)
        
        # Dictionary of pairs to rewrite the word
        pairs = dict()
        
        # For each character in the word, assign the lowest available symbol
        for i in range(len(self.sym_list)):
            sym = self.sym_list[i]
            if sym not in pairs:
                pairs[sym] = letters.pop()
        self.W = ','.join([pairs[x] for x in self.sym_list])
   
    def is_repeat(self, sow):
        """ Checks if a SOW is a repeat word."""
        finds = subfinder(self.sym_list,sow.split(','))
        if len(finds)==2:
            return True
        else:
            return False
        
    def is_return(self, sow):
        """ Checks if a SOW is a return word."""
        sow_list = sow.split(',')
        finds = subfinder(self.sym_list,sow_list)
        sub_list = delete_sublist(sow_list, self.W.split(','))
        rfinds = subfinder(sub_list,sow_list[::-1])
        # Reverses one word and checks for equality
        if len(finds)*len(rfinds)==1:
            return True
        else:
            return False
        
    def are_consecutive(self, sym1, sym2):
        """Determines whether sym1 and sym2 are consecutive symbols"""
        idx = self.order.index(sym1)
        if sym1 == sym2:
            return False
        elif idx != len(self.order)-1 and sym2 == self.order[idx + 1]:
            return True
        else:
            return False        
    
    def reduce(self, to_reduce):
        """
        Generate new DOWs by deleting the SOWs in the set to_reduce

        Parameters
        ----------
        to_reduce : set
            Set of maximal repeat and return words.

        Returns
        -------
        ret : set
            Set of words obtained by deleting SOWs, in ascending order.

        """
        ret = set()
        for sow in to_reduce:
            ret.add(DOW(','.join([x for x in self.sym_list if x not in 
                                  sow.split(',')]), asc_order=True))
        return ret

    def remove_loops(self):
        """Remove all loops from a DOW."""
        loops = set() 
        i=0
        for i in range(len(self.sym_list)-1):
            if self.sym_list[i]==self.sym_list[i+1]:  # Loops correspond to repeats
                loops.add(self.sym_list[i])
        # remove loops
        return DOW(','.join([x for x in self.sym_list if x not in loops]))

    def find_patterns(self):
        """Returns the set of all maximal repeat or return words in a DOW"""
        # Turns the word into a list of letters
        s_list = self.sym_list
        length = len(s_list)
        
        to_reduce = set()
        
        # Sets of repeat and return words
        rep_patterns = set()
        ret_patterns = set()
        
        i=0
        while i < length-1:
            # If a letter is followed by its successor it could be a repeat word
            if self.are_consecutive(s_list[i], s_list[i+1]):
            # if int(word_list[i+1]) == int(word_list[i])+1:
                pattern = list()
                pattern.append(s_list[i])
                j = i+1
                pattern.append(s_list[j])
                while j < length -1 and self.are_consecutive(s_list[j], s_list[j+1]):
                # while j < length-1 and int(word_list[j+1]) == int(word_list[j])+1:
                    j += 1
                    pattern.append(s_list[j])
                last1 = j
                pString = ",".join(pattern)
                # Check that it is a repeat word and add to list
                if self.is_repeat(pString):
                    rep_patterns.add(pString)
                    i = last1
            # If a letter is followed by its predecessor it may be a return word
            elif self.are_consecutive(s_list[i+1], s_list[i]):
                pattern = list()
                pattern.append(s_list[i])
                j = i+1
                pattern.append(s_list[j])
                while j < length -1 and self.are_consecutive(s_list[j+1], s_list[j]):
                    j += 1
                    pattern.append(s_list[j])
                last2 = j
                p = pattern[::-1] #+ pattern
                pString = ",".join(p)
                # Check that it is a return word and add to list
                if self.is_return(pString):
                    ret_patterns.add(pString)
                    i = last2 
            to_reduce.update(rep_patterns)
            to_reduce.update(ret_patterns)
            i += 1
        red_chars = [tr.split for tr in to_reduce]
        triv_set = set()
        for w in s_list:
            if w not in red_chars:
                nw = ",".join([w])
                triv_set.add(nw)
        # used letters won't be added as trivial repeat/return words
        used = set()
        for pat in to_reduce:
            used.update(set(pat))
        # deletes used letters
        triv_set.difference_update(used)
        to_reduce.update(triv_set)
        return to_reduce

def order_chars(char_list):
    """
    Order the symbols in the list, integers before letters, and upper case 
    letters before lower case letters.
    """
    integers = list()
    letters = list()
    for x in char_list:
        if x.isdigit():
            integers.append(int(x))
        elif x.isalpha():
            letters.append(x)
    return [str(x) for x in sorted(integers)] + sorted(letters)

def minimum_chars(char_list):
    """
    Finds the least value characters equivalent to those in the given list.
    """
    integers = list()
    upper = list()
    lower = list()
    for x in char_list:
        if x.isdigit():
            integers.append(x)
        elif x.isupper():
            upper.append(x)
        elif x.islower():
            lower.append(x)
    ord_ints = [str(i+1) for i in range(len(integers))]
    ord_ups = [x for x in string.ascii_uppercase[0:len(upper)]]
    ord_lows = [x for x in string.ascii_lowercase[0:len(lower)]]
    pairs = {k:v for (k,v) in zip(integers + upper + lower, ord_ints + ord_ups + ord_lows)}
    return [pairs[x] for x in char_list]

def subfinder(biglist, pattern):
    """Finds instances of the pattern list in a bigger list."""
    matches = list()
    for i in range(len(biglist)):
        if biglist[i] == pattern[0] and biglist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    return matches

def delete_sublist(sublist, biglist):
    """Deletes sublist from list."""
    for i in range(len(sublist)):
        idx = biglist.index(sublist[i])
        del biglist[idx]
    return biglist

def getdows(n):
    """Produces a list of ascending order DOWs with n symbols"""
    if n < 1:
        print('n must be an integer greater than zero')
    else:    
        words = [[1,1]]
        wordlen = 2*n
        currlen = 2
        while currlen != wordlen:
            currlen += 2
            newwords = []
            for word in words:
                temp_word = [a + 1 for a in word]
                temp_word.insert(0,1)
                for i in range(1,currlen):
                    newword = list(temp_word)
                    newword.insert(i,1)
                    newwords.append(newword)
            words = newwords
    ret = [','.join([str(y) for y in x]) for x in words]
    return ret

def list_duplicates_of(seq,item):
    """Lists duplicate indices of instances of item in the list seq"""
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def separation(w):
    """Computes the total separation of a DOW"""
    sep = 0
    word_list = w.split(',')
    
    l = len(word_list)
    size = int(l/2)
    for i in range(1,size+1):
        locs = list_duplicates_of(word_list,str(i))
        d = max(locs) - min(locs) - 1
        sep += d
    return sep

def tangled(n):
    """Returns the tangled cord on n symbols."""
    if n < 1:
        print('n must be an integer greater than zero')
        return
    else:    
        word_list = ['1']
        for i in range(1,n):
            word_list.append(str(i+1))
            word_list.append(str(i))
        word_list.append(str(n))
    word = ','.join(word_list)
    return word
