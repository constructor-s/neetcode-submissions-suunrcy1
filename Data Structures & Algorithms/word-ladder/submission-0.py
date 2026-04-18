from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {}
        q = deque()
        q.append((1, beginWord))
        while q:
            dist, word = q.popleft()
            if word == endWord:
                return dist
            if word not in visited:
                visited[word] = dist
                for word2 in wordList:
                    if sum(int(c1!=c2) for c1, c2 in zip(word, word2)) == 1:
                        q.append((dist+1, word2))
        return 0