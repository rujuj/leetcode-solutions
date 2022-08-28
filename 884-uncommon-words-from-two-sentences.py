class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = {}
        uncommonList = []
        words = s1.split() + s2.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        for word in counts:
            if counts[word] == 1:
                uncommonList.append(word)
        return uncommonList