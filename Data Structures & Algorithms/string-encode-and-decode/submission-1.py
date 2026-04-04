from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # find delimiter '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])  # get length
            word = s[j+1:j+1+length]  # extract string
            res.append(word)

            i = j + 1 + length  # move to next

        return res