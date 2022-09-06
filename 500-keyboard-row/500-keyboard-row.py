class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return filter(lambda word:
                        set(word.lower()) - set("qwertyuiop") == set() or
                        set(word.lower()) - set("asdfghjkl") == set() or
                        set(word.lower()) - set("zxcvbnm") == set(),
                    words) 
                
                
                    