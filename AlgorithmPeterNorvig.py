from SpellingAlgorithm import SpellingAlgorithm
import collections

#http://norvig.com/spell-correct.html
class PeterNorvig(SpellingAlgorithm):
        
    def __init__(self):
        super(PeterNorvig,self).__init__()
        self.__alphabet__ = 'abcdefghijklmnopqrstuvwxyz'
            
    def Correct(self,word):

        knownSet = self.__Known__([word])
    
        editDistance1Set = self.__Known__(self.__EditDistance1__(word))    
    
        editDistance2Set = self.__EditDistance2__(word)
        
        candidates = knownSet or editDistance1Set or editDistance2Set or [word]
        
        #this return the item with the largest count in the dict        
        correctedWord = max(candidates, key = self.__mKnownWords__.get)
    
        return correctedWord
        
    #get each word count    
    def Train(self,words):
        self.__mKnownWords__ = collections.defaultdict(lambda: 1)
    
        #add one smoothing
        for f in words:
            self.__mKnownWords__[f] += 1
            
    def Spelltest(self,tests, bias = None, verbose = False):
    
        import time
    
        n, bad, unknown, start = 0, 0, 0, time.clock()
    
        if bias:
            for target in tests:
                self.__mKnownWords__[target] += bias
                          
        for target, wrongs in tests.items():
            for wrong in wrongs.split():
                n += 1
                        
                w = self.Correct(wrong)

                if w != target:
                    bad += 1
                    unknown += (target not in self.__mKnownWords__)
                    if verbose:
                        print '%r => %r (%d); expected %r (%d)' % (wrong, w, __mKnownWords__[w], target, __mKnownWords__[target])
                        
        return dict(bad = bad, n = n, bias = bias, pct = int(100. - 100.* bad / n), 
                    unknown = unknown, secs = int(time.clock() - start) )
                
            
    def __Known__(self,words):
        return set(w for w in words if w in self.__mKnownWords__)
            
    def __EditDistance1__(self,word):
    
       splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
      
       deletes = [a + b[1:] for a, b in splits if b]
   
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
   
       replaces = [a + c + b[1:] for a, b in splits for c in self.__alphabet__ if b]
   
       inserts = [a + c + b for a, b in splits for c in self.__alphabet__]
   
       return set(deletes + transposes + replaces + inserts)

    def __EditDistance2__(self,word):
        knownEdit2 = [e2 for e1 in self.__EditDistance1__(word) for e2 in self.__EditDistance1__(e1) if e2 in self.__mKnownWords__]
        
        return set(knownEdit2)
    
    