class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [k for k,v in collections.Counter(sorted(words)).most_common(k)]