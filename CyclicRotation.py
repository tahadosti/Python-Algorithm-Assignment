def solution(A, K):
    # Check if the array is empty
    if len(A) == 0:
        return A

    # Calculate the rotations
    K = K % len(A)

    # Check if rotation is needed
    if K == 0:
        return A

    # Rotate and return the array
    return A[-K:] + A[:-K]
