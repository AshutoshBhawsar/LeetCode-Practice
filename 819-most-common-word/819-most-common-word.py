class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hash_map={'!':1,'?':1,'\'':1,',':1,';':1,'.':1,'\"':1}
        new_para=""
        for i in paragraph:
            if i not in hash_map:
                new_para+=i.lower()
            else:
                new_para+=' '
        word_list=collections.Counter(new_para.split(' '))
        new_dict=dict(sorted(word_list.items(), key=lambda item: item[1], reverse=True))
        print(new_dict)
        for key,value in new_dict.items():
            if key not in banned and key!="":
                return key
        