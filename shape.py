# Project: Gain a Pound of muscle a week
# Creater: Brain Dunigan
# Email: bdunigan80@gmail.com
# Creation / Modification Date: 10-12-2018

print("This is the calculator for gaining a pound of  muscle a month.")
print("")
print("Hello there. What is your name? ")
user_name = input("Please enter in your name: ")
print(" Welcome " + user_name + ". " "You will be asked a number of question. \n "
"Once all the needed information has been obtained you will be provided with the \n "
"amount of calories you will need in order to gain a pound of muscle in a week")
print("")
body_weight = int(input("Please enter you body weight in pound. "))
lift_time = int(input("Please enter how many minutes you lift weight for per week. "))
cardio_time = int(input("Please enter how many minutes of cardio you do per week. "))

strenght_time = lift_time * 5
arobic_time = cardio_time * 8
calorie_needs = body_weight * 12
resting_metobolic_rate = calorie_needs * 1.6
total_exercise_time = (strenght_time + arobic_time)/7

Daily_cal_needs = resting_metobolic_rate + total_exercise_time

Cals_needed_for_gain = Daily_cal_needs + 500

print("Well " + user_name + ", you need a total of " + str(Cals_needed_for_gain) + "each week in order to gain 1 pound of mucle each week.")