class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index1=-1
        for i in range(len(word)):
            if word[i]==ch:
                index1=i
                break
        if index1<0:
            return word
        return word[index1::-1]+word[index1+1:]