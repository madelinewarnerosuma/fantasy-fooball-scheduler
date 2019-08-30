import sys
if sys.version_info[0] != 3:
    print("Error: this script requires Python 3")
    sys.exit(1)
########################## help and usage information ##########################

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

########################## functions ##########################

#function for error handling - deal with each possible mistype scenario
#function for printing out the schedule with the names (?)
###Need to find a way to store the hardcoded schedule in a sleek format

