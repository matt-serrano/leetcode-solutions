class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            weight = 0
            for c in word:
                weight += weights[ord(c) - ord('a')]
            
            mapped_char = chr(ord('a') + (25 - (weight % 26)))
            result.append(mapped_char)
        
        return "".join(result)