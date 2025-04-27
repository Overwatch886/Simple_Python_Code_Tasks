#importing random module
import random
#creating an empty list to store the results
results = []
#getting user input for number of trials
print(" I can help you calculate the probability of getting a streak of 6 head or and tails in a given number of coin tosses")
user_input = int(input('Input the amount of tail you want me to randomly flip the coin.')
#a random 0 equates to tails and a 1 to heads
for i in range(user_input) :
    #generating a random number
    coin = random.randint(0, 1)
    results.append(coin)
    #checking the  results for 6 streaks of heads or tails
    streak = 0
    no_of_6tail_streaks = 0
    no_of_6head_streaks = 0
    for j in range(1, len(results)):
        if results[j] == results[j-1]:
            streak += 1
        else:
            streak = 0
        #checking if the streak is 6
        #counting the number of streaks
        if streak == 6 and results[j] == 1:
            no_of_6head_streaks += 1
        elif streak == 6 and results[j] == 0:
            no_of_6tail_streaks += 1
#calculating the probability
probability_of_6head_streak = no_of_6head_streaks / len(results)
probability_of_6tail_streak = no_of_6tail_streaks / len(results)
probability_of_any_6streak = probability_of_6head_streak + probability_of_6tail_streak
#displaying the results
print("With " + str(no_of_6head_streaks) + " streaks of 6 heads gotten, the probability of 6 heads streak is ", probability_of_6head_streak)
print("With " + str(no_of_6tail_streaks) + " streaks of 6 tails gotten, the probability of 6 tails streak is ", probability_of_6tail_streak)
print("With " + str(no_of_6head_streaks+no_of_6tail_streaks) + " streaks of 6 heads and tails gotten, the probability of 6 streaks of head and tail is ", probability_of_any_6streak)
