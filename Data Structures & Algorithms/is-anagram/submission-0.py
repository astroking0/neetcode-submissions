from collections import Counter

class Solution:
    def isAnagram(self, s : str, t : str) -> bool:
        return Counter(s) == Counter(t)
solution = Solution()
s1 = "farrari"
t1 = "rarrafi"
s2 = "silktan"
t2 = "killtons"
print(solution.isAnagram(s1, t1))
print(solution.isAnagram(s2, t2))
