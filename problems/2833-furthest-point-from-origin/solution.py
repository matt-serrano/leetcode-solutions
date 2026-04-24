class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        wild = 0

        for i in moves:
            if (i == 'R'):
                right += 1
            elif (i == 'L'):
                left += 1
            else:
                wild += 1

        return abs(left - right) + wild
