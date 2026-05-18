#calculate the run rate and required run rate to win match
total_score = input("enter the total score: ")
current_score = input("enter the current run score: ")
total_overs = input("enter the total overs: ")
total_balls = int(total_overs) * 6
balls_faced = input(float("enter the balls faced: "))
remaining_balls = total_balls - int(balls_faced)
curreent_run_rate = int(current_score) / int(remaining_balls)

