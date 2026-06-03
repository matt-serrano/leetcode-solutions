# Find the number of rotations for the target
        # Also need to check if the number is in the array
        # Two portions of the array, left and right, which are both sorted
        # left <= right, left, mid, and right pointers
    
        # Implementation:
        # Use binary search to divide the array and compare the target to understand where to search
        # Compare target to leftmost value, then move accordingly