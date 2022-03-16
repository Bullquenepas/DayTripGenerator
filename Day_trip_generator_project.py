# Tasks

# 1. Create a GitHub repository and clone it down to your local computer to store your code in a remote repository

# 2. Create your Python project in Visual Studio Code

# 3. Write the code for the project and be sure to test as you go along

# a. Store the trip options for destinations, restaurants, transportation, and entertainment in a List (this would be good to place at the top of the file)

destination_options = ['Tokyo', 'Greece', 'Peru', 'Spain']

restaurant_options = ['Italian restaurant', 'Spanish restaurant', 'Sea food restaurant', 'Asian restaurant']

transportation_options = ['Train', 'Bus', 'Rental', 'Rideshare']

entertainment_options = ['Museum', 'Live theater', 'Stand-up comedy', 'Local tours']

# b. Get a random element from each of those sets of options. We recommend declaring variables for a random destination, restaurant, transportation, and entertainment

# if instructions meant 1 function for each list

import random

def possible_destination_at_random(passed_in_destination): 
    rand_destination = random.choice(passed_in_destination)
    return rand_destination

result_random_destination = possible_destination_at_random(destination_options)
#print(result_random_destination)

def possible_restaurant_at_random(passed_in_restaurant):
    rand_restaurant = random.choice(passed_in_restaurant)
    return rand_restaurant

result_random_restaurant = possible_restaurant_at_random(restaurant_options)
#print(result_random_restaurant)

def possible_transportation_at_random(passed_in_transportation):
    rand_transportation = random.choice(passed_in_transportation)
    return rand_transportation

result_random_transportation = possible_transportation_at_random(transportation_options)
#print(result_random_transportation)

def possible_entertainment_at_random(passed_in_entertainment):
    rand_entertainment = random.choice(passed_in_entertainment)
    return rand_entertainment

result_random_entertainment = possible_entertainment_at_random(entertainment_options)
#print (result_random_entertainment)


# #if instructions meant 1 function for all
# def trip_at_random(passed_in_trip):
#     rand_trip = random.choice(passed_in_trip)
#     return rand_trip

# result_random_destination = trip_at_random(destination_options)
# result_random_restaurant = trip_at_random(restaurant_options)
# result_random_transportation = trip_at_random(transportation_options)
# result_random_entertainment = trip_at_random(entertainment_options)
#print(result_random_...)

# c. Display the initial random trip to your user

trip_question = input('Would you like to select a random trip?(Yes or No) ').upper()
if(trip_question == 'YES'):
    print(result_random_destination, result_random_restaurant, result_random_transportation, result_random_entertainment)
elif(trip_question == 'NO'):
    print('Good bye.')
    no_trips = False
    while no_trips is False:
        trip_question2 = input('If you wish to continue enter Yes. ').upper()
        if(trip_question2 == 'YES'):
            no_trips = True
        

# d. Prompt the user to see if they are satisfied // # e. IF not, find out which trip feature they want to change and randomly select a new feature. // # f. Keep doing this process until the user is satisfied with the trip

user_reaction1 = input('Are you satisfied with the random trip selected? ').upper()

if(user_reaction1 == 'YES'):
    print('Great! The next step is to confirm the trip.')
elif(user_reaction1 == 'NO'):
    print("No problem. Let's find another option.")
    is_satisfied = False
    while is_satisfied is False:
        user_reaction2 = input('Which trip feature would you like to adjust? Destination, Restaurant, Transportation, or Entertainment? If you are satisfied with selection please type "Done" ').upper()
        if(user_reaction2 == 'DESTINATION'):
            print(result_random_destination)
        if(user_reaction2 == 'RESTAURANT'):
            print(result_random_restaurant)
        if(user_reaction2 == 'TRANSPORTATION'):
            print(result_random_transportation)
        if(user_reaction2 == 'ENTERTAINMENT'):
            print(result_random_entertainment)
        if(user_reaction2 == 'DONE'):
            is_satisfied = True


# g. Display the completed trip to the console.

if(user_reaction1 == 'YES'):
    print('Trip confirmed. ' )