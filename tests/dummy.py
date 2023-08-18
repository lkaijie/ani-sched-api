import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the root directory by going up one level from the script directory
root_dir = os.path.dirname(script_dir)

# Append the root directory to the Python path
sys.path.append(root_dir)
# print(sys.path)
from ani_sched import *

ani_sched = AniSched()




anime = ani_sched.search_anime("spy x family")
print(anime[0][0])
print(anime[0][1])


extracted = ani_sched.extract_search_link(anime[0][1])
print(extracted)
