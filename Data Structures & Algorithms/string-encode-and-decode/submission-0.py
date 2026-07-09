
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result

solution = Solution()

strs = ["hello", "world"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print(f"Original: {strs}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
print(f"Equal: {strs == decoded}")  

strs = ["", "hello", "", "world", ""]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print(f"Equal: {strs == decoded}")  

strs = ["hello#world", "foo#bar", "#", "##"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print(f"Equal: {strs == decoded}")  

strs = ["hello"]
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print(f"Equal: {strs == decoded}")  