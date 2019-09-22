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

def getWeekOne(divisionList):
    # divisionList[0] = divisionOne
    # divisionList[1] = divisionTwo
    # divisionList[2] = divisionThree
    weekOne = {}
    for division in divisionList:
        weekOne[division[0]] = division[1]
        weekOne[division[2]] = division[3]

    return weekOne

def getWeekTwo(divisionList):
    return {}

def getWeekThree(divisionList):
    return {}

def getWeekFour(divisionList):
    divisionOne = divisionList[0]
    divisionTwo = divisionList[1]
    divisionThree = divisionList[2]
    return {divisionOne[3]: divisionOne[0],
            divisionOne[2]: divisionOne[1],
            divisionTwo[0]: divisionTwo[2],
            divisionTwo[3]: divisionTwo[1],
            divisionThree[3]: divisionThree[0],
            divisionThree[1]: divisionThree[2]
            }

def getWeekFive(divisionList):
    return {}

def getWeekSix(divisionList):
    return {}

def getWeekSeven(divisionList):
    return {}

def getWeekEight(divisionList):
    # divisionList[0] = divisionOne
    # divisionList[1] = divisionTwo
    # divisionList[2] = divisionThree
    weekEight = {}
    for division in divisionList:
        weekEight[division[1]] = division[0]
        weekEight[division[3]] = division[2]

    return weekEight

def getWeekNine(divisionList):
    return {}

def getWeekTen(divisionList):
    return {}

def getWeekEleven(divisionList):
    divisionOne = divisionList[0]
    divisionTwo = divisionList[1]
    divisionThree = divisionList[2]
    return {divisionOne[0]: divisionOne[3],
            divisionOne[1]: divisionOne[2],
            divisionTwo[2]: divisionTwo[0],
            divisionTwo[1]: divisionTwo[3],
            divisionThree[0]: divisionThree[3],
            divisionThree[2]: divisionThree[1]
            }

def getWeekTwelve(divisionList):
    return {}

def getWeekThirteen(divisionList):
    return {}

def createGameDictionary(divisionList):
    # D1: [A, B, C, D]
    # D2: [E, F, G, H]
    # D3: [I, J, K, L]
    return [getWeekOne(divisionList),  getWeekTwo(divisionList), getWeekThree(divisionList), getWeekFour(divisionList),
            getWeekFive(divisionList), getWeekSix(divisionList), getWeekSeven(divisionList), getWeekEight(divisionList),
            getWeekNine(divisionList), getWeekTen(divisionList), getWeekEleven(divisionList),
            getWeekTwelve(divisionList), getWeekThirteen(divisionList)]

def printWeekSchedule(weekList):
    for i in range(1, len(weekList) + 1):
        print("Week " + str(i) + ":")
        for away, home in weekList[i-1].items():
            print(away + " @ " + home)
        print(" ")

def main():
    divisionOne = []
    divisionTwo = []
    divisionThree = []
    divisionNameList = [divisionOne, divisionTwo, divisionThree]
    letterArray = ["A", "B", "C", "D"]

    for i in range(1, 4):
        print("Please print the first name of each owner in division " + str(i) + "- then press enter.")
        for j in range(1, 5):
            divisionNameList[i-1].append(input("Division " + str(i) + ", Team " + letterArray[j-1] + ": "))

    weekDictionary = createGameDictionary(divisionNameList)
    printWeekSchedule(weekDictionary)

main()
