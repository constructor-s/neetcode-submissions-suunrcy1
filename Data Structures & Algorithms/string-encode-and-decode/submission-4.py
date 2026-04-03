class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(chr(len(s))+s for s in strs) # chr(len(s)) because length is < 256

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        n = ord(s[0])
        return [s[1:n+1]] + self.decode(s[n+1:])
