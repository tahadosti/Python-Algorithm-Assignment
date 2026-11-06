def solution(A):
    # Calculate the total sum
    total = sum(A)

    # Start with an empty left side
    left_sum = 0
    min_diff = float('inf')

    # Try every possible split
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total - left_sum

        # Calculate the difference
        diff = abs(left_sum - right_sum)

        # Update the minimum difference
        min_diff = min(min_diff, diff)

    return min_diff
