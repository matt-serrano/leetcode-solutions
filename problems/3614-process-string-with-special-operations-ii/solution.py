class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Forward pass: compute final length and track metadata
        l = 0
        star_used = []     # whether each '*' actually deleted a char
        hash_sizes = []    # store length BEFORE each '#'

        for c in s:
            if c.islower():
                l += 1
            elif c == '*':
                if l > 0:
                    l -= 1
                    star_used.append(True)
                else:
                    star_used.append(False)
            elif c == '#':
                hash_sizes.append(l)
                l *= 2
            elif c == '%':
                pass

        # If k is out of range
        if k >= l:
            return '.'

        # Reverse pass: walk backwards and undo operations
        si = len(s) - 1
        star_i = len(star_used) - 1
        hash_i = len(hash_sizes) - 1

        while si >= 0:
            c = s[si]

            if c.islower():
                # This lowercase existed in final string
                if k == l - 1:
                    return c
                l -= 1

            elif c == '*':
                # Undo only if it actually deleted something
                if star_used[star_i]:
                    l += 1
                star_i -= 1

            elif c == '#':
                # Undo doubling
                prev = hash_sizes[hash_i]
                hash_i -= 1

                if k >= prev:
                    k -= prev
                l = prev

            elif c == '%':
                # Undo reversal
                k = l - 1 - k

            si -= 1

        return '.'