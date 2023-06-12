# https://github.com/GrandEmperorBinks

import random                                                                                                                        #Import 'random' library
import time                                                                                                                          #Import 'time' library

targetList = []                                                                                                                      #Defining lists (currently blank) for use later on
responseList = []
differenceList = []
roundsList = []
avList = []

def calculateRating(e):                                                                                                               #Defining a small function for use later on
    if e <= 0.25:                                                                                                                     #Function will determine a rating based on the given input, and will then return the determined rating
        return 'Excellent!'
    elif e <= 0.5:
        return 'Great!'
    elif e <= 1:
        return 'Good!'
    elif e <= 2:
        return 'OK!'
    elif e > 2:
        return 'Miss!'

print('Welcome to the Response Time Tester!')                                                                                        #Print welcome messages
print('You will be asked to press Enter after random amounts of time.')
print('How close can you get?')
print(' ')

while True:                                                                                                                          #Loop the following continually
    try:                                                                                                                             #Attempt the following code
        rounds = int(input('Enter desired number of rounds: '))                                                                      #Ask user for input, covert it to an integer, then store it as 'rounds'
        if rounds <= 0:
            print('Invalid input! Please enter a positive number.')                                                                  #Display an error message
            continue
        else:
            break                                                                                                                    #Break out of loop
    except ValueError:                                                                                                               #If the code encounters an error in the 'Try' section
        print('Invalid input! Please enter a positive number.')                                                                      #Display an error message

for num in range(1, rounds+1):                                                                                                       #For each number, until the value of num > value of rounds
    print(f'Round {num} of {rounds}')                                                                                                #Print current round number, out of total number of rounds
    target = random.randint(2, 8)                                                                                                    #Randomly select a number between 2 & 8, inclusive
    print('Press enter to begin round')
    input()
    print(f'Press Enter in {target} seconds, starting in...', end='')
    for number in range(1, 4):
        print(f'{number} ', end='')
        time.sleep(1)
    print('NOW!')
    timeInitial = time.time()                                                                                                        #Measure current time, store as 'timeInitial' variable
    input()                                                                                                                          #Wait for enter key
    timeFinal = time.time()                                                                                                          #Measure current time, store as 'timeFinal' variable
    response = timeFinal - timeInitial                                                                                               #Calculate response time
    response = round(response, 2)                                                                                                    #Round response to 2 decimal places
    difference = round(response - target, 2)                                                                                         #Calculate difference between target and response, convert to absolute value, and store as 'difference' variable
    print(f'That was {response} seconds')                                                                                            #Print message showing response time 
    rating = calculateRating(abs(difference))                                                                                             #Pass 'difference' to calculateRating function and store result as 'rating'
    print(f'{rating}\n')                                                                                                             #Print rating
    targetList.append(target)                                                                                                        #Add 'target' to 'targetList' list
    responseList.append(response)                                                                                                    #Add 'response' to 'responesList' list
    differenceList.append(difference)                                                                                                #Add 'difference' to 'differenceList' list
    roundsList.append(num)                                                                                                           #Add 'num' to 'roundsList' list

print('Testing Complete! Press Enter to see a breakdown of your results.')                                                           #Print completion message
input()
print('Round  Target  Response  Difference')                                                                                         #Print results table
print('-----  ------  --------  ----------')
for num in range(rounds):                                                                                                            #For each number, until the value of num > value of rounds
    print(f'{num+1:<5d}  {targetList[num]:<6d}  {responseList[num]:<8}  {abs(differenceList[num]):<10}')                             #Print results for current round, where round = num
earlyLate = sum(responseList) - sum(targetList)
if earlyLate == 0:                                                                                                                   #Calculate if the response is normally too early or too late
    print('You respond too early just as many times as you respond too late')
elif earlyLate > 0:
    print('You usually respond too late')
elif earlyLate < 0:
    print('You usually respond too early')

avList = map(abs, differenceList)                                                                                                    #Convert all values in 'differenceList' to absolute values, and add each one to the 'avList' list, so they are ready to be used to calculate the average difference
avDifference = round(sum(avList)/rounds, 2)                                                                                          #Calculate average difference for whole test
finalRating = calculateRating(avDifference)                                                                                          #Calculate final rating by passing the average difference to the calculateRating function
bestResponse  = differenceList.index(min(differenceList, key = abs))                                                                 #Define variable for the best response
worstResponse = differenceList.index(max(differenceList, key = abs))                                                                 #Define variable for the worst response
print(f'The best response was in round {roundsList[bestResponse]}, with a difference of {min(differenceList, key = abs)}s')          #Print a message showing the quickest response time
print(f'The worst response was in round {roundsList[worstResponse]}, with a difference of {max(differenceList, key = abs)}s')        #Print a message showing the slowest response time
print(f'Your average difference is: {avDifference} seconds')                                                                         #Print a message showing the average difference
print(f'Your overall rating is: {finalRating}')                                                                                      #Print a message showing the final rating
