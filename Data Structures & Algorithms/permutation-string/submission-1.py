class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Generate dict that contains the counts of chars in s1
        char_counts = {}
        for c in s1:
            char_counts[c] = char_counts.get(c, 0) + 1

        # Initialize window
        for i in range(len(s1)):
            c = s2[i]
            char_counts[c] = char_counts.get(c, 0) - 1

        i = len(s1)
        while i < len(s2):
            if not any(char_counts.values()):
                return True

            # Remove char s2[i - len(s1)]
            c = s2[i - len(s1)]
            char_counts[c] += 1

            # Add char s2[i]
            c = s2[i]
            char_counts[c] = char_counts.get(c, 0) - 1

            i += 1

        return not any(char_counts.values())
