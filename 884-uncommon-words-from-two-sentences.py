class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommonList = []
        commonList = []
        words = s1.split() + s2.split()
        for i, word in enumerate(words):
            if word not in commonList:
                if i + 1 >= len(words):
                    uncommonList.append(word)
                elif word in words[i + 1:]:
                    commonList.append(word)
                elif word not in words[i + 1:]:
                    uncommonList.append(word)
            # if word is already in the commonList then just ignore it :)    
        return uncommonList