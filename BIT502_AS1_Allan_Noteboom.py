#moldule imported to clear console
import os

# This section prints out the main menu and asks you where you want to go
def main_menu():
    os.system('cls')
    
    main_menu = ['1. Membership Plans', '2. Optional Extras', '3. Gym Challenge', '4. Exit The Program'] 
    print('MAIN MENU')
    print(' ')
    for i in main_menu:
            print(i)
    while True:    
        main_menu_option = input('Where would you like to go? ')
        if main_menu_option == '1':
            os.system('cls')
            membership_menu()
        elif main_menu_option == '2':
            optional_extras()
        elif main_menu_option == '3':
            gym_challenge()
        elif main_menu_option == '4':
            print('Thank you. Until next time!')
            quit()
        else:
            print('This is an invalid option. Try again')
            continue

#This section prints the membership menu and asks you to select an option
def membership_menu():
    os.system('cls')
    
    membership_menu = ['1. Basic', '2. Regular', '3. Premium', '4. Return To Main Menu', '5. Exit The Program']
    print('MEMBERSHIP PLANS')
    print(' ')
    for option in membership_menu:
        print(option)
            
    while True:
        membership_cost = input('Which plan are you interested in? ')
        if membership_cost == '1':
            basic_membership()
        elif membership_cost == '2':
            regular_membership()
        elif membership_cost == '3':
            premium_membership()
        elif membership_cost == '4':
            main_menu()
        elif membership_cost == '5':
            print('Thank you. Until next time!')
            quit()
        else:
            print('This is an invalid option. Try again')
            continue
        
#This shows all the info for the basic membership option in the membership plans menu
def basic_membership():
    os.system('cls')
    
    print('BASIC MEMBERSHIP')
    print(' ')
    while True:
        print('Basic membership costs $10')
        go_back = input('Would you like to go back to previous menu (y/n)? ')
        if go_back.lower() == 'y' or go_back.lower() == 'yes':
            membership_menu()
        elif go_back.lower == 'n' or go_back.lower == 'no':
            print('Thank you. Until next time!')
            quit()
        else:
            print('You have selected an invalid option. try again.')
            continue

#This shows all the info for the regular membership option in the membership plans menu        
def regular_membership():
    os.system('cls')
    
    print('REGULAR MEMBERSHIP')
    print(' ')
    print('Regular membership costs $15')
    while True:
        go_back = input('Would you like to go back to previous menu (y/n)? ')
    
        if go_back.lower() == 'y' or go_back.lower() == 'yes':
            membership_menu()
        elif go_back.lower == 'n' or go_back.lower == 'no':
            print('Thank you. Until next time!')
            quit()
        else:
            print('You have selected an invalid option. try again.')
            continue

#This shows all the info for the premium membership option in the membership plans menu       
def premium_membership():
    os.system('cls')
    
    print('PREMIUM MEMBERSHIP')
    print(' ')
    print('Premium membership costs $20')
    while True:
        go_back = input('Would you like to go back to previous menu (y/n)? ')
    
        if go_back.lower() == 'y' or go_back.lower() == 'yes':
            membership_menu()
        elif go_back.lower == 'n' or go_back.lower == 'no':
            print('Thank you. Until next time!')
            quit()
        else:
            print('You have selected an invalid option. try again.')
            continue
        
#This section prints out the optional extras along with a description
def optional_extras():
    os.system('cls')
    
    print('OPTIONAL EXTRAS')
    print(' ')
    print('- 24/7 gym acces is $1')
    print(' - The client will be upgraded to allow them to access the facilities \n   24 hours a day, 7 days a week.')
    print(' ')
    print('- Personal training is $20')
    print(' - A personal trainer will meet with you weekly to discuss their plans \n   and be available for questions.')
    print(' ')
    print('- Diet consultaion is $20')
    print(' - A professional trainer will meet weekly to consult and work with the \n   client and their nutriional needs.')
    print(' ')
    print('- Online video access is $2')
    print(' - Provides the client with access to various videos made by the gyms \n   personal trainers.')
    print(' ')
    
    #This section asks user if they want to buy any of the optional extras 
    while True:
        add_gym_access = input('Would you like to add 24/7 gym access (yes/no)? ')
        if add_gym_access.lower() == 'yes' or add_gym_access.lower() == 'y':
            gym_access = 1
            break
        elif add_gym_access.lower() == 'no' or add_gym_access.lower() == 'n':
            gym_access = 0
            break
        else:
            print('You have selected an invalid option. Please try again next time.')
            continue

    while True:
        add_personal_training = input('Would you like personal training (yes/no)? ')
        if add_personal_training.lower() == 'yes' or add_personal_training.lower() == 'y':
            personal_training = 20
            break
        elif add_personal_training.lower() == 'no' or add_personal_training.lower() == 'n':
            personal_training = 0
            break
        else:
            print('You have selected an invalid option. Please try again next time.')
            continue
        
    while True:
        add_diet_consultation = input('Would you like diet consultation (yes/no)? ')
        if add_diet_consultation.lower() == 'yes' or add_diet_consultation.lower() == 'y':
            diet_consultation = 20
            break
        elif add_diet_consultation.lower() == 'no' or add_diet_consultation.lower() == 'n':
            diet_consultation = 0
            break
        else:
            print('You have selected an invalid option. Please try again next time.')
            continue
        
    while True:
        add_video_access = input('Would you like video access (yes/no)? ')
        if add_video_access.lower() == 'yes' or add_video_access.lower() == 'y':
            video_access = 2
            break
        elif add_video_access.lower() == 'no' or add_video_access.lower() == 'n':
            video_access = 0
            break
        else:
            print('You have selected an invalid option. Please try again next time.')
            continue
         
    #This section calculates the total cost of the extra options user wished to buy and shows them their total
    total_extras = gym_access + personal_training + diet_consultation + video_access
    
    os.system('cls')
    
    print(' ')
    print(f'THE TOTAL COST FOR YOU OPTIONAL EXTRAS IS ${total_extras}')
    print(' ')
    print(' ')
    
    #lets client return to main menu
    while True:
        go_back = input('Would you like to return to the main menu (yes/no)? ')
        if go_back.lower() == 'yes' or go_back.lower() == 'y':
            main_menu()
        elif go_back.lower() == 'no' or go_back.lower() == 'n':
            print('Thank you. Until next time!')
            quit()
        else:
            print("Invalid option. Please try again.")
            continue
        
#This section prints out the activities for the main challenge
def gym_challenge():
    os.system('cls')
    
    gym_challenge_activities = ['1. 50 skips with a skipping rope', '2. 20 push-ups', '3. 10 squads', '4. 100m run']
    print('GYM CHALLENGE')
    print(' ')
    print('Welcome to the gym challenge. Please record your times in second four the following four exersises')
    for activity in gym_challenge_activities:
         print(activity)
    print(' ')
    
    # asks if user is ready to start or would like to return to main menu
    while True:    
        start_gym_challenge = input('PLease press s to start or b to go back to main menu. ')
        #This section records the times it took to complete the gym challenge
        if start_gym_challenge == 's':
            os.system('cls')
            skips = input('How many seconds did it take to complete the skipping challenge? \n')
            push_ups = input('How many seconds did it take to complete the push ups challenge? \n')
            squads = input('How many seconds did it take to complete the squads challenge? \n')
            run = input('How many seconds did it take to complete the running challenge? \n')
            break
        elif start_gym_challenge == 'b':
            main_menu()
        else:
            continue 
        
    #variables to calculate total time and how much they have to improve to go up a tier in the gym chalenge
    gym_challenge_total_time = int(skips) + int(push_ups) + int(squads) + int(run) - 45
    
    bronze = int(gym_challenge_total_time) - 479
    silver = int(gym_challenge_total_time) - 359
    gold = int(gym_challenge_total_time) - 299
    record = int(gym_challenge_total_time) - 265
    
    # Shows user their total time and what tier they are in and how many seconds until they reah next tier
    os.system('cls')
    
    if gym_challenge_total_time >= 480:
        print(f'Well done! This challenge took you {gym_challenge_total_time} seconds, you are in the Steel tier')
        print(f'If you improve by {bronze} seconds you will get into the Bronze tier')
    elif gym_challenge_total_time >= 360 and gym_challenge_total_time < 480:
        print(f'Well done! This challenge took you {gym_challenge_total_time} seconds, you are in the Bronze tier')
        print(f'If you improve by {silver} seconds you will get into the Silver tier')
    elif gym_challenge_total_time >= 300 and gym_challenge_total_time < 360:
        print(f'Well done! This challenge took you {gym_challenge_total_time} seconds, you are in the Silver tier')
        print(f'If you improve by {gold} seconds you will get into the Gold tier')
    elif gym_challenge_total_time <= 300 and gym_challenge_total_time > 265:
        print(f'Well done! This challenge took you {gym_challenge_total_time} seconds, you are in the Gold tier')
        print(f'If you improve by {record} seconds you will beat the gym record')
    else:
        print('Congratulation, You have beaten the current gyn record of 264 seconds.')
        print(f'Your total time is {gym_challenge_total_time}')

    while True:
        go_back = input('Would you like to return to the main menu (y/n)? ')
        if go_back == 'y' or go_back == 'yes':
            main_menu()
        elif go_back.lower == 'n' or go_back.lower == 'no':
            print('Thank you. Until next time!')
            quit()
        else:
            print('You have selected an invalid option. try again.')
            continue
        
main_menu()
