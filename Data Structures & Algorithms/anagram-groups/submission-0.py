from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
        
        return list(anagram_map.values())

solution = Solution()
str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
str2 = ['abt', 'bat', 'tab', 'tap', 'pat', 'apt', 'mat', 'tam', 'atm', 'cat', 'act', 'tac']
print(solution.groupAnagrams(str1))
print(solution.groupAnagrams(str2))
    