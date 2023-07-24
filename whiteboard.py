# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship


# we get a list of string
#step one: define the function and indentify our params
def solution(matches):
#step two: looked at each string, found our scores based on the col compared two scores and determain win loss or tie  added to our total score the 
# score we got from our team 
    result = 0
    for scores in matches:
        our_score = scores.split(":")
        home = int(our_score[0])
        away = int(our_score[1])
        #convert strings to ints 
        if home > away:
            result += 3
        elif home < away:
            result += 0 
        else:
            result += 1
#step three return our season total (result).