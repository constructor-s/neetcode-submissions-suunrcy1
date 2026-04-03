class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def get_all_combos(n: int) -> List[str]:
            if n == 1:
                return [chr(i) for i in range(256)]
            result = []
            for item in get_all_combos(n-1):
                for i in range(256):
                    result.append(item + chr(i))
            return result

        delim_len = 1
        found = False
        while not found:
            for delim in get_all_combos(delim_len):
                for s in strs:
                    if delim in s:
                        break
                else:
                    found = True
                    break
            delim_len += 1
        
        # print([ord(i) for i in delim])

        return chr(len(delim)) + delim + delim.join(strs)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        delim_len = ord(s[0])
        delim = s[1:1+delim_len]
        
        return s[1+delim_len:].split(delim)
