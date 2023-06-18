class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or word==word.lower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False
        