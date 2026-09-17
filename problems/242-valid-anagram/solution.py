class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_t = {}
        set_s = {}

        for i in range(len(s)):
            if s[i] in set_s:
                set_s[s[i]] += 1
            else:
                set_s[s[i]] = 1

        for i in range(len(t)):
            if t[i] in set_t:
                set_t[t[i]] += 1
            else:
                set_t[t[i]] = 1

        return set_t == set_s