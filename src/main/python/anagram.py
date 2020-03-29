from collections import Counter
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    answer = []
    m, n = len(s), len(p)
    if m < n:
        return answer
    pCounter = Counter(p)
    sCounter = Counter(s[:n-1])
    print(pCounter)
    print(sCounter)

    index = 0
    for index in range(n - 1, m):
        sCounter[s[index]] += 1
        if sCounter == pCounter:
            answer.append(index - n + 1)
        sCounter[s[index - n + 1]] -= 1
        if sCounter[s[index - n + 1]] == 0:
            del sCounter[s[index - n + 1]]
    return answer

s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result_dict = defaultdict(lambda: [])
        for s in strs:
            hash_val = hash(frozenset(Counter(s).items()))
            result_dict[hash_val].append(s)
        return list(result_dict.values())