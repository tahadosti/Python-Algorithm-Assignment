def solution(A):
    # Find the total number of elements
    n = len(A) + 1

    # Calculate the expected sum
    total = n * (n + 1) // 2

    # Calculate the missing number
    missing = total - sum(A)

    return missing
