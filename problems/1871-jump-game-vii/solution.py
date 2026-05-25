class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        k = 0
        jumpList = []
        for i in range(1, len(s)):
            if s[i] == "0":
                k += 1
                jumpList.append(k)

                k = 0
                continue

            k += 1

        return minJump in jumpList and maxJump in jumpList

