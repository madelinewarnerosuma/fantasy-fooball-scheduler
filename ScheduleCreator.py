import sys

if sys.version_info[0] != 3:
    print("Error: this script requires Python 3")
    sys.exit(1)
# ######################### help and usage information ##########################

help_msg = "This script takes the names of each owner from each division and assigns them a schedule."

""""

"""

usage_msg = """
Usage:
  python3 ScheduleCreator.py
  
  Please print the first name of each owner in division 1 - then press enter.
  For example:
  Adam Bob Chris Dan <enter>
  Please print the first name of each owner in division 2
  Please print the first name of each owner in division 3
  
  Then, do the work to assign them to the correct divisions
  
For more Information:
  python3 ScheduleCreator.py --help
"""


# ######################### functions ##########################

# function for error handling - deal with each possible mistype scenario
# function for printing out the schedule with the names (?)
# Need to find a way to store the hardcoded schedule in a sleek format

# dict: size of 13, in order

def createWeekOneDict(divisionList):
    # divisionList[0] = divisionOne
    # divisionList[1] = divisionTwo
    # divisionList[2] = divisionThree
    weekOne = {}
    for division in divisionList:
        weekOne[division[0]] = division[1]
        weekOne[division[2]] = division[3]

    return weekOne

def createWeekEightDict(divisionList):
    # divisionList[0] = divisionOne
    # divisionList[1] = divisionTwo
    # divisionList[2] = divisionThree
    weekEight = {}
    for division in divisionList:
        weekEight[division[1]] = division[0]
        weekEight[division[3]] = division[2]

    return weekEight

def createGameDictionary(divisionList):
    # D1: [A, B, C, D]
    # D2: [E, F, G, H]
    # D3: [I, J, K, L]
    divisionOne = divisionList[0]
    divisionTwo = divisionList[1]
    divisionThree = divisionList[2]

    weekOne = createWeekOneDict(divisionList)

    weekFour = {divisionOne[3]: divisionOne[0],
                divisionOne[2]: divisionOne[1],
                divisionTwo[0]: divisionTwo[2],
                divisionTwo[3]: divisionTwo[1],
                divisionThree[3]: divisionThree[0],
                divisionThree[1]: divisionThree[2]
               }
    weekEight = createWeekEightDict(divisionList)
    return [weekOne, weekFour, weekEight]

def printWeekSchedule(weekList):
    print("Week 1:")
    print("Week 2:")
    print("Week 3:")
    print("Week 4:")
    print("Week 5:")
    print("Week 6:")
    print("Week 7:")
    print("Week 8:")
    print("Week 9:")
    print("Week 10:")
    print("Week 11:")
    print("Week 12:")
    print("Week 13:")


def main():
    divisionOne = []
    divisionTwo = []
    divisionThree = []
    print("Please print the first name of each owner in division 1 - then press enter.")

    for i in range(1, 4):
        divisionOne.append(input("Division One, Team " + str(i)))

    print("Please print the first name of each owner in division 2 - then press enter.")
    for j in range(1, 4):
        divisionTwo.append(input("Division Two, Team " + str(j) + "name:"))

    for k in range(1, 4):
        divisionThree.append(input("Division Three, Team " + str(k) + "name:"))



main()
