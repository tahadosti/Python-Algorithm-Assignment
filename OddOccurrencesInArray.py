def solution(A):
    # Store the unpaired number
    result = 0

    # Use XOR to cancel paired numbers
    for number in A:
        result = result ^ number

    # Return the unpaired number
    return result
