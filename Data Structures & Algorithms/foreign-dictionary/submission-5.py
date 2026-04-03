class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for i in range(len(words) - 1):
            for char1, char2 in zip(words[i], words[i+1]):
                if char1 != char2:
                    if char1 not in graph:
                        graph[char1] = {char2}
                    else:
                        graph[char1].add(char2)
                    break
            else:
                # So the words have the same prefix
                if len(words[i+1]) < len(words[i]):
                    return ""
        
        sequence = []
        # Do DFS, store post-order
        def dfs(start):
            if start in sequence:
                return []

            result = []
            stack = [start]
            while stack:
                curr = stack[-1]
                if curr not in graph:
                    # reached the end
                    stack.pop()
                    result.append(curr)
                else:
                    for child in graph[curr]:
                        if child in stack:
                            raise ValueError()
                        if child not in result and child not in sequence:
                            stack.append(child)
                            break
                    else:
                        # reached the end
                        stack.pop()
                        result.append(curr)

            return list(reversed(result))

        print(graph)
        for start in graph:
            try:
                sequence = dfs(start) + sequence
            except ValueError:
                return ""

        for word in words:
            for ch in word:
                if ch not in sequence:
                    sequence.append(ch)

        return "".join(sequence)
