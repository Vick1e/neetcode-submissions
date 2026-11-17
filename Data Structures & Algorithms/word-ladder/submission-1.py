class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet= set(wordList)

        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])

        wordSet.discard(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for i  in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        q.append((newWord, steps+1))
                        wordSet.remove(newWord)

        return 0


        