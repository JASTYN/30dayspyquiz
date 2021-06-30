

def processScores():
    # Allow user to enter scores
    scores = 0
    scoreCount = 0
    while (scoreCount < 3): # input 3 scores
        newScore = input(''Enter a valid score\n'')
        if newScore.isdigit() and int(newScore) >= 0:
            newScore = int(newScore) # cast to integer
            scores = scores + newScore # sum all scores
            scoreCount = scoreCount + 1 # increment number of scores
        else:
            print(''Invalid input. Please try again.'')
            continue
        # calculate average
        if (scoreCount == 3):
            calcAverage(scores, scoreCount)