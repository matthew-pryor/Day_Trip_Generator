import random

def list_of_things_that_interest_me(list):
    random_choice = random.choice(list)
    return random_choice


def day_trip_generator():

    need_help_planning_trip = True
    
    while need_help_planning_trip is True:

        do_i_want_to_plan = input("Welcome to the random trip generator, are you ready to let us plan your day trip? Yes or No? ")
        print('\n')
        
        if(do_i_want_to_plan == 'No' or do_i_want_to_plan == 'no'):
            need_help_planning_trip = False
            print('Well, I am sorry to hear that, have fun planning it yourself and come back if you change your mind!')

        elif(do_i_want_to_plan == 'Yes' or do_i_want_to_plan == 'yes'):
            
            need_help_planning_trip = True
            satisfied_answers = False

            list_of_destinations = ['New York', 'Kansas City', 'Saint Louis', 'Chicago', 'Louisville', 'Tampa']
            random_destination = list_of_things_that_interest_me(list_of_destinations)
            print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")

            list_of_cuisine = ['Chinese', 'Mexican', 'Ethiopian', 'Midwest BBQ', 'Eastcoast BBQ', 'Thai', 'sushi', 'breakfast food']
            random_cuisine = list_of_things_that_interest_me(list_of_cuisine)
            print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")

            list_of_transportation = ['a taxi/Uber/Lyft', 'a train', 'a bike', 'your personally operated vehicle', 'a bus', 'an airplane']
            random_transportaion = list_of_things_that_interest_me(list_of_transportation)
            print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")

            list_of_entertainment = ['parooz Topgolf', 'to the movies', 'meander through a museum', 'see a sportsgame', 'play in an arcade', 'go for a hike', 'drive goKarts']
            random_entertainment = list_of_things_that_interest_me(list_of_entertainment)
            print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
            print('\n')

            while satisfied_answers is False:

                    are_you_happy_with_the_trip = input('Are you happy with what we have selected for you? Yes or No? ')
                    print('\n')
                    
                    if(are_you_happy_with_the_trip == 'Yes' or are_you_happy_with_the_trip == 'yes'):
                        satisfied_answers = True
                        need_help_planning_trip = False

                        print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")                
                        print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                        print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                        print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                        print("This is your itinerary, enjoy the trip! It was fun planning it for you!")

                    elif(are_you_happy_with_the_trip == 'No' or are_you_happy_with_the_trip == 'no'):
                        satisfied_answers = False
                        need_help_planning_trip = False
                        want_to_reroll_specifics_or_quit = True

                        while want_to_reroll_specifics_or_quit is True:

                            reroll_everything = input("Sorry to hear that, do you want to reroll everything? Yes or No? ")
                            print('\n')

                            if(reroll_everything == 'Yes' or reroll_everything == 'yes'):
                                
                                need_help_planning_trip = True
                                satisfied_answers = True
                                want_to_reroll_specifics_or_quit = False
                                break

                            elif(reroll_everything == 'No' or reroll_everything == 'no'):

                                desire_to_quit = False

                                while desire_to_quit is False:

                                    stop_rerolling = input("Do you want to stop rerolling? Yes or No? ")
                                    print('\n')

                                    if(stop_rerolling == 'Yes' or stop_rerolling == 'yes'):
                                        
                                        print('Well, I am sorry to hear that, have fun planning it yourself and come back if you change your mind!')

                                        desire_to_quit = True
                                        want_to_reroll_specifics_or_quit = False
                                        satisfied_answers = True
                                        need_help_planning_trip = False

                                    elif(stop_rerolling == 'No' or stop_rerolling == 'no'):
                                        
                                        rerolled_satisfaction = False     

                                        while rerolled_satisfaction is False:

                                            value = input(f"Well then what specifically didn't you like about the trip? Please type in the number associated with the choice that you did not like. Don't worry, you'll be able to keep randomizing until you're satisfied: Destination({random_destination}) = 1, Cuisine({random_cuisine}) = 2, Transportation({random_transportaion}) = 3, Entertainment({random_entertainment}) = 4. ")
                                            print('This option will be rerolled.')
                                            print('\n')

                                            if(value == '1'):

                                                list_of_destinations = ['New York', 'Kansas City', 'Saint Louis', 'Chicago', 'Louisville', 'Tampa']
                                                list_of_destinations.remove(random_destination)
                                                random_destination = list_of_things_that_interest_me(list_of_destinations)
                                                print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")
                                                print('\n')
                                                rerolled_satisfaction = True
                                                complete_satisfaction = False

                                            elif(value == '2'):
                                                    
                                                list_of_cuisine = ['Chinese', 'Mexican', 'Ethopian', 'Midwest BBQ', 'Eastcoast BBQ', 'Thai', 'sushi', 'breakfast food']
                                                list_of_cuisine.remove(random_cuisine)
                                                random_cuisine = list_of_things_that_interest_me(list_of_cuisine)
                                                print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                                                print('\n')
                                                rerolled_satisfaction = True
                                                complete_satisfaction = False

                                            elif(value == '3'):
                                                    
                                                list_of_transportation = ['a taxi/Uber/Lyft', 'a train', 'a bike', 'your personally operated vehicle', 'a bus', 'an airplane']
                                                list_of_transportation.remove(random_transportaion)
                                                random_transportaion = list_of_things_that_interest_me(list_of_transportation)
                                                print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                                                print('\n')
                                                rerolled_satisfaction = True
                                                complete_satisfaction = False

                                            elif(value == '4'):
                                                    
                                                list_of_entertainment = ['parooz Topgolf', 'to the movies', 'meander through a museum', 'see a sportsgame', 'play in an arcade', 'go for a hike', 'drive goKarts']
                                                list_of_entertainment.remove(random_entertainment)
                                                random_entertainment = list_of_things_that_interest_me(list_of_entertainment)
                                                print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                                                print('\n')
                                                rerolled_satisfaction = True
                                                complete_satisfaction = False

                                            else:
                                                rerolled_satisfaction = False
                                                complete_satisfaction = True
                                                print('Invalid response, try again.')
                                                print('\n')

                                            while complete_satisfaction is False:

                                                reroll_options = input("Do you want to reroll anymore options you didn't like? Yes or No? ")
                                                print('\n')

                                                if(reroll_options == 'No' or reroll_options == 'no'):
                                                    complete_satisfaction = True
                                                    rerolled_satisfaction = True
                                                    desire_to_quit = True
                                                    need_help_planning_trip = False
                                                    want_to_reroll_specifics_or_quit = False
                                                    satisfied_answers = True
                                                    need_help_planning_trip = False

                                                    print(f"Congratulations, it looks like you're going to {random_destination} for your day trip! Have fun!")                
                                                    print(f"Delicious, it looks like you'll be eating {random_cuisine} while you're there! Hopefully you don't have an allergy!")
                                                    print(f"Interesting choice, it looks like you'll be taking {random_transportaion} to get around. I'm sure you can make it work!")
                                                    print(f"Oh Fun! I guess you're gonna go {random_entertainment} on your day trip. Enjoy!")
                                                    print("This is your final itinerary, I hope your new trip lives up to your expectations!")
                                                    break

                                                
                                                elif(reroll_options == 'Yes' or reroll_options == 'yes'):
                                                    rerolled_satisfaction = False
                                                    complete_satisfaction = True

                                                else:
                                                    complete_satisfaction = False
                                                    rerolled_satisfaction = False
                                                    print('Invalid response, try again.')
                                                    print('\n')

                                    else:
                                        need_help_planning_trip = False
                                        print('Invalid response, try again.')
                                        print('\n')

                            else:
                                want_to_reroll_specifics_or_quit = False
                                print('Invalid response, try again.')
                                print('\n')

                    else:
                        satisfied_answers = False
                        print('Invalid response, try again.')
                        print('\n')

        else:
            need_help_planning_trip = True
            print('Invalid response, try again.')
            print('\n')


day_trip_generator()