class Solution:

    def encode(self, strs: List[str]) -> str:
        to_return = ""
        for i in strs:
            to_return += f"{len(i)}*" + i
        return to_return

    def decode(self, s: str) -> List[str]:
        to_return = []
        if s == "":
            return to_return
        i = 0
        while i < len(s):
            sliced_string = s[i:]
            string_len = int(sliced_string[0 : sliced_string.index('*')])
            to_append = sliced_string[sliced_string.index('*') + 1 : 1 + len(str(string_len)) + string_len]
            to_return.append(to_append)
            i += string_len + 1 + len(str(string_len))
        return to_return
