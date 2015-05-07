'''
spell checker with noisy channel model

'''
import re
import TestCase 
from AlgorithmPeterNorvig import PeterNorvig

class SpellChecker:
    
    def __init__(self,path,algorithm):
        
        self.__mAlgorithm__  = algorithm
        
        with open(path,'r') as f:
            data = f.read()
            words = self.__Tokenize__(data)
            self.__mAlgorithm__.Train(words)    
        
    #extract the words and return them in a list
    def __Tokenize__(self,text):
        return re.findall('[a-z]+', text.lower()) 
                    
    #public method
    def Correct(self,word):
        return self.__mAlgorithm__.Correct(word)
        
    def Spelltest(self,tests, bias = None, verbose = False):    
        return self.__mAlgorithm__.Spelltest(tests,bias,verbose)
    
        
def main():
    
    peterNorvig = PeterNorvig()
    
    path = 'big.txt'
    spellChecker = SpellChecker(path,peterNorvig)
    
    print spellChecker.Spelltest(TestCase.tests1,None,False)
    #print spellChecker.spelltest(TestCase.tests2,None,False)

if __name__ == "__main__":
    main()
