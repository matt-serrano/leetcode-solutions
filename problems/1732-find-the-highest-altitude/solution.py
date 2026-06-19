class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        length = len(gain)
        highest = altitudes[0]
        
        for i in range(length):
            altitudes.append(altitudes[i] + gain[i])
            
            if altitudes[i + 1] > highest:
                highest = altitudes[i + 1]

        return highest