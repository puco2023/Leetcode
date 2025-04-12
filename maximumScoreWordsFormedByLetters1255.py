from collections import Counter
class Solution(object):
    def maxScoreWords(self, words, letters, score):
        hashMap = {}
        for i, s in enumerate(score):
            hashMap[chr(ord("a") + i)] = s
        self.ans = 0
        remaining = Counter(letters)
        def backtrack(start, remaining, currScore):
            self.ans = max(self.ans, currScore)
            for i in range(start, len(words)):
                currWord = Counter(words[i])
                counter = remaining.copy() 
                if any(counter[char] < currWord[char] for char in currWord):
                    continue
                for char in currWord:
                    counter[char] -= currWord[char]
                wordScore = sum(hashMap[key] * count for key, count in currWord.items())
                backtrack(i + 1, counter, currScore + wordScore)
        backtrack(0, remaining, 0)
        return self.ans
