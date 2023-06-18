class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result_str=""
        for word in title.split():
            if len(word)<3:
                result_str+=word.lower()+" "
                continue
            else:
                result_str+=word[0].upper()+word[1:].lower()+" "
        return result_str[:-1]