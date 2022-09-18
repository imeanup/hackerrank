#  The number of valleys can be counted as the number of steps taken upwards to sea level (i.e., when 'level' goes from -1 to 0. 
# This is true, because each such step ends the sequence of steps below sea level, signifying the end of a valley.

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    level = 0
    for i in path:
        if i == "U":
            level += 1
        else:
            level -= 1
        if level == 0 and i == "U":
            valley += 1
    return valley
