class Solution(object):
    def mergeAlternately(self, word1, word2):
        s=""
        for i in range(min(len(word1),len(word2))):
            s+=word1[i]
            s+=word2[i]
        for i in range(min(len(word1),len(word2)),max(len(word1),len(word2))):
            if len(word1)>len(word2):
                s+=word1[i]
            else:
                s+=word2[i]
        return s
