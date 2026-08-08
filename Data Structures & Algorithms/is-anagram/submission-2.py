class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = {}
        for i in range(len(s)):
            if s[i] not in table_s:
                table_s[s[i]] = 1
            else:
                table_s[s[i]] += 1
        table_t = {}
        for i in range(len(t)):
            if t[i] not in table_s:
                return False
            elif t[i] not in table_t:
                table_t[t[i]] = 1
            else:
                table_t[t[i]] += 1
        if set(table_t) != set(table_s):
            return False
        for i in table_t:
            if table_t[i] != table_s[i]:
                return False
        return True
        


        