class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr:
                curr[w] = {}

            curr = curr[w]
        curr["word"] = word

    def search(self, word: str) -> bool:
        curr_level = [self.root]
        for w in word:
            next_level = []
            for n in curr_level:
                for k, v in n.items():
                    if k != "word" and (
                        w == "." or w == k
                    ):
                        next_level.append(v)
            curr_level = next_level
        for n in curr_level:
            if "word" in n:
                return True
        return False
