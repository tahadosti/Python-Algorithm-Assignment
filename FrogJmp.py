def solution(X, Y, D):
    # Calculate the distance to the target
    distance = Y - X

    # Find the minimum number of jumps
    jumps = (distance + D - 1) // D

    return jumps
