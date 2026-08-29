class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {'(': ')', '[': ']', '{': '}'}
        forward_brackets = set(['(', '[', '{'])
        backward_brackets = set([')',']','}'])
        forward_count = 0
        backward_count = 0
        for i in range(len(s)):
            if s[i] in forward_brackets:
                stack.append(brackets_map[s[i]])
                forward_count += 1
            if s[i] in backward_brackets:
                backward_count += 1
                if stack == []:
                    return False
                if s[i] != stack.pop():
                    return False
        if forward_count == backward_count:
            return True
        else:
            return False


        