
score_names _ ["Love", "Fifteen", "Thirty", "Forty"]

___ tennis_score(player1_points, player2_points):
    if player1_points == player2_points:
        r_ "{0}-All".f..(score_names[player1_points])
    else:
        r_ "{0}-{1}".f..(score_names[player1_points],
                                    score_names[player2_points])