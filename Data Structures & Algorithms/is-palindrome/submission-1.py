class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [c for c in s.lower() if c.isalnum()]
        print(s_list)
        for i in range(len(s_list) // 2):
            if s_list[i] != s_list[len(s_list) - 1 - i]:
                print(i)
                return False
        return True
        
        