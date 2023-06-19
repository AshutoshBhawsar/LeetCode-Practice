class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def isPrice(word: str) -> bool:
            return word.startswith('$') and word[1:].isnumeric()
        
        list_words=sentence.split()
        for i in range(len(list_words)):
            if isPrice(list_words[i]):
                price=int(list_words[i][1:])
                list_words[i]="${:.2f}".format(price-price*discount/100)
        return (" ".join(list_words))
                