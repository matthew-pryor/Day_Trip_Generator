import random

def list_of_things_that_interest_me(list):
    random_choice = random.choice(list)
    return random_choice


def day_trip_generator():
    satisfied_answers = False

    do_i_want_to_plan = input("Welcome to the random trip generator, are you ready to let us plan your day trip? Yes or No? ")
    print('\n')
    
    if(do_i_want_to_plan == 'No' or do_i_want_to_plan == 'no'):
            print('Well, I am sorry to hear that, have fun planning it yourself and come back if you change your mind!')
            print('\n')
            satisfied_answers == True

    else:

        while satisfied_answers is False:

            if (do_i_want_to_plan == 'Yes' or do_i_want_to_plan == 'yes'):

                list_of_destinations = ['New York', 'Kansas City', 'Saint Louis', 'Chicago', 'Louisville', 'Tampa']
                random_destination = list_of_things_that_interest_me(list_of_destinations)
                print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")

                list_of_cuisine = ['Chinese', 'Mexican', 'Etheopian', 'Midwest BBQ', 'Eastcoast BBQ', 'Thai', 'sushi', 'breakfast food']
                random_cuisine = list_of_things_that_interest_me(list_of_cuisine)
                print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")

                list_of_transportation = ['a taxi/Uber/Lyft', 'a train', 'a bike', 'your personally operated vehicle', 'a bus', 'an airplane']
                random_transportaion = list_of_things_that_interest_me(list_of_transportation)
                print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")

                list_of_entertainment = ['parooz Topgolf', 'to the movies', 'meander through a museum', 'see a sportsgame', 'play in an arcade', 'go for a hike', 'drive goKarts']
                random_entertainment = list_of_things_that_interest_me(list_of_entertainment)
                print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                print('\n')

                are_you_happy_with_the_trip = input('Are you happy with what we have selected for you? Yes or No? ')
                print('\n')
                
                if(are_you_happy_with_the_trip == 'Yes' or are_you_happy_with_the_trip == 'yes'):
                    satisfied_answers = True

                    print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")                
                    print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                    print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                    print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                    print("This is your itinerary, enjoy the trip! It was fun planning it for you!")

                else:
                    reroll_everything = input("Sorry to hear that, do you want to reroll everything? Yes or No? ")
                    print('\n')

                    if(reroll_everything == 'Yes' or reroll_everything == 'yes'):
                        
                        satisfied_answers = False

                    elif(reroll_everything == 'No' or reroll_everything == 'no'):

                        satisfied_answers = True
                        rerolled_satisfaction = False

                        while rerolled_satisfaction is False:
                            value = input(f"What specifically didn't you like about the trip? Please type in the number associated with the choice that you did not like. Don't worry, you'll be able to keep randomizing until you're satisfied: Destination({random_destination}) = 1, Cuisine({random_cuisine}) = 2, Transportation({random_transportaion}) = 3, Entertainment({random_entertainment}) = 4. ")
                            print('This option will be rerolled.')
                            print('\n')

                            if(value == '1'):

                                list_of_destinations = ['New York', 'Kansas City', 'Saint Louis', 'Chicago', 'Louisville', 'Tampa']
                                list_of_destinations.remove(random_destination)
                                random_destination = list_of_things_that_interest_me(list_of_destinations)

                            elif(value == '2'):
                                    
                                list_of_cuisine = ['Chinese', 'Mexican', 'Etheopian', 'Midwest BBQ', 'Eastcoast BBQ', 'Thai', 'sushi', 'breakfast food']
                                list_of_cuisine.remove(random_cuisine)
                                random_cuisine = list_of_things_that_interest_me(list_of_cuisine)

                            elif(value == '3'):
                                    
                                list_of_transportation = ['a taxi/Uber/Lyft', 'a train', 'a bike', 'your personally operated vehicle', 'a bus', 'an airplane']
                                list_of_transportation.remove(random_transportaion)
                                random_transportaion = list_of_things_that_interest_me(list_of_transportation)

                            elif(value == '4'):
                                    
                                list_of_entertainment = ['parooz Topgolf', 'to the movies', 'meander through a museum', 'see a sportsgame', 'play in an arcade', 'go for a hike', 'drive goKarts']
                                list_of_entertainment.remove(random_entertainment)
                                random_entertainment = list_of_things_that_interest_me(list_of_entertainment)
                                

                            print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")                
                            print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                            print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                            print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                            print('\n')


                            reroll_options = input("Do you want to reroll anymore options you didn't like? Yes or No? ")
                            print('\n')

                            if(reroll_options == 'No' or reroll_options == 'no'):
                                rerolled_satisfaction = True

                                print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")                
                                print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                                print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                                print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                                print("This is your final itinerary, I hope your new trip lives up to your expectations!")

                            else:
                                rerolled_satisfaction = False



day_trip_generator()