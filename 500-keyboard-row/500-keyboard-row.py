class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Set approach
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
          w = set(word.lower())
          if w <= line1 or w <= line2 or w <= line3:
            ret.append(word)
        return ret
        
        
        
        
        
        
        # One liner
#         return filter(lambda word:
#                         set(word.lower()) - set("qwertyuiop") == set() or
#                         set(word.lower()) - set("asdfghjkl") == set() or
#                         set(word.lower()) - set("zxcvbnm") == set(),
#                     words) 
                
                
                    