class Solution:
    def processStr(self, s: str) -> str:
        arr = []

        for i in s:
            if i.islower(): arr.append(i)
            elif arr and i == '*': arr.pop()
            elif i == '#': arr += arr
            elif i == '%': arr = arr[::-1]

        return "".join(arr)