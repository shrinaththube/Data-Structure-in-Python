'''
Created on Jun 24, 2016

@author: Shrinath Thube
'''

class TrieNode(object):
    
    def __init__(self):
        self.alpha = {}
        self.it_is_last_alpha = False
        
    def __str__(self):
        return str(self.alpha) +"  "+ str(self.it_is_last_alpha)
    
    def is_contain(self,ch):
        return self.alpha.has_key(ch)
    
    # send None if key is not present
    def next_trie_node(self,ch):
        return self.alpha.get(ch)
    
    def add_alpha(self,ch,next_trie_node):
        self.alpha.setdefault(ch,next_trie_node)
        
class Trie(object):
    
    def __init__(self):
        self.root = None
        self.word_count = 0
    
    """ Insert word in trie"""
    def add_word(self,word_string):
        if not word_string: return
        if self.root == None:
            self.root = TrieNode() #Trie is not yet formed
 
        traverse = self.root
        for ch in word_string:
            if traverse.is_contain(ch):
                traverse = traverse.next_trie_node(ch)
            else:
                new_trie_node = TrieNode()
                traverse.add_alpha(ch, new_trie_node)
                traverse = traverse.next_trie_node(ch)
        
        traverse.it_is_last_alpha = True    #indicates end of word
            
    """Using backTarck - DFS - return all words that are in trie"""
    def print_all_words(self,root,word,result_wl):
        if root == None: return
        if root.it_is_last_alpha:
            result_wl.append(''.join(word)) 
            
        for ch in root.alpha:
            word.append(ch)
            self.print_all_words(root.next_trie_node(ch),word, result_wl)  
            word.pop()     
        return result_wl
    
    """ return all words that contains given prefix
    iterate up to last character of prefix call to print all node with root as last char node
    """
    def print_all_contains_prefix(self,prefix,root):
        if not prefix: return None
        if root == None: return None
      
        travese = root
        for pr in prefix:
            if not travese.is_contain(pr):
                print "No word is from this prefix"
                return None
            travese = travese.next_trie_node(pr)
        
        return self.print_all_words(travese, [prefix], [])
    
    """ return True if word is in Trie else return False"""
    def is_word_contain(self,word,root):
        if root == None: return False
        if not word: return False
        
        traverse = root
        for ch in word:
            if not traverse.is_contain(ch):
                return False
            traverse = traverse.next_trie_node(ch)
        return traverse.it_is_last_alpha #return true if last word set true
        
    def del_word(self,word,root):
        if root == None:
            print "trie is not formed yet"
            return False
        if not word:
            if not root.it_is_last_alpha: return False 
            root.it_is_last_alpha = False
            return len(root.alpha) == 0 # return true if does not having any children
        if not root.is_contain(word[:1]):
            print "word is not present in trie"
            return False
        
        safe_to_delet = self.del_word(word[1:], root.next_trie_node(word[:1]))
            
        if safe_to_delet:
            root.alpha.pop(word[:1])
            return len(root.alpha) == 0
        
        return False
    


t1 = Trie()
t1.add_word("abc")
t1.add_word("abcd")
t1.add_word("abctpq")
t1.add_word("pqrs")
t1.add_word("abcdefghi")
t1.add_word("thube")
t1.add_word("sanjay")
t1.add_word("shrinath")

print t1.print_all_words(t1.root,[],[])
print t1.print_all_contains_prefix("th", t1.root)

print "Shrinath present in trie - ", t1.is_word_contain("shrinath", t1.root)

t1.del_word("shrinath", t1.root)

print t1.print_all_words(t1.root,[],[])
print "Shrinath present in trie - ", t1.is_word_contain("shrinath", t1.root)
