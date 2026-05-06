class Solution:

    def encode(self, strs: List[str]) -> str:
        endoded_str = ''

        for s in strs:
            endoded_str += f"{len(s)}#{s}"
        
        return endoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1 : j+length+1]
            decoded_strs.append(word)
            i = j + length + 1
        
        return decoded_strs